from pathlib import Path

import pytest
from PIL import Image

from src.display.display_manager import DisplayManager
from src.display.waveshare_display import WaveshareDisplay


class StubDeviceConfig:
    def __init__(self, current_image_file):
        self.current_image_file = str(current_image_file)

    def get_config(self, key, default=None):
        values = {
            "orientation": "horizontal",
            "inverted_image": False,
            "image_settings": {},
        }
        return values.get(key, default)

    def get_resolution(self):
        return (8, 6)


class FailingDisplay:
    def display_image(self, image, image_settings):
        raise RuntimeError("simulated panel transfer failure")


class RecordingEpd:
    def __init__(self):
        self.calls = []

    def Clear(self):
        self.calls.append("clear")

    def getbuffer(self, image):
        self.calls.append("buffer")
        return b"frame"

    def display(self, buffer):
        self.calls.append("display")

    def sleep(self):
        self.calls.append("sleep")


def test_failed_hardware_transfer_keeps_last_successful_current_image(tmp_path):
    current_image_path = tmp_path / "current.png"
    Image.new("RGB", (8, 6), "black").save(current_image_path)

    manager = DisplayManager.__new__(DisplayManager)
    manager.device_config = StubDeviceConfig(current_image_path)
    manager.display = FailingDisplay()

    with pytest.raises(RuntimeError, match="simulated panel transfer failure"):
        manager.display_image(Image.new("RGB", (8, 6), "white"))

    with Image.open(current_image_path) as persisted:
        assert persisted.getpixel((0, 0)) == (0, 0, 0)


def test_waveshare_update_does_not_clear_last_frame_before_transfer():
    display = WaveshareDisplay.__new__(WaveshareDisplay)
    display.epd_display = RecordingEpd()
    display.epd_display_init = lambda: display.epd_display.calls.append("init")
    display.bi_color_display = False

    display.display_image(Image.new("1", (8, 6), 255))

    assert display.epd_display.calls == ["init", "buffer", "display", "sleep"]
