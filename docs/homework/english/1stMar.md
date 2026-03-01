# Logic Puzzles: Lists
Date: 1st Mar 2026
Topic: Lists — Building, Filtering & Searching

*Five puzzles to introduce the list — Python's most useful container. A list holds multiple values in one variable: `basket = []` starts empty; `basket.append(x)` adds `x` to the end; `len(basket)` tells you how many items are inside.*

---

## Puzzle 1: The Robot Fruit Picker (Easy)
**The Story**: A robot walks past trees numbered 1 to 10. It only picks fruit from a tree if the tree number is **divisible by 3**. Each picked tree number is added to its basket list.

**The Question**: Build the `basket` list using a loop. What does the basket contain? How many fruits did it pick, and what is the total weight (tree number = weight in grams)?

**Example Test Case**:
- Trees 1 to 6: trees 3 and 6 are divisible by 3 → basket = `[3, 6]`, count = 2, total = 9.

**Hint**: Start with `basket = []`. Inside a loop from 1 to 10, use `if tree % 3 == 0:` then `basket.append(tree)`.

**Check Your Logic**:
- Trees 1–6: basket = `[3, 6]`, count = **2**, total = **9**.
- Trees 1–10: basket = `[3, 6, 9]`, count = **3**, total = **18**.

```python
# Starting Code
basket = []

for tree in range(1, 11):
    # If tree number is divisible by 3, append it to basket
    pass

print(f"Basket: {basket}")
print(f"Number of fruits: {len(basket)}")
print(f"Total weight: {sum(basket)} grams")
```

---

## Puzzle 2: The School Report (Easy–Medium)
**The Story**: A teacher has 12 student scores and wants two separate lists: one for students who **passed** (score ≥ 60) and one for students who **failed** (score < 60).

**The Question**: Loop over the scores and fill the two lists. How many passed and how many failed?

Scores: `[45, 72, 88, 55, 91, 60, 78, 43, 95, 67, 82, 50]`

**Example Test Case**:
- Scores `[80, 55, 65]`: passed = `[80, 65]`, failed = `[55]`.

**Hint**: Start with `passed = []` and `failed = []`. Use `for score in scores:` and inside, check `if score >= 60:` to decide which list to append to.

**Check Your Logic**:
- Passed (score ≥ 60): 72, 88, 91, 60, 78, 95, 67, 82 → **8 students**.
- Failed (score < 60): 45, 55, 43, 50 → **4 students**.

```python
# Starting Code
scores = [45, 72, 88, 55, 91, 60, 78, 43, 95, 67, 82, 50]
passed = []
failed = []

for score in scores:
    # Append to passed or failed depending on the score
    pass

print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Passed count: {len(passed)}, Failed count: {len(failed)}")
```

---

## Puzzle 3: The Baker's Running Total (Medium)
**The Story**: A baker writes down his earnings each day for a week. He wants a "running total" list — after each day, how much has he earned *so far*?

Daily earnings: `[12, 8, 15, 5, 20, 10, 18]`

**The Question**: Build a `running_totals` list where each entry is the cumulative sum up to that day.

**Example Test Case**:
- Daily `[10, 5, 3]` → running totals = `[10, 15, 18]`.

**Hint**: Keep a `total = 0` variable. For each `earning` in the list, add it to `total`, then `running_totals.append(total)`.

**Check Your Logic**:
- After day 1: **12**.
- After day 3: **35** (12 + 8 + 15).
- After day 7 (final total): **88**.

```python
# Starting Code
daily_earnings = [12, 8, 15, 5, 20, 10, 18]
running_totals = []
total = 0

for earning in daily_earnings:
    # 1. Add earning to total
    # 2. Append total to running_totals
    pass

print(f"Running totals: {running_totals}")
print(f"Final total: {total}")
```

---

## Puzzle 4: The Mountain Hiker (Medium–Hard)
**The Story**: A hiker records their **elevation change** each hour. Starting at 0 meters, positive numbers mean climbing up and negative numbers mean going down.

Hourly changes: `[3, -1, 5, -2, 4, -3, 6, -1, 2, -4]`

**The Question**: Build an `elevations` list (elevation after each hour). Then find the **highest elevation** reached — but **without using Python's built-in `max()` function**. Use a second loop to search through the list yourself.

**Example Test Case**:
- Changes `[3, -1, 5]` → elevations = `[3, 2, 7]`, highest = **7**.

**Hint**: Part 1: start at `elevation = 0`, loop over changes, update `elevation`, append to list. Part 2: start `highest = 0`, loop over `elevations`, update `highest` if the current value is bigger.

**Check Your Logic**:
- Elevations list: `[3, 2, 7, 5, 9, 6, 12, 11, 13, 9]`.
- Highest elevation: **13** (reached at hour 9).

```python
# Starting Code
changes = [3, -1, 5, -2, 4, -3, 6, -1, 2, -4]
elevation = 0
elevations = []

# Part 1: build the elevations list
for change in changes:
    # Update elevation and append to elevations
    pass

# Part 2: find the highest elevation (no max() allowed!)
highest = 0
for e in elevations:
    # If e is greater than highest, update highest
    pass

print(f"Elevation history: {elevations}")
print(f"Highest point reached: {highest} meters")
```

---

## Puzzle 5: The Bouncing Ball (Challenging)
**The Story**: A rubber ball is dropped from **100 meters**. Each time it bounces, it reaches **60%** of the previous height. You record every bounce height (rounded to 2 decimal places) — but only while the height is **≥ 1 meter** (below that it barely moves).

**The Question**: Build a `bounces` list of all recorded bounce heights. How many bounces are recorded? What is the height of the **5th bounce**?

**Example Test Case**:
- Start 10m, factor 0.5: bounce 1 = 5.0, bounce 2 = 2.5, bounce 3 = 1.25, bounce 4 = 0.625 → stop.
- Bounces recorded: `[5.0, 2.5, 1.25]`, count = **3**, 2nd bounce = **2.5**.

**Hint**: Start `height = 100.0`. Use `while True:`. Inside: update `height = round(height * 0.6, 2)`. If `height < 1`, use `break` to stop. Otherwise, `bounces.append(height)`. Then access the 5th bounce with `bounces[4]` (lists start at index 0!).

**Check Your Logic**:
- Bounce 1: **60.0**, Bounce 2: **36.0**, Bounce 3: **21.6**, Bounce 4: **12.96**, Bounce 5: **7.78**.
- Total bounces recorded (height ≥ 1): **9**.
- Bounce 10 = 0.6 (< 1, not recorded).

```python
# Starting Code
height = 100.0
bounce_factor = 0.6
bounces = []

while True:
    height = round(height * bounce_factor, 2)
    if height < 1:
        break
    # Append height to bounces
    pass

print(f"All bounces: {bounces}")
print(f"Number of bounces: {len(bounces)}")
print(f"5th bounce height: {bounces[4]}")  # index 4 = 5th item
```
