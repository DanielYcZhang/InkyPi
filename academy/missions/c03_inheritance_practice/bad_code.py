"""
Refactoring Challenge (C-03): Inheritance

You'll experience why inheritance and super() matter by trying to add features
to code that copy-pastes instead of inheriting.

Stage 1: Working Code (GIVEN)
Stage 2: Feature Request (TODO - using the given code)
Stage 3: Refactored Version (TODO - using inheritance)
Stage 4: Same Feature Request (TODO - using your refactored code)

You can run this file: python3 bad_code.py
"""

# ============================================================
# STAGE 1: Working Code (but with copy-paste instead of inheritance)
# ============================================================
# This works TODAY, but it copy-pastes the base drawing code.
# Let's see what happens when requirements change...

class PetCard_Bad:
    """Card that duplicates base drawing code"""
    def __init__(self, title, level):
        self.title = title
        self.level = level
    
    def draw(self, draw, w, h):
        # Draw border
        padding = 12
        draw.rectangle((padding, padding, w - padding, h - padding), 
                      outline=(0,0,0), width=2)
        # Draw title
        draw.text((padding + 8, padding + 8), self.title, fill=(0,0,0))
        # Draw level badge
        draw.rectangle((w - 76, 16, w - 16, 38), outline=(0,0,0), width=2)
        draw.text((w - 70, 20), f"LV {self.level}", fill=(0,0,0))

class ItemCard_Bad:
    """Card that DUPLICATES base drawing code (BAD!)"""
    def __init__(self, title, rarity):
        self.title = title
        self.rarity = rarity
    
    def draw(self, draw, w, h):
        # Draw border (SAME CODE as PetCard!)
        padding = 12
        draw.rectangle((padding, padding, w - padding, h - padding), 
                      outline=(0,0,0), width=2)
        # Draw title (SAME CODE as PetCard!)
        draw.text((padding + 8, padding + 8), self.title, fill=(0,0,0))
        # Draw rarity stars
        draw.text((w - 70, 20), f"★ {self.rarity}", fill=(0,0,0))

def stage1_demo():
    """Stage 1: This works but has duplication"""
    draw = FakeDraw()
    pet = PetCard_Bad("Fluffy", 5)
    item = ItemCard_Bad("Magic Sword", "Rare")
    
    print("  PetCard:")
    pet.draw(draw, 200, 100)
    print("\n  ItemCard:")
    item.draw(draw, 200, 100)

# ============================================================
# STAGE 2: FEATURE REQUEST #1 (on bad code)
# ============================================================
"""
PRODUCT MANAGER REQUEST:
"We need to add a subtitle to ALL cards, and add a third card type (QuestCard)."

TODO: 
1. Add a `subtitle` parameter to both PetCard_Bad and ItemCard_Bad
2. Draw the subtitle at (padding + 8, padding + 28) in both classes
3. Create a new QuestCard_Bad class with title, subtitle, and difficulty level
4. Copy-paste the base drawing code into QuestCard_Bad

Count your metrics:
- New/modified lines in PetCard_Bad: ___
- New/modified lines in ItemCard_Bad: ___
- New/modified lines in QuestCard_Bad: ___
- Total lines changed: ___
- Number of places where subtitle drawing is duplicated: ___
- Pain level (1-10): ___
"""

class PetCard_Bad_WithSubtitle:
    # TODO: Add subtitle parameter and draw it
    pass

class ItemCard_Bad_WithSubtitle:
    # TODO: Add subtitle parameter and draw it (copy-paste!)
    pass

class QuestCard_Bad:
    # TODO: Create new card, copy-paste ALL the base drawing code
    pass

def stage2_demo():
    """Stage 2: Feature request on bad code"""
    draw = FakeDraw()
    try:
        pet = PetCard_Bad_WithSubtitle("Fluffy", "Loyal Companion", 5)
        item = ItemCard_Bad_WithSubtitle("Magic Sword", "Ancient Relic", "Rare")
        quest = QuestCard_Bad("Dragon Slayer", "Defeat the dragon", 10)
        
        print("  PetCard with subtitle:")
        pet.draw(draw, 200, 100)
        print("\n  ItemCard with subtitle:")
        item.draw(draw, 200, 100)
        print("\n  QuestCard:")
        quest.draw(draw, 200, 100)
    except Exception as e:
        print(f"  Not implemented yet: {e}")

# ============================================================
# STAGE 3: REFACTORED VERSION (using inheritance)
# ============================================================
"""
Rewrite using a BaseCard class and inheritance.

Hint: 
- Create BaseCard with __init__(title, subtitle) and draw() method
- Make PetCard, ItemCard, QuestCard inherit from BaseCard
- Use super().__init__(...) and super().draw(...) to reuse base code
"""

class BaseCard:
    # TODO: Implement base class with shared code
    pass

class PetCard_Good(BaseCard):
    # TODO: Inherit from BaseCard, use super()
    pass

class ItemCard_Good(BaseCard):
    # TODO: Inherit from BaseCard, use super()
    pass

class QuestCard_Good(BaseCard):
    # TODO: Inherit from BaseCard, use super()
    pass

def stage3_demo():
    """Stage 3: Refactored with inheritance"""
    draw = FakeDraw()
    try:
        pet = PetCard_Good("Fluffy", "Loyal Companion", 5)
        item = ItemCard_Good("Magic Sword", "Ancient Relic", "Rare")
        quest = QuestCard_Good("Dragon Slayer", "Defeat the dragon", 10)
        
        print("  PetCard (refactored):")
        pet.draw(draw, 200, 100)
        print("\n  ItemCard (refactored):")
        item.draw(draw, 200, 100)
        print("\n  QuestCard (refactored):")
        quest.draw(draw, 200, 100)
    except Exception as e:
        print(f"  Not implemented yet: {e}")

# ============================================================
# STAGE 4: SAME FEATURE REQUEST (on good code)
# ============================================================
"""
SAME REQUEST: Add subtitle to all cards, plus new QuestCard type.

But now you have inheritance! Count the changes:
- Lines changed in BaseCard: ___
- Lines changed in PetCard_Good: ___
- Lines changed in ItemCard_Good: ___
- Lines needed for QuestCard_Good: ___
- Total lines: ___
- Pain level (1-10): ___

Compare Stage 2 vs Stage 4:
- Improvement ratio: ___ (Stage 2 total ÷ Stage 4 total)
- Duplicated code: Stage 2 = ___ places, Stage 4 = ___ places
"""

# The good news: You already did this in Stage 3!
# The subtitles are in BaseCard, so ALL cards get them automatically.
# Compare your effort in Stage 2 vs Stage 3.

# ============================================================
# TESTING HARNESS
# ============================================================

class FakeDraw:
    """Simulates drawing commands for testing"""
    def rectangle(self, box, outline=None, width=1):
        print(f"    rectangle {box}")
    
    def text(self, pos, text, fill=None):
        print(f"    text at {pos}: '{text}'")

if __name__ == "__main__":
    print("="*60)
    print("Stage 1: Working Code (with duplication)")
    print("="*60)
    stage1_demo()
    
    print("\n" + "="*60)
    print("Stage 2: Feature Request on Bad Code")
    print("="*60)
    stage2_demo()
    
    print("\n" + "="*60)
    print("Stage 3: Refactored Version (with inheritance)")
    print("="*60)
    stage3_demo()
    
    print("\n" + "="*60)
    print("COMPARISON: Stage 2 (bad) vs Stage 3 (good)")
    print("="*60)
    print("Notice: In Stage 3, adding subtitle was AUTOMATIC!")
    print("BaseCard handles it, so all subclasses get it for free.")
