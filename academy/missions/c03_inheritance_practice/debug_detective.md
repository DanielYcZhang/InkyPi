# Debug Detective (C-03)

## The Broken Code

Someone tried to use inheritance but made mistakes. Here's their code:

```python
class BaseCard:
    def __init__(self, title):
        self.title = title
    
    def draw(self, draw, w, h):
        padding = 12
        draw.rectangle((padding, padding, w - padding, h - padding), 
                      outline=(0,0,0), width=2)
        draw.text((padding + 8, padding + 8), self.title, fill=(0,0,0))

class SpecialCard(BaseCard):
    def __init__(self, title, badge_text):
        self.title = title  # Set title ourselves
        self.badge_text = badge_text
    
    def draw(self, draw, w, h):
        # Draw base card stuff
        padding = 12
        draw.rectangle((padding, padding, w - padding, h - padding), 
                      outline=(0,0,0), width=2)
        draw.text((padding + 8, padding + 8), self.title, fill=(0,0,0))
        
        # Add special badge
        draw.rectangle((w - 76, 16, w - 16, 38), outline=(255,0,0), width=2)
        draw.text((w - 70, 20), self.badge_text, fill=(255,0,0))

# Test it
draw = FakeDraw()
card = SpecialCard("Hero Card", "★★★")
card.draw(draw, 200, 100)
```

---

## Your Mission

### 1. Predict (Before Running)

Before running this code, answer:
- Will this code run without errors? (Yes/No)
yes, the code will run assuming FakeDraw exists
- If yes, what's WRONG with it even though it runs?
It copies code from the parent class and doesn't use super().draw()
- If no, what error will appear?

**Your prediction:**


---

### 2. Analysis (Find the Problems)

There are at least 3 problems with this code related to inheritance. Find them:

**Problem 1:**
- Line number(s): 20
- What's wrong: it manually sets title instead of letting base card do it
- Why is this bad: it wastes time and can cause issues easier
- How to fix it: call super().__init__(title)

**Problem 2:**
- Line number(s): 25-28
- What's wrong: copy and pasted the border and text drawing code
- Why is this bad: it wastes time and can cause issues easier
- How to fix it: call super().draw(draw, w, h)

**Problem 3:**
- Line number(s): whole SpecialCard class
- What's wrong: it overides the methods but never calls super()
- Why is this bad:it essentially acts like a stranger to BaseCard, not a child
- How to fix it: call super() for the stuff

---

### 3. The Designer's Nightmare

Imagine the designer says: "Make the border 3 pixels thick instead of 2."

**With the buggy code above:**
- How many lines need to change? 2
- List all the line numbers that need updating: 15, 27

**If the code used `super()` correctly:**
- How many lines would need to change? 1
- Which line(s)? 15

---

### 4. Fix the Code

Rewrite `SpecialCard` to use inheritance properly:

```python
class SpecialCard(BaseCard):
    def __init__(self, title, badge_text):
        # Your fixed __init__ here
        super().__init__(title)
        self.badge_text = badge_text
        
    
    def draw(self, draw, w, h):
        # Your fixed draw method here
        super().draw(draw, w, h)

        # Add special badge
        draw.rectangle((w - 76, 16, w - 16, 38), outline=(255,0,0), width=2)
        draw.text((w - 70, 20), self.badge_text, fill=(255,0,0))
```

---

### 5. Verify Your Fix

After fixing, answer these:

1. If `BaseCard.draw()` changes, does `SpecialCard` automatically get the update?
   - Before fix: Yes / No
   no
   - After fix: Yes / No
   yes

2. How many lines of code are duplicated between `BaseCard` and `SpecialCard`?
   - Before fix: 5
   - After fix: 0

3. If you add a third card type `class PowerCard(BaseCard)`, how much base drawing code do you need to write?
   - Before fix approach: 5
   - After fix approach: 0

---

### 6. Concept Connection

This debugging challenge teaches you:

**What NOT to do:**
- copy and paset code from parent class to child class
- make child class override parent class method without calling super()

**What TO do:**
- use super() to call parent class method
- only write code for child class specific features

**The main lesson about inheritance:**
(In one sentence)
inheritance is about sharing code between classes, not copying it
---

### 7. Real-World Bug Story

Describe a scenario where the "before fix" approach would cause a real bug in a production game:

**Scenario:**
you make a game where there are monsters and stuff, they have health, damage anad armour.
**What goes wrong:**
you realize that the armour isn't working for the monsters and it isn't actually preventing damage like it should.
**How proper inheritance prevents it:**
if all the monsters inherit from the same base class, you can fix the bug in one place and it will work for all monsters.