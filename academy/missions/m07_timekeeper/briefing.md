# Briefing: Mission 07 — The Timekeeper

You have awakened a plugin. Now you will make it display something that changes in the real world:
**time**.

---

## The Big Idea
Time is “data from the world”. Your plugin will:
1) fetch the current time (`datetime.now(...)`)
2) turn it into text (formatting)
3) draw it on the screen

---

## New Tools (Micro-lessons with Syntax Cards)

### 1) Variables = "Name a value"
**Hook**: A variable is a labeled chest. Put a value in, get it back later.

**Definition**: A variable stores a reference to a value so you can reuse it.

**Syntax**
```py
now = datetime.now()
hour = now.hour
```

**Common mistakes**
- Typos in variable names → `NameError: name '...' is not defined`
- Reusing names like `time` or `datetime` (shadowing imports) → confusing bugs.

**Where used in this mission**: `src/plugins/m07_timekeeper/m07_timekeeper.py` inside `generate_image(...)`

### 2) `datetime` = "Ask the clock for the current time"
**Hook**: `datetime` is your clock tool.

**Definition**: `datetime` is a standard library module for working with dates and times.

**Syntax**
```py
from datetime import datetime
now = datetime.now()
```

**Common mistakes**
- Forgetting the import → `NameError: datetime is not defined`
- Writing `import datetime` then calling `datetime.now()` (wrong) instead of `datetime.datetime.now()`.

**Where used in this mission**: `src/plugins/m07_timekeeper/m07_timekeeper.py`

### 3) Formatting = "Turn data into text"
**Hook**: The screen can’t display “a datetime object”. It needs a string.

**Definition**: Formatting converts values into human-friendly strings.

**Syntax**
```py
time_text = now.strftime("%H:%M")
date_text = now.strftime("%a %b %d")
```
- `%H` = 24-hour hour
- `%M` = minutes

**Common mistakes**
- Using the wrong format codes (fix by changing the pattern and observing output).

**Where used in this mission**: `src/plugins/m07_timekeeper/m07_timekeeper.py`

### 4) f-strings = "Inject values into text"
**Hook**: f-strings are your text magic for mixing variables with words.

**Definition**: An f-string lets you put expressions inside `{}` and Python evaluates them.

**Syntax**
```py
label = f"Time: {time_text}"
```

**Common mistakes**
- Forgetting the `f` → you literally see `{time_text}` on screen.

**Where used in this mission**: `src/plugins/m07_timekeeper/m07_timekeeper.py`

### 5) Types (`str` vs `int`) = "Different kinds of items"
**Hook**: A number and a word are different tools.

**Definition**: Python values have types. Strings hold text; ints hold whole numbers.

**Syntax**
```py
minute = now.minute      # int
minute_text = str(minute)  # str
```

**Common mistakes**
- Trying to combine `str` and `int` without converting → `TypeError`

**Where used in this mission**: when building the final text you draw

---

## What “Success” Looks Like
- The plugin shows the correct time.
- After a minute passes and you refresh the plugin, the displayed minute changes.
- Running `python3 check.py` in this mission folder prints PASS.

