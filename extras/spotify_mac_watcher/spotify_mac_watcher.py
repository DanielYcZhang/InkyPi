#!/usr/bin/env python3

import json
import os
import socket
import subprocess
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import requests


SCRIPT_DIR = Path(__file__).resolve().parent
STATE_FILE = SCRIPT_DIR / "spotify_mac_watcher_state.json"
ENV_FILE = SCRIPT_DIR / ".env"
HEADER_NAME = "X-InkyPi-Spotify-Token"
FIELD_SEPARATOR = "\x1f"


def load_env_file(path):
    if not path.exists():
        return

    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


def get_required_env(name):
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required setting: {name}")
    return value


def now_iso():
    return datetime.now(timezone.utc).isoformat()


def compute_identity(track):
    track_fields = [track.get("title"), track.get("artist"), track.get("album"), track.get("artwork_url")]
    if any(track_fields):
        return "|".join(value or "" for value in track_fields)
    return f"state:{track['player_state']}"


def fetch_spotify_state():
    script = f"""
    tell application "System Events"
        set spotifyRunning to (name of processes) contains "Spotify"
    end tell
    if spotifyRunning is false then
        return "not_running{FIELD_SEPARATOR}{FIELD_SEPARATOR}{FIELD_SEPARATOR}{FIELD_SEPARATOR}"
    end if
    tell application "Spotify"
        try
            set trackName to name of current track
            set artistName to artist of current track
            set albumName to album of current track
            set artworkUrl to artwork url of current track
            set playerState to player state as string
            return playerState & "{FIELD_SEPARATOR}" & trackName & "{FIELD_SEPARATOR}" & artistName & "{FIELD_SEPARATOR}" & albumName & "{FIELD_SEPARATOR}" & artworkUrl
        on error
            set playerState to player state as string
            return playerState & "{FIELD_SEPARATOR}{FIELD_SEPARATOR}{FIELD_SEPARATOR}{FIELD_SEPARATOR}"
        end try
    end tell
    """
    result = subprocess.run(["osascript", "-e", script], check=True, capture_output=True, text=True)
    output = result.stdout.strip().split(FIELD_SEPARATOR)
    while len(output) < 5:
        output.append("")

    player_state, title, artist, album, artwork_url = output[:5]
    track = {
        "title": title or None,
        "artist": artist or None,
        "album": album or None,
        "artwork_url": artwork_url or None,
        "player_state": player_state or "not_running",
        "source_updated_at": now_iso(),
        "device_name": os.getenv("DEVICE_NAME") or socket.gethostname(),
    }
    track["identity"] = compute_identity(track)
    return track


def load_state():
    if not STATE_FILE.exists():
        return {}
    with STATE_FILE.open(encoding="utf-8") as state_file:
        return json.load(state_file)


def save_state(state):
    with STATE_FILE.open("w", encoding="utf-8") as state_file:
        json.dump(state, state_file, indent=2)


@dataclass
class DebouncedPublisher:
    debounce_seconds: float
    pending_track: Optional[dict] = None
    pending_since: Optional[float] = None
    last_sent_identity: Optional[str] = None
    last_sent_state: Optional[str] = None

    def observe(self, track, now_ts):
        track_signature = (track["identity"], track["player_state"])

        if self.pending_track is None:
            self.pending_track = track
            self.pending_since = now_ts
            return None

        pending_signature = (self.pending_track["identity"], self.pending_track["player_state"])
        if track_signature != pending_signature:
            self.pending_track = track
            self.pending_since = now_ts
            return None

        if now_ts - self.pending_since < self.debounce_seconds:
            return None

        if track["identity"] == self.last_sent_identity and track["player_state"] == self.last_sent_state:
            return None

        self.last_sent_identity = track["identity"]
        self.last_sent_state = track["player_state"]
        return track


def post_update(track, base_url, token, timeout):
    response = requests.post(
        f"{base_url.rstrip('/')}/spotify_now_playing/update",
        json=track,
        headers={HEADER_NAME: token},
        timeout=timeout,
    )
    response.raise_for_status()
    return response.json()


def main():
    load_env_file(ENV_FILE)

    base_url = get_required_env("PI_BASE_URL")
    token = get_required_env("SPOTIFY_PUSH_TOKEN")
    poll_interval = float(os.getenv("POLL_INTERVAL_SECONDS", "1"))
    debounce_seconds = float(os.getenv("DEBOUNCE_SECONDS", "3"))
    http_timeout = float(os.getenv("HTTP_TIMEOUT_SECONDS", "5"))

    persisted_state = load_state()
    publisher = DebouncedPublisher(
        debounce_seconds=debounce_seconds,
        pending_track=persisted_state.get("pending_track"),
        pending_since=persisted_state.get("pending_since"),
        last_sent_identity=persisted_state.get("last_sent_identity"),
        last_sent_state=persisted_state.get("last_sent_state"),
    )

    while True:
        try:
            now_ts = time.time()
            current_track = fetch_spotify_state()
            track_to_send = publisher.observe(current_track, now_ts)
            if track_to_send:
                post_update(track_to_send, base_url, token, http_timeout)

            save_state(
                {
                    "pending_track": publisher.pending_track,
                    "pending_since": publisher.pending_since,
                    "last_sent_identity": publisher.last_sent_identity,
                    "last_sent_state": publisher.last_sent_state,
                    "last_sent_at": now_iso() if track_to_send else persisted_state.get("last_sent_at"),
                }
            )
            persisted_state = load_state()
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            print(f"[spotify_mac_watcher] {exc}", flush=True)

        time.sleep(poll_interval)


if __name__ == "__main__":
    main()
