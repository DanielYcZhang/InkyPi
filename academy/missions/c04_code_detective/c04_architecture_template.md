# C-04: Architecture Documentation

**Your Name**: _____________  
**Date**: _____________

This file documents your understanding of the InkyPi system architecture.

---

## CHECKPOINT 1: Web UI Entry Point

**HTTP Endpoint**: [the URL path you found, e.g., `/api/generate/<plugin_id>`]

**File**: [path to web server file,  e.g., `server.py`]

**Function**: [handler function name, e.g., `generate_plugin_image(plugin_id)`]

**What it does** (in your own words):
[1-2 sentences explaining what happens when this endpoint is called]

### Reflection
- What surprised you about finding this?
- Did you expect the web server to be more complex or simpler?

---

## CHECKPOINT 2: Plugin Discovery

**PluginManager file**: [path, e.g., `core/plugin_manager.py`]

**Discovery method**: [method name, e.g., `load_plugins()` or `discover_plugins()`]

**How it works**:
1. [Step 1: e.g., "Scans src/plugins/ directory"]
2. [Step 2: e.g., "Looks for plugin-info.json files"]
3. [Step 3: e.g., "Loads Python modules"]
4. [Step 4: e.g., "Instantiates plugin classes"]

**Detective Question 1**: What happens if `plugin-info.json` is missing or invalid?
[Your answer based on reading the code]

**Detective Question 2**: How does InkyPi know which Python file to load?
[Your answer]

### Reflection
- Did you expect plugin discovery to be automatic or manual?
- What could go wrong in this process?

---

## CHECKPOINT 3: BasePlugin Contract

**BasePlugin file**: [path, e.g., `core/base_plugin.py`]

**Required methods** (that every plugin MUST implement):
- `[method signature, e.g., generate_image(self, settings, device_config) -> Image]`
- [any others?]

**Optional methods** (provided by BasePlugin):
- `[method name and purpose]`
- [any others?]

**Parameters explained**:
- `settings`: [What is this? e.g., "User configuration from web UI"]
- `device_config`: [What is this? e.g., "Display hardware specs"]

**Detective Question 3**: What's the return type of `generate_image()`? What happens if you return something else?
[Your answer]

**Detective Question 4**: Look at your C-02 CreatureCard. Which parts came from BasePlugin vs which you added?
[Your answer]

### Reflection
- What's the PURPOSE of BasePlugin?
- How does this relate to "interfaces" or "contracts"?

---

## CHECKPOINT 4: Image Rendering Flow

**Display module file**: [path, e.g., `core/display.py`]

**Rendering function**: [function name, e.g., `update_display(image)`]

**What happens to the Image**:
1. [e.g., "PIL Image returned from generate_image()"]
2. [e.g., "Image resized/rotated"]
3. [e.g., "Converted to display color mode"]
4. [e.g., "Written to hardware"]

**Hardware interaction**:
- [e.g., "Uses inky.display.set_image()" OR "Writes to /dev/fb0"]

**Detective Question 5**: What happens if your plugin returns an image with the WRONG size?
[Your answer]

### Reflection
- How many "layers" are there between your code and hardware?
- Why is the system organized this way?

---

## System Architecture Diagram

Draw the complete flow from user action to display update:

```
User (Web Browser)
    ↓ HTTP POST /api/generate/<plugin_id>
    ↓
┌─────────────────────────────────────┐
│ Web Server (server.py)              │
│ - Route handler                     │
└─────────────────────────────────────┘
    ↓
┌─────────────────────────────────────┐
│ PluginManager                       │
│ - Looks up plugin by ID             │
└─────────────────────────────────────┘
    ↓
┌─────────────────────────────────────┐
│ Your Plugin (e.g., CreatureCard)    │
│ - Generates PIL Image               │
└─────────────────────────────────────┘
    ↓
┌─────────────────────────────────────┐
│ Display Module                      │
│ - Converts and writes to hardware   │
└─────────────────────────────────────┘
    ↓
E-Ink Display Hardware
```

**OR** describe it in words:

```
[Write a paragraph describing the complete flow from button click to display update]
```

---

## My "Aha!" Moments

### 1. [Biggest surprise]
**What I thought**: [Your assumption before]
**What I found**: [What code actually does]
**Why this matters**: [How this changes understanding]

### 2. [Second insight]
**What I thought**: _______
**What I found**: _______
**Why this matters**: _______

### 3. [Third discovery]
**What I thought**: _______
**What I found**: _______
**Why this matters**: _______

---

## Debugging Scenarios

### Scenario 1: Plugin doesn't appear in web UI
**Where would you look first?** 
[Your answer: which file/function?]

**What could cause this?**
[List 2-3 possibilities]

### Scenario 2: Plugin shows up but clicking "Generate" crashes
**Where would you check?**
[Your answer]

**Most likely causes?**
[List 2-3 possibilities]

### Scenario 3: Image displays but looks wrong
**Which module is probably the issue?**
[Your answer]

**How would you confirm?**
[Your debugging steps]

---

## Before/After Comparison

**Before this mission:**
- My understanding of BasePlugin: _______
- When I saw stack traces: _______
- If I needed to debug: _______

**After this mission:**
- My understanding of BasePlugin: _______
- When I see stack traces: _______
- If I need to debug: _______

---

## Next Steps

One thing I'll do differently in future missions:
_______

One question I still have:
_______

---

**Completion**: Run `python3 check.py` to validate this file!
