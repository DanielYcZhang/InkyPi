import logging
from datetime import datetime

from PIL import Image

from plugins.base_plugin.base_plugin import BasePlugin
from services.spotify_now_playing_service import get_artwork_data_uri, read_state

logger = logging.getLogger(__name__)

DEFAULT_SETTINGS = {
    "inactiveScreenMode": "show_state_screens",
    "artworkStyle": "square_left",
    "fallbackArtworkStyle": "text_only",
    "textAlignment": "left",
    "titleLines": "2",
    "artistLines": "2",
    "artworkCornerStyle": "rounded",
    "showAlbumName": "false",
    "showStatusLabel": "true",
    "showDeviceName": "false",
    "showLastUpdatedTime": "false",
}


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


def _normalize_paused_behavior(value):
    if value == "show_paused_badge":
        return "show_paused_screen"
    if value == "show_as_normal":
        return "show_last_track"
    if value == "treat_as_nothing_playing":
        return "show_nothing_playing_screen"
    if value in {"show_paused_screen", "show_last_track", "show_nothing_playing_screen"}:
        return value
    return "show_paused_screen"


def _normalize_inactive_screen_mode(settings):
    inactive_mode = settings.get("inactiveScreenMode")
    if inactive_mode in {"keep_last_track", "show_state_screens", "show_nothing_playing_for_all"}:
        return inactive_mode

    paused_behavior = _normalize_paused_behavior(settings.get("pausedBehavior", "show_paused_screen"))
    empty_state_mode = settings.get("emptyStateMode", "show_last_track")

    if paused_behavior == "show_last_track" and empty_state_mode == "show_last_track":
        return "keep_last_track"
    if paused_behavior == "show_nothing_playing_screen":
        return "show_nothing_playing_for_all"
    return "show_state_screens"


class SpotifyNowPlaying(BasePlugin):
    def generate_settings_template(self):
        template_params = super().generate_settings_template()
        template_params["style_settings"] = True
        return template_params

    def _build_template_params(self, settings, timezone_str=None):
        state = read_state()
        player_state = state.get("player_state", "not_running")
        show_album_name = _to_bool(settings.get("showAlbumName", DEFAULT_SETTINGS["showAlbumName"]))
        show_status_label = _to_bool(settings.get("showStatusLabel", DEFAULT_SETTINGS["showStatusLabel"]))
        show_device_name = _to_bool(settings.get("showDeviceName", DEFAULT_SETTINGS["showDeviceName"]))
        show_last_updated_time = _to_bool(settings.get("showLastUpdatedTime", DEFAULT_SETTINGS["showLastUpdatedTime"]))
        inactive_screen_mode = _normalize_inactive_screen_mode(settings)
        artwork_style = settings.get("artworkStyle", DEFAULT_SETTINGS["artworkStyle"])
        fallback_artwork_style = settings.get("fallbackArtworkStyle", DEFAULT_SETTINGS["fallbackArtworkStyle"])
        text_alignment = settings.get("textAlignment", DEFAULT_SETTINGS["textAlignment"])
        title_lines = _to_positive_int(settings.get("titleLines", DEFAULT_SETTINGS["titleLines"]), 2)
        artist_lines = _to_positive_int(settings.get("artistLines", DEFAULT_SETTINGS["artistLines"]), 2)
        artwork_corner_style = settings.get("artworkCornerStyle", DEFAULT_SETTINGS["artworkCornerStyle"])

        has_track_data = bool(state.get("title") or state.get("artist") or state.get("album"))
        show_paused_screen = player_state == "paused" and inactive_screen_mode == "show_state_screens"
        show_nothing_playing_screen = player_state in {"stopped", "not_running"} and inactive_screen_mode != "keep_last_track"
        show_paused_as_nothing = player_state == "paused" and inactive_screen_mode == "show_nothing_playing_for_all"
        no_track_data_screen = not has_track_data and inactive_screen_mode != "keep_last_track"
        show_empty_state = show_paused_screen or show_paused_as_nothing or no_track_data_screen or show_nothing_playing_screen

        status_label = ""
        if player_state == "paused" and inactive_screen_mode == "keep_last_track":
            status_label = "Paused"
        elif player_state in {"stopped", "not_running"} and inactive_screen_mode == "keep_last_track":
            status_label = "Nothing Playing"
        if not show_status_label:
            status_label = ""

        title = state.get("title") or "Nothing Playing"
        artist = state.get("artist") or "Spotify"
        state_message = None
        if show_paused_screen:
            title = "Paused"
            artist = "Spotify playback is paused"
            state_message = "Spotify will update again when music starts."
            status_label = ""
        elif show_paused_as_nothing or show_nothing_playing_screen or no_track_data_screen:
            title = "Nothing Playing"
            artist = "Spotify"
            state_message = "Start a song on your Mac to show it here."
            if show_paused_as_nothing:
                status_label = ""

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
            "state_message": state_message,
            "status_label": status_label,
            "show_album_name": show_album_name,
            "show_empty_state": show_empty_state,
            "artwork_style": artwork_style,
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
