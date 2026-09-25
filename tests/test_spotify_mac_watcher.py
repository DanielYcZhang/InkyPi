from extras.spotify_mac_watcher.spotify_mac_watcher import (
    DebouncedPublisher,
    compute_identity,
    heartbeat_is_due,
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
