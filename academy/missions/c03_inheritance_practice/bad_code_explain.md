# Refactoring Challenge (C-03) — Analysis

## Part 1: Change Impact Metrics

**Feature Request**: "Add subtitle to all cards, plus add a new QuestCard type"

### With the Original Code (Stage 2):

1. How many lines did you add or modify in `PetCard_Bad_WithSubtitle`?
3
2. How many lines did you add or modify in `ItemCard_Bad_WithSubtitle`?
3
3. How many total lines did you write for `QuestCard_Bad` (including all the duplicated code)?
16
4. List each place where you had to duplicate the base drawing code:
   - petcard_bad
   - itemcard_bad
   - questcard_bad

5. What could break if you forgot to add the subtitle in one of the three classes?
you would have a missing subtitle in one of the classes, so the ui would look weird
6. Total lines changed in Stage 2: 22

---

### With Your Refactored Code (Stage 3):

7. How many lines did you add/modify in `BaseCard` to add subtitle support?
3
8. How many lines did you add/modify in `PetCard_Good`?
1
9. How many lines did you add/modify in `ItemCard_Good`?
1
10. How many total lines for `QuestCard_Good` (NOT counting inherited code)?
7
11. Where is the subtitle drawing code located? (Which class?)
BaseCard class
12. Total lines changed in Stage 3: 12

13. **Improvement ratio**: 1.8 (Stage 2 total ÷ Stage 3 total)

these questions were basically the same ones in bad_code.py, remove it in bad_code.py next challenge
---

## Part 2: The Team Collaboration Test

**Scenario**: Your teammate (who has never seen this code) needs to add a 4th card type: `AchievementCard` with a medal icon.

### With the original (Stage 2) approach:

14. List what your teammate needs to figure out and do:
   - [ ] Find where the border drawing code is
   - [ ] Find where the title drawing code is
   - [ ] Find where the subtitle drawing code is
   - [ ] Copy-paste all of that into the new class
   - [ ] Add the medal icon code
   - [ ] Hope they didn't mess up the copy-paste

15. How many lines will they need to copy-paste? like 10 i think, depends really

16. If you later change the border thickness in `BaseCard`, does their `AchievementCard` get the update automatically?
   - Yes / No
   no
   - Why?
   because they aren't using inheritance

### With your refactored (Stage 3) approach:

17. Write the EXACT code your teammate would need to write for `AchievementCard`:

```python
class AchievementCard(BaseCard):
    def __init__(self, title, subtitle, achievement_name):
        super().__init__(title, subtitle)
        self.achievement_name = achievement_name
    
    def draw(self, draw, w, h):
        super().draw(draw, w, h)
        # whatever draw medal code is
```

18. How many lines is that? around 6 excluding the medal code

19. If you later change the border thickness in `BaseCard`, does their `AchievementCard` get the update automatically?
   - Yes / No
   yes
   - Why?
   because it is using inheritance

20. Which approach is better for team collaboration? Explain in 1-2 sentences:
the refactored code is better because it is using inheritance
---

## Part 3: Second Feature Request (Stress Test)

**New Requirement**: "All cards need a background color option. Add a `bg_color` parameter and draw a colored rectangle as the background (before the border)."

21. With the Stage 2 approach (no inheritance), predict:
   - How many classes need updating?
   4
   - How many lines of code total?
   around like 15
   - Risk of bugs from forgetting one class: Low / Medium / High
   medium-high ish

22. With the Stage 3 approach (with inheritance), predict:
   - How many classes need updating?
   1
   - How many lines of code total?
   like 5
   - Risk of bugs: Low / Medium / High
   pretty low

23. At what point does inheritance become ESSENTIAL instead of just "nice to have"?
   - When you have 3 or more subclasses?
   - When the shared code is 10 or more lines?
   - Complete: "Inheritance becomes essential when when you have 3 or more subclasses and/or the shared code is 10 or more lines"

---

## Part 4: When "Bad" (No Inheritance) is Actually Acceptable

24. List 2-3 SPECIFIC scenarios where NOT using inheritance is reasonable:

   **Scenario 1**: 
   - Context: when the logic between classes is completely different
   - Why it's OK: because you don't have stuff to share so inheritance is not needed

   **Scenario 2**:
   - Context:when you only have like 2 classes
   - Why it's OK: sometimes its just easier to copy and past if its just a small amount

   **Scenario 3** (optional):
   - Context: when its like 1 line of code you need to copy
   - Why it's OK: sometimes its just easier to copy and past if its just a small amount 

25. The "Rule of Three" says: Don't create a base class until you have at least 3 similar classes. Why do you think this rule exists?
   because if you make a base class too early you might end up with stuff that isn't similar so you wait until around 3 similar classes to make a base class to make sure the pattern is real
26. When should you AVOID inheritance? (Hint: What if the classes aren't actually related?)
   - Bad example: `class Dog(Database)` - why is this wrong?
   because dogs and databases aren't related much at all

---

## Part 5: Real-World Connection

27. Think about a mobile game you've played that has many similar items (characters, weapons, enemies, etc.). How do you think the developers organized their code?
   - Do they copy-paste each character's base stats?
   no
   - Or do they use inheritance?
   yes
   - What clues tell you?
   shared things that are common between all the charactesr like health, damage, movement speed.

28. Imagine you're the lead programmer on a team of 5 developers building a card game. Everyone is creating new card types. Would you:
   - [ ] Let everyone copy-paste the base card code
   - [ ] Create a BaseCard class and tell everyone to inherit from it
   - Explain your choice and what problems it prevents:
i would create a BaseCard class and tell everyone to inherit from it becauseit prevents code duplication and makes it easier to change things later on

29. You've been working on a card game for 6 months. You now have 50 different card types. The designer says "change the border color on ALL cards." How long does this take?
   - Without inheritance: a long time
   - With inheritance: a short time

30. Complete this sentence:
   "The main reason we use inheritance is not to save typing, but to prevent code duplication and make it easier to change things later on"

---

## Reflection

31. What surprised you most about this refactoring exercise?
idk

32. Before this mission, what did you think `super()` did? What do you think now?
i thought it was required ig, now i understand that it calls the parent's class method to reuse its logic

33. Can you think of a situation where you've seen duplicated code (in a game, app, or website) that could have been solved with inheritance? Describe it:
no i cant think of a situation
