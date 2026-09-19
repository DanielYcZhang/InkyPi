from datetime import datetime, timezone
from types import SimpleNamespace

from src.services import spotify_idle_monitor as monitor_module
from src.services.spotify_idle_monitor import get_idle_since, quote_is_due


def utc(value):
    return datetime.fromisoformat(value).astimezone(timezone.utc)


def test_explicit_pause_uses_idle_start_time():
    state = {
        "player_state": "paused",
        "idle_started_at": "2026-03-15T12:00:00+00:00",
        "received_at": "2026-03-15T12:00:00+00:00",
    }

    assert get_idle_since(state, utc("2026-03-15T12:10:00+00:00"), stale_after_seconds=120) == utc(
        "2026-03-15T12:00:00+00:00"
    )


def test_stale_playing_heartbeat_counts_as_idle_when_laptop_disappears():
    state = {
        "player_state": "playing",
        "received_at": "2026-03-15T12:00:00+00:00",
    }

    assert get_idle_since(state, utc("2026-03-15T12:03:00+00:00"), stale_after_seconds=120) == utc(
        "2026-03-15T12:00:00+00:00"
    )


def test_fresh_playing_heartbeat_is_not_idle():
    state = {
        "player_state": "playing",
        "received_at": "2026-03-15T12:00:00+00:00",
    }

    assert get_idle_since(state, utc("2026-03-15T12:01:00+00:00"), stale_after_seconds=120) is None


def test_quote_becomes_due_after_configured_delay():
    state = {
        "player_state": "paused",
        "idle_started_at": "2026-03-15T12:00:00+00:00",
        "received_at": "2026-03-15T12:00:00+00:00",
        "quote_active": False,
    }
    settings = {"inactiveScreenMode": "show_quote_after_idle", "quoteIdleMinutes": "30"}

    assert quote_is_due(state, settings, utc("2026-03-15T12:29:59+00:00")) is False
    assert quote_is_due(state, settings, utc("2026-03-15T12:30:00+00:00")) is True


def test_monitor_refreshes_once_when_playing_heartbeat_goes_stale(monkeypatch):
    playlist = object()
    plugin_instance = SimpleNamespace(
        settings={"inactiveScreenMode": "show_state_screens", "quoteIdleMinutes": "30"}
    )
    state = {
        "player_state": "playing",
        "received_at": "2026-03-15T12:00:00+00:00",
        "quote_active": False,
    }
    inactive_state = {
        **state,
        "player_state": "not_running",
        "inferred_idle": True,
        "idle_started_at": state["received_at"],
    }
    refresh_task = SimpleNamespace(running=True, updates=[], manual_update=lambda update: refresh_task.updates.append(update))
    monitor = monitor_module.SpotifyIdleMonitor(None, refresh_task, stale_after_seconds=120)

    monkeypatch.setattr(monitor, "_find_active_instance", lambda: (playlist, plugin_instance))
    monkeypatch.setattr(monitor_module, "read_state", lambda: state)
    monkeypatch.setattr(
        monitor_module,
        "mark_stale_playback_inactive",
        lambda expected_received_at: (inactive_state, expected_received_at == state["received_at"]),
    )

    changed = monitor.check_once(utc("2026-03-15T12:03:00+00:00"))

    assert changed is True
    assert len(refresh_task.updates) == 1
