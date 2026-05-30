import logging
from datetime import datetime

from PIL import Image

from plugins.base_plugin.base_plugin import BasePlugin
from services.spotify_now_playing_service import get_artwork_data_uri, read_state

logger = logging.getLogger(__name__)


def _to_bool(value):
    return str(value).lower() == "true"


def _to_positive_int(value, default):
    try:
        parsed = int(value)
        return parsed if parsed > 0 else default
    except (TypeError, ValueError):
        return default


def _format_last_updated(state, timezone_str=None):
    timestamp = state.get("received_at") or state.get("source_updated_at")
    if not timestamp:
        return None

    try:
        dt = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    except ValueError:
        return None

    if timezone_str:
        try:
            import pytz

            dt = dt.astimezone(pytz.timezone(timezone_str))
        except Exception:
            pass

    return dt.strftime("Updated %I:%M %p").replace(" 0", " ")


class SpotifyNowPlaying(BasePlugin):
    def generate_settings_template(self):
        template_params = super().generate_settings_template()
        template_params["style_settings"] = True
        return template_params

    def _build_template_params(self, settings, timezone_str=None):
        state = read_state()
        player_state = state.get("player_state", "not_running")
        show_album_name = _to_bool(settings.get("showAlbumName", "false"))
        show_status_label = _to_bool(settings.get("showStatusLabel", "true"))
        show_device_name = _to_bool(settings.get("showDeviceName", "false"))
        show_last_updated_time = _to_bool(settings.get("showLastUpdatedTime", "false"))
        empty_state_mode = settings.get("emptyStateMode", "show_last_track")
        paused_behavior = settings.get("pausedBehavior", "show_paused_badge")
        fallback_artwork_style = settings.get("fallbackArtworkStyle", "text_only")
        text_alignment = settings.get("textAlignment", "left")
        title_lines = _to_positive_int(settings.get("titleLines", "2"), 2)
        artist_lines = _to_positive_int(settings.get("artistLines", "2"), 2)
        artwork_corner_style = settings.get("artworkCornerStyle", "rounded")
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
            "show_last_updated_time": show_last_updated_time,
            "last_updated_text": _format_last_updated(state, timezone_str),
            "text_alignment": text_alignment,
            "title_lines": title_lines,
            "artist_lines": artist_lines,
            "artwork_corner_style": artwork_corner_style,
        }
        return template_params

    def generate_image(self, settings, device_config):
        dimensions = device_config.get_resolution()
        if device_config.get_config("orientation") == "vertical":
            dimensions = dimensions[::-1]

        template_params = self._build_template_params(
            settings,
            timezone_str=device_config.get_config("timezone"),
        )
        image = self.render_image(dimensions, "spotify_now_playing.html", "spotify_now_playing.css", template_params)
        if not image:
            raise RuntimeError("Failed to render Spotify now playing image.")
        return image
