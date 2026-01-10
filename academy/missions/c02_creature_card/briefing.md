# Briefing: C-02 — The Creature Card

You are going to create a creature card and draw it on the display. This mission introduces **classes**, **objects**, and **properties** in a friendly way.

---

## The Big Idea
A **class** is a blueprint. An **object** is the thing you build from that blueprint. Properties are the facts about the thing.

---

## New Tools (Micro-lessons with Syntax Cards)

### 1) Class = "Blueprint"
**Hook**: A class is a blueprint for building a thing.

**Definition**: A class groups data and behavior into one reusable definition.

**Syntax**
```py
class Creature:
    ...
```

**Common mistakes**
- Forgetting the colon after the class name.

**Use vs Avoid**
- Use a class when you need a reusable shape or concept.
- Avoid a class if a simple function or dict is enough.

**Where used in this mission**: `class Creature`.

### 2) Object = "The thing you built"
**Hook**: An object is the real creature you create.

**Definition**: An object is an instance of a class.

**Syntax**
```py
creature = Creature("Pip", "Cat", 5)
```

**Common mistakes**
- Forgetting to pass required arguments.

**Use vs Avoid**
- Use objects when you need to store related values together.
- Avoid many separate variables for one thing.

**Where used in this mission**: creating the creature card data.

### 3) Properties = "Facts about the thing"
**Hook**: Properties are labels on the creature card.

**Definition**: Properties are values stored on the object using `self`.

**Syntax**
```py
self.name = name
self.level = level
```

**Common mistakes**
- Using local variables instead of `self.*`.

**Use vs Avoid**
- Use properties for data that belongs to the object.
- Avoid global variables for per-object data.

**Where used in this mission**: inside `__init__`.

### 4) Methods = "What it can do"
**Hook**: A method is an ability the object has.

**Definition**: A method is a function inside a class.

**Syntax**
```py
def draw(self, draw, w, h):
    ...
```

**Common mistakes**
- Forgetting `self` as the first parameter.

**Use vs Avoid**
- Use methods for actions that use the object's data.
- Avoid passing lots of object data into external functions.

**Where used in this mission**: drawing the creature card.

---

## What “Success” Looks Like
- A creature card appears with a name, species, and level.
- The class stores properties in `self`.
- The plugin draws the card using the creature object.
