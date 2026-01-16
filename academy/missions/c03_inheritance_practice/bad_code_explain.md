# Refactoring Challenge (C-03) — Analysis

## Part 1: Change Impact Metrics

**Feature Request**: "Add subtitle to all cards, plus add a new QuestCard type"

### With the Original Code (Stage 2):

1. How many lines did you add or modify in `PetCard_Bad_WithSubtitle`?

2. How many lines did you add or modify in `ItemCard_Bad_WithSubtitle`?

3. How many total lines did you write for `QuestCard_Bad` (including all the duplicated code)?

4. List each place where you had to duplicate the base drawing code:
   - 
   - 
   - 

5. What could break if you forgot to add the subtitle in one of the three classes?

6. Total lines changed in Stage 2: ___

---

### With Your Refactored Code (Stage 3):

7. How many lines did you add/modify in `BaseCard` to add subtitle support?

8. How many lines did you add/modify in `PetCard_Good`?

9. How many lines did you add/modify in `ItemCard_Good`?

10. How many total lines for `QuestCard_Good` (NOT counting inherited code)?

11. Where is the subtitle drawing code located? (Which class?)

12. Total lines changed in Stage 3: ___

13. **Improvement ratio**: ___ (Stage 2 total ÷ Stage 3 total)

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

15. How many lines will they need to copy-paste? ___

16. If you later change the border thickness in `BaseCard`, does their `AchievementCard` get the update automatically?
   - Yes / No
   - Why?

### With your refactored (Stage 3) approach:

17. Write the EXACT code your teammate would need to write for `AchievementCard`:

```python
class AchievementCard(BaseCard):
    def __init__(self, title, subtitle, achievement_name):
        # Your answer here
        
    
    def draw(self, draw, w, h):
        # Your answer here
```

18. How many lines is that? ___

19. If you later change the border thickness in `BaseCard`, does their `AchievementCard` get the update automatically?
   - Yes / No
   - Why?

20. Which approach is better for team collaboration? Explain in 1-2 sentences:

---

## Part 3: Second Feature Request (Stress Test)

**New Requirement**: "All cards need a background color option. Add a `bg_color` parameter and draw a colored rectangle as the background (before the border)."

21. With the Stage 2 approach (no inheritance), predict:
   - How many classes need updating? ___
   - How many lines of code total? ___
   - Risk of bugs from forgetting one class: Low / Medium / High

22. With the Stage 3 approach (with inheritance), predict:
   - How many classes need updating? ___
   - How many lines of code total? ___
   - Risk of bugs: Low / Medium / High

23. At what point does inheritance become ESSENTIAL instead of just "nice to have"?
   - When you have ___ or more subclasses?
   - When the shared code is ___ or more lines?
   - Complete: "Inheritance becomes essential when ___"

---

## Part 4: When "Bad" (No Inheritance) is Actually Acceptable

24. List 2-3 SPECIFIC scenarios where NOT using inheritance is reasonable:

   **Scenario 1**: 
   - Context: 
   - Why it's OK: 

   **Scenario 2**:
   - Context:
   - Why it's OK:

   **Scenario 3** (optional):
   - Context:
   - Why it's OK:

25. The "Rule of Three" says: Don't create a base class until you have at least 3 similar classes. Why do you think this rule exists?

26. When should you AVOID inheritance? (Hint: What if the classes aren't actually related?)
   - Bad example: `class Dog(Database)` - why is this wrong?

---

## Part 5: Real-World Connection

27. Think about a mobile game you've played that has many similar items (characters, weapons, enemies, etc.). How do you think the developers organized their code?
   - Do they copy-paste each character's base stats?
   - Or do they use inheritance?
   - What clues tell you?

28. Imagine you're the lead programmer on a team of 5 developers building a card game. Everyone is creating new card types. Would you:
   - [ ] Let everyone copy-paste the base card code
   - [ ] Create a BaseCard class and tell everyone to inherit from it
   - Explain your choice and what problems it prevents:

29. You've been working on a card game for 6 months. You now have 50 different card types. The designer says "change the border color on ALL cards." How long does this take?
   - Without inheritance: ___
   - With inheritance: ___

30. Complete this sentence:
   "The main reason we use inheritance is not to save typing, but to ___________________"

---

## Reflection

31. What surprised you most about this refactoring exercise?

32. Before this mission, what did you think `super()` did? What do you think now?

33. Can you think of a situation where you've seen duplicated code (in a game, app, or website) that could have been solved with inheritance? Describe it:
