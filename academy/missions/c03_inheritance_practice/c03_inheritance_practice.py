from plugins.base_plugin.base_plugin import BasePlugin
from PIL import Image, ImageDraw


class BaseCard:
    def __init__(self, title):
        self.title = title

    def draw(self, draw, w, h):
        padding = 12
        # draw.rectangle(box, ...) expects (x1, y1, x2, y2).
        draw.rectangle((padding, padding, w - padding, h - padding), outline=(0, 0, 0), width=2)
        # draw.text((x, y), text, ...) writes text at that position.
        draw.text((padding + 8, padding + 8), self.title, fill=(0, 0, 0))


class PetCard(BaseCard):
    def __init__(self, title, badge_text):
        super().__init__(title)
        self.badge_text = badge_text

    def draw(self, draw, w, h):
        # Reuse the base drawing
        super().draw(draw, w, h)

        # Add a special badge
        badge_w = 60
        badge_h = 22
        badge_x = w - badge_w - 16
        badge_y = 16
        # draw.rectangle(box, ...) expects (x1, y1, x2, y2).
        draw.rectangle(
            (badge_x, badge_y, badge_x + badge_w, badge_y + badge_h),
            outline=(0, 0, 0),
            width=2,
        )
        # draw.text((x, y), text, ...) writes text at that position.
        draw.text((badge_x + 6, badge_y + 4), self.badge_text, fill=(0, 0, 0))

        # TODO:
        # - Move the badge to a new spot.
        # - Change the badge text.
        # - Add a second badge or icon.


class InheritancePractice(BasePlugin):
    def generate_image(self, settings, device_config):
        w, h = device_config.get_resolution()
        # Image.new(mode, size, color) creates a blank image.
        # - mode: "RGB" means red/green/blue pixels
        # - size: (width, height) in pixels
        # - color: (r, g, b) background color
        img = Image.new("RGB", (w, h), (255, 255, 255))
        # ImageDraw.Draw(img) returns a drawing tool for this image.
        draw = ImageDraw.Draw(img)

        card = PetCard("Pet Profile", "LV 5")
        card.draw(draw, w, h)

        return img
