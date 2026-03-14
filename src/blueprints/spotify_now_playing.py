import logging

from flask import Blueprint, current_app, jsonify, request

from plugins.plugin_registry import get_plugin_instance
from refresh_task import PlaylistRefresh
from services.spotify_now_playing_service import (
    SPOTIFY_PLUGIN_ID,
    is_authorized,
    normalize_payload,
    update_state,
)

logger = logging.getLogger(__name__)
spotify_now_playing_bp = Blueprint("spotify_now_playing", __name__)


def _find_active_spotify_instance(device_config):
    playlist_manager = device_config.get_playlist_manager()
    refresh_task = current_app.config["REFRESH_TASK"]
    active_playlist = playlist_manager.determine_active_playlist(refresh_task._get_current_datetime())
    if not active_playlist:
        return None, None

    for plugin_instance in active_playlist.plugins:
        if plugin_instance.plugin_id == SPOTIFY_PLUGIN_ID:
            return active_playlist, plugin_instance
    return None, None


def _trigger_display_refresh(device_config):
    refresh_task = current_app.config["REFRESH_TASK"]
    display_manager = current_app.config["DISPLAY_MANAGER"]
    playlist, plugin_instance = _find_active_spotify_instance(device_config)
    if not plugin_instance:
        return False

    plugin_config = device_config.get_plugin(SPOTIFY_PLUGIN_ID)
    if not plugin_config:
        return False

    if refresh_task.running:
        refresh_task.manual_update(PlaylistRefresh(playlist, plugin_instance, force=True))
        return True

    plugin = get_plugin_instance(plugin_config)
    image = plugin.generate_image(plugin_instance.settings, device_config)
    display_manager.display_image(image, image_settings=plugin_config.get("image_settings", []))
    return True


@spotify_now_playing_bp.route("/spotify_now_playing/update", methods=["POST"])
def update_spotify_now_playing():
    device_config = current_app.config["DEVICE_CONFIG"]

    try:
        if not is_authorized(request, device_config):
            return jsonify({"error": "Unauthorized"}), 401

        normalized_state = normalize_payload(request.get_json(silent=True))
        state, changed = update_state(normalized_state)
        display_triggered = _trigger_display_refresh(device_config) if changed else False
        return jsonify(
            {
                "success": True,
                "changed": changed,
                "display_triggered": display_triggered,
                "identity": state.get("identity"),
            }
        )
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400
    except Exception as exc:
        logger.exception("Failed to update Spotify now playing state")
        return jsonify({"error": str(exc)}), 500
