# Briefing: C-03 — The Inheritance Practice

You will build a base card and then a special card that **inherits** from it. This is where `super()` makes sense.

---

## Concepts in This Mission
- Base class
- Subclass
- Inheritance
- super()

---

## The Big Idea
Inheritance lets you reuse shared behavior and then add your own twist.

---

## Concept Explanations (Analogy → Definition → Example → Where Used)

### 1) Base class = "Common foundation"
**Analogy**: A base class is the shared foundation for similar things.

**Definition**: A base class holds behavior or data that many subclasses share.

**Example**
```py
class BaseCard:
    ...
```

**Where used in this mission**: `class BaseCard` in `c03_inheritance_practice.py`.

### 2) Inheritance = "Is-a relationship"
**Analogy**: A PetCard *is a* BaseCard with extra features.

**Definition**: A subclass inherits behavior from a base class.

**Example**
```py
class PetCard(BaseCard):
    ...
```

**Where used in this mission**: `class PetCard(BaseCard)`.

### 3) super() = "Ask the parent for help"
**Analogy**: `super()` lets you reuse the parent’s setup or drawing.

**Definition**: `super()` calls the parent class implementation.

**Example**
```py
super().__init__(title)
super().draw(draw, w, h)
```

**Where used in this mission**: `PetCard.draw(...)`.

---

## What “Success” Looks Like
- The subclass calls `super()` correctly.
- The base drawing appears plus a special badge from the subclass.

Use/avoid guidance is practiced in `bad_code.py`.
