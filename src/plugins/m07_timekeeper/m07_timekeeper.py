# Import the tools we need to draw images
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
# Import the "Parent" class that all plugins must copy
from plugins.base_plugin.base_plugin import BasePlugin, STATIC_DIR

from datetime import datetime

class Timekeeper(BasePlugin):
    def __init__(self, base_dir):
        super().__init__(base_dir)

    def generate_image(self, settings, device_config):
    
        width, height = device_config.get_resolution()
        image = Image.new('1', (width, height), 255)
        draw = ImageDraw.Draw(image)

        # Get the current time
        now = datetime.now()
        time_text = now.strftime("%H:%M")
        time_label = f"Time: {time_text}"
        
        font_path = Path(STATIC_DIR) / "fonts" / "Paintingwithchocolate-K5mo.ttf"
        large_font = ImageFont.truetype(str(font_path), size=40)
        
        text_box = draw.textbbox((0, 0), time_label, font=large_font)
        text_width = text_box[2] - text_box[0]
        text_height = text_box[3] - text_box[1]
        x = (width - text_width) // 2
        y = (height - text_height) // 2

        draw.text((x, y), time_label, font=large_font, fill=0 )

        return image