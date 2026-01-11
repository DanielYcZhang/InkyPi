# Briefing: C-02 — The Creature Card

You are going to create a creature card and draw it on the display. This mission introduces **classes**, **objects**, **properties**, and **methods** in a friendly way.

---

## Concepts in This Mission
- Class
- Object
- Property
- Method

---

## The Big Idea
A **class** is a blueprint. An **object** is the thing you build from that blueprint. Properties are the facts about the thing. Methods are the actions it can do.

---

## Concept Explanations (Analogy → Definition → Example → Where Used)

### 1) Class = "Blueprint"
**Analogy**: A class is a blueprint for building a thing.

**Definition**: A class groups data and behavior into one reusable definition.

**Example**
```py
class Creature:
    ...
```

**Where used in this mission**: `class Creature` in `c02_creature_card.py`.

### 2) Object = "The thing you built"
**Analogy**: An object is the real creature you create.

**Definition**: An object is an instance of a class.

**Example**
```py
creature = Creature("Pip", "Cat", 5)
```

**Where used in this mission**: inside `CreatureCard.generate_image(...)`.

### 3) Property = "Facts about the thing"
**Analogy**: Properties are labels on the creature card.

**Definition**: Properties are values stored on the object using `self`.

**Example**
```py
self.name = name
self.level = level
```

**Where used in this mission**: inside `Creature.__init__`.

### 4) Method = "What it can do"
**Analogy**: A method is an ability the object has.

**Definition**: A method is a function inside a class.

**Example**
```py
def draw(self, draw, w, h):
    ...
```

**Where used in this mission**: `Creature.draw(...)`.

---

## What “Success” Looks Like
- A creature card appears with a name, species, and level.
- The class stores properties in `self`.
- The plugin draws the card using the creature object.

Use/avoid guidance is practiced in `bad_code.py`.
