from plugins.base_plugin.base_plugin import BasePlugin
from PIL import Image, ImageDraw


# ============================================================
# CHECKPOINT 2: BaseCard - The Foundation
# ============================================================
# This is the BASE class that holds code shared by ALL card types.
# Every card needs a border and title, so we write it ONCE here.

class BaseCard:
    """Base class for all cards - defines shared border and title"""
    
    def __init__(self, title):
        """
        Constructor for base card.
        
        Args:
            title (str): The title text to display on the card
        """
        self.title = title
    
    def draw(self, draw, x, y, w, h):
        """
        Draw the base card (border + title).
        All subclasses will call this via super().draw()
        
        Args:
            draw: PIL ImageDraw object
            w: Image width
            h: Image height
        """
        padding = 12
        
        # Draw border rectangle
        # draw.rectangle expects (x1, y1, x2, y2)
        draw.rectangle(
            (x + padding, y + padding, x + w - padding, y + h - padding),
            outline=(0, 0, 0),
            width=2
        )
        
        # Draw title text
        # draw.text expects (x, y) position
        draw.text(
            (x + padding + 8, y + padding + 8),
            self.title,
            fill=(0, 0, 0)
        )
        
        # ============================================================
        # CHALLENGE 1 TODO: Add a footer bar here
        # ============================================================
        # After you complete CHECKPOINT 4, come back here and add:
        footer_y = h - 20
        draw.line((padding, footer_y, w - padding, footer_y), fill=(0,0,0), width=2)
        # 
        # Observe: Both PetCard AND ItemCard will get the footer automatically!
        # That's the power of inheritance - change ONE place, affect ALL subclasses.


# ============================================================
# CHECKPOINT 3: PetCard - First Subclass
# ============================================================
# PetCard INHERITS from BaseCard (notice the (BaseCard) in line below)
# This means PetCard automatically gets border + title from BaseCard.
# We only add what's UNIQUE to pet cards: the level badge.

class PetCard(BaseCard):
    """Pet card with a level badge - inherits border/title from BaseCard"""
    


    def __init__(self, title, badge_text):
        """
        Constructor for pet card.
        
        IMPORTANT: Notice we call super().__init__(title)
        This tells BaseCard to handle the title setup.
        
        Args:
            title (str): Card title (handled by BaseCard)
            badge_text (str): Text for the pet badge (e.g., "LV 5")
        """
        # Ask the parent (BaseCard) to handle title
        super().__init__(title)
        # Store our pet-specific data
        self.badge_text = badge_text
    
    def draw(self, draw, x, y, w, h):
        """
        Draw pet card = base card + pet badge
        
        CRITICAL LINE: super().draw(draw, w, h)
        This calls BaseCard.draw() to get border + title
        Then we add ONLY the pet-specific badge
        """
        # ============================================================
        # CHECKPOINT 3 EXPERIMENT: Comment out the next line
        # ============================================================
        # Try commenting out super().draw(draw, w, h) and generate the image.
        # What disappears? (Answer: border and title)
        # Uncomment it and generate again. What comes back?
        # This proves super() calls the parent's method to reuse its code!
        
        super().draw(draw, x, y, w, h)  # Reuse base card drawing
        #super(), get parent class method
        #.draw, find the function name draw and call it
        #(draw, w, h), pass in the parameters draw is pen, w is width, h is height
        
        # Now add ONLY pet-specific badge
        badge_w = 60
        badge_h = 22
        badge_x = x + w - badge_w - 16
        badge_y = y + 16
        
        # Draw badge rectangle
        draw.rectangle(
            (badge_x, badge_y, badge_x + badge_w, badge_y + badge_h),
            outline=(0, 0, 0),
            width=2
        )
        
        # Draw badge text
        draw.text(
            (badge_x + 6, badge_y + 4),
            self.badge_text,
            fill=(0, 0, 0)
        )
        
        # ============================================================
        # PRACTICE TODOS (After CHECKPOINT 3)
        # ============================================================
        # TODO 1: Move the badge to bottom-right corner
        #   Hint: Change badge_y to use (h - badge_h - 16)
        
        # TODO 2: Change badge color to blue
        #   Hint: Change fill=(0, 0, 0) to fill=(0, 0, 255)
        
        # TODO 3: Make badge bigger
        #   Hint: Increase badge_w and badge_h
        
        # ============================================================
        # SURPRISE TODO
        # ============================================================
        # Add a tiny star icon (★) next to the badge text
        # Hint: draw.text((badge_x - 10, badge_y + 4), "★", fill=(255,215,0))


# ============================================================
# CHECKPOINT 4 TODO: ItemCard - Second Subclass
# ============================================================
# Create a second subclass to prove inheritance works for multiple types!
# Follow the same pattern as PetCard:
# 1. Inherit from BaseCard
# 2. Call super().__init__(title) in __init__
# 3. Call super().draw(draw, w, h) in draw()
# 4. Add ONLY item-specific rarity stars

# Uncomment and complete this:
class ItemCard(BaseCard):
    """Item card with rarity stars - inherits border/title from BaseCard"""
    
    def __init__(self, title, rarity):
        # Call super().__init__(title) to let BaseCard handle title
        super().__init__(title)
        
        # Store rarity in self.rarity
        self.rarity = rarity
    
    def draw(self, draw, x, y, w, h):
        # Call super().draw(draw, w, h) to get border/title
        super().draw(draw, x, y, w, h)
        
        # Add rarity stars in top-right
        star_x = x + w - 70
        star_y = y + 20
        draw.text((star_x, star_y), f"★ {self.rarity}", fill=(255, 165, 0))


# ============================================================
# CHALLENGE 3 TODO: QuestCard - Third Subclass (Speed Test)
# ============================================================
# Time yourself! How fast can you create a new card type with inheritance?
# 
# Requirements:
# - Inherits from BaseCard
# - __init__ takes (title, difficulty) - difficulty is like "Hard" or "Easy"
# - draw() calls super().draw() then shows difficulty at bottom
# 
# Template:
# class QuestCard(BaseCard):
#     def __init__(self, title, difficulty):
#         # Your code here
#         
#     
#     def draw(self, draw, w, h):
#         # Your code here


# ============================================================
# The Plugin Class (Don't modify unless you're doing stretch)
# ============================================================

class InheritancePractice(BasePlugin):
    def generate_image(self, settings, device_config):
        """Generate the card display"""
        w, h = device_config.get_resolution()
        
        # Create blank white canvas
        img = Image.new("RGB", (w, h), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        
        # ============================================================
        # CHECKPOINT 2-3: Single PetCard
        # ============================================================
        pet_card = PetCard("Fluffy", "LV 5")
        pet_card.draw(draw, 10, 10, 220, 100) 

        item_card = ItemCard("Magic Sword", "Rare")
        item_card.draw(draw, 10, h // 2, 220, 100)
        
        # ============================================================
        # CHECKPOINT 4: Multiple Cards (Uncomment after creating ItemCard)
        # ============================================================
        # Display both PetCard and ItemCard to prove inheritance works!
        # 
        # pet_card = PetCard("Fluffy", "LV 5")
        # pet_card.draw(draw, 10, 10)
        # 
        # item_card = ItemCard("Magic Sword", "Rare")
        # item_card.draw(draw, 10, h // 2)
        
        # ============================================================
        # CHALLENGE 3: All Three Cards (After creating QuestCard)
        # ============================================================
        # quest_card = QuestCard("Dragon Slayer", "Hard")
        # quest_card.draw(draw, 10, h - 80)
        
        return img


# ============================================================
# LEARNING NOTES
# ============================================================
"""
KEY CONCEPTS YOU'RE PRACTICING:

1. BASE CLASS (BaseCard):
   - Holds code SHARED by all card types (border, title)
   - Written ONCE, used by ALL subclasses
   - Think: Toyota's platform used by Camry/RAV4/Prius

2. INHERITANCE (PetCard(BaseCard)):
   - PetCard "IS-A" BaseCard
   - Automatically gets border and title methods
   - Only adds what's UNIQUE (pet badge)

3. super():
   - super().draw() = "Run parent's draw method"
   - Prevents copy-pasting base code
   - If BaseCard.draw() changes, all subclasses get the update

4. DRY PRINCIPLE:
   - Don't Repeat Yourself
   - Border code written once (BaseCard)
   - Not copy-pasted 3 times (PetCard, ItemCard, QuestCard)

METRICS TO TRACK:
- Without inheritance: 3 cards × 6 lines of border code = 18 lines
- With inheritance: 6 lines (BaseCard) + 3 lines (3 × super() calls) = 9 lines
- SAVINGS: 50% reduction!
- With 10 card types: 60 lines → 15 lines = 75% reduction!

WHEN TO USE INHERITANCE:
✅ When 3+ classes share significant code (Rule of Three)
✅ When there's a clear "IS-A" relationship
✅ When shared code might change (one update affects all)

WHEN NOT TO USE:
❌ Only 1-2 similar classes (duplication not painful yet)
❌ No "IS-A" relationship (Dog is NOT a Database)
❌ Shared code is simple and won't change

DEBUGGING TIPS:
- Missing border/title? Check if you called super().draw()
- AttributeError on self.title? Check if you called super().__init__()
- Unsure what to inherit? Ask: "IS this class A that base class?"
"""
