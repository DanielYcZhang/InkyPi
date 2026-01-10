# Briefing: Mission 08 — The Artist

Time to draw.

In InkyPi, “graphics” means you generate an image and draw shapes onto it. You will learn the coordinate grid and how to place pixels with intent.

---

## The Big Idea
The screen is a grid:
- `(0, 0)` is the **top-left**
- `x` increases to the **right**
- `y` increases **down**

You don’t want “magic numbers” that only work on one screen size. You want drawings based on the display width/height.

---

## New Tools (Micro-lessons with Syntax Cards)

### 1) Functions + Parameters = "A named action with inputs"
**Hook**: A function is a named action; parameters are the inputs you must provide.

**Definition**: A function (or method) is a reusable block of code. The **signature** is the list of required parameters.

**Syntax**
```py
img = Image.new(mode, size, color)
```

**Common mistakes**
- Passing the wrong number of parameters.
- Mixing up the order of parameters.

**Use vs Avoid**
- Use a function signature to know what inputs are required.
- Avoid guessing; check docs or use help() in Python.

**Where used in this mission**: `Image.new("RGB", (w, h), (255, 255, 255))`.

**How to find required parameters**
- Read the library docs, or use `help(Image.new)` in a Python shell.
- Look at examples in the codebase.

### 2) Coordinates = "A map grid"
**Hook**: Coordinates are a treasure map: X across, Y down.

**Definition**: A coordinate is a pair `(x, y)` that points to a location on the image.

**Syntax**
```py
center = (w // 2, h // 2)
top_left = (0, 0)
```

**Common mistakes**
- Swapping X and Y (things appear in the wrong place).
- Assuming Y goes upward (it goes downward).

**Use vs Avoid**
- Use coordinates when you place anything on the canvas.
- Avoid guessing positions without checking `w` and `h`.

**Where used in this mission**: inside `generate_image(...)` when placing shapes/text.

### 3) Tuples = "Bundle values together"
**Hook**: A tuple is a small bundle you carry as one item.

**Definition**: A tuple groups values together. Pillow uses tuples for coordinates and colors.

**Syntax**
```py
point = (10, 20)          # (x, y)
color = (0, 0, 0)         # (r, g, b)
box = (x1, y1, x2, y2)    # rectangle bounds
```

**Common mistakes**
- Forgetting commas: `(10)` is not a tuple; `(10, )` is a 1-item tuple.

**Use vs Avoid**
- Use tuples for grouped values like `(x, y)` or `(r, g, b)`.
- Avoid mixing up the order (e.g., `(y, x)` by accident).

**Where used in this mission**: shape positions and colors.

### 4) The Draw object = "Your paintbrush"
**Hook**: `ImageDraw.Draw(img)` is your paintbrush for the image.

**Definition**: Pillow’s `ImageDraw` provides methods to draw shapes and text onto an image.

**Syntax**
```py
img = Image.new("RGB", (w, h), (255, 255, 255))
draw = ImageDraw.Draw(img)
draw.rectangle((10, 10, 100, 60), outline=(0, 0, 0), width=3)
```

**Common mistakes**
- Forgetting to create `draw` (then you can’t draw anything).

**Use vs Avoid**
- Use a `Draw` object for all shapes and text.
- Avoid calling `draw.*` before creating it.

**Where used in this mission**: `src/plugins/m08_artist/m08_artist.py`

### 5) Loops (`for`) = "Repeat on purpose"
**Hook**: A loop is a copy machine with control.

**Definition**: `for` repeats code for each item or number.

**Syntax**
```py
for i in range(3):
    x = 20 + i * 40
    draw.ellipse((x, 80, x + 20, 100), fill=(0, 0, 0))
```

**Common mistakes**
- Indentation errors (the repeated block must be indented).

**Use vs Avoid**
- Use loops when you repeat a drawing step.
- Avoid copy-pasting the same line 3 times.

**Where used in this mission**: drawing repeated dots/stripes/patterns.

### 6) Helper functions = "Don’t repeat yourself"
**Hook**: If you copy-paste 3 times, it’s time for a helper.

**Definition**: A helper function is a small named piece of code you can call from `generate_image(...)`.

**Syntax**
```py
def draw_center_cross(draw, center, size, color):
    ...
```

**Common mistakes**
- Defining the function but never calling it.

**Use vs Avoid**
- Use helpers when a drawing step repeats.
- Avoid over-abstracting if it only happens once.

**Where used in this mission**: optional, but recommended.

---

## What “Success” Looks Like
- The plugin draws your name + at least 2 shapes.
- The layout scales based on the display dimensions (uses `w` and `h`).
- Running `python3 check.py` in this mission folder prints PASS.
