from io import BytesIO

import pytest
from PIL import Image

from src.services import spotify_now_playing_service as service


@pytest.fixture
def spotify_cache_paths(tmp_path, monkeypatch):
    cache_path = tmp_path / "spotify_now_playing.json"
    artwork_dir = tmp_path / "spotify_art"
    monkeypatch.setattr(service, "SPOTIFY_CACHE_PATH", str(cache_path))
    monkeypatch.setattr(service, "SPOTIFY_ARTWORK_DIR", str(artwork_dir))
    return cache_path, artwork_dir


def valid_payload(**overrides):
    payload = {
        "identity": "Song|Artist|Album|art",
        "title": "Song",
        "artist": "Artist",
        "album": "Album",
        "artwork_url": "https://example.com/art.png",
        "player_state": "playing",
        "source_updated_at": "2026-03-15T12:00:00+00:00",
        "device_name": "MacBook Pro",
    }
    payload.update(overrides)
    return payload


def image_bytes():
    image = Image.new("RGB", (12, 12), "black")
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    return buffer.getvalue()


class MockResponse:
    def __init__(self, content):
        self.content = content

    def raise_for_status(self):
        return None


def test_normalize_payload_rejects_missing_identity():
    with pytest.raises(ValueError):
        service.normalize_payload(valid_payload(identity=None))


def test_update_state_writes_new_track(spotify_cache_paths, monkeypatch):
    monkeypatch.setattr(service.requests, "get", lambda *args, **kwargs: MockResponse(image_bytes()))
    state, changed = service.update_state(service.normalize_payload(valid_payload()))

    assert changed is True
    assert state["title"] == "Song"
    assert state["artwork_path"].endswith(".png")
    assert service.read_state()["identity"] == "Song|Artist|Album|art"


def test_update_state_ignores_duplicate_payload(spotify_cache_paths, monkeypatch):
    monkeypatch.setattr(service.requests, "get", lambda *args, **kwargs: MockResponse(image_bytes()))
    payload = service.normalize_payload(valid_payload())
    service.update_state(payload)

    _, changed = service.update_state(payload)
    assert changed is False


def test_update_state_preserves_previous_track_for_stopped_state(spotify_cache_paths, monkeypatch):
    monkeypatch.setattr(service.requests, "get", lambda *args, **kwargs: MockResponse(image_bytes()))
    original_state, _ = service.update_state(service.normalize_payload(valid_payload()))

    state, changed = service.update_state(
        service.normalize_payload(
            valid_payload(
                identity="state:stopped",
                title=None,
                artist=None,
                album=None,
                artwork_url=None,
                player_state="stopped",
            )
        )
    )

    assert changed is True
    assert state["title"] == "Song"
    assert state["player_state"] == "stopped"
    assert state["artwork_path"] == original_state["artwork_path"]


def test_update_state_keeps_existing_artwork_on_download_failure(spotify_cache_paths, monkeypatch):
    monkeypatch.setattr(service.requests, "get", lambda *args, **kwargs: MockResponse(image_bytes()))
    original_state, _ = service.update_state(service.normalize_payload(valid_payload()))

    def raise_error(*args, **kwargs):
        raise RuntimeError("network down")

    monkeypatch.setattr(service.requests, "get", raise_error)
    state, changed = service.update_state(
        service.normalize_payload(valid_payload(player_state="paused", source_updated_at="2026-03-15T12:01:00+00:00"))
    )

    assert changed is True
    assert state["artwork_path"] == original_state["artwork_path"]


def test_update_state_preserves_multi_artist_string(spotify_cache_paths):
    state, changed = service.update_state(
        service.normalize_payload(
            valid_payload(artist="Travis Scott, Kendrick Lamar", artwork_url=None)
        )
    )

    assert changed is True
    assert state["artist"] == "Travis Scott, Kendrick Lamar"
    assert service.read_state()["artist"] == "Travis Scott, Kendrick Lamar"
