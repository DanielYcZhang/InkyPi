from plugins.base_plugin.base_plugin import BasePlugin
from PIL import Image, ImageDraw
from pathlib import Path


class Creature:
    def __init__(self, name, species, age, weight):
        # Properties (facts about the creature)
        self.name = name
        self.species = species
        self.age = age
        self.weight = weight

    def draw(self, img, draw, w, h, icon=None):
        # Draw the creature card using its properties
        padding = 12
        # draw.rectangle(box, ...) expects (x1, y1, x2, y2).
        draw.rectangle((padding, padding, w - padding, h - padding), outline=0, width=2)

        text_x = padding + 20  # Moved text block right
        text_y = padding + 20  # Moved text block down
        line_gap = 18

        # draw.text((x, y), text, ...) writes text at that position.
        draw.text((text_x, text_y), f"Name: {self.name}", fill=0)
        draw.text((text_x, text_y + line_gap), f"Species: {self.species}", fill=0)
        draw.text((text_x, text_y + line_gap * 2), f"Age: {self.age}", fill=0)
        draw.text((text_x, text_y + line_gap * 3), f"Weight: {self.weight}", fill=0)

        # Practice TODOs:
        # 1) Add a new property (favorite_food, power, or skill).
        # 2) Draw that property on the card.
        # 3) Move the text block by changing text_x/text_y.

        # Surprise TODO:
        # - Add a small badge box near the name (a tiny rectangle + text).
        
        # Surprise: Add a small badge box near the name
        # Calculate the width of the name text to position the badge dynamically
        name_text = f"Name: {self.name}"
        bbox = draw.textbbox((0, 0), name_text)  # Get bounding box of the text, 0,0 is just a reference point
        text_width = bbox[2] - bbox[0]  # Width of the name text
        badge_x = text_x + text_width + 10  # Position badge 10 pixels after the name text
        badge_y = text_y - 5  # 5 pixels above the name line
        # Instead of text, paste a small resized version of icon.png as the badge
        if icon:
            img.paste(icon, (badge_x, badge_y))  # Paste the icon at the badge position

        # Stretch TODO (optional):
        # - Add a second creature card below the first.
        # - Add a divider line between cards.


class CreatureCard(BasePlugin):
    def generate_image(self, settings, device_config):
        w, h = device_config.get_resolution()
        # Image.new(mode, size, color) creates a blank image.
        # - mode: "1" means 1-bit pixels (black and white)
        # - size: (width, height) in pixels
        # - color: 255 for white background
        img = Image.new('1', (w, h), 255)
        # ImageDraw.Draw(img) returns a drawing tool for this image.
        draw = ImageDraw.Draw(img)

        # Load and resize the icon for the badge
        icon_path = Path(__file__).parent / "icon.png"
        icon = Image.open(icon_path).convert('1').resize((15, 15))  # Resize to 15x15 for small badge

        # Create an object from the class
        creature = Creature("Pip", "Cat", 5, 10)

        # Ask the object to draw itself, passing the icon for the badge
        creature.draw(img, draw, w, h, icon)

        return img
