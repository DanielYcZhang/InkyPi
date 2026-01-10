from plugins.base_plugin.base_plugin import BasePlugin
from PIL import Image, ImageDraw


class Artist(BasePlugin):
    def generate_image(self, settings, device_config):
        # 1) Canvas setup
        w, h = device_config.get_resolution()
        # Image.new(mode, size, color) creates a blank image.
        # - mode: "RGB" means red/green/blue pixels
        # - size: (width, height) in pixels
        # - color: (r, g, b) background color
        img = Image.new("RGB", (w, h), (255, 255, 255))
        # ImageDraw.Draw(img) returns a drawing tool for this image.
        # ImageDraw is the library, Draw() is the function, draw is our variable name.
        draw = ImageDraw.Draw(img)

        # 2) Your name (change this)
        name = "YOUR NAME"
        text_pos = (20, 20)
        # draw.text((x, y), text, ...) writes text at that position.
        draw.text(text_pos, name, fill=(0, 0, 0))

        # 3) A border rectangle (shape #1)
        border = 10
        # draw.rectangle(box, ...) expects (x1, y1, x2, y2).
        draw.rectangle(
            (border, border, w - border, h - border),
            outline=(0, 0, 0),
            width=2,
        )

        # 4) A diagonal line (shape #2)
        # draw.line((x1, y1, x2, y2), ...) draws a straight line.
        draw.line((border, h - border, w - border, border), fill=(0, 0, 0), width=2)

        # 5) A repeated pattern using a loop (3 dots)
        dot_radius = 6
        dot_y = h - border - dot_radius * 2
        spacing = dot_radius * 3
        for i in range(3):
            x = border + i * spacing
            # draw.ellipse(box, ...) draws an oval inside the box.
            draw.ellipse(
                (x, dot_y, x + dot_radius * 2, dot_y + dot_radius * 2),
                fill=(0, 0, 0),
            )

        # TODO:
        # - Move the name to a new position.
        # - Replace the line with a rectangle or ellipse.
        # - Make the dots span the full width.
        # - Add a tiny "stamp" box in a corner with your initials.

        return img
