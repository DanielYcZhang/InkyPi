import json
from types import SimpleNamespace

from extras.spotify_mac_watcher import spotify_mac_watcher as watcher
from extras.spotify_mac_watcher.spotify_mac_watcher import (
    DebouncedPublisher,
    compute_identity,
    fetch_spotify_state,
    heartbeat_is_due,
    load_state,
    resolve_base_url,
    save_state,
    should_post_update,
)


def track(identity, state="playing"):
    return {
        "identity": identity,
        "player_state": state,
        "title": identity,
        "artist": "Artist",
        "album": "Album",
        "artwork_url": None,
        "source_updated_at": "2026-03-15T12:00:00+00:00",
        "device_name": "MacBook Pro",
    }


def test_compute_identity_uses_track_fields():
    identity = compute_identity(
        {
            "title": "Song",
            "artist": "Artist",
            "album": "Album",
            "artwork_url": "https://example.com/art.png",
            "player_state": "playing",
        }
    )
    assert identity == "Song|Artist|Album|https://example.com/art.png"


def test_compute_identity_falls_back_to_state():
    identity = compute_identity(
        {
            "title": None,
            "artist": None,
            "album": None,
            "artwork_url": None,
            "player_state": "not_running",
        }
    )
    assert identity == "state:not_running"


def test_debounced_publisher_only_emits_final_stable_track():
    publisher = DebouncedPublisher(debounce_seconds=3)

    assert publisher.observe(track("A"), 0) is None
    assert publisher.observe(track("B"), 1) is None
    assert publisher.observe(track("C"), 2) is None
    assert publisher.observe(track("C"), 4) is None

    emitted = publisher.observe(track("C"), 5.2)
    assert emitted["identity"] == "C"


def test_debounced_publisher_ignores_duplicate_stable_state():
    publisher = DebouncedPublisher(debounce_seconds=1)

    publisher.observe(track("A"), 0)
    emitted = publisher.observe(track("A"), 1.1)
    assert emitted["identity"] == "A"
    publisher.mark_sent(emitted)
    assert publisher.observe(track("A"), 2.5) is None


def test_debounced_publisher_retries_track_until_delivery_is_acknowledged():
    publisher = DebouncedPublisher(debounce_seconds=1)

    publisher.observe(track("A"), 0)
    assert publisher.observe(track("A"), 1.1)["identity"] == "A"
    assert publisher.observe(track("A"), 2.0)["identity"] == "A"


def test_heartbeat_does_not_publish_an_unsettled_skip_candidate():
    publisher = DebouncedPublisher(debounce_seconds=3)

    publisher.observe(track("A"), 0)
    publisher.observe(track("B"), 1)

    assert publisher.is_settled(track("B"), 2) is False
    assert publisher.is_settled(track("B"), 4.1) is True


def test_heartbeat_is_due_after_interval():
    assert heartbeat_is_due(now_ts=160, last_posted_at=100, heartbeat_seconds=60) is True
    assert heartbeat_is_due(now_ts=159, last_posted_at=100, heartbeat_seconds=60) is False


def test_failed_heartbeat_retries_after_retry_interval():
    assert should_post_update(
        has_change=False,
        is_settled=True,
        now_ts=161,
        last_success_at=100,
        last_attempt_at=160,
        heartbeat_seconds=60,
        retry_interval=5,
    ) is False
    assert should_post_update(
        has_change=False,
        is_settled=True,
        now_ts=165,
        last_success_at=100,
        last_attempt_at=160,
        heartbeat_seconds=60,
        retry_interval=5,
    ) is True


def test_corrupt_state_file_recovers_cleanly(tmp_path, monkeypatch):
    state_path = tmp_path / "watcher-state.json"
    state_path.write_text("{partial", encoding="utf-8")
    monkeypatch.setattr(watcher, "STATE_FILE", state_path)

    assert load_state() == {}


def test_state_file_is_replaced_atomically(tmp_path, monkeypatch):
    state_path = tmp_path / "watcher-state.json"
    monkeypatch.setattr(watcher, "STATE_FILE", state_path)

    save_state({"last_sent_identity": "track-1"})

    assert json.loads(state_path.read_text(encoding="utf-8")) == {"last_sent_identity": "track-1"}
    assert list(tmp_path.glob("*.tmp")) == []


def test_spotify_probe_has_a_hard_timeout(monkeypatch):
    observed = {}

    def fake_run(command, **kwargs):
        observed.update(kwargs)
        return SimpleNamespace(stdout="playing\x1fSong\x1fArtist\x1fAlbum\x1fhttps://example.com/art.png\n")

    monkeypatch.setattr(watcher.subprocess, "run", fake_run)

    state = fetch_spotify_state(timeout=7)

    assert observed["timeout"] == 7
    assert state["title"] == "Song"


def test_pi_hostname_resolves_to_cached_ip_url():
    resolved = resolve_base_url(
        "http://raspberrypi.local:8080",
        resolver=lambda hostname: "192.168.1.213",
    )

    assert resolved == "http://192.168.1.213:8080"


def test_pi_ip_url_does_not_require_name_resolution():
    def fail_if_called(hostname):
        raise AssertionError(f"resolver unexpectedly called for {hostname}")

    assert resolve_base_url("http://192.168.1.213", resolver=fail_if_called) == "http://192.168.1.213"
