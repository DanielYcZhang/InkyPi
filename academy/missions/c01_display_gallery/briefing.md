# Briefing: C-01 — The Display Gallery

You are going to build a tiny art wall: three labeled boxes arranged neatly on the screen.

This mission is about **variables** and **layout**, not fancy art. If you can place boxes predictably, you can place anything.

---

## The Big Idea
The display is a grid. If you name the important numbers (padding, box size, gaps), your layout becomes easy to change.

---

## New Tools (Micro-lessons with Syntax Cards)

### 1) Variables = "Labeled containers"
**Hook**: A variable is a labeled container you can reuse.

**Definition**: A variable stores a value so you can use it later by name.

**Syntax**
```py
padding = 10
box_width = 80
```

**Common mistakes**
- Using vague names like `x` or `n` for everything.

**Use vs Avoid**
- Use variables for any number you might change.
- Avoid hard-coding the same number in many places.

**Where used in this mission**: layout values like padding and box sizes.

### 2) Functions + Parameters = "A named action with inputs"
**Hook**: A function is a named action; parameters are the inputs you must provide.

**Definition**: A function (or method) is a reusable block of code. The **signature** is the list of required parameters.

**Syntax**
```py
result = Image.new(mode, size, color)
```

**Common mistakes**
- Passing the wrong number of parameters.
- Mixing up the order of parameters.

**Use vs Avoid**
- Use function signatures to know what inputs are required.
- Avoid guessing; check docs or use help() in Python.

**Where used in this mission**: `Image.new("RGB", (w, h), (255, 255, 255))`.

**OOP context**
- `Image` is a class (a blueprint).
- `Image.new(...)` is a class method that creates an image object.
- `ImageDraw.Draw(img)` returns a draw object that knows how to draw on that image.

**How to find required parameters**
- Read the library docs, or use `help(Image.new)` in a Python shell.
- Look at examples in the codebase.

### 3) Coordinates = "A map grid"
**Hook**: Coordinates are a treasure map: X across, Y down.

**Definition**: A coordinate is a pair `(x, y)` that points to a location on the image.

**Syntax**
```py
top_left = (0, 0)
center = (w // 2, h // 2)
```

**Common mistakes**
- Swapping X and Y.
- Forgetting that Y goes downward.

**Use vs Avoid**
- Use `(x, y)` pairs for positions.
- Avoid guessing positions without checking `w` and `h`.

**Where used in this mission**: placing boxes and labels.

### 4) Loops = "Repeat on purpose"
**Hook**: A loop repeats a block of code multiple times.

**Definition**: `for i in range(n)` repeats the indented block `n` times.

**Syntax**
```py
for i in range(3):
    print(i)
```

**Common mistakes**
- Wrong indentation (loop body must be indented).

**Use vs Avoid**
- Use loops for repeated drawing steps.
- Avoid copy-pasting the same line many times.

**Where used in this mission**: drawing three boxes with `range(box_count)`.

### 5) Types = "Different kinds of stuff"
**Hook**: A number and a word are not the same thing.

**Definition**: A type is the kind of value a variable holds (e.g., number vs text).

**Syntax**
```py
count = 3       # int
label = "Box"   # str
```

**Common mistakes**
- Trying to add a number to a string without conversion.

**Use vs Avoid**
- Use strings for labels; numbers for sizes and positions.
- Avoid mixing them without converting.

**Where used in this mission**: labels and layout values.

---

## What “Success” Looks Like
- Three labeled boxes are placed neatly on the screen.
- Changing one variable (like padding) updates the whole layout.
- The plugin returns a valid image.
