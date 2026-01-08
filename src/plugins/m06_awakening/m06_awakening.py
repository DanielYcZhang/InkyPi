# Import the tools we need to draw images
from PIL import Image, ImageDraw, ImageFont
# Import the "Parent" class that all plugins must copy
from plugins.base_plugin.base_plugin import BasePlugin

# Define our new plugin class named "Awakening"
class Awakening(BasePlugin):
    
    # This function runs once when InkyPi starts up
    def __init__(self, base_dir):
        # Call the setup function of the parent class
        super().__init__(base_dir)

    # This is the main function. It runs every time the screen updates.
    def generate_image(self, settings, device_config):
        
        # 1. Ask the device: "How big is the screen?"
        # It gives us the Width (800) and Height (480)
        width, height = device_config.get_resolution()

        # 2. Create the blank paper (Canvas)
        # '1' = Black & White mode
        # 255 = Fill the background with White
        image = Image.new('1', (width, height), 255)
        
        # Create a "pencil" tool to draw on this specific image
        draw = ImageDraw.Draw(image)

        # 3. Get the user's input
        # Look for "name" in settings. If empty, use "Commander"
        name = settings.get("name", "Commander")
        # Create the full sentence
        text_string = f"Hello, {name}"

        # 4. Load a font
        # load_default() grabs a basic pixel font built into Python
        font = ImageFont.load_default()

        # 5. Calculate Math to Center the Text
        # Draw an invisible box around the text to measure it
        text_bbox = draw.textbbox((0, 0), text_string, font=font)
        
        # Calculate width (Right edge - Left edge)
        text_width = text_bbox[2] - text_bbox[0]
        # Calculate height (Bottom edge - Top edge)
        text_height = text_bbox[3] - text_bbox[1]
        
        # Find the center X (Horizontal)
        x = (width - text_width) // 2
        # Find the center Y (Vertical)
        y = (height - text_height) // 2

        # 6. Actually draw the text
        # (x, y) = where to start drawing
        # fill=0 = Draw in Black ink (Remember: 0 is Black, 255 is White)
        draw.text((x, y), text_string, font=font, fill=0)

        # 7. Hand the finished picture back to InkyPi
        return image
