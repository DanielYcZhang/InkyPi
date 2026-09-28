import threading
from types import SimpleNamespace

from PIL import Image

from src import refresh_task as refresh_task_module
from src.refresh_task import RefreshTask


def test_nonblocking_manual_update_is_queued():
    refresh_task = RefreshTask.__new__(RefreshTask)
    refresh_task.running = True
    refresh_task.condition = SimpleNamespace()
    refresh_task.manual_update_requests = []

    class Condition:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            return None

        def notify_all(self):
            pass

    refresh_task.condition = Condition()
    action = object()

    assert refresh_task.request_manual_update(action) is True
    assert len(refresh_task.manual_update_requests) == 1
    assert refresh_task.manual_update_requests[0].action is action


def test_nonblocking_manual_update_is_rejected_when_worker_is_stopped():
    refresh_task = RefreshTask.__new__(RefreshTask)
    refresh_task.running = False

    assert refresh_task.request_manual_update(object()) is False


def test_second_update_queues_while_display_is_busy(monkeypatch):
    display_started = threading.Event()
    release_display = threading.Event()
    second_executed = threading.Event()

    class DeviceConfig:
        def __init__(self):
            self.refresh_info = SimpleNamespace(image_hash="")

        def get_config(self, key, default=None):
            if key == "timezone":
                return "UTC"
            return default

        def get_playlist_manager(self):
            return None

        def get_refresh_info(self):
            return self.refresh_info

        def get_plugin(self, plugin_id):
            return {"id": plugin_id, "image_settings": []}

        def write_config(self):
            pass

    class DisplayManager:
        def display_image(self, image, image_settings=None):
            display_started.set()
            release_display.wait(timeout=2)

    class Action:
        def __init__(self, color, executed=None):
            self.color = color
            self.executed = executed

        def get_plugin_id(self):
            return "spotify_now_playing"

        def execute(self, plugin, device_config, current_dt):
            if self.executed:
                self.executed.set()
            return Image.new("RGB", (2, 2), self.color)

        def get_refresh_info(self):
            return {"refresh_type": "test", "plugin_id": "spotify_now_playing"}

    monkeypatch.setattr(
        refresh_task_module,
        "get_plugin_instance",
        lambda config: SimpleNamespace(config={"image_settings": []}),
    )
    refresh_task = RefreshTask(DeviceConfig(), DisplayManager())
    refresh_task.start()

    try:
        assert refresh_task.request_manual_update(Action("black")) is True
        assert display_started.wait(timeout=1)

        request_returned = threading.Event()

        def queue_second_update():
            refresh_task.request_manual_update(Action("white", second_executed))
            request_returned.set()

        request_thread = threading.Thread(target=queue_second_update)
        request_thread.start()
        assert request_returned.wait(timeout=0.2)

        release_display.set()
        assert second_executed.wait(timeout=1)
        request_thread.join(timeout=1)
    finally:
        release_display.set()
        refresh_task.stop()
