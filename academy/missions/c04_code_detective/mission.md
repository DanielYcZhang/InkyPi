# Mission C-04: The Code Detective

**Objective**: Understand how the InkyPi system works by reading the source code. Trace the flow from web UI button click to display update.

**Estimated Time**: 2 hours

**Deliverable**: `c04_architecture.md` with system diagram and answered detective questions.

---

## Why This Mission Matters

You've built 5 plugins (M-06, M-07, C-01, C-02, C-03). Each time, you inherited from `BasePlugin` and implemented `generate_image()`. But have you ever wondered:

-  **WHO** actually calls your `generate_image()` method?
- **WHERE** does `device_config` come from?
- **WHAT** happens to the image you return?
- **HOW** does InkyPi discover your plugin-info.json file?

**In the real world:**
- **Spotify engineers** spend their first weeks reading Spotify's codebase before writing features
- **Game developers** study the engine architecture before building game logic
- **Mobile app teams** understand the framework (iOS/Android) before adding screens

**Software engineering is 80% reading code, 20% writing code.** This mission teaches the most important skill in professional development: **code reading**.

**After this mission:**
- ✅ You'll know exactly where to look when debugging
- ✅ You'll understand the system instead of copying patterns blindly
- ✅ You'll read stack traces and recognize file names
- ✅ You'll confidently modify the system (you know what's safe)

---

## Mental Model Check

Before you start reading code, write down your current understanding:

**Question 1**: What do you think happens between clicking "Generate Image" in the web UI and seeing the result on the display?

```
Write your guess here (it's OK to be wrong! this is your starting point):

Step 1: _____________http request
Step 2: _____________the server recieves the request
Step 3: _____________runs the generate_image() method
Step 4: _____________returns the image
Step 5: _____________updates the display
...
```

**Question 2**: Why do all plugins inherit from `BasePlugin`? What do you think `BasePlugin` does?

```
Your theory:
_____________because it is the base anad baseplugin has all the methods that the plugins need to have
```

**Question 3**: How do you think InkyPi "discovers" that your plugin exists?

```
Your guess:
_____________it looks for plugin-info.json
```

Save these answers! You'll compare them to what you actually find.

---

## CHECKPOINT 1: Find the Web UI Entry Point (15 min)

### Goal
Locate the code that runs when you click "Generate Image" in the web browser.

### Steps

1. **Open the InkyPi web UI in your browser** (if not already running):
   ```bash
   # The web UI should be at http://<your-pi-ip>:5000 or similar
   ```

2. **Open browser DevTools** (F12 or right-click → Inspect)
   - Click on the "Network" tab
   - Click "Generate Image" for any plugin
   - Look at the HTTP request that was sent
   - Note the URL (something like `/api/generate/<plugin_id>` or `/generate/<plugin_id>`)

3. **Find the server code**:
   - Navigate to InkyPi root directory: `~/InkyPi` (or wherever you cloned it)
   - Look for the web server file (probably `server.py`, `app.py`, `main.py`, or in a `web/` folder)
   - Open that file in VS Code

4. **Search for the route**:
   - Use Cmd+F (or Ctrl+F) to search for the URL path you saw (e.g., `/generate`)
   - Find the function that handles this route (it's probably decorated with `@app.route(...)` or similar)

### Deliverable for Checkpoint 1

In `c04_architecture.md`, write:

```markdown
## CHECKPOINT 1: Web UI Entry Point

**HTTP Endpoint**: [the URL path, e.g., `/api/generate/<plugin_id>`]

**File**: [path to file, e.g., `server.py` or `web/routes.py`]

**Function**: [function name, e.g., `generate_plugin_image(plugin_id)`]

**What it does** (in your own words):
[1-2 sentences explaining what this function does when called]
```

### Reflection

- What surprised you about finding this?
- Did you expect the web server to be more complex or simpler?

---

## CHECKPOINT 2: Trace Plugin Discovery (20 min)

### Goal
Understand how InkyPi finds and loads your plugins.

### Steps

1. **From the web route**, look for calls to plugin-related code:
   - Look for imports like `from .plugin_manager import ...` or `from plugins import ...`
   - Find where the function calls something like `plugin_manager.load_plugins()` or `get_plugin(plugin_id)`

2. **Navigate to PluginManager**:
   - Use "Go to Definition" (Cmd+Click or F12 on the import) to jump to `plugin_manager.py` (or equivalent)
   - Alternatively, use `grep` to find it:
     ```bash
     cd ~/InkyPi
     grep -r "class PluginManager" .
     ```

3. **Find plugin discovery logic**:
   - Look for a method that scans for plugins (search for `src/plugins` or `plugin-info.json`)
   - Read the code that:
     - Lists folders in `src/plugins/`
     - Reads `plugin-info.json` files
     - Loads the Python modules

4. **Answer these detective questions**:
   - Where does it look for plugins? (which directory?)
   - What file does it require to recognize a plugin? (plugin-info.json)
   - How does it load the Python code? (importlib? `__import__`?)

### Deliverable for Checkpoint 2

In `c04_architecture.md`, add:

```markdown
## CHECKPOINT 2: Plugin Discovery

**PluginManager file**: [path, e.g., `core/plugin_manager.py`]

**Discovery method**: [method name, e.g., `load_plugins()` or `discover_plugins()`]

**How it works**:
1. [Step 1: e.g., "Scans src/plugins/ directory for folders"]
2. [Step 2: e.g., "For each folder, looks for plugin-info.json"]
3. [Step 3: e.g., "Reads JSON to get plugin ID and class name"]
4. [Step 4: e.g., "Imports the Python module and instantiates the class"]

**Detective Question 1**: What happens if `plugin-info.json` is missing or invalid?
[Your answer based on reading the code]

**Detective Question 2**: How does InkyPi know which Python file to load?
[Your answer: probably from plugin-info.json's "class" field or file naming convention]
```

### Reflection

> **📝 Answer in `workbook.md`** (Checkpoint 2 Reflections)

---

## CHECKPOINT 3: Understand the BasePlugin Contract (25 min)

### Goal
Read `BasePlugin` source code and understand the interface (contract) that all plugins must follow.

### Steps

1. **Find BasePlugin**:
   - Look in your previous plugin code (e.g., `c02_creature_card.py`)
   - See the import: `from ...base_plugin import BasePlugin` (or similar)
   - Use "Go to Definition" to open `base_plugin.py`
   - Or search: `grep -r "class BasePlugin" ~/InkyPi`

2. **Read the class definition**:
   - What methods does `BasePlugin` define?
   - Which methods are abstract (must be implemented by subclasses)?
   - Which methods have default implementations?
   - Read the docstrings (comments explaining each method)

3. **Compare to your CreatureCard**:
   - Open `c02_creature_card.py`
   - Which methods did you implement? (probably `generate_image`)
   - Which methods did you NOT implement? (probably others that BasePlugin provides)

4. **Understand the contract**:
   - What MUST every plugin have? (required methods and signature)
   - What's OPTIONAL? (extra methods, properties)
   - What's FORBIDDEN? (things that would break the plugin system)

### Deliverable for Checkpoint 3

In `c04_architecture.md`, add:

```markdown
## CHECKPOINT 3: BasePlugin Contract

**BasePlugin file**: [path, e.g., `core/base_plugin.py` or `plugins/base.py`]

**Required methods** (that every plugin MUST implement):
- `[method signature, e.g., generate_image(self, settings, device_config) -> Image]`
- [any others?]

**Optional methods** (provided by BasePlugin with defaults):
- `[method name and what it does]`
- [any others?]

**Parameters explained**:
- `settings`: [What is this? Where does it come from? e.g., "User configuration from web UI"]
- `device_config`: [What is this? e.g., "Display hardware info like resolution"]

**Detective Question 3**: What's the return type of `generate_image()`? What happens if you return something else?
[Your answer]

**Detective Question 4**: Look at your C-02 CreatureCard. Which parts came from BasePlugin vs which you added?
[Your answer with specific examples]
```

### Reflection

> **📝 Answer in `workbook.md`** (Checkpoint 3 Reflections)

---

## CHECKPOINT 4: Follow the Image Rendering Flow (30 min)

### Goal
Trace what happens AFTER your `generate_image()` returns the PIL Image.

### Steps

1. **Return to the web route** function (from Checkpoint 1):
   - After calling plugin's `generate_image()`, what does it do with the returned image?
   - Does it call another function/module?

2. **Find the display module**:
   - Look for imports related to display/rendering (e.g., `from .display import update_display`)
   - Search for files with names like `display.py`, `renderer.py`, `inky_display.py`
   - Use grep: `grep -r "def update_display" ~/InkyPi` or similar

3. **Read the rendering code**:
   - How does it convert PIL Image to display format?
   - Where does it write the data? (look for hardware paths like `/dev/inky` or library calls like `inky.display()`)
   - Are there any transformations? (resize, rotate, color conversion?)

4. **Complete the flow**:
   - You should now be able to trace: Button click → Route → PluginManager → YourPlugin → Image → Display → Hardware

### Deliverable for Checkpoint 4

In `c04_architecture.md`, add:

```markdown
## CHECKPOINT 4: Image Rendering Flow

**Display module file**: [path, e.g., `core/display.py`]

**Rendering function**: [function name, e.g., `update_display(image)`]

**What happens to the Image**:
1. [e.g., "PIL Image is returned from generate_image()"]
2. [e.g., "Image is resized/rotated to match display orientation"]
3. [e.g., "Image is converted to display color mode (e.g., palette-based)"]
4. [e.g., "Pixel data is written to hardware via library or device file"]

**Hardware interaction**:
- [e.g., "Uses inky library's display.set_image() method" OR "Writes raw bytes to /dev/fb0"]

**Detective Question 5**: What happens if your plugin returns an image with the WRONG size?
[Your answer based on code reading: does it crash? resize? error?]
```

### Reflection

> **📝 Answer in `workbook.md`** (Checkpoint 4 Reflections)

---

## Practice Challenge 1: Draw the Architecture Diagram (20 min)

### Goal
Create a single diagram showing the COMPLETE flow from user action to display update.

### Instructions

In `c04_architecture.md`, create a section called "System Architecture Diagram" and draw the flow using ASCII art or description:

```markdown
## System Architecture Diagram

User (Web Browser)
    ↓ HTTP POST /api/generate/<plugin_id>
    ↓ (sends: plugin_id, settings)
┌─────────────────────────────────────┐
│ Web Server (server.py)              │
│ - Route handler function            │
│ - Receives request                  │
└─────────────────────────────────────┘
    ↓ calls plugin_manager.generate_image(plugin_id, settings, device_config)
    ↓
┌─────────────────────────────────────┐
│ PluginManager                       │
│ - Has loaded_plugins dict           │
│ - Looks up plugin by ID             │
│ - Calls plugin's generate_image()  │
└─────────────────────────────────────┘
    ↓ plugin_instance.generate_image(settings, device_config)
    ↓
┌─────────────────────────────────────┐
│ Your Plugin (e.g., CreatureCard)    │
│ - Extends BasePlugin                │
│ - Implements generate_image()       │
│ - Creates PIL Image                 │
│ - Returns Image object              │
└─────────────────────────────────────┘
    ↓ returns PIL.Image
    ↓
┌─────────────────────────────────────┐
│ Display Module                      │
│ - Receives PIL Image                │
│ - Converts/resizes if needed        │
│ - Writes to e-ink hardware          │
└─────────────────────────────────────┘
    ↓
┌─────────────────────────────────────┐
│ E-Ink Display Hardware              │
│ - Pixels update                     │
│ - User sees result!                 │
└─────────────────────────────────────┘
```

**OR** describe it in words if you prefer:

```
The flow starts when the user clicks "Generate Image" in the browser. This sends an HTTP POST request to the web server's /api/generate/<plugin_id> route. 

The route handler receives the plugin ID and settings, then calls PluginManager.generate_image(). The PluginManager looks up the plugin instance from its loaded_plugins dictionary (populated during startup). It then calls that instance's generate_image() method, passing settings and device_config.

The plugin's generate_image() (e.g., CreatureCard.generate_image()) creates a PIL Image object and returns it. The PluginManager receives this image and passes it to the Display Module...

[continue describing each step]
```

### Success Criteria

Your diagram or description should show:
- ✅ All major components (Web Server, PluginManager, Plugin, Display, Hardware)
- ✅ The flow direction (arrows or sequence)
- ✅ What data is passed at each step (settings, Image object, etc.)
- ✅ Clear start (user action) and end (display update)

---

## Practice Challenge 2: The "Aha!" Moments (10 min)

### Goal
Reflect on what you learned and what surprised you.

### Instructions

In `c04_architecture.md`, add a section:

```markdown
## My "Aha!" Moments

### 1. [Biggest surprise]
**What I thought**: [Your assumption before reading code]
**What I found**: [What the code actually does]
**Why this matters**: [How this changes your understanding]

### 2. [Second insight]
**What I thought**: _______
**What I found**: _______
**Why this matters**: _______

### 3. [Third discovery]
**What I thought**: _______
**What I found**: _______
**Why this matters**: _______
```

**Examples** (don't copy these, find your own!):
- "I thought BasePlugin had complex magic. Actually, it's just a simple interface!"
- "I assumed plugins were discovered at request time. They're actually loaded once at startup!"
- "I didn't know `device_config` came from hardware detection on boot."

---

## Practice Challenge 3: Debugging Scenarios (10 min)

### Goal
Apply your architecture knowledge to real debugging scenarios.

### Instructions

In `c04_architecture.md`, answer these scenario questions:

```markdown
## Debugging Scenarios (Using My New Knowledge)

### Scenario 1: Plugin doesn't appear in web UI
**Where would you look first?** 
[Your answer: which file/function? why?]

**What could cause this?**
[List 2-3 possibilities based on your understanding of plugin discovery]

### Scenario 2: Plugin shows up but clicking "Generate" crashes
**Where would you check?**
[Your answer]

**Most likely causes?**
[List 2-3 possibilities]

### Scenario 3: Image displays but looks wrong (colors, size)
**Which module is probably the issue?**
[Your answer]

**How would you confirm?**
[Your debugging steps]
```

---

## Success Criteria (Skills You've Proven)

### ✅ Skill 1: Code Tracing - Following Execution Paths

**The Test**:
- [ ] You can trace from HTTP request → your plugin code
- [ ] You know where `generate_image()` gets called from
- [ ] You understand the flow: Web → Manager → Plugin → Display

**This Proves**: You can navigate a codebase systematically, not randomly.

**Metric**: Your architecture diagram shows the complete flow with no missing steps.

---

### ✅ Skill 2: Interface Understanding - Reading Contracts

**The Test**:
- [ ] You've read `BasePlugin` source code
- [ ] You can explain what methods are required vs optional
- [ ] You understand WHY plugins inherit from BasePlugin

**This Proves**: You understand abstraction and contracts (interfaces).

**Metric**: Your "Detective Question 3 & 4" answers correctly identify required methods and explain BasePlugin's purpose.

---

### ✅ Skill 3: System Thinking - Seeing the Big Picture

**The Test**:
- [ ] Your diagram shows all major components
- [ ] You can explain how components interact
- [ ] You understand WHY the system is organized this way (separation of concerns)

**This Proves**: You think architecturally, not just about individual files.

**Metric**: Your "Aha!" moments include at least one insight about system design/architecture.

---

### ✅ Skill 4: Debugging Preparedness - Knowing Where to Look

**The Test**:
- [ ] You can predict where bugs might occur (based on which component)
- [ ] Your debugging scenarios show logical reasoning
- [ ] You can read stack traces and recognize file names

**This Proves**: You're ready to debug production code confidently.

**Metric**: Your debugging scenario answers reference specific files/modules you discovered during code reading.

---

## Validation

Run this from the mission folder:

```bash
cd ~/InkyPi/academy/missions/c04_code_detective
python3 check.py
```

The check script validates:
- ✅ `c04_architecture.md` exists and has required sections
- ✅ Architecture diagram is present
- ✅ All 5 detective questions answered
- ✅ "Aha!" moments documented (proof of thinking)
- ✅ Debugging scenarios completed

---

## Reflection Questions

After completing this mission, answer the final reflection questions in `workbook.md`:
- How has your view of BasePlugin changed?
- When you see a stack trace now, what will you do differently?
- If you were to add a NEW feature to InkyPi, where would you start?
- What's one thing you wish you had known before building your first plugin?

---

## Next Mission Preview

**M-08: The Anime Gallery** - Now that you understand how InkyPi loads and displays plugins, let's build something VISUAL: loading and displaying anime character images!

You'll use `Image.open()` (not just `Image.new()`), learn about file paths, resizing, and compositing. But NOW you'll know exactly where your code fits in the larger system!

---

## Notes

**Time Breakdown** (Estimated):
- Checkpoint 1: 15 min (find web route)
- Checkpoint 2: 20 min (plugin discovery)
- Checkpoint 3: 25 min (BasePlugin contract)
- Checkpoint 4: 30 min (image rendering)
- Practice Challenge 1: 20 min (diagram)
- Practice Challenge 2: 10 min (aha moments)
- Practice Challenge 3: 10 min (debugging scenarios)
- **Total**: ~2 hours 10 min (flexible based on reading speed)

**This is a READING mission**, not a writing mission. You're not creating a new plugin. You're understanding the system that RUNS your plugins. This knowledge will make EVERY future mission easier!
