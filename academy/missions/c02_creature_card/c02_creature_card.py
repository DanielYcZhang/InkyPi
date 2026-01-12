from plugins.base_plugin.base_plugin import BasePlugin
from PIL import Image, ImageDraw


class Creature:
    def __init__(self, name, species, level):
        # Properties (facts about the creature)
        self.name = name
        self.species = species
        self.level = level

    def draw(self, draw, w, h):
        # Draw the creature card using its properties
        padding = 12
        # draw.rectangle(box, ...) expects (x1, y1, x2, y2).
        draw.rectangle((padding, padding, w - padding, h - padding), outline=(0, 0, 0), width=2)

        text_x = padding + 8
        text_y = padding + 8
        line_gap = 18

        # draw.text((x, y), text, ...) writes text at that position.
        draw.text((text_x, text_y), f"Name: {self.name}", fill=(0, 0, 0))
        draw.text((text_x, text_y + line_gap), f"Species: {self.species}", fill=(0, 0, 0))
        draw.text((text_x, text_y + line_gap * 2), f"Level: {self.level}", fill=(0, 0, 0))

        # Practice TODOs:
        # 1) Add a new property (favorite_food, power, or skill).
        # 2) Draw that property on the card.
        # 3) Move the text block by changing text_x/text_y.

        # Surprise TODO:
        # - Add a small badge box near the name (a tiny rectangle + text).

        # Stretch TODO (optional):
        # - Add a second creature card below the first.
        # - Add a divider line between cards.


class CreatureCard(BasePlugin):
    def generate_image(self, settings, device_config):
        w, h = device_config.get_resolution()
        # Image.new(mode, size, color) creates a blank image.
        # - mode: "RGB" means red/green/blue pixels
        # - size: (width, height) in pixels
        # - color: (r, g, b) background color
        img = Image.new("RGB", (w, h), (255, 255, 255))
        # ImageDraw.Draw(img) returns a drawing tool for this image.
        draw = ImageDraw.Draw(img)

        # Create an object from the class
        creature = Creature("Pip", "Cat", 5)

        # Ask the object to draw itself
        creature.draw(draw, w, h)

        return img
