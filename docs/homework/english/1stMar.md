# Logic Puzzles: Lists
Date: 1st Mar 2026
Topic: Lists — Building, Filtering & Searching

*Five puzzles to introduce the list — Python's most useful container. A list holds multiple values in one variable: `basket = []` starts empty; `basket.append(x)` adds `x` to the end; `len(basket)` tells you how many items are inside. Below are five more exercises (easy to hard).*

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

---

## Puzzle 6: The Square Collector (Easy)
**The Story**: You need a list of **squares** of the numbers 1 through 8 (1², 2², 3², …). Each squared value goes into a list.

**The Question**: Build a `squares` list using a loop. What is the list? What is the **sum** of the squares?

**Example Test Case**:
- Numbers 1 to 4: squares = `[1, 4, 9, 16]`, sum = **30**.

**Hint**: `squares = []`, then loop `for n in range(1, 9):` and `squares.append(n * n)`.

**Check Your Logic**:
- Squares list: `[1, 4, 9, 16, 25, 36, 49, 64]`.
- Sum of squares: **204**.

```python
# Starting Code
squares = []

for n in range(1, 9):
    # Append n squared to squares
    pass

print(f"Squares: {squares}")
print(f"Sum: {sum(squares)}")
```

---

## Puzzle 7: The First Pass (Easy–Medium)
**The Story**: A teacher looks through exam scores in order. She wants to find the **first** score that is **≥ 70** (first pass). She also wants to know **which position** (index) that score is at.

Scores: `[55, 62, 48, 71, 59, 88, 73, 65]`

**The Question**: Loop through the list. When you find the first score ≥ 70, store it and its index, then stop. Print the value and the position (e.g. "First pass at index 3: 71").

**Example Test Case**:
- Scores `[60, 65, 72, 80]`: first pass is **72** at index **2**.

**Hint**: Use `for i in range(len(scores)):` so you have both index `i` and value `scores[i]`. When `scores[i] >= 70`, save the value and index, then `break`.

**Check Your Logic**:
- First score ≥ 70: **71** at index **3** (4th position).

```python
# Starting Code
scores = [55, 62, 48, 71, 59, 88, 73, 65]
first_pass_value = None
first_pass_index = None

for i in range(len(scores)):
    # If scores[i] >= 70, set first_pass_value and first_pass_index, then break
    pass

print(f"First pass at index {first_pass_index}: {first_pass_value}")
```

---

## Puzzle 8: The Daily Difference (Medium)
**The Story**: A weather station records the **temperature at noon** each day for a week. You want a list of **day-to-day changes**: today's temp minus yesterday's.

Temperatures: `[20, 22, 19, 23, 21, 24, 20]`

**The Question**: Build a `differences` list. The first entry is `temperatures[1] - temperatures[0]`, the second is `temperatures[2] - temperatures[1]`, and so on. How many differences are there?

**Example Test Case**:
- Temps `[10, 15, 12]` → differences = `[5, -3]` (two differences).

**Hint**: `differences = []`. Loop with `for i in range(1, len(temperatures)):` and append `temperatures[i] - temperatures[i - 1]`.

**Check Your Logic**:
- Differences: `[2, -3, 4, -2, 3, -4]` (length **6**).

```python
# Starting Code
temperatures = [20, 22, 19, 23, 21, 24, 20]
differences = []

for i in range(1, len(temperatures)):
    # Append (today - yesterday) to differences
    pass

print(f"Day-to-day differences: {differences}")
print(f"Number of differences: {len(differences)}")
```

---

## Puzzle 9: No Duplicates (Medium–Hard)
**The Story**: You have a list that might repeat numbers. You want a **new** list with each number appearing **only the first time** it occurs. Order must stay the same.

Numbers: `[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]`

**The Question**: Build a `unique` list. Loop over the original list; for each number, only append it to `unique` if it is **not already** in `unique`.

**Example Test Case**:
- `[2, 3, 2, 4, 3]` → unique = `[2, 3, 4]`.

**Hint**: `unique = []`. For each `x in numbers:`, check `if x not in unique:` then `unique.append(x)`.

**Check Your Logic**:
- Unique list: `[3, 1, 4, 5, 9, 2, 6]` (length **7**).

```python
# Starting Code
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
unique = []

for x in numbers:
    # If x is not already in unique, append it
    pass

print(f"Unique (order preserved): {unique}")
print(f"Count: {len(unique)}")
```

---

## Puzzle 10: The Consecutive Triplet Sums (Challenging)
**The Story**: You have a list of numbers. You want a new list where each entry is the **sum of three consecutive** numbers: first = nums[0]+nums[1]+nums[2], second = nums[1]+nums[2]+nums[3], and so on.

Numbers: `[10, 20, 30, 40, 50, 60]`

**The Question**: Build a `triplet_sums` list. Use a loop over **indices** so you can access `nums[i]`, `nums[i+1]`, and `nums[i+2]`. How far can `i` go? (Stop when there aren’t three numbers left.)

**Example Test Case**:
- `[5, 10, 15, 20]` → triplet_sums = `[30, 45]` (5+10+15 and 10+15+20).

**Hint**: Loop `for i in range(len(nums) - 2):`. Inside, append `nums[i] + nums[i+1] + nums[i+2]` to `triplet_sums`.

**Check Your Logic**:
- Triplet sums: `[60, 90, 120, 150]` (length **4**).
- First sum = 10+20+30 = **60**, last = 40+50+60 = **150**.

```python
# Starting Code
nums = [10, 20, 30, 40, 50, 60]
triplet_sums = []

for i in range(len(nums) - 2):
    # Append sum of nums[i], nums[i+1], nums[i+2]
    pass

print(f"Triplet sums: {triplet_sums}")
print(f"Count: {len(triplet_sums)}")
```
