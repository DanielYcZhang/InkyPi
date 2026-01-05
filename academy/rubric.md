# InkyPi Academy — Mission Completion Rubric

This is a lightweight rubric for a parent/coach (or AI agent) to evaluate “done” without turning learning into a test.

## A) Outcome (0–2)
- **0**: Nothing visible changes; unclear goal.
- **1**: Partial visible output (renders sometimes / only in one case).
- **2**: Outcome is clearly visible and repeatable.

## B) Understanding (0–2)
- **0**: Can’t explain what the code does.
- **1**: Can explain the happy path (“it works”), but not why.
- **2**: Can explain what happens + why, and what would break it.

## C) Code Quality (0–2)
- **0**: Random copy/paste; hard to modify.
- **1**: Works, but lots of magic numbers / repeated code.
- **2**: Names are clear; repeated code extracted to small functions; minimal “magic”.

## D) Debugging Behavior (0–2)
- **0**: Gets stuck; waits for rescue immediately.
- **1**: Tries one thing (print, change a value), then asks for help.
- **2**: Reads error messages, isolates the failure, tries a couple targeted fixes.

## E) Stretch (0–2, optional)
- **0**: No stretch attempted.
- **1**: Attempted a stretch, even if imperfect.
- **2**: Stretch works and is integrated cleanly.

**Typical “pass”**: A + B + D at 1+ (the win is outcome + learning + debugging).

