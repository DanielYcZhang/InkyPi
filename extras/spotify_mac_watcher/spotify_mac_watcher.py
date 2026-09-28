#!/usr/bin/env python3

import json
import ipaddress
import os
import socket
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional
from urllib.parse import urlsplit, urlunsplit

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


def resolve_hostname(hostname, timeout=3):
    result = subprocess.run(
        [
            sys.executable,
            "-c",
            "import socket, sys; print(socket.gethostbyname(sys.argv[1]))",
            hostname,
        ],
        check=True,
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    address = result.stdout.strip()
    if address and ipaddress.ip_address(address).version == 4:
        return address
    raise OSError(f"Unable to resolve {hostname}")


def resolve_base_url(base_url, resolver=None):
    parts = urlsplit(base_url)
    hostname = parts.hostname
    if not hostname:
        raise ValueError(f"Invalid PI_BASE_URL: {base_url}")

    try:
        ipaddress.ip_address(hostname)
        return base_url
    except ValueError:
        resolver = resolver or resolve_hostname
        resolved_host = resolver(hostname)

    netloc = resolved_host
    if parts.port:
        netloc = f"{netloc}:{parts.port}"
    return urlunsplit((parts.scheme, netloc, parts.path, parts.query, parts.fragment))


def heartbeat_is_due(now_ts, last_posted_at, heartbeat_seconds):
    return heartbeat_seconds > 0 and now_ts - last_posted_at >= heartbeat_seconds


def should_post_update(
    has_change,
    is_settled,
    now_ts,
    last_success_at,
    last_attempt_at,
    heartbeat_seconds,
    retry_interval,
):
    if not is_settled or now_ts - last_attempt_at < retry_interval:
        return False
    if has_change:
        return True
    return heartbeat_is_due(now_ts, last_success_at, heartbeat_seconds)


def log(message):
    timestamp = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[spotify_mac_watcher] {timestamp} - {message}", flush=True)


def fetch_spotify_state(timeout=8):
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
    result = subprocess.run(
        ["osascript", "-e", script],
        check=True,
        capture_output=True,
        text=True,
        timeout=timeout,
    )
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
    try:
        with STATE_FILE.open(encoding="utf-8") as state_file:
            return json.load(state_file)
    except (OSError, json.JSONDecodeError) as exc:
        log(f"ignoring unreadable state file: {exc}")
        return {}


def save_state(state):
    temp_path = STATE_FILE.with_suffix(f"{STATE_FILE.suffix}.tmp")
    with temp_path.open("w", encoding="utf-8") as state_file:
        json.dump(state, state_file, indent=2)
        state_file.flush()
        os.fsync(state_file.fileno())
    os.replace(temp_path, STATE_FILE)


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

        return track

    def mark_sent(self, track):
        self.last_sent_identity = track["identity"]
        self.last_sent_state = track["player_state"]

    def is_settled(self, track, now_ts):
        if self.pending_track is None or self.pending_since is None:
            return False
        pending_signature = (self.pending_track["identity"], self.pending_track["player_state"])
        track_signature = (track["identity"], track["player_state"])
        return track_signature == pending_signature and now_ts - self.pending_since >= self.debounce_seconds


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
    applescript_timeout = float(os.getenv("APPLESCRIPT_TIMEOUT_SECONDS", "8"))
    heartbeat_seconds = float(os.getenv("HEARTBEAT_SECONDS", "60"))
    retry_interval = float(os.getenv("RETRY_INTERVAL_SECONDS", "5"))

    persisted_state = load_state()
    publisher = DebouncedPublisher(
        debounce_seconds=debounce_seconds,
        pending_track=persisted_state.get("pending_track"),
        pending_since=persisted_state.get("pending_since"),
        last_sent_identity=persisted_state.get("last_sent_identity"),
        last_sent_state=persisted_state.get("last_sent_state"),
    )
    last_posted_at = float(persisted_state.get("last_posted_at") or 0)
    last_post_attempt_at = last_posted_at
    resolved_base_url = persisted_state.get("resolved_base_url")
    log(f"started; target={base_url}, poll={poll_interval}s, debounce={debounce_seconds}s")

    while True:
        try:
            now_ts = time.time()
            current_track = fetch_spotify_state(timeout=applescript_timeout)
            track_to_send = publisher.observe(current_track, now_ts)
            is_settled = publisher.is_settled(current_track, now_ts)
            sent_change = False
            if should_post_update(
                has_change=track_to_send is not None,
                is_settled=is_settled,
                now_ts=now_ts,
                last_success_at=last_posted_at,
                last_attempt_at=last_post_attempt_at,
                heartbeat_seconds=heartbeat_seconds,
                retry_interval=retry_interval,
            ):
                last_post_attempt_at = now_ts
                update = track_to_send or current_track
                try:
                    resolved_base_url = resolve_base_url(base_url)
                except (OSError, subprocess.SubprocessError):
                    pass
                post_update(update, resolved_base_url or base_url, token, http_timeout)
                publisher.mark_sent(update)
                last_posted_at = now_ts
                if track_to_send:
                    sent_change = True
                    log(f"sent {update['player_state']}: {update.get('title') or update['identity']}")

            next_state = {
                "pending_track": publisher.pending_track,
                "pending_since": publisher.pending_since,
                "last_sent_identity": publisher.last_sent_identity,
                "last_sent_state": publisher.last_sent_state,
                "last_sent_at": now_iso() if sent_change else persisted_state.get("last_sent_at"),
                "last_posted_at": last_posted_at,
                "resolved_base_url": resolved_base_url,
            }
            if next_state != persisted_state:
                save_state(next_state)
            persisted_state = next_state
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            log(str(exc))

        time.sleep(poll_interval)


if __name__ == "__main__":
    main()
