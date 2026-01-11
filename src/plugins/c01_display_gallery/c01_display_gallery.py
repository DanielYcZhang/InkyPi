from plugins.base_plugin.base_plugin import BasePlugin
from PIL import Image, ImageDraw


class DisplayGallery(BasePlugin):
    def generate_image(self, settings, device_config):
        # Canvas setup
        w, h = device_config.get_resolution()
        # Image.new(mode, size, color) creates a blank image.
        # - mode: "RGB" means red/green/blue pixels
        # - size: (width, height) in pixels
        # - color: (r, g, b) background color
        img = Image.new('1', (w, h), 255)
        # ImageDraw.Draw(img) returns a drawing tool for this image.
        # ImageDraw is the library, Draw() is the function, draw is our variable name.
        draw = ImageDraw.Draw(img)

        # Layout variables (change these to see different results)
        padding = 12
        gap = 50
        box_count = 3
        box_height = int(h * 0.45)
        box_width = (w - padding * 2 - gap * (box_count - 1)) // box_count

        # Box style
        outline_color = 0  # 0 = black for 1-bit mode
        label_color = 0    # 0 = black for 1-bit mode

        # Draw three boxes in a row.
        # Loop repeats the box drawing for each index 0..box_count-1.
        for i in range(box_count):
            x1 = padding + i * (box_width + gap)
            y1 = padding
            x2 = x1 + box_width
            y2 = y1 + box_height

            # draw.rectangle(box, ...) expects (x1, y1, x2, y2).
            draw.rectangle((x1, y1, x2, y2), outline=outline_color, width=2)
            # draw.text((x, y), text, ...) writes text at that position.
            draw.text((x1 + 6, y2 + 6), f"Box {i + 1}", fill=label_color)

        # TODO:
        # - Change padding or gap and observe the layout shift.
        # - Make one box taller or wider.
        # - Add a small "stamp" box in the bottom-right corner.

        return img
