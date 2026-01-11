# InkyPi Academy — Mission Template (Python)

Use this template to create new mission folders under `academy/missions/` and new learning missions in `academy/syllabus.md`.

---

## 0) Metadata
- **Mission ID**: `M-XX`
- **Codename**: `The ______`
- **Hook**: `"__________"`
- **Recommended duration**: `45–90 minutes`
- **Prereqs**: (which missions must be completed first)
- **Creates / modifies**:
  - Plugin path: `src/plugins/mXX_name/`
  - Files: list exact files the learner will touch

---

## 1) Outcome (Visible Result)
Describe what will be visible in the web UI and/or on the display.

Example:
- “A new plugin appears in the web UI with an icon, and it renders a ‘Hello Name’ card.”

---

## 2) Build (Smallest Slice That Works)
Write the fewest steps that produce the outcome.

**Minimum plugin skeleton**
- `plugin-info.json` with `id`, `display_name`, `class`
- Python file with a class that inherits `BasePlugin`
- A `generate_image(self, settings, device_config)` method returning a `PIL.Image`

**Stop point**: define exactly when the learner should pause and test.

---

## 3) Teach (Micro-lessons)
Teach only what is needed to complete this mission.

For each concept:
- **Definition** (1–2 sentences, plain language)
- **Syntax pattern** (a short snippet, 1–5 lines)
- **Common mistake** (and what the error looks like)
- **Where we use it in this mission** (point to a file/function)

Example concept list:
- Imports
- Variables + types
- Lists/dicts
- `if/for`
- Functions
- Exceptions

---

## 4) Practice (Tiny Experiments)
2–4 “change one thing and observe” tasks.
- Keep them safe (no breaking the whole service).
- Make results visible (layout, text, colors, data values).

Add one **Bad vs Good** exercise:
- Show a small “bad” snippet.
- Ask the learner to fix it and explain why the fix is better.
- Ask when the bad version might still be acceptable.
- Prefer `bad_code.py` (runnable) plus `bad_code_explain.md`.

---

## 5) Check (Acceptance Criteria)
Write objective “done” checks:
- The plugin appears in the UI
- The plugin renders an image without crashing
- The output matches expected behavior

If you add a mission `check.py`, list exactly what it validates.

---

## 5.1) Self-Learning Module (Required)
Include the self-learning module in each mission:
- Add `explain.md`, `predict.md`, `trace.md`, `bad_code.py`, and `bad_code_explain.md`
- Generate `copilot_input.txt` in `check.py` for AI grading
- Extend `check.py` to validate that the files exist and are filled

Template: `academy/self_learning_module.md`

---

## 6) Stretch (Optional)
Only if motivation is high:
- Add settings UI (`settings.html`)
- Add better layout
- Add caching/error screens
- Add a second data source

---

## 7) Reflection (1–3 Questions)
Examples:
- What part was confusing at first, and what made it click?
- What does this function return, and why?
- What would you refactor if you had 30 more minutes?
