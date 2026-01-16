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
- If yes, what's WRONG with it even though it runs?
- If no, what error will appear?

**Your prediction:**


---

### 2. Analysis (Find the Problems)

There are at least 3 problems with this code related to inheritance. Find them:

**Problem 1:**
- Line number(s): ___
- What's wrong:
- Why is this bad:
- How to fix it:

**Problem 2:**
- Line number(s): ___
- What's wrong:
- Why is this bad:
- How to fix it:

**Problem 3:**
- Line number(s): ___
- What's wrong:
- Why is this bad:
- How to fix it:

---

### 3. The Designer's Nightmare

Imagine the designer says: "Make the border 3 pixels thick instead of 2."

**With the buggy code above:**
- How many lines need to change? ___
- List all the line numbers that need updating:

**If the code used `super()` correctly:**
- How many lines would need to change? ___
- Which line(s)?

---

### 4. Fix the Code

Rewrite `SpecialCard` to use inheritance properly:

```python
class SpecialCard(BaseCard):
    def __init__(self, title, badge_text):
        # Your fixed __init__ here
        
    
    def draw(self, draw, w, h):
        # Your fixed draw method here
```

---

### 5. Verify Your Fix

After fixing, answer these:

1. If `BaseCard.draw()` changes, does `SpecialCard` automatically get the update?
   - Before fix: Yes / No
   - After fix: Yes / No

2. How many lines of code are duplicated between `BaseCard` and `SpecialCard`?
   - Before fix: ___
   - After fix: ___

3. If you add a third card type `class PowerCard(BaseCard)`, how much base drawing code do you need to write?
   - Before fix approach: ___
   - After fix approach: ___

---

### 6. Concept Connection

This debugging challenge teaches you:

**What NOT to do:**
- 
- 

**What TO do:**
- 
- 

**The main lesson about inheritance:**
(In one sentence)

---

### 7. Real-World Bug Story

Describe a scenario where the "before fix" approach would cause a real bug in a production game:

**Scenario:**

**What goes wrong:**

**How proper inheritance prevents it:**
