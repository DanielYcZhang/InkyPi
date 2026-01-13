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
        padding = 24
        gap = 24
        box_count = 4
        box_height = int(h * 0.45)
        box_width = (w - padding * 2 - gap * (box_count - 1)) // box_count
        #box_width = (w<width of canvas> - padding<around the edge of screen/canvas> * 2<left and rights sides of screen> - gap<gap between boxes> * (box_count -1)<box count -1 since 3 boxes = 2 gaps between>)

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
            draw.text((x1 + 6, y2 + 6), f"Gallery Box {i + 1}", fill=label_color)

        # Surprise: Add initials stamp in the corner
        stamp_x = w - 30
        stamp_y = h - 20
        draw.text((stamp_x, stamp_y), "DZ", fill=label_color)  # DZ = Daniel Zhang initials

        # TODO for Stretch:
        # - Uncomment below to center the boxes on screen (divide by 2)
        # center_offset = (w - (box_count * box_width + (box_count - 1) * gap)) // 2
        # x1 = center_offset + i * (box_width + gap)
        #
        # - Uncomment to add divider lines between boxes
        # if i < box_count - 1:
        #     divider_x = x2 + gap // 2
        #     draw.line((divider_x, y1, divider_x, y2), fill=outline_color, width=1)

        return img
