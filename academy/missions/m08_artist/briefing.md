# Briefing: Mission 08 — The Artist

Time to draw.

In InkyPi, “graphics” means you generate an image and draw shapes onto it. You will learn the coordinate grid and how to place pixels with intent.

---

## Concepts in This Mission
- Pillow Image + Draw
- Coordinates
- Tuples
- Loops
- Functions + Parameters (reading signatures)

---

## The Big Idea
The screen is a grid:
- `(0, 0)` is the **top-left**
- `x` increases to the **right**
- `y` increases **down**

You don’t want “magic numbers” that only work on one screen size. You want drawings based on the display width/height.

---

## Concept Explanations (Analogy → Definition → Example → Where Used)

### 1) Functions + Parameters = "A named action with inputs"
**Analogy**: A function is a named action; parameters are the inputs you must provide.

**Definition**: A function (or method) is a reusable block of code. The **signature** is the list of required parameters.

**Example**
```py
img = Image.new(mode, size, color)
```

**Where used in this mission**: `Image.new(...)` in `m08_artist.py`.

### 2) Coordinates = "A map grid"
**Analogy**: Coordinates are a treasure map: X across, Y down.

**Definition**: A coordinate is a pair `(x, y)` that points to a location on the image.

**Example**
```py
center = (w // 2, h // 2)
```

**Where used in this mission**: `text_pos = (20, 20)` and shape positions in `m08_artist.py`.

### 3) Tuples = "Bundle values together"
**Analogy**: A tuple is a small bundle you carry as one item.

**Definition**: A tuple groups values together. Pillow uses tuples for coordinates and colors.

**Example**
```py
color = (0, 0, 0)
```

**Where used in this mission**: coordinates and color tuples in `m08_artist.py`.

### 4) Draw object = "Your paintbrush"
**Analogy**: `ImageDraw.Draw(img)` is your paintbrush for the image.

**Definition**: The Draw object provides methods to draw shapes and text onto an image.

**Example**
```py
draw = ImageDraw.Draw(img)
draw.rectangle((10, 10, 100, 60), outline=(0, 0, 0), width=3)
```

**Where used in this mission**: drawing shapes and text in `m08_artist.py`.

### 5) Loops (`for`) = "Repeat on purpose"
**Analogy**: A loop is a copy machine with control.

**Definition**: `for` repeats code for each item or number.

**Example**
```py
for i in range(3):
    draw.ellipse(...)
```

**Where used in this mission**: repeated dots in `m08_artist.py`.

---

## What “Success” Looks Like
- The plugin draws your name + at least 2 shapes.
- The layout scales based on the display dimensions (uses `w` and `h`).
- Running `python3 check.py` in this mission folder prints PASS.

Use/avoid guidance is practiced in `bad_code.py`.
