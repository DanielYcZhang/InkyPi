# Mission Instructions: The Inheritance Practice

**Objective**: Build a base card class and specialized cards that inherit from it using `super()`.

---

## Why This Mission Matters

You just learned to create classes for creatures. But what if you're building a game with 20 different card types: PetCards, ItemCards, QuestCards, AchievementCards, PowerCards...

Each card type needs:
- **Shared stuff**: Border, title, background (same for ALL cards)
- **Unique stuff**: Pet badge, item rarity stars, quest difficulty indicator (different per type)

Without inheritance, you'll copy-paste the shared code 20 times. With inheritance, you write it ONCE.

**Real-world connection**:
- **Hearthstone/Magic**: Hundreds of card types, all share border/mana cost display, each has unique abilities
- **Pokemon TCG**: All cards have HP/attacks display, but each pokemon draws its own artwork/type
- **Mobile RPGs**: Base character stats display + specialized class indicators (Warrior/Mage/Rogue)

**The problem we're solving**:
From the briefing, you saw that without inheritance, 3 card types means:
- 9 lines of border code (duplicated × 3)
- 9 lines of title code (duplicated × 3)
- Designer says "thicker border"? → Update 3 places (and hope you don't miss one!)
- Add 4th card type? → Copy-paste 6 more lines

**What success looks like**:
- **Technically**: BaseCard draws border/title once, PetCard adds only pet-specific badge
- **Conceptually**: You understand inheritance prevents duplication via `super()`
- **Practically**: Designer changes border? Update ONE place. Add 10 card types? Each only writes 5 unique lines

---

## Step 0: Understand the Problem First

**Before writing any code, build your mental model:**

1. **Read `briefing.md`** - Review the problem story showing 3 card classes with duplicated border/title code. See how inheritance with `super()` solves it.

2. **Mental Model Check** - After reading the briefing, write your answers:
   
   **Q: In one sentence, what problem does inheritance solve?**
   
   
   
   **Q: Without inheritance, if you have 5 card types and need to change the border thickness, how many places do you update?**
   
   

3. **Key Analogy Check**: Can you explain the Toyota/Camry/RAV4 analogy?
   - Toyota platform (base class) = shared features
   - Camry/RAV4 (subclasses) = inherit platform + add unique body
   - If Toyota improves safety, all models get it automatically

If you can explain this, you're ready!

---

## Build (Incremental Checkpoints)

### 🎯 CHECKPOINT 1: Plugin Registers (5 minutes)

**Goal**: Your plugin appears in the web UI dropdown

**Why this checkpoint matters**: Confirms basic setup

**Steps**:
1. Create plugin folder:
   ```bash
   cd ~/InkyPi
   mkdir -p src/plugins/c03_inheritance_practice
   ```

2. Create `src/plugins/c03_inheritance_practice/plugin-info.json`:
   ```json
   {
     "display_name": "C03 Inheritance Practice",
     "id": "c03_inheritance_practice",
     "class": "InheritancePractice"
   }
   ```

3. Restart service:
   ```bash
   sudo systemctl restart inkypi.service
   ```

**✅ Success Looks Like**:
- [ ] "C03 Inheritance Practice" appears in plugin dropdown
- [ ] No errors in terminal

**🚫 If Stuck**:
- Verify JSON syntax
- Check folder name matches `id`

**💭 Pause and Reflect** (30 seconds):
*You've done this twice already (C01, C02). What's the pattern you're seeing in all plugin-info.json files?*

---

### 🎯 CHECKPOINT 2: Base Card Appears (10 minutes)

**Goal**: A simple card with border and title displays

**Why this checkpoint matters**: Proves the BASE class works before adding subclasses

**Steps**:
1. Copy template:
   ```bash
   cp academy/missions/c03_inheritance_practice/c03_inheritance_practice.py src/plugins/c03_inheritance_practice/
   ```

2. Open the file in VS Code

3. Look at the `BaseCard` class (lines 5-14):
   - `__init__` takes `title` parameter
   - `draw()` method draws border and title

4. Generate the image in web UI

**✅ Success Looks Like**:
- [ ] A card with black border appears
- [ ] "Pet Profile" title is visible
- [ ] Badge in top-right corner (from PetCard)

**💭 Pause and Reflect**:
*Look at lines 23-24 in PetCard.draw():*
```python
super().draw(draw, w, h)
```
*What does this line do? Why don't we re-write the border/title code in PetCard?*

**Answer space**:


---

### 🎯 CHECKPOINT 3: Understanding super() (15 minutes)

**Goal**: Understand what `super()` does by tracing the execution

**Why this checkpoint matters**: `super()` is the key to preventing duplication

**The Experiment**:
1. In `PetCard.draw()`, **comment out** line 24:
   ```python
   # super().draw(draw, w, h)  # COMMENTED OUT
   ```

2. Generate the image

3. **Observe**: What's missing?

4. Uncomment line 24, generate again

5. **Compare**: What came back?

**✅ Success Looks Like**:
- [ ] Without `super()`: Only badge visible (no border, no title)
- [ ] With `super()`: Border + title + badge

**💭 Pause and Reflect - The "Aha!" Moment**:
*Answer these:*

**Q1: When you commented out `super().draw()`, what disappeared?**  


**Q2: What does this prove about what `super()` does?**  


**Q3: If BaseCard.draw() is 6 lines of code, how many lines did `super()` save you from duplicating?**  


**Key Insight**: `super()` = "run the parent's method first, then I'll add my extras"

---

### 🎯 CHECKPOINT 4: Multiple Card Types (20 minutes)

**Goal**: Create a second subclass to prove inheritance is reusable

**Why this checkpoint matters**: Inheritance pays off when you have MULTIPLE subclasses sharing the SAME base

**Steps**:
1. In the same file, after `PetCard` class, add a new subclass:

```python
class ItemCard(BaseCard):
    def __init__(self, title, rarity):
        super().__init__(title)
        self.rarity = rarity
    
    def draw(self, draw, w, h):
        super().draw(draw, w, h)  # Reuse base border/title
        
        # Add ONLY item-specific rarity stars
        star_x = w - 70
        star_y = 20
        draw.text((star_x, star_y), f"★ {self.rarity}", fill=(255, 165, 0))
```

2. In `generate_image()`, create BOTH cards:
```python
pet_card = PetCard("Fluffy", "LV 5")
pet_card.draw(draw, 10, 10)

item_card = ItemCard("Magic Sword", "Rare")
item_card.draw(draw, 10, h // 2)
```

3. Generate the image

**✅ Success Looks Like**:
- [ ] Two cards appear (top half: pet, bottom half: item)
- [ ] Both have border + title (from BaseCard)
- [ ] Pet has badge, item has stars
- [ ] You didn't duplicate the border/title code

**💭 Pause and Reflect - Count the Savings**:
*Fill in the metrics:*

**Without inheritance (copy-paste approach)**:
- BaseCard border code: 6 lines
- PetCard duplicates it: 6 lines
- ItemCard duplicates it: 6 lines
- **Total border code**: 18 lines

**With inheritance (`super()` approach)**:
- BaseCard border code: 6 lines
- PetCard: 1 line (`super().draw()`)
- ItemCard: 1 line (`super().draw()`)
- **Total**: 8 lines

**Savings**: 18 - 8 = ___ lines saved (for just 2 subclasses!)

**If you had 10 card types**:
- Without inheritance: 6 × 10 = 60 lines
- With inheritance: 6 + (1 × 9) = 15 lines
- **Savings**: ___ lines!

---

## Practice Challenges (Learning Through Experimentation)

### 🎯 Challenge 1: Add Shared Behavior to BaseCard
**Learning Objective**: Changes to the base class affect ALL subclasses automatically

**The Challenge**:
1. In `BaseCard.draw()`, add a footer bar at the bottom:
   ```python
   # After the title, add:
   footer_y = h - 20
   draw.line((padding, footer_y, w - padding, footer_y), fill=(0, 0, 0), width=2)
   ```

2. Generate the image

**Observe This**:
- Both PetCard AND ItemCard now have footer bars
- You added code to ONE place (BaseCard)
- Both subclasses inherited it automatically

**Reflection Question**:
*If you had 20 card types and added this footer, how many classes would you need to update?*
- Without inheritance: ___
- With inheritance: ___

---

### 🎯 Challenge 2: Break It to Understand It
**Learning Objective**: Understanding what happens when you forget `super()`

**The Challenge**:
1. In `ItemCard.__init__`, **remove** the `super().__init__(title)` line
2. Try to generate the image
3. **Observe the error message**

**Observe This**:
- What error appears? (Copy it):


- Which line causes it? ___

- What does this tell you about `super().__init__()`?

**Fix It**:
- Add `super().__init__(title)` back
- Verify it works again

**Reflection**:
*Why do you need `super().__init__(title)` in the child class? What would break if you just set `self.title = title` yourself?*

(Hint: For this simple case, it would work! But `super().__init__()` ensures the parent's setup logic runs. If BaseCard had more complex initialization, you'd need it.)

---

### 🎯 Challenge 3: Third Card Type (Speed Test)
**Learning Objective**: With inheritance, adding new types is FAST

**The Challenge**:
Create a `QuestCard` class with a difficulty indicator:
- Inherits from `BaseCard`
- `__init__` takes `title` and `difficulty`
- `draw()` calls `super().draw()` then adds difficulty text

**Time yourself**: How long to add a complete new card type?

**Template to fill**:
```python
class QuestCard(BaseCard):
    def __init__(self, title, difficulty):
        # TODO: Your code here
        
    
    def draw(self, draw, w, h):
        # TODO: Your code here
```

**Reflection**:
- How many lines of code did you write? ___
- How much of the base functionality (border/title) did you get for free? ___
- **Time to create**: ___ minutes

*Compare: Without inheritance, you'd rewrite border code (6 lines) + title code (2 lines) + difficulty code (2 lines) = 10 lines*

---

## Self-Learning Module (Required)

Complete these exercises to deepen your understanding:

📝 **explain.md** - Answer questions about Vehicle/ElectricCar/Motorcycle inheritance
- 22 line-specific questions
- Transfer challenge: Design Weapon/Sword/Bow system

🐛 **debug_detective.md** - Find 3 bugs in broken inheritance code
- Not using `super().__init__()`
- Duplicating parent code instead of calling `super().draw()`
- Missing the concept entirely

🔄 **bad_code.py** - 4-Stage refactoring journey:
- Stage 1: PetCard, ItemCard, QuestCard with DUPLICATED border code
- Stage 2: Feature request - "Add subtitle to all cards" → Count pain (30+ lines)
- Stage 3: Refactor with BaseCard + inheritance
- Stage 4: Same request → Count relief (5 lines)
- **Target ratio: 6:1 improvement**

📊 **bad_code_explain.md** - Analyze with 33 questions:
- Part 1: Change Impact Metrics (Stage 2 vs 4 comparison)
- Part 2: Team Collaboration ("teammate adds AchievementCard")
- Part 3: Second Feature Request (background color)
- Part 4: When NOT to use inheritance (Rule of Three, unrelated classes)
- Part 5: Real-World (mobile games with 50 card types)

**Run validation**:
```bash
cd ~/InkyPi/academy/missions/c03_inheritance_practice
python3 check.py
```

---

## Success Criteria (Skills You've Proven)

### ✅ Skill 1: Base Class Extraction - DRY Principle

**The Test**:
- [ ] BaseCard contains shared code (border, title)
- [ ] PetCard and ItemCard both call `super().draw()`
- [ ] Adding footer to BaseCard affects both subclasses

**This Proves**: You understand extracting shared behavior to prevent duplication

**Metrics** (from bad_code exercise):
- Without inheritance: ___ lines for 3 card types
- With inheritance: ___ lines for 3 card types
- Improvement ratio: ___ : 1

---

### ✅ Skill 2: Using super() - Reusing Parent Logic

**The Test**:
- [ ] Removed `super().draw()` and observed missing border/title
- [ ] Understand `super()` = "run parent method first"
- [ ] Know when to call `super().__init__()`

**This Proves**: You understand `super()` prevents copy-paste

**Real-World Parallel**: Just like ElectricCar calls super() to get base Vehicle features, then adds battery info

---

### ✅ Skill 3: Inheritance Hierarchy - Is-A Relationship

**The Test**:
- [ ] Can explain: "PetCard IS-A BaseCard"
- [ ] Know PetCard automatically has `title` property (from BaseCard)
- [ ] Completed Challenge 3 (QuestCard) in < 5 minutes

**This Proves**: You recognize when to use inheritance (shared + unique)

---

### ✅ Skill 4: Pattern Recognition (from explain.md)

**The Test**:
- [ ] Answered questions about Vehicle/ElectricCar code
- [ ] Identified where `super()` is called and why
- [ ] Designed Weapon/Sword/Bow system using inheritance

**This Proves**: Can apply inheritance pattern to new domains

---

### ✅ Skill 5: Knowing When NOT to Use Inheritance

**The Test** (from bad_code_explain.md):
- [ ] Listed scenarios where simple code is better (Rule of Three)
- [ ] Identified bad inheritance: `class Dog(Database)` is wrong
- [ ] Know when composition > inheritance

**This Proves**: Nuanced judgment, not just "inheritance is always good"

---

## 🎯 Overall Success = Understanding, Not Just Functionality

**You've truly succeeded when you can**:
- [ ] Explain the copy-paste nightmare without inheritance (show line counts)
- [ ] Predict what changes when you modify BaseCard
- [ ] Justify when to extract a base class (3+ similar classes)
- [ ] Design a simple inheritance hierarchy for a different system

**"Cards display" is baseline. "I understand WHY `super()` prevents duplication" is success.**

---

## Quick Reference Commands

**Create plugin**:
```bash
mkdir -p src/plugins/c03_inheritance_practice
cp academy/missions/c03_inheritance_practice/c03_inheritance_practice.py src/plugins/c03_inheritance_practice/
```

**Restart service**:
```bash
sudo systemctl restart inkypi.service
```

**Validate**:
```bash
cd ~/InkyPi/academy/missions/c03_inheritance_practice
python3 check.py
```

**Test bad_code**:
```bash
python3 bad_code.py
```

**Add icon**:
```bash
cp src/plugins/clock/icon.png src/plugins/c03_inheritance_practice/icon.png
```

---

## Completion Checklist

Before moving to the next mission:

- [ ] CHECKPOINT 1-4 completed (multiple cards display)
- [ ] Challenge 1 (footer bar affects all cards)
- [ ] Challenge 2 (broke and fixed `super()`)
- [ ] Challenge 3 (created QuestCard in < 5 min)
- [ ] Filled explain.md, debug_detective.md, bad_code_explain.md
- [ ] Completed bad_code.py (all 4 stages with metrics)
- [ ] `check.py` passes
- [ ] Can explain Toyota/Camry analogy
- [ ] Know when NOT to use inheritance (Rule of Three)

**Time to celebrate!** You've mastered inheritance - a cornerstone of object-oriented programming.

---

## After This Mission

**Concepts you've internalized**:
- Base class = Shared foundation for similar things
- Inheritance = "Is-a" relationship (PetCard IS-A BaseCard)
- `super()` = Reuse parent's method (prevents duplication)
- `super().__init__()` = Let parent handle its setup
- DRY principle = Don't Repeat Yourself
- Rule of Three = Extract base class when 3+ classes share code

**Next mission preview**: You'll build more complex plugins using OOP principles. You now know classes, objects, inheritance - the building blocks of scalable systems.

**How to review later**: In 1 week, design a game character system (BaseCharacter → Warrior/Mage/Rogue) from scratch. If you use `super()` correctly, you've internalized it!

---

## Mission-Specific Tips

**Common Pitfall**: Forgetting to call `super().draw()` in subclass
- Symptom: Only badge shows, no border/title
- Fix: Always call `super().draw(draw, w, h)` first

**Design Pattern**: Base class → Subclasses
- Base: What ALL variants share
- Subclasses: What makes each unique
- If 80% is shared, inheritance is perfect

**When to stop**: Don't create inheritance hierarchies more than 2-3 levels deep in this course. BaseCard → PetCard is perfect. BaseCard → CardType → SpecialCardType → UltraRareCardType gets confusing fast!
