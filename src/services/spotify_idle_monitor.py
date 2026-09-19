import logging
import threading
from datetime import datetime, timezone

from plugins.spotify_now_playing.quotes import MOTIVATIONAL_QUOTES
from refresh_task import PlaylistRefresh
from services.spotify_now_playing_service import (
    SPOTIFY_PLUGIN_ID,
    activate_idle_quote,
    mark_stale_playback_inactive,
    read_state,
)

logger = logging.getLogger(__name__)


def _parse_datetime(value):
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)
    except (AttributeError, ValueError):
        return None


def get_idle_since(state, now, stale_after_seconds=120):
    player_state = state.get("player_state", "not_running")
    if player_state in {"paused", "stopped", "not_running"}:
        return _parse_datetime(state.get("idle_started_at") or state.get("received_at"))

    last_seen = _parse_datetime(state.get("received_at"))
    if player_state == "playing" and last_seen and (now - last_seen).total_seconds() >= stale_after_seconds:
        return last_seen
    return None


def _quote_delay_minutes(settings):
    try:
        return min(max(int(settings.get("quoteIdleMinutes", 30)), 1), 10080)
    except (TypeError, ValueError):
        return 30


def quote_is_due(state, settings, now=None, stale_after_seconds=120):
    if settings.get("inactiveScreenMode") != "show_quote_after_idle" or state.get("quote_active"):
        return False

    now = now or datetime.now(timezone.utc)
    idle_since = get_idle_since(state, now, stale_after_seconds)
    if not idle_since:
        return False
    return (now - idle_since).total_seconds() >= _quote_delay_minutes(settings) * 60


class SpotifyIdleMonitor:
    def __init__(self, device_config, refresh_task, check_interval_seconds=15, stale_after_seconds=120):
        self.device_config = device_config
        self.refresh_task = refresh_task
        self.check_interval_seconds = check_interval_seconds
        self.stale_after_seconds = stale_after_seconds
        self.stop_event = threading.Event()
        self.thread = None

    def start(self):
        if not self.thread or not self.thread.is_alive():
            self.stop_event.clear()
            self.thread = threading.Thread(target=self._run, daemon=True, name="spotify-idle-monitor")
            self.thread.start()

    def stop(self):
        self.stop_event.set()
        if self.thread:
            self.thread.join(timeout=self.check_interval_seconds + 1)

    def _find_active_instance(self):
        playlist_manager = self.device_config.get_playlist_manager()
        playlist = playlist_manager.determine_active_playlist(self.refresh_task._get_current_datetime())
        if not playlist:
            return None, None
        for plugin_instance in playlist.plugins:
            if plugin_instance.plugin_id == SPOTIFY_PLUGIN_ID:
                return playlist, plugin_instance
        return None, None

    def check_once(self, now=None):
        playlist, plugin_instance = self._find_active_instance()
        if not plugin_instance:
            return False

        now = now or datetime.now(timezone.utc)
        state = read_state()
        display_changed = False
        if state.get("player_state") == "playing" and get_idle_since(
            state, now, self.stale_after_seconds
        ):
            state, display_changed = mark_stale_playback_inactive(state.get("received_at"))

        quote_activated = False
        if quote_is_due(state, plugin_instance.settings, now, self.stale_after_seconds):
            _, quote_activated = activate_idle_quote(len(MOTIVATIONAL_QUOTES))

        changed = display_changed or quote_activated
        if changed and self.refresh_task.running:
            self.refresh_task.manual_update(PlaylistRefresh(playlist, plugin_instance, force=True))
        return changed

    def _run(self):
        while not self.stop_event.wait(self.check_interval_seconds):
            try:
                self.check_once()
            except Exception:
                logger.exception("Failed to check Spotify idle quote state")
