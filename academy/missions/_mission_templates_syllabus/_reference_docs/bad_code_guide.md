# Enhanced bad_code Exercise Template

## Philosophy
The bad_code exercise should not just show "this is bad, make it better." Instead, it should:
1. **Simulate the pain of changing bad code** when requirements evolve
2. **Measure the improvement** with concrete metrics (lines changed, places updated)
3. **Connect to team collaboration** ("your teammate needs to...")
4. **Teach when bad is acceptable** with nuanced understanding

## bad_code.py Structure

### Template Format:

```python
"""
Refactoring Challenge ([Mission ID])

You'll experience why [core concept] matters by feeling the pain without it.

Stage 1: Working Code (GIVEN)
Stage 2: Feature Request (TODO - using the given code)
Stage 3: Refactored Version (TODO - using [core concept])
Stage 4: Same Feature Request (TODO - using your refactored code)

You can run this file: python3 bad_code.py
"""

# ============================================================
# STAGE 1: Working Code (but messy)
# ============================================================
# This works fine TODAY. But let's see what happens when
# requirements change...

def bad_version():
    """Current working code - uses [anti-pattern]"""
    # [Implementation that works but is fragile]
    pass

# ============================================================
# STAGE 2: FEATURE REQUEST #1
# ============================================================
"""
PRODUCT MANAGER REQUEST:
"We need [change that requires touching many places]"

TODO: Modify bad_version() to handle this request.
      Track metrics:
      - Lines changed: ___
      - Functions/blocks updated: ___
      - Pain level (1-10): ___
"""

def bad_version_with_feature():
    # TODO: Copy bad_version and modify it
    pass

# ============================================================
# STAGE 3: REFACTORED VERSION
# ============================================================
"""
Now rewrite using [core concept from mission].

Hint: Use [class/loop/function/etc.]
"""

def good_version():
    # TODO: Rewrite using [core concept]
    pass

# ============================================================
# STAGE 4: SAME FEATURE REQUEST (on good code)
# ============================================================
"""
Apply the SAME feature request to your refactored version.

Track metrics:
- Lines changed: ___
- Functions/blocks updated: ___
- Pain level (1-10): ___

Compare Stage 2 vs Stage 4. What's the improvement?
"""

def good_version_with_feature():
    # TODO: Apply the same feature request
    pass

# ============================================================
# TESTING HARNESS
# ============================================================

class FakeDraw:
    """Simulates drawing commands for testing"""
    def text(self, pos, text, fill=None):
        print(f"  text at {pos}: '{text}'")
    
    def rectangle(self, box, outline=None, width=1):
        print(f"  rectangle {box}")

if __name__ == "__main__":
    print("Stage 1: Working Code")
    bad_version()
    
    print("\nStage 2: Feature Request on Bad Code")
    try:
        bad_version_with_feature()
    except Exception as e:
        print(f"  Not implemented yet: {e}")
    
    print("\nStage 3: Refactored Version")
    try:
        good_version()
    except Exception as e:
        print(f"  Not implemented yet: {e}")
    
    print("\nStage 4: Feature Request on Good Code")
    try:
        good_version_with_feature()
    except Exception as e:
        print(f"  Not implemented yet: {e}")
```

## bad_code_explain.md Structure

### Template Format:

```markdown
# Refactoring Challenge ([Mission ID]) — Analysis

## Part 1: Change Impact Metrics

**Feature Request**: [Describe the change that students implemented]

### With the Original Code (Stage 2):
1. How many lines did you add or modify?
2. How many different places in the code needed updates?
3. List each location you had to remember to update:
   - 
   - 
   - 
4. What could break if you forgot one location?

### With Your Refactored Code (Stage 4):
5. How many lines did you add or modify?
6. How many different places needed updates?
7. What's the improvement ratio? (Original lines ÷ Refactored lines)

---

## Part 2: The Team Collaboration Test

**Scenario**: Your teammate (who has never seen this code) needs to add [another instance/feature].

### With the original code:
8. List what your teammate needs to figure out before making the change:
   - 
   - 
   - 

9. What's the chance they'll make a mistake? (Low/Medium/High) Why?

### With your refactored code:
10. What does your teammate need to understand?
11. Write the EXACT code they would add (be specific):
```python
# Your answer here
```

12. Why is this easier for team collaboration?

---

## Part 3: Second Feature Request (Stress Test)

**New Requirement**: [Describe a second, different change]

13. With the original approach, predict:
    - Lines to change: ___
    - Risk of bugs: (Low/Medium/High)
    - Time estimate: ___ minutes

14. With your refactored approach, predict:
    - Lines to change: ___
    - Risk of bugs: (Low/Medium/High)
    - Time estimate: ___ minutes

15. At what point does the refactored approach become ESSENTIAL?
    (When you have ___ items? When ___ people work on it?)

---

## Part 4: When "Bad" is Actually Acceptable

16. List 2-3 SPECIFIC scenarios where the "bad" approach is reasonable:
    
    **Scenario 1**: 
    - Context: 
    - Why it's OK: 
    
    **Scenario 2**:
    - Context:
    - Why it's OK:
    
17. What's the rule of thumb for when to refactor?
    (Hint: Think about the "Rule of Three" in programming)

---

## Part 5: Real-World Connection

18. Describe a time when you (or someone you know) struggled to modify some code. What made it difficult?

19. Look at the [mission name] code you wrote. If you had to maintain it for 2 years and add 20 new features, what would make your life easier?

20. Complete this sentence: 
    "The main reason we use [core concept] is not to make code shorter, but to ___________________"

---

## Reflection

21. What surprised you most about this exercise?

22. When you write code tomorrow, what will you do differently?
```

---

## Example: C-02 Enhanced bad_code.py

```python
"""
Refactoring Challenge (C-02): Classes vs Scattered Variables

You'll experience why classes matter by trying to add features without them.
"""

# STAGE 1: Working Code (GIVEN)
def bad_version():
    """Three creatures using separate variables"""
    # Creature 1
    name1 = "Pip"
    species1 = "Cat"
    level1 = 5
    
    # Creature 2
    name2 = "Rex"
    species2 = "Dog"
    level2 = 7
    
    # Creature 3
    name3 = "Spark"
    species3 = "Dragon"
    level3 = 12
    
    # Draw them
    draw = FakeDraw()
    draw.text((20, 20), f"Name: {name1}", fill=(0,0,0))
    draw.text((20, 35), f"Species: {species1}", fill=(0,0,0))
    draw.text((20, 50), f"Level: {level1}", fill=(0,0,0))
    
    draw.text((20, 80), f"Name: {name2}", fill=(0,0,0))
    draw.text((20, 95), f"Species: {species2}", fill=(0,0,0))
    draw.text((20, 110), f"Level: {level2}", fill=(0,0,0))
    
    draw.text((20, 140), f"Name: {name3}", fill=(0,0,0))
    draw.text((20, 155), f"Species: {species3}", fill=(0,0,0))
    draw.text((20, 170), f"Level: {level3}", fill=(0,0,0))

# STAGE 2: FEATURE REQUEST
"""
PRODUCT MANAGER SAYS:
"We need 5 creatures instead of 3, and each needs a 'health' property."

TODO: Copy bad_version() and modify it. Count:
- New lines added: ___
- Existing lines modified: ___
- Places you had to update: ___
"""

def bad_version_with_health():
    # TODO: Add 2 more creatures and health property to all
    # Count how many copy-pastes!
    pass

# STAGE 3: REFACTORED VERSION
"""
Rewrite using a Creature class.
"""

class Creature:
    # TODO: Add __init__ and draw method
    pass

def good_version():
    # TODO: Create 3 creatures using the class
    # TODO: Draw them
    pass

# STAGE 4: SAME FEATURE REQUEST
"""
Add 2 more creatures and health property.
Count the changes - how is it different?
"""

def good_version_with_health():
    # TODO: Same feature request, class-based approach
    pass

# [Testing harness as shown above]
```

## Key Teaching Improvements

### 1. **Concrete Pain Points**
- Not theoretical: "imagine if you had 50..."
- Actual: "Add 2 more creatures, count the lines"

### 2. **Measurable Metrics**
- Lines changed: 24 vs 3
- Places updated: 8 vs 1
- Quantifiable improvement

### 3. **Team Empathy**
- "Your teammate needs to add a creature"
- Teaches collaboration, not just syntax
- Aligns with "when multiple people work on this" from briefing

### 4. **Progressive Discovery**
- Stage 1: Works fine!
- Stage 2: Oh no, this is painful
- Stage 3: Ah, this is better!
- Stage 4: WOW, so much easier!

### 5. **Nuanced Understanding**
- When is "bad" actually OK?
- Rule of Three: 1-2 items = OK, 3+ = refactor
- Context matters

---

## Alignment with Teaching Philosophy

| Teaching Principle | How bad_code Exercise Addresses It |
|-------------------|-----------------------------------|
| **Show the pain** | Feature request on bad code = visceral experience |
| **Concrete examples** | Actual line counts, not "imagine" scenarios |
| **Scalability thinking** | "What if 50 creatures?" becomes real with 5 |
| **Collaboration context** | "Your teammate needs to..." questions |
| **Deep understanding** | Not just "what" but "when" and "why" |
| **Real-world connection** | "Describe a time when..." |
| **Metrics-driven** | Measure improvement, not just feel it |

This transforms bad_code from "fix this broken code" to "experience why architecture matters through painful then delightful feature changes."
