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
        show_status_label = _to_bool(settings.get("showStatusLabel", "true"))
        show_device_name = _to_bool(settings.get("showDeviceName", "false"))
        empty_state_mode = settings.get("emptyStateMode", "show_last_track")
        paused_behavior = settings.get("pausedBehavior", "show_paused_badge")
        fallback_artwork_style = settings.get("fallbackArtworkStyle", "text_only")
        empty_state_message = settings.get("emptyStateMessage", "Nothing Playing").strip() or "Nothing Playing"

        has_track_data = bool(state.get("title") or state.get("artist") or state.get("album"))
        if player_state == "paused" and paused_behavior == "treat_as_nothing_playing":
            show_empty_state = True
        else:
            show_empty_state = not has_track_data or (
                player_state in {"stopped", "not_running"} and empty_state_mode == "show_nothing_playing"
            )

        status_label = ""
        if player_state == "paused" and paused_behavior == "show_paused_badge":
            status_label = "Paused"
        elif player_state in {"stopped", "not_running"} and not show_empty_state:
            status_label = "Nothing Playing"
        if not show_status_label:
            status_label = ""

        title = state.get("title") or empty_state_message
        artist = state.get("artist") or "Spotify"
        if show_empty_state:
            title = empty_state_message
            if empty_state_mode == "show_nothing_playing" or paused_behavior == "treat_as_nothing_playing":
                artist = "Spotify"

        artwork_data_uri = get_artwork_data_uri(state.get("artwork_path"))
        show_artwork = bool(artwork_data_uri) and not show_empty_state
        show_artwork_placeholder = (
            not show_artwork and fallback_artwork_style == "placeholder_block" and not show_empty_state
        )
        reserve_artwork_space = fallback_artwork_style != "hide_artwork" and (show_artwork or show_artwork_placeholder)

        template_params = {
            "plugin_settings": settings,
            "title": title,
            "artist": artist,
            "album": state.get("album"),
            "device_name": state.get("device_name"),
            "status_label": status_label,
            "show_album_name": show_album_name,
            "show_empty_state": show_empty_state,
            "artwork_style": settings.get("artworkStyle", "square_left"),
            "artwork_data_uri": artwork_data_uri,
            "show_device_name": show_device_name,
            "show_artwork": show_artwork,
            "show_artwork_placeholder": show_artwork_placeholder,
            "reserve_artwork_space": reserve_artwork_space,
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
