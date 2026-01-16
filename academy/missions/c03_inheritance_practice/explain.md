# Explain-Back (C-03)

## Part 1: New Example Code

Here's a different example using the same inheritance patterns you learned:

```python
class Vehicle:
    """Base class for all vehicles"""
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_info(self, draw, x, y):
        draw.text((x, y), f"Brand: {self.brand}", fill=(0,0,0))
        draw.text((x, y + 20), f"Model: {self.model}", fill=(0,0,0))

class ElectricCar(Vehicle):
    def __init__(self, brand, model, battery_range):
        super().__init__(brand, model)
        self.battery_range = battery_range
    
    def display_info(self, draw, x, y):
        super().display_info(draw, x, y)
        draw.text((x, y + 40), f"Range: {self.battery_range} km", fill=(0,0,0))
        draw.rectangle((x, y + 60, x + 100, y + 70), outline=(0,255,0), width=2)
        draw.text((x + 5, y + 62), "ELECTRIC", fill=(0,255,0))

class Motorcycle(Vehicle):
    def __init__(self, brand, model, engine_size):
        super().__init__(brand, model)
        self.engine_size = engine_size
    
    def display_info(self, draw, x, y):
        super().display_info(draw, x, y)
        draw.text((x, y + 40), f"Engine: {self.engine_size}cc", fill=(0,0,0))
```

---

## Part 2: Line-Specific Questions

**Line 2:** `"""Base class for all vehicles"""`
1. Why is this called a "base" class?
2. What do you think `ElectricCar` and `Motorcycle` have in common with `Vehicle`?

**Line 4:** `def __init__(self, brand, model):`
3. What is `__init__`? (Hint: Remember from C-02!)
4. Why does `Vehicle.__init__` only take `brand` and `model`, not battery info?

**Line 13:** `super().__init__(brand, model)`
5. What does `super()` mean in this line?
6. Why do we need to call `super().__init__(...)` instead of just setting `self.brand = brand` manually?
7. What would happen if you forgot this line and tried to access `self.brand` later?

**Line 18:** `super().display_info(draw, x, y)`
8. Is this calling the parent's method or the child's method? How do you know?
9. Why call `super().display_info(...)` BEFORE drawing the electric badge?
10. If you swapped lines 18 and 19-20, what would change visually?

**Line 11:** `class ElectricCar(Vehicle):`
11. What does the `(Vehicle)` part mean?
12. Does `ElectricCar` automatically have a `display_info` method even before line 17? Why?

**Line 20:** `draw.text((x, y + 40), f"Range: {self.battery_range} km", fill=(0,0,0))`
13. Why is this line at `y + 40` instead of `y + 20`?
14. What does this tell you about what `super().display_info(...)` already drew?

---

## Part 3: Comparison Questions

15. Both `ElectricCar` and `Motorcycle` call `super().display_info(...)`. What code do they AVOID duplicating because of this?

16. If you wanted to change the font color of the brand/model text for ALL vehicles, where would you make the change?
   - [ ] In `Vehicle.display_info`
   - [ ] In both `ElectricCar.display_info` and `Motorcycle.display_info`
   - Explain your answer:

17. Imagine adding a third vehicle: `class Truck(Vehicle)`. List what code you would need to write:
   ```python
   class Truck(Vehicle):
       # Your answer here
   ```

---

## Part 4: Concept Transfer Challenge

18. Design a new inheritance system for a game:
   - **Base class**: `Weapon` (has `name` and `damage` properties)
   - **Subclass 1**: `Sword` (adds `blade_length` property)
   - **Subclass 2**: `Bow` (adds `arrow_count` property)
   
   Write the `__init__` method for `Sword` that uses `super()`:
   ```python
   class Sword(Weapon):
       def __init__(self, name, damage, blade_length):
           # Your code here
   ```

19. In 2-3 sentences, explain why using inheritance for `Sword` and `Bow` is better than creating two completely separate classes with no base class.

---

## Part 5: C-03 Mission Connection

20. In `c03_inheritance_practice.py`, find where `super()` is called and write the line number: ___

21. What would happen if you removed the `super().draw(...)` call from `PetCard`?

22. Reflection: You're building a game with 50 different enemy types. They all have health, position, and a draw method, but each enemy looks different. Would you use inheritance? Why or why not?
