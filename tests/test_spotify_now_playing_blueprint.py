from flask import Flask

from src.blueprints.spotify_now_playing import spotify_now_playing_bp


class StubRefreshTask:
    def __init__(self):
        self.running = True
        self.calls = []

    def _get_current_datetime(self):
        from datetime import datetime
        import pytz

        return datetime.now(pytz.UTC)

    def manual_update(self, action):
        self.calls.append(action)


class StubPlaylist:
    def __init__(self, plugins):
        self.plugins = plugins


class StubPluginInstance:
    def __init__(self, plugin_id, settings=None):
        self.plugin_id = plugin_id
        self.settings = settings or {}


class StubPlaylistManager:
    def __init__(self, playlist):
        self.playlist = playlist

    def determine_active_playlist(self, current_dt):
        return self.playlist


class StubDeviceConfig:
    def __init__(self, token="secret", playlist=None):
        self._token = token
        self._playlist_manager = StubPlaylistManager(playlist)

    def load_env_key(self, key):
        return self._token

    def get_playlist_manager(self):
        return self._playlist_manager

    def get_plugin(self, plugin_id):
        return {"id": plugin_id, "image_settings": []}


class StubDisplayManager:
    def display_image(self, image, image_settings=None):
        pass


def payload(**overrides):
    data = {
        "identity": "Song|Artist|Album|art",
        "title": "Song",
        "artist": "Artist",
        "album": "Album",
        "artwork_url": None,
        "player_state": "playing",
        "source_updated_at": "2026-03-15T12:00:00+00:00",
        "device_name": "MacBook Pro",
    }
    data.update(overrides)
    return data


def create_app(tmp_path, monkeypatch, playlist_plugins=None):
    from src.services import spotify_now_playing_service as service

    monkeypatch.setattr(service, "SPOTIFY_CACHE_PATH", str(tmp_path / "state.json"))
    monkeypatch.setattr(service, "SPOTIFY_ARTWORK_DIR", str(tmp_path / "art"))

    app = Flask(__name__)
    app.register_blueprint(spotify_now_playing_bp)
    playlist = StubPlaylist(playlist_plugins or [])
    app.config["DEVICE_CONFIG"] = StubDeviceConfig(playlist=playlist)
    app.config["REFRESH_TASK"] = StubRefreshTask()
    app.config["DISPLAY_MANAGER"] = StubDisplayManager()
    return app


def test_webhook_rejects_missing_token(tmp_path, monkeypatch):
    app = create_app(tmp_path, monkeypatch)
    client = app.test_client()

    response = client.post("/spotify_now_playing/update", json=payload())
    assert response.status_code == 401


def test_webhook_updates_cache_and_triggers_refresh(tmp_path, monkeypatch):
    app = create_app(tmp_path, monkeypatch, playlist_plugins=[StubPluginInstance("spotify_now_playing")])
    client = app.test_client()

    response = client.post(
        "/spotify_now_playing/update",
        json=payload(),
        headers={"X-InkyPi-Spotify-Token": "secret"},
    )

    assert response.status_code == 200
    assert response.get_json()["changed"] is True
    assert len(app.config["REFRESH_TASK"].calls) == 1


def test_identical_second_push_does_not_trigger_refresh(tmp_path, monkeypatch):
    app = create_app(tmp_path, monkeypatch, playlist_plugins=[StubPluginInstance("spotify_now_playing")])
    client = app.test_client()
    headers = {"X-InkyPi-Spotify-Token": "secret"}

    client.post("/spotify_now_playing/update", json=payload(), headers=headers)
    response = client.post("/spotify_now_playing/update", json=payload(), headers=headers)

    assert response.status_code == 200
    assert response.get_json()["changed"] is False
    assert len(app.config["REFRESH_TASK"].calls) == 1
