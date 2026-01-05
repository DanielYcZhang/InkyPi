# Briefing: Mission 06 — The Awakening

You are no longer just operating the machine.
You are about to **teach it a new ability**.

In InkyPi, abilities are called **plugins**.

---

## The Big Idea
Every plugin is a small Python class that can **generate one image** for the display.

- Input: `settings` (a dictionary of options) and `device_config` (screen size, timezone, secrets)
- Output: **one** `PIL.Image` object

If the plugin can produce an image, InkyPi can show it.

---

## New Tools (Micro-lessons with Syntax Cards)

Each section below follows the same “Syntax Card” structure:
**Hook → Definition → Syntax → Common mistakes → Where used**.

### 1) Imports (`import`) = "Get tools from the shelf"
**Hook**: We don’t build a hammer. We import it.

**Definition**: `import` loads code from another module so you can use its names in your file.

**Syntax**
```py
from PIL import Image, ImageDraw
from plugins.base_plugin.base_plugin import BasePlugin
```
- `from X import Y` means “from module `X`, bring the name `Y` into this file”.

**Common mistakes**
- `ModuleNotFoundError: No module named ...` → typo, or you’re not running inside the InkyPi environment.
- Importing the wrong thing (e.g. `ImageDraw` vs `ImageDraw.Draw`).

**Where used in this mission**: `src/plugins/m06_awakening/m06_awakening.py`

### 2) Classes (`class`) = "Define a new type of thing"
**Hook**: You’re defining a new kind of plugin.

**Definition**: A `class` groups data + functions (methods). In InkyPi, each plugin is a class.

**Syntax**
```py
class Awakening(BasePlugin):
    ...
```
- `Awakening` = the class name (a new “type” you’re creating)
- `(BasePlugin)` = inheritance (“Awakening is a BasePlugin”)
- `:` starts the indented block for the class body

**Common mistakes**
- Missing `:` → `SyntaxError: invalid syntax`
- Indentation not consistent → `IndentationError`
- Not inheriting from `BasePlugin` → InkyPi won’t treat it as a plugin.

**Where used in this mission**: `src/plugins/m06_awakening/m06_awakening.py`

### 3) Functions/Methods (`def`) = "Give your class an ability"
**Hook**: `def` gives your class an ability.

**Definition**: `def` defines a **function**. Inside a class, it’s called a **method**. In InkyPi, the most important method is `generate_image`.

**Syntax**
```py
def generate_image(self, settings, device_config):
    # body (indented)
    return img
```
- `generate_image` = method name
- `( ... )` = **parameters** (inputs). Commas separate them.
- `:` starts the indented block for the method body
- `return img` sends a value back to whoever called the method

**Common mistakes**
- Missing `:` → `SyntaxError`
- Wrong indentation → `IndentationError`
- Forgetting `return img` → plugin runs but returns `None` (nothing to show)
- Returning the wrong type → runtime crash when InkyPi expects a `PIL.Image`

**Where used in this mission**: `src/plugins/m06_awakening/m06_awakening.py` in `Awakening.generate_image(...)`

### 4) `self` = "Me" (the current plugin)
**Hook**: `self` is the plugin pointing at its own chest: “me”.

**Definition**: In a class method, `self` is the current object (the plugin instance). Python passes it automatically when you call `plugin.generate_image(...)`.

**Syntax**
```py
class Awakening(BasePlugin):
    def generate_image(self, settings, device_config):
        ...
```
- `self` must be the first parameter in instance methods

**Common mistakes**
- Forgetting `self` → arguments shift and you may see:
  - `TypeError: generate_image() takes 3 positional arguments but 4 were given`

**Where used in this mission**: `src/plugins/m06_awakening/m06_awakening.py` method definition

### 5) Parameters, arguments, and parentheses
**Hook**: Parentheses are the “input ports” of a function.

**Definition**:
- **Parameters** are the names in the function definition.
- **Arguments** are the real values you pass when calling the function.

**Syntax**
```py
def hello(name):          # name = parameter
    return f"Hi {name}"

hello("Commander")        # "Commander" = argument
```

**Common mistakes**
- Mixing them up is normal; remember: **parameters = definition**, **arguments = call**.

**Where used in this mission**: `generate_image(self, settings, device_config)` parameters

### 6) `settings` (dict) = "A backpack of options"
**Hook**: `settings` is a backpack: you reach in and pull out options.

**Definition**: A dictionary stores key/value pairs. In InkyPi, settings from the web UI arrive as a dict.

**Syntax**
```py
name = settings.get("name", "Commander")
```
- `"name"` = the key you’re looking up
- `"Commander"` = default value if the key doesn’t exist yet

**Common mistakes**
- Using `settings["name"]` when it doesn’t exist → `KeyError: 'name'`
- Assuming settings values are the right type (often they are strings).

**Where used in this mission**: `src/plugins/m06_awakening/m06_awakening.py` inside `generate_image(...)`

### 7) “Fail loudly” with `RuntimeError`
**Hook**: If something important is missing, don’t “half work”. Show a clear message.

**Definition**: Raising `RuntimeError` stops the plugin and reports a message in the web UI.

**Syntax**
```py
if not name:
    raise RuntimeError("Name is required.")
```

**Common mistakes**
- Raising a vague message (“Error”) instead of a helpful one (“Name is required”).
- Catching exceptions too early and hiding the real problem.

**Where used in this mission**: optional, if you decide name must be non-empty

---

## What “Success” Looks Like
- A new plugin appears in the InkyPi web UI.
- When you run it, it shows a **Hello card** on the display.
- Running `python3 check.py` in this mission folder prints PASS.
