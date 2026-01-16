# Briefing: C-03 — The Inheritance Practice

You will build a base card and then a special card that **inherits** from it. This mission teaches why inheritance exists and when to use `super()`.

---

## The Problem: Copy-Paste Nightmare

Imagine you're building a card system for your game. You need different types of cards: Pet cards, Item cards, Quest cards, Achievement cards.

Without inheritance, your code looks like this:

```python
class PetCard:
    def __init__(self, title, pet_level):
        self.title = title
        self.pet_level = pet_level
    
    def draw(self, draw, w, h):
        # Draw border
        padding = 12
        draw.rectangle((padding, padding, w - padding, h - padding), 
                      outline=(0,0,0), width=2)
        # Draw title
        draw.text((padding + 8, padding + 8), self.title, fill=(0,0,0))
        # Draw pet-specific badge
        draw.rectangle((w - 76, 16, w - 16, 38), outline=(0,0,0), width=2)
        draw.text((w - 70, 20), f"LV {self.pet_level}", fill=(0,0,0))

class ItemCard:
    def __init__(self, title, rarity):
        self.title = title
        self.rarity = rarity
    
    def draw(self, draw, w, h):
        # Draw border (SAME CODE!)
        padding = 12
        draw.rectangle((padding, padding, w - padding, h - padding), 
                      outline=(0,0,0), width=2)
        # Draw title (SAME CODE!)
        draw.text((padding + 8, padding + 8), self.title, fill=(0,0,0))
        # Draw item-specific icon
        draw.text((w - 70, 20), f"★ {self.rarity}", fill=(0,0,0))

class QuestCard:
    def __init__(self, title, difficulty):
        self.title = title
        self.difficulty = difficulty
    
    def draw(self, draw, w, h):
        # Draw border (SAME CODE AGAIN!)
        padding = 12
        draw.rectangle((padding, padding, w - padding, h - padding), 
                      outline=(0,0,0), width=2)
        # Draw title (SAME CODE AGAIN!)
        draw.text((padding + 8, padding + 8), self.title, fill=(0,0,0))
        # Draw quest-specific indicator
        draw.text((w - 70, 20), f"Lvl {self.difficulty}", fill=(0,0,0))
```

**The Pain Points:**
- **Lines 11-15** are copy-pasted in all 3 classes (9 duplicated lines!)
- Your designer says: "Make the border thicker" → You need to change 3 places
- Your designer says: "Change the background color" → Change 3 places
- You add a 4th card type → Copy-paste the shared code AGAIN
- You forget to update one class → Cards look inconsistent (BUG!)

**When your designer makes 10 changes, you're changing 30 places. One missed update = broken game.**

---

## The Solution: Inheritance to the Rescue

**Inheritance** is like creating a "family" of classes. The parent class (base class) holds everything that's SHARED. The children (subclasses) only add what's UNIQUE.

Think of it like car manufacturing:
- **Base Class** = Toyota's standard platform (chassis, engine basics, safety features)
- **Subclasses** = Camry (adds sedan body), RAV4 (adds SUV body), Prius (adds hybrid system)

Each car model **inherits** the platform, then adds its specialty. If Toyota improves the safety system, ALL models get it automatically!

Here's the same card system with inheritance:

```python
class BaseCard:
    """The shared foundation for ALL cards"""
    def __init__(self, title):
        self.title = title
    
    def draw(self, draw, w, h):
        # Border (defined ONCE)
        padding = 12
        draw.rectangle((padding, padding, w - padding, h - padding), 
                      outline=(0,0,0), width=2)
        # Title (defined ONCE)
        draw.text((padding + 8, padding + 8), self.title, fill=(0,0,0))

class PetCard(BaseCard):
    def __init__(self, title, pet_level):
        super().__init__(title)  # Ask parent to handle title
        self.pet_level = pet_level
    
    def draw(self, draw, w, h):
        super().draw(draw, w, h)  # Draw the base card first
        # Add ONLY the pet-specific badge
        draw.rectangle((w - 76, 16, w - 16, 38), outline=(0,0,0), width=2)
        draw.text((w - 70, 20), f"LV {self.pet_level}", fill=(0,0,0))

class ItemCard(BaseCard):
    def __init__(self, title, rarity):
        super().__init__(title)
        self.rarity = rarity
    
    def draw(self, draw, w, h):
        super().draw(draw, w, h)  # Reuse base drawing
        # Add ONLY the item-specific icon
        draw.text((w - 70, 20), f"★ {self.rarity}", fill=(0,0,0))

class QuestCard(BaseCard):
    def __init__(self, title, difficulty):
        super().__init__(title)
        self.difficulty = difficulty
    
    def draw(self, draw, w, h):
        super().draw(draw, w, h)  # Reuse base drawing
        # Add ONLY the quest-specific indicator
        draw.text((w - 70, 20), f"Lvl {self.difficulty}", fill=(0,0,0))
```

**Benefits:**
- Border and title code written ONCE (in BaseCard)
- Designer says "thicker border"? → Change ONE place (BaseCard.draw)
- Add 10 more card types? → Each only writes 3-5 lines (their unique part)
- Shared behavior stays consistent across ALL cards
- No copy-paste = no bugs from forgetting to update one class

**When your designer makes 10 changes to shared elements, you change 1 place instead of 30.**

---

## Breaking It Down

### 1) Base Class = "Common Foundation"

**Analogy**: Like a building foundation that all apartments share (plumbing, electricity, structure). Each apartment then adds its own style.

**Definition**: A base class holds behavior or data that many subclasses share.

**Before/After:**

```python
# Before (no base class): Repeat shared code everywhere
class PetCard:
    def draw(self, draw, w, h):
        draw.rectangle(...)  # Shared border
        draw.text(...)       # Shared title
        draw.text(...)       # Pet-specific badge

class ItemCard:
    def draw(self, draw, w, h):
        draw.rectangle(...)  # DUPLICATE: Same border code
        draw.text(...)       # DUPLICATE: Same title code
        draw.text(...)       # Item-specific icon

# After (with base class): Write shared code ONCE
class BaseCard:
    def draw(self, draw, w, h):
        draw.rectangle(...)  # Shared border (ONCE)
        draw.text(...)       # Shared title (ONCE)

class PetCard(BaseCard):
    def draw(self, draw, w, h):
        super().draw(draw, w, h)  # Reuse base drawing
        draw.text(...)             # ONLY pet-specific part
```

**Why Better**: Change border thickness? Before = edit 2 classes. After = edit 1 class.

**Common Mistakes**:
- Putting unique (not shared) code in the base class
- Making base class too specific instead of general

**Where Used**: `class BaseCard` in `c03_inheritance_practice.py`

**Scalability**: With 20 card types, before = 600 duplicated lines. After = 30 lines (one base, 20 tiny subclasses).

---

### 2) Inheritance = "Is-A Relationship"

**Analogy**: A Prius **is a** Toyota car. It has everything a Toyota car has (wheels, engine, steering), plus hybrid-specific features.

**Definition**: A subclass inherits behavior from a base class by putting the base class name in parentheses.

**Before/After:**

```python
# Before: No relationship, each card starts from scratch
class PetCard:
    # Write EVERYTHING from scratch
    pass

class ItemCard:
    # Write EVERYTHING from scratch again
    pass

# After: Inheritance establishes relationship
class PetCard(BaseCard):  # PetCard IS-A BaseCard
    # Automatically gets all BaseCard methods
    # Only write what's DIFFERENT
    pass
```

**Why Better**: PetCard gets `draw()` for free. Only override if you need to add/change something.

**Common Mistakes**:
- Using inheritance when there's no "is-a" relationship
  - Bad: `class Dog(Database)` (Dog is NOT a Database)
  - Good: `class Dog(Animal)` (Dog IS an Animal)
- Inheriting from the wrong base class

**Where Used**: `class PetCard(BaseCard)` in `c03_inheritance_practice.py`

**Team Collaboration**: When your teammate sees `class PetCard(BaseCard)`, they instantly know: "Ah, it's a type of card, so it probably has a title and border."

---

### 3) super() = "Ask the Parent for Help"

**Analogy**: Like asking your parent for help with homework. You don't redo the work they already did; you start from where they finished.

**Definition**: `super()` calls the parent class's method, so you can reuse its logic and then add your own.

**Before/After:**

```python
# Before: Copy-paste parent's code into child
class PetCard(BaseCard):
    def draw(self, draw, w, h):
        # COPY-PASTE all the base drawing code
        padding = 12
        draw.rectangle((padding, padding, w - padding, h - padding), 
                      outline=(0,0,0), width=2)
        draw.text((padding + 8, padding + 8), self.title, fill=(0,0,0))
        
        # Add pet-specific part
        draw.text((w - 70, 20), f"LV {self.pet_level}", fill=(0,0,0))

# After: Use super() to reuse parent's work
class PetCard(BaseCard):
    def draw(self, draw, w, h):
        super().draw(draw, w, h)  # Ask BaseCard to draw itself
        # Add ONLY pet-specific part
        draw.text((w - 70, 20), f"LV {self.pet_level}", fill=(0,0,0))
```

**Why Better**: If BaseCard.draw() changes, PetCard automatically uses the new version. No manual updates needed!

**Common Mistakes**:
- Forgetting `super()` and losing parent's work
- Calling `super()` in the wrong order (e.g., drawing badge BEFORE border)

**Where Used**: `super().__init__(title)` and `super().draw(...)` in `c03_inheritance_practice.py`

**Real-World Example**: 
- Parent changes border from 2px to 3px
- Without `super()`: You must find and update 20 subclasses
- With `super()`: All 20 subclasses get the update automatically

---

## Key Principle: DRY (Don't Repeat Yourself)

Inheritance is the answer to: "I'm copy-pasting the same code everywhere."

**Rule of Thumb**:
- 1-2 classes with similar code? → OK to duplicate (for now)
- 3+ classes with similar code? → Time to extract a base class
- Changing shared code requires updating N classes? → DEFINITELY need inheritance

---

## What "Success" Looks Like

- The subclass calls `super()` to reuse parent's work
- The subclass only writes its UNIQUE behavior (not duplicating base behavior)
- Changing the base class affects all subclasses automatically (intentionally!)
- Code is shorter, clearer, and easier to maintain

Use/avoid guidance is practiced in `bad_code.py`.
