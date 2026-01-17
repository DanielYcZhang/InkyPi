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

    # UPDATED: We added 'start_y' here.
    # WHY: To draw a second card below the first one, we need to tell this function
    # exactly where on the screen (vertical Y position) to start drawing.
    def draw(self, img, draw, w, start_y, icon=None):
        # The space between the card border and the screen edge
        padding = 12
        
        # Calculate the top and bottom of THIS specific card.
        # We add 'start_y' to move the whole box down if this is the second card.
        card_height = 110
        top = start_y + padding
        bottom = top + card_height
        
        # Draw the card border
        # box = (left_x, top_y, right_x, bottom_y)
        draw.rectangle((padding, top, w - padding, bottom), outline=0, width=2)

        # Text Positioning
        # We set text_y relative to 'top', so the text moves with the card.
        text_x = padding + 20
        text_y = top + 20  
        line_gap = 18

        # Draw the stats
        draw.text((text_x, text_y), f"Name: {self.name}", fill=0)
        draw.text((text_x, text_y + line_gap), f"Species: {self.species}", fill=0)
        draw.text((text_x, text_y + line_gap * 2), f"Age: {self.age}", fill=0)
        draw.text((text_x, text_y + line_gap * 3), f"Weight: {self.weight}", fill=0)

        # --- Badge Logic (Surprise TODO) ---
        # 1. Calculate how wide the name text is so we don't draw over it.
        name_text = f"Name: {self.name}"
        bbox = draw.textbbox((0, 0), name_text)
        text_width = bbox[2] - bbox[0]
        
        # 2. Position the badge to the right of the name.
        badge_x = text_x + text_width + 10
        badge_y = text_y - 3  # Shift up slightly to align with text
        
        # 3. Paste the icon if it exists
        if icon:
            # We cast to int() because pixels can't be decimals
            img.paste(icon, (int(badge_x), int(badge_y)))


class CreatureCard(BasePlugin):
    def generate_image(self, settings, device_config):
        # Get screen resolution (w = width, h = height)
        w, h = device_config.get_resolution()
        
        # Create the main canvas
        # Mode '1' = 1-bit color (Pure Black & White). 
        # Color 255 = White background.
        img = Image.new('1', (w, h), 255)
        draw = ImageDraw.Draw(img)

        # --- ICON PROCESSING (The Fix) ---
        icon_path = Path(__file__).parent / "icon.png"
        
        # Step 1: Open the image normally
        raw_icon = Image.open(icon_path)
        
        # Step 2: Resize it while it is still in High Quality color
        raw_icon = raw_icon.resize((15, 15))
        
        # Step 3: Create a blank white background image (RGBA mode)
        # RGBA = Red, Green, Blue, Alpha (Transparency).
        # We need this white layer because converting transparency directly to '1-bit' turns it black.
        icon = Image.new("RGBA", raw_icon.size, "white")
        
        # Step 4: Paste the icon onto the white background.
        # The third argument 'raw_icon' acts as a "mask" -> it tells Python to only paste
        # the pixels that are NOT transparent.
        if raw_icon.mode == 'RGBA':
            icon.paste(raw_icon, (0, 0), raw_icon)
        else:
            icon.paste(raw_icon, (0, 0))
            
        # Step 5: Now it's safe to convert to Black & White (1-bit)
        icon = icon.convert('1')
        # ----------------------------------

        # --- STRETCH TODO: Multiple Cards ---
        
        # 1. Create two different creatures
        pip = Creature("Pip", "Cat", 5, 10)
        rex = Creature("Rex", "Dog", 3, 25)

        # 2. Draw the first creature at the top (start_y = 0)
        pip.draw(img, draw, w, 0, icon)

        # 3. Draw a Divider Line between the cards
        # We pick Y=135 because the first card is about 120px tall + padding
        divider_y = 135
        draw.line((10, divider_y, w - 10, divider_y), fill=0, width=2)

        # 4. Draw the second creature BELOW the line
        # We tell it to start drawing at pixel 140
        rex.draw(img, draw, w, 140, icon)

        return img