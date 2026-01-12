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

## 2) Concepts You Will Learn (List Only)
List the concepts (no explanations here). Example:
- Variables
- Loops
- Function parameters
- Coordinates

---

## 3) Glossary (with Examples)
Define 5–10 terms with a one-line definition and a short example.
Each term should point to a real line in the mission code.

---

## 4) Briefing (Concept Explanations)
The detailed teaching happens in `briefing.md`, not in `mission.md`.
For each concept in the list:
1) Analogy
2) Definition
3) Tiny code snippet
4) Where it appears in this mission

---

## 5) Build (Smallest Slice That Works)
Write the fewest steps that produce the outcome.

**Minimum plugin skeleton**
- `plugin-info.json` with `id`, `display_name`, `class`
- Python file with a class that inherits `BasePlugin`
- A `generate_image(self, settings, device_config)` method returning a `PIL.Image`

**Stop point**: define exactly when the learner should pause and test.

---

## 6) Practice (Inside the .py Template)
All practice and “Do-It” tasks live in the `.py` template as TODOs.
Keep tasks short, visible, and safe.
Include the **Surprise** as a TODO in the `.py` template.

Include one **Bad vs Good** exercise:
- Provide `bad_code.py` and `bad_code_explain.md`.
- Ask the learner to fix the bad code and explain why it is better.
- Ask when the bad version might still be acceptable.

---

## 7) Check (Acceptance Criteria)
Write objective “done” checks:
- The plugin appears in the UI
- The plugin renders an image without crashing
- The output matches expected behavior

If you add a mission `check.py`, list exactly what it validates.

---

## 7.1) Self-Learning Module (Required)
Include the self-learning module in each mission:
- Add `explain.md`, `predict.md`, `trace.md`, `bad_code.py`, and `bad_code_explain.md`
- Generate `copilot_input.txt` in `check.py` for AI grading
- Extend `check.py` to validate that the files exist and are filled
 - Put concept checkpoints in `explain.md`

Template: `academy/self_learning_module.md`

---

## 8) Surprise (The Wow Moment)
Add a small surprise element (font, visual effect, data reveal).

---

## 9) Stretch (Optional)
Only if motivation is high:
- Add settings UI (`settings.html`)
- Add better layout
- Add caching/error screens
- Add a second data source

---

## 10) Reflection (1–3 Questions)
Examples:
- What part was confusing at first, and what made it click?
- What does this function return, and why?
- What would you refactor if you had 30 more minutes?
