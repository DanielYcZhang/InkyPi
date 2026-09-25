import base64
import hashlib
import json
import logging
import os
import random
import threading
from datetime import datetime, timezone
from io import BytesIO

import requests
from PIL import Image

from utils.app_utils import resolve_path

logger = logging.getLogger(__name__)

SPOTIFY_PLUGIN_ID = "spotify_now_playing"
SPOTIFY_PUSH_TOKEN_ENV = "SPOTIFY_PUSH_TOKEN"
SPOTIFY_PUSH_TOKEN_HEADER = "X-InkyPi-Spotify-Token"
SPOTIFY_CACHE_PATH = resolve_path(os.path.join("static", "images", "saved", "spotify_now_playing.json"))
SPOTIFY_ARTWORK_DIR = resolve_path(os.path.join("static", "images", "saved", "spotify_now_playing"))
VALID_PLAYER_STATES = {"playing", "paused", "stopped", "not_running"}
STATE_LOCK = threading.RLock()


def get_cache_path():
    return SPOTIFY_CACHE_PATH


def get_artwork_dir():
    return SPOTIFY_ARTWORK_DIR


def _ensure_parent_dir(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)


def _ensure_artwork_dir():
    os.makedirs(get_artwork_dir(), exist_ok=True)


def _now_iso():
    return datetime.now(timezone.utc).isoformat()


def get_push_token(device_config):
    return device_config.load_env_key(SPOTIFY_PUSH_TOKEN_ENV)


def is_authorized(request, device_config):
    expected_token = get_push_token(device_config)
    if not expected_token:
        raise RuntimeError(f"{SPOTIFY_PUSH_TOKEN_ENV} is not configured.")
    return request.headers.get(SPOTIFY_PUSH_TOKEN_HEADER) == expected_token


def read_state():
    with STATE_LOCK:
        cache_path = get_cache_path()
        if not os.path.exists(cache_path):
            return {}

        with open(cache_path, encoding="utf-8") as cache_file:
            return json.load(cache_file)


def write_state(state):
    with STATE_LOCK:
        cache_path = get_cache_path()
        _ensure_parent_dir(cache_path)
        with open(cache_path, "w", encoding="utf-8") as cache_file:
            json.dump(state, cache_file, indent=2)


def _normalize_text(value):
    if value is None:
        return None
    value = str(value).strip()
    return value or None


def normalize_payload(payload, received_at=None):
    if not isinstance(payload, dict):
        raise ValueError("Payload must be a JSON object.")

    identity = _normalize_text(payload.get("identity"))
    player_state = _normalize_text(payload.get("player_state"))
    source_updated_at = _normalize_text(payload.get("source_updated_at"))
    device_name = _normalize_text(payload.get("device_name"))

    if not identity:
        raise ValueError("Field 'identity' is required.")
    if player_state not in VALID_PLAYER_STATES:
        raise ValueError(f"Field 'player_state' must be one of: {', '.join(sorted(VALID_PLAYER_STATES))}.")
    if not source_updated_at:
        raise ValueError("Field 'source_updated_at' is required.")
    if not device_name:
        raise ValueError("Field 'device_name' is required.")

    try:
        datetime.fromisoformat(source_updated_at.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("Field 'source_updated_at' must be a valid ISO-8601 datetime.") from exc

    normalized = {
        "identity": identity,
        "title": _normalize_text(payload.get("title")),
        "artist": _normalize_text(payload.get("artist")),
        "album": _normalize_text(payload.get("album")),
        "artwork_url": _normalize_text(payload.get("artwork_url")),
        "player_state": player_state,
        "source_updated_at": source_updated_at,
        "device_name": device_name,
        "received_at": received_at or _now_iso(),
    }
    return normalized


def _display_signature(state):
    keys = [
        "identity",
        "title",
        "artist",
        "album",
        "artwork_url",
        "player_state",
        "device_name",
        "artwork_path",
        "quote_active",
        "quote_index",
        "inferred_idle",
    ]
    return {key: state.get(key) for key in keys}


def _download_artwork(artwork_url, identity, timeout=10):
    if not artwork_url:
        return None

    _ensure_artwork_dir()
    response = requests.get(artwork_url, timeout=timeout)
    response.raise_for_status()

    with Image.open(BytesIO(response.content)) as artwork:
        artwork = artwork.convert("RGB")
        artwork_hash = hashlib.sha256(identity.encode("utf-8")).hexdigest()[:16]
        artwork_path = os.path.join(get_artwork_dir(), f"{artwork_hash}.png")
        artwork.save(artwork_path, format="PNG")
    return artwork_path


def update_state(normalized_state):
    with STATE_LOCK:
        existing_state = read_state()
        merged_state = dict(existing_state)
        merged_state.update(normalized_state)

        preserve_existing_metadata = normalized_state["player_state"] in {"stopped", "not_running"}
        for field in ["title", "artist", "album", "artwork_url"]:
            if preserve_existing_metadata and not normalized_state.get(field):
                merged_state[field] = existing_state.get(field)

        artwork_path = existing_state.get("artwork_path")
        incoming_artwork_url = normalized_state.get("artwork_url")
        artwork_url = merged_state.get("artwork_url")
        identity = merged_state.get("identity")
        should_redownload = bool(incoming_artwork_url) and (
            artwork_url != existing_state.get("artwork_url") or identity != existing_state.get("identity")
        )

        if should_redownload:
            try:
                artwork_path = _download_artwork(artwork_url, identity)
            except Exception as exc:
                logger.warning("Failed to download Spotify artwork: %s", exc)
                if identity != existing_state.get("identity"):
                    artwork_path = None
        elif not artwork_url:
            artwork_path = None

        merged_state["artwork_path"] = artwork_path
        merged_state["version"] = 2

        previous_player_state = existing_state.get("player_state")
        player_state = normalized_state["player_state"]
        merged_state["inferred_idle"] = False
        if player_state == "playing":
            merged_state["idle_started_at"] = None
            merged_state["quote_active"] = False
        elif previous_player_state == "playing" or not existing_state.get("idle_started_at"):
            merged_state["idle_started_at"] = normalized_state["received_at"]
            merged_state["quote_active"] = False

        display_changed = _display_signature(merged_state) != _display_signature(existing_state)
        if merged_state != existing_state:
            write_state(merged_state)

        return merged_state, display_changed


def mark_stale_playback_inactive(expected_received_at):
    """Mark a vanished watcher as inactive without overwriting a newer heartbeat."""
    with STATE_LOCK:
        state = read_state()
        if state.get("player_state") != "playing" or state.get("received_at") != expected_received_at:
            return state, False

        state["player_state"] = "not_running"
        state["inferred_idle"] = True
        state["idle_started_at"] = expected_received_at
        state["quote_active"] = False
        state["version"] = 2
        write_state(state)
        return state, True


def activate_idle_quote(quote_count):
    if quote_count <= 0:
        raise ValueError("quote_count must be greater than zero")

    with STATE_LOCK:
        state = read_state()
        if state.get("quote_active"):
            return state, False

        collection_changed = state.get("quote_deck_size") != quote_count
        deck = [] if collection_changed else [
            index
            for index in state.get("quote_deck", [])
            if isinstance(index, int) and 0 <= index < quote_count
        ]
        last_quote_index = state.get("last_quote_index")
        if not deck:
            deck = list(range(quote_count))
            random.shuffle(deck)
            if len(deck) > 1 and deck[-1] == last_quote_index:
                deck[0], deck[-1] = deck[-1], deck[0]

        quote_index = deck.pop()
        state["quote_active"] = True
        state["quote_index"] = quote_index
        state["last_quote_index"] = quote_index
        state["quote_deck"] = deck
        state["quote_deck_size"] = quote_count
        write_state(state)
        return state, True


def get_artwork_data_uri(artwork_path):
    if not artwork_path or not os.path.exists(artwork_path):
        return None

    with open(artwork_path, "rb") as artwork_file:
        encoded = base64.b64encode(artwork_file.read()).decode("ascii")
    return f"data:image/png;base64,{encoded}"
