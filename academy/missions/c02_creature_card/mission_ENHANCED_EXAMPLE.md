# Mission Instructions: The Creature Card

**Objective**: Build a plugin that displays a creature card using classes and objects.

---

## Why This Mission Matters

Every game you've played has inventory items, character sheets, enemy profiles, or card collections. Behind the scenes, there's a fundamental question: How do you organize the code for 100 different creatures without copy-pasting everything 100 times?

**Real-world connection**: 
- **Pokemon**: 1000+ pokemon, each with name, type, level, stats. Think they copy-paste the "display pokemon" code 1000 times? No way!
- **Fortnite**: Hundreds of weapons and items in your inventory. Each has a name, rarity, damage, icon.
- **Your phone's contact app**: Each contact has name, phone, email, photo. Same display structure, different data.

**The problem we're solving**: 
Without classes, creating 3 creatures looks like this:
```python
creature1_name = "Pip"
creature1_species = "Cat"  
creature1_level = 5

creature2_name = "Rex"
creature2_species = "Dog"
creature2_level = 7

# Drawing code copy-pasted 3 times...
draw.text((20, 20), f"Name: {creature1_name}")
draw.text((20, 40), f"Species: {creature1_species}")
# ... repeated for creature2, creature3...
```

For 100 creatures? 300 variables + 100 copy-pasted drawing blocks. Change how you display species? Update 100 places. One typo? Game breaks.

**What success looks like**:
- **Technically**: A creature card appears with name, species, and level
- **Conceptually**: You understand why classes organize related data and behavior together
- **Practically**: You can create 100 creatures with 100 clean lines instead of 1000 messy lines

---

## Step 0: Understand the Problem First

**Before writing any code, build your mental model:**

1. **Read `briefing.md`** - See the scattered-variables nightmare, then the class-based rescue. Pay attention to the before/after code comparisons.

2. **Mental Model Check** - After reading the briefing, write your answers:
   
   **Q: In one sentence, what problem does this mission solve?**
   
   
   
   **Q: If you had 50 creatures without classes, what would break when you add a new property (like "health")?**
   
   

3. **Ready check**: Can you explain the difference between a class (blueprint) and an object (thing built from blueprint) using the car/Toyota analogy? If yes, proceed.

---

## Build (Incremental Checkpoints)

### 🎯 CHECKPOINT 1: Plugin Registers (5 minutes)

**Goal**: Your plugin appears in the web UI dropdown (even if it doesn't work yet)

**Why this checkpoint matters**: Confirms InkyPi can discover your plugin. If this fails, nothing else works.

**Steps**:
1. Create plugin folder:
   ```bash
   cd ~/InkyPi
   mkdir -p src/plugins/c02_creature_card
   ```

2. Create `src/plugins/c02_creature_card/plugin-info.json`:
   ```json
   {
     "display_name": "C02 Creature Card",
     "id": "c02_creature_card",
     "class": "CreatureCard"
   }
   ```

3. Restart service:
   ```bash
   sudo systemctl restart inkypi.service
   ```

4. Open web UI and check the plugin dropdown

**✅ Success Looks Like**:
- [ ] "C02 Creature Card" appears in the plugin dropdown
- [ ] No error in terminal when you run `sudo journalctl -u inkypi.service -n 20`

**🚫 If Stuck**:
- Check JSON syntax (commas, quotes, brackets)
- Verify folder name matches `id` field
- Restart the service again

**💭 Pause and Reflect** (30 seconds):
*The plugin-info.json tells InkyPi where to find your code. What would happen if the "class" field was "Creature" instead of "CreatureCard"?*

---

### 🎯 CHECKPOINT 2: Blank Canvas (10 minutes)

**Goal**: Plugin generates a blank white image (no crashes)

**Why this checkpoint matters**: Proves your plugin file loads and can return an image. The foundation before adding creatures.

**Steps**:
1. Copy template:
   ```bash
   cp academy/missions/c02_creature_card/c02_creature_card.py src/plugins/c02_creature_card/
   ```

2. Open `src/plugins/c02_creature_card/c02_creature_card.py` in VS Code

3. Find TODO #1: "Create blank white canvas"
   - Hint: You need `Image.new(...)` with white background
   - The template has comments guiding you

4. In web UI, generate the image

**✅ Success Looks Like**:
- [ ] A blank white rectangle appears on the display
- [ ] No Python errors in the web UI or terminal
- [ ] File size is reasonable (not 0 KB)

**🚫 If Stuck**:
- Check you're returning the `img` object
- Verify `w` and `h` values (from `device_config`)
- Make sure you called `return img` at the end

**💭 Pause and Reflect**:
*You just used `Image.new("RGB", (w, h), (255, 255, 255))`. In your own words, what does each parameter do?*


---

### 🎯 CHECKPOINT 3: First Creature Object (20 minutes)

**Goal**: Create a Creature class with properties, draw ONE creature

**Why this checkpoint matters**: This is the core concept - defining a blueprint (class) and creating a thing from it (object).

**Steps**:
1. Find TODO #2 in the file: "Define Creature class"

2. Create the class with `__init__` method:
   - Takes `name`, `species`, `level` as parameters
   - Stores them in `self.name`, `self.species`, `self.level`

3. Add a `draw()` method to the class:
   - Takes `draw`, `x`, `y` as parameters
   - Draws 3 lines of text: name, species, level

4. In the plugin's `generate_image()` method, create ONE creature:
   ```python
   creature = Creature("Pip", "Cat", 5)
   ```

5. Draw it:
   ```python
   creature.draw(draw, 20, 20)
   ```

6. Generate in web UI

**✅ Success Looks Like**:
- [ ] Three lines of text appear: "Name: Pip", "Species: Cat", "Level: 5"
- [ ] Text is readable and positioned correctly
- [ ] No errors

**💭 Pause and Reflect** - **Compare and Count**:
*Without a class, displaying 3 properties would need:*
- 3 variables: `name = "Pip"`, `species = "Cat"`, `level = 5`
- 3 draw.text() calls

*With a class*:
- 1 object: `creature = Creature("Pip", "Cat", 5)`
- 1 draw call: `creature.draw(...)`

*For 10 creatures:*
- Without class: 30 variables + 30 draw calls = ___ lines
- With class: 10 objects + 10 draw calls = ___ lines
- **The savings**: ___

---

### 🎯 CHECKPOINT 4: Multiple Creatures (15 minutes)

**Goal**: Create and display 3 different creatures to prove the class is reusable

**Steps**:
1. Find TODO #3: "Create multiple creatures"

2. Create 3 creature objects:
   ```python
   creature1 = Creature("Pip", "Cat", 5)
   creature2 = Creature("Rex", "Dog", 7)
   creature3 = Creature("Spark", "Dragon", 12)
   ```

3. Draw them at different Y positions:
   ```python
   creature1.draw(draw, 20, 20)
   creature2.draw(draw, 20, 60)
   creature3.draw(draw, 20, 100)
   ```

**✅ Success Looks Like**:
- [ ] 3 different creatures appear, stacked vertically
- [ ] Each has correct name, species, level
- [ ] All use the same drawing logic (from the class)

**💭 Pause and Reflect**:
*If your designer says "Add a border around each creature's info", how many places in your code need updates?*
- Without class: ___
- With class: ___
- (Answer: 1 - just the `draw()` method in the Creature class!)

---

## Practice Challenges (Learning Through Experimentation)

### 🎯 Challenge 1: Add a New Property
**Learning Objective**: Classes make adding features scalable

**The Challenge**:
Add a `health` property to all creatures:
1. Update `__init__` to accept `health` parameter
2. Store it in `self.health`
3. Display it in the `draw()` method

**Count This**:
- How many places in `__init__` did you change? ___
- How many places in `draw()` did you change? ___
- How many times did you update creature1, creature2, creature3? ___
- **Total changes**: ___

**Reflection**:
*If you had 50 creatures, how many lines would you change with classes vs without?*


---

### 🎯 Challenge 2: Break It to Understand It
**Learning Objective**: Understanding `self` and why it's needed

**The Challenge**:
1. In the `draw()` method, change `self.name` to just `name`
2. Try to generate the image
3. Observe the error message

**Observe This**:
- What error appears? (Copy it):
- Which line fails?

**Reflection**:
- Why does `self.name` work but `name` doesn't?
- What is `self` pointing to?

(Answer: `self` refers to the specific creature object. Without it, Python doesn't know which creature's name you mean!)

---

### 🎯 Challenge 3: Card Borders
**Learning Objective**: Methods can use `self` properties for calculations

**The Challenge**:
In the `Creature.draw()` method, add a rectangle border around each creature's info:
- The border should be sized based on the text
- Hint: Use `self.level` to make higher-level creatures bigger!

**Observe This**:
- Higher level creatures have bigger borders
- All use the same drawing logic

**Reflection**:
*How does putting the `draw()` method INSIDE the class help keep code organized?*

---

## Self-Learning Module (Required)

Complete these exercises to deepen your understanding:

📝 **explain.md** - Answer questions about a Vehicle/ElectricCar inheritance example
- Tests: Can you recognize classes/objects in different code?
- 13 line-specific questions
- Design a Weapon/Sword system to prove you can transfer the pattern

🐛 **debug_detective.md** - Find bugs in broken class code
- Find 3 common mistakes (missing `self`, wrong `__init__`, etc.)
- Connect errors to concepts from briefing

🔄 **bad_code.py** - 4-Stage refactoring journey:
- Stage 1: See scattered variables approach (it works!)
- Stage 2: Add "health" property to 3 creatures → count pain (15+ lines)
- Stage 3: Refactor with classes
- Stage 4: Add "health" again → count relief (3 lines)
- **Target ratio: 5:1 improvement**

📊 **bad_code_explain.md** - Analyze with metrics:
- Part 1: Change Impact (exact line counts)
- Part 2: Team Collaboration ("teammate adds 4th creature")
- Part 3: Scalability (50 creatures scenario)
- Part 4: When classes are overkill (Rule of Three)
- Part 5: Real-world (Pokemon, contact apps)

**Run validation**:
```bash
cd ~/InkyPi/academy/missions/c02_creature_card
python3 check.py
```

---

## Success Criteria (Skills You've Proven)

### ✅ Skill 1: Class Design - Organizing Related Data

**The Test**:
- [ ] Creature class has `__init__` with 3+ properties
- [ ] All properties stored with `self.`
- [ ] Can create multiple objects from same class

**This Proves**: You understand classes as blueprints that group related data (name, species, level belong together)

**Metrics** (from bad_code exercise):
- Without class (scattered variables): ___ lines for 3 creatures
- With class: ___ lines for 3 creatures
- Improvement ratio: ___ : 1

---

### ✅ Skill 2: Methods - Behavior Belongs with Data

**The Test**:
- [ ] `draw()` method inside Creature class
- [ ] Method uses `self.name`, `self.species`, `self.level`
- [ ] All creatures use the same drawing logic

**This Proves**: You understand methods as actions that belong to objects. Creature knows how to draw itself.

**Real-World Parallel**: Just like a Pokemon object knows its own stats AND how to display itself in the Pokedex

---

### ✅ Skill 3: Understanding `self`

**The Test**:
- [ ] Can explain what `self` means in `__init__`
- [ ] Can explain why `self.name` works but `name` doesn't in `draw()`
- [ ] Completed "Break It" challenge and understood the error

**This Proves**: You understand `self` is how an object refers to its own data

---

### ✅ Skill 4: Pattern Recognition (from explain.md)

**The Test**:
- [ ] Answered questions about Vehicle class (different example)
- [ ] Identified classes vs objects in unfamiliar code
- [ ] Designed Weapon/Sword system using same pattern

**This Proves**: You can recognize and apply class patterns in new situations

---

### ✅ Skill 5: Scalability Thinking (from bad_code_explain.md)

**The Test**:
- [ ] Calculated improvement ratio (Stage 2 vs Stage 4)
- [ ] Predicted impact of adding 6th creature
- [ ] Answered "50 creatures" scenario questions

**This Proves**: You understand classes aren't just about working code, but about MAINTAINABLE code at scale

---

## 🎯 Overall Success = Understanding, Not Just Functionality

**You've truly succeeded when you can**:
- [ ] Explain the scattered-variables problem to someone (without code)
- [ ] Draw a diagram showing class (blueprint) vs object (thing)
- [ ] Predict: "If I add a property to the class, all objects get it"
- [ ] Design a simple class system for a different domain (books, vehicles, weapons)

**"Three creatures appear on screen" is baseline. "I understand why classes beat scattered variables" is success.**

---

## Quick Reference Commands

**Create plugin structure**:
```bash
mkdir -p src/plugins/c02_creature_card
cp academy/missions/c02_creature_card/c02_creature_card.py src/plugins/c02_creature_card/
```

**Restart service**:
```bash
sudo systemctl restart inkypi.service
```

**Validate mission**:
```bash
cd ~/InkyPi/academy/missions/c02_creature_card
python3 check.py
```

**Test bad_code**:
```bash
python3 bad_code.py
```

**Add icon** (temporary):
```bash
cp src/plugins/clock/icon.png src/plugins/c02_creature_card/icon.png
```

---

## Completion Checklist

Before moving to the next mission:

- [ ] All 4 checkpoints completed (3 creatures display)
- [ ] Added `health` property (Challenge 1)
- [ ] Broke and fixed `self` (Challenge 2)
- [ ] Attempted card borders (Challenge 3)
- [ ] Filled explain.md, debug_detective.md, bad_code_explain.md
- [ ] Completed bad_code.py (4 stages)
- [ ] `check.py` passes
- [ ] Can explain class vs object using car/Toyota analogy
- [ ] Understand when NOT to use classes (Rule of Three)

**Time to celebrate!** You've learned the foundation of object-oriented programming.

---

## After This Mission

**Concepts you've internalized**:
- Class = Blueprint, Object = Thing built from blueprint
- Properties (`self.name`) = Facts about the object
- Methods (`def draw(self)`) = Actions the object can do
- `self` = How an object refers to itself
- DRY principle = Don't Repeat Yourself (classes prevent copy-paste)

**Next mission preview**: C-03 (Inheritance Practice) - Learn how to create specialized versions of classes. PetCard will INHERIT from BaseCard, so you don't copy-paste shared behavior. Think: Toyota classes inherit from Car class.

**How to review later**: In 1 week, try to design a Book class (with title, author, pages, and a display() method) from scratch. If you can, you've internalized it!
