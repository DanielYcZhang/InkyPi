from PIL import Image

from src.plugins.spotify_now_playing.spotify_now_playing import SpotifyNowPlaying


class StubDeviceConfig:
    def get_resolution(self):
        return (800, 480)

    def get_config(self, key, default=None):
        if key == "orientation":
            return "horizontal"
        return default


def plugin_config():
    return {"id": "spotify_now_playing"}


def test_plugin_builds_playing_params(monkeypatch):
    plugin = SpotifyNowPlaying(plugin_config())

    monkeypatch.setattr(
        "src.plugins.spotify_now_playing.spotify_now_playing.read_state",
        lambda: {
            "title": "A Very Long Song Title",
            "artist": "Artist Name, Collaborator",
            "album": "Album Name",
            "player_state": "playing",
            "device_name": "MacBook Pro",
            "artwork_path": None,
        },
    )
    monkeypatch.setattr(
        "src.plugins.spotify_now_playing.spotify_now_playing.get_artwork_data_uri",
        lambda path: None,
    )

    params = plugin._build_template_params(
        {
            "showAlbumName": "true",
            "showStatusLabel": "true",
            "showDeviceName": "false",
            "emptyStateMode": "show_last_track",
            "pausedBehavior": "show_paused_badge",
            "fallbackArtworkStyle": "text_only",
            "emptyStateMessage": "Nothing Playing",
        }
    )
    assert params["show_empty_state"] is False
    assert params["show_album_name"] is True
    assert params["title"] == "A Very Long Song Title"
    assert params["artist"] == "Artist Name, Collaborator"
    assert params["show_device_name"] is False


def test_plugin_builds_empty_state(monkeypatch):
    plugin = SpotifyNowPlaying(plugin_config())

    monkeypatch.setattr(
        "src.plugins.spotify_now_playing.spotify_now_playing.read_state",
        lambda: {"player_state": "not_running", "artwork_path": None},
    )
    monkeypatch.setattr(
        "src.plugins.spotify_now_playing.spotify_now_playing.get_artwork_data_uri",
        lambda path: None,
    )

    params = plugin._build_template_params(
        {
            "showAlbumName": "false",
            "showStatusLabel": "true",
            "showDeviceName": "false",
            "emptyStateMode": "show_nothing_playing",
            "pausedBehavior": "show_paused_badge",
            "fallbackArtworkStyle": "text_only",
            "emptyStateMessage": "Nothing Playing",
        }
    )
    assert params["show_empty_state"] is True
    assert params["title"] == "Nothing Playing"


def test_plugin_preserves_non_english_metadata(monkeypatch):
    plugin = SpotifyNowPlaying(plugin_config())

    monkeypatch.setattr(
        "src.plugins.spotify_now_playing.spotify_now_playing.read_state",
        lambda: {
            "title": "Привет",
            "artist": "Мияги & Эндшпиль",
            "album": "Hajime",
            "player_state": "playing",
            "device_name": "MacBook Pro",
            "artwork_path": None,
        },
    )
    monkeypatch.setattr(
        "src.plugins.spotify_now_playing.spotify_now_playing.get_artwork_data_uri",
        lambda path: None,
    )

    params = plugin._build_template_params(
        {
            "showAlbumName": "true",
            "showStatusLabel": "true",
            "showDeviceName": "false",
            "emptyStateMode": "show_last_track",
            "pausedBehavior": "show_paused_badge",
            "fallbackArtworkStyle": "text_only",
            "emptyStateMessage": "Nothing Playing",
        }
    )
    assert params["title"] == "Привет"
    assert params["artist"] == "Мияги & Эндшпиль"


def test_plugin_preserves_long_single_word_title(monkeypatch):
    plugin = SpotifyNowPlaying(plugin_config())

    monkeypatch.setattr(
        "src.plugins.spotify_now_playing.spotify_now_playing.read_state",
        lambda: {
            "title": "GOOSEBUMPS",
            "artist": "Travis Scott",
            "album": "Birds in the Trap Sing McKnight",
            "player_state": "playing",
            "device_name": "MacBook Pro",
            "artwork_path": None,
        },
    )
    monkeypatch.setattr(
        "src.plugins.spotify_now_playing.spotify_now_playing.get_artwork_data_uri",
        lambda path: None,
    )

    params = plugin._build_template_params(
        {
            "showAlbumName": "true",
            "showStatusLabel": "true",
            "showDeviceName": "false",
            "emptyStateMode": "show_last_track",
            "pausedBehavior": "show_paused_badge",
            "fallbackArtworkStyle": "text_only",
            "emptyStateMessage": "Nothing Playing",
        }
    )
    assert params["title"] == "GOOSEBUMPS"


def test_plugin_hides_status_label_when_disabled(monkeypatch):
    plugin = SpotifyNowPlaying(plugin_config())

    monkeypatch.setattr(
        "src.plugins.spotify_now_playing.spotify_now_playing.read_state",
        lambda: {
            "title": "Track",
            "artist": "Artist",
            "album": "Album",
            "player_state": "paused",
            "device_name": "MacBook Pro",
            "artwork_path": None,
        },
    )
    monkeypatch.setattr(
        "src.plugins.spotify_now_playing.spotify_now_playing.get_artwork_data_uri",
        lambda path: None,
    )

    params = plugin._build_template_params(
        {
            "showAlbumName": "false",
            "showStatusLabel": "false",
            "showDeviceName": "false",
            "emptyStateMode": "show_last_track",
            "pausedBehavior": "show_paused_badge",
            "fallbackArtworkStyle": "text_only",
            "emptyStateMessage": "Nothing Playing",
        }
    )
    assert params["status_label"] == ""


def test_plugin_can_treat_paused_as_nothing_playing(monkeypatch):
    plugin = SpotifyNowPlaying(plugin_config())

    monkeypatch.setattr(
        "src.plugins.spotify_now_playing.spotify_now_playing.read_state",
        lambda: {
            "title": "Track",
            "artist": "Artist",
            "album": "Album",
            "player_state": "paused",
            "device_name": "MacBook Pro",
            "artwork_path": None,
        },
    )
    monkeypatch.setattr(
        "src.plugins.spotify_now_playing.spotify_now_playing.get_artwork_data_uri",
        lambda path: None,
    )

    params = plugin._build_template_params(
        {
            "showAlbumName": "false",
            "showStatusLabel": "true",
            "showDeviceName": "false",
            "emptyStateMode": "show_nothing_playing",
            "pausedBehavior": "treat_as_nothing_playing",
            "fallbackArtworkStyle": "text_only",
            "emptyStateMessage": "Idle",
        }
    )
    assert params["show_empty_state"] is True
    assert params["title"] == "Idle"
    assert params["artist"] == "Spotify"


def test_plugin_can_show_artwork_placeholder(monkeypatch):
    plugin = SpotifyNowPlaying(plugin_config())

    monkeypatch.setattr(
        "src.plugins.spotify_now_playing.spotify_now_playing.read_state",
        lambda: {
            "title": "Track",
            "artist": "Artist",
            "album": "Album",
            "player_state": "playing",
            "device_name": "MacBook Pro",
            "artwork_path": None,
        },
    )
    monkeypatch.setattr(
        "src.plugins.spotify_now_playing.spotify_now_playing.get_artwork_data_uri",
        lambda path: None,
    )

    params = plugin._build_template_params(
        {
            "showAlbumName": "false",
            "showStatusLabel": "true",
            "showDeviceName": "true",
            "emptyStateMode": "show_last_track",
            "pausedBehavior": "show_paused_badge",
            "fallbackArtworkStyle": "placeholder_block",
            "emptyStateMessage": "Nothing Playing",
        }
    )
    assert params["show_artwork"] is False
    assert params["show_artwork_placeholder"] is True
    assert params["reserve_artwork_space"] is True


def test_plugin_generate_image_uses_render_image(monkeypatch):
    plugin = SpotifyNowPlaying(plugin_config())

    monkeypatch.setattr(plugin, "_build_template_params", lambda settings: {"plugin_settings": settings})
    monkeypatch.setattr(
        plugin,
        "render_image",
        lambda dimensions, html_file, css_file, template_params: Image.new("RGB", dimensions, "white"),
    )

    image = plugin.generate_image({"showAlbumName": "false"}, StubDeviceConfig())
    assert image.size == (800, 480)
