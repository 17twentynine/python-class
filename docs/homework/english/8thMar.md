# Logic Puzzles: Lists (More Practice)
Date: 8th Mar 2026
Topic: Lists — Indices, Searching & Sliding Windows

*Five more list puzzles (easy to hard). Build lists, find first matches, differences, unique values, and sliding-window sums.*

---

## Puzzle 1: The Square Collector (Easy)
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

## Puzzle 2: The First Pass (Easy–Medium)
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

## Puzzle 3: The Daily Difference (Medium)
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

## Puzzle 4: No Duplicates (Medium–Hard)
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

## Puzzle 5: The Consecutive Triplet Sums (Challenging)
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
