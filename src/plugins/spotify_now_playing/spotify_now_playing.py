import logging

from PIL import Image

from plugins.base_plugin.base_plugin import BasePlugin
from services.spotify_now_playing_service import get_artwork_data_uri, read_state

logger = logging.getLogger(__name__)


def _to_bool(value):
    return str(value).lower() == "true"


class SpotifyNowPlaying(BasePlugin):
    def generate_settings_template(self):
        template_params = super().generate_settings_template()
        template_params["style_settings"] = True
        return template_params

    def _build_template_params(self, settings):
        state = read_state()
        player_state = state.get("player_state", "not_running")
        show_album_name = _to_bool(settings.get("showAlbumName", "false"))
        empty_state_mode = settings.get("emptyStateMode", "show_last_track")

        has_track_data = bool(state.get("title") or state.get("artist") or state.get("album"))
        show_empty_state = not has_track_data or (
            player_state in {"stopped", "not_running"} and empty_state_mode == "show_nothing_playing"
        )

        status_label = ""
        if player_state == "paused":
            status_label = "Paused"
        elif player_state in {"stopped", "not_running"} and not show_empty_state:
            status_label = "Nothing Playing"

        template_params = {
            "plugin_settings": settings,
            "title": state.get("title") or "Nothing Playing",
            "artist": state.get("artist") or "Spotify",
            "album": state.get("album"),
            "device_name": state.get("device_name"),
            "status_label": status_label,
            "show_album_name": show_album_name,
            "show_empty_state": show_empty_state,
            "artwork_style": settings.get("artworkStyle", "square_left"),
            "artwork_data_uri": get_artwork_data_uri(state.get("artwork_path")),
        }
        return template_params

    def generate_image(self, settings, device_config):
        dimensions = device_config.get_resolution()
        if device_config.get_config("orientation") == "vertical":
            dimensions = dimensions[::-1]

        template_params = self._build_template_params(settings)
        image = self.render_image(dimensions, "spotify_now_playing.html", "spotify_now_playing.css", template_params)
        if not image:
            raise RuntimeError("Failed to render Spotify now playing image.")
        return image
