# Briefing: C-03 — The Inheritance Practice

You will build a base card and then a special card that **inherits** from it. This is where `super()` makes sense.

---

## The Big Idea
Inheritance lets you reuse shared behavior and then add your own twist.

---

## New Tools (Micro-lessons with Syntax Cards)

### 1) Base class = "Common foundation"
**Hook**: A base class is the shared foundation for similar things.

**Definition**: A base class holds behavior or data that many subclasses share.

**Syntax**
```py
class BaseCard:
    ...
```

**Common mistakes**
- Putting too much in the base class so it becomes confusing.

**Use vs Avoid**
- Use a base class when multiple things share the same logic.
- Avoid inheritance if the classes are not truly related.

**Where used in this mission**: `class BaseCard`.

### 2) Inheritance = "Is-a relationship"
**Hook**: A PetCard *is a* BaseCard with extra features.

**Definition**: A subclass inherits behavior from a base class.

**Syntax**
```py
class PetCard(BaseCard):
    ...
```

**Common mistakes**
- Inheriting from something unrelated.

**Use vs Avoid**
- Use inheritance when the subclass truly is a specialized version.
- Avoid inheritance if you only need a small helper function.

**Where used in this mission**: `class PetCard(BaseCard)`.

### 3) super() = "Ask the parent for help"
**Hook**: `super()` lets you reuse the parent’s setup or drawing.

**Definition**: `super()` calls the parent class implementation.

**Syntax**
```py
super().__init__(title)
super().draw(draw, w, h)
```

**Common mistakes**
- Forgetting to call `super()` in `__init__`.

**Use vs Avoid**
- Use `super()` to reuse parent logic instead of copying it.
- Avoid using `super()` if there is no parent behavior to reuse.

**Where used in this mission**: the subclass constructor and draw method.

---

## What “Success” Looks Like
- The subclass calls `super()` correctly.
- The base drawing appears plus a special badge from the subclass.
