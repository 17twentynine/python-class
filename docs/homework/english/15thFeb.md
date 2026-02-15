# Logic Puzzles: Three for Today
Date: 15th Feb 2026
Topic: Loops & Conditions

*Three short puzzles—simpler than next week's game theory set.*

## Puzzle 1: The Even Number Collector
**The Story**: A robot is told to walk past boxes numbered 1, 2, 3, … up to 50. It may only pick up a box if the number on it is **even**. It adds each picked number to its running total.

**The Question**: What is the **total** of all even numbers from 1 to 50? (So: 2 + 4 + 6 + … + 50.)

**Example Test Case**:
- If the range were 1 to 10: evens are 2, 4, 6, 8, 10 → total = **30**.

**Hint**: Loop from 1 to 50. Inside the loop, use `if number % 2 == 0:` to check if the number is even. If it is, add it to a variable like `total`.

**Check Your Logic**:
- For 1 to 10: total = **30**.
- For 1 to 50: total = **650**.

```python
# Starting Code
total = 0

for number in range(1, 51):
    # If number is even, add it to total
    pass

print(f"Total of evens (1 to 50): {total}")
```

---

## Puzzle 2: The Fives Counter
**The Story**: A teacher has a list of seat numbers from 1 to 100. She wants to know how many seats are in rows that get a "group prize"—and those are exactly the rows whose number is divisible by 5 (5, 10, 15, …, 100).

**The Question**: How many numbers from 1 to 100 are **divisible by 5**? (Just count them.)

**Example Test Case**:
- If the range were 1 to 20: the multiples of 5 are 5, 10, 15, 20 → count = **4**.

**Hint**: Loop from 1 to 100. Use `if number % 5 == 0:` and then add 1 to a counter variable.

**Check Your Logic**:
- For 1 to 20: count = **4**.
- For 1 to 100: count = **20**.

```python
# Starting Code
count = 0

for number in range(1, 101):
    # If number is divisible by 5, add 1 to count
    pass

print(f"Numbers divisible by 5 (1 to 100): {count}")
```

---

## Puzzle 3: The Sum of the First Odd Numbers
**The Story**: The first **odd** numbers are 1, 3, 5, 7, 9, … (each is 2 more than the previous). You need the sum of the **first 10** of these: 1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19.

**The Question**: What is that total?

**Example Test Case**:
- First 3 odd numbers: 1 + 3 + 5 = **9**.

**Hint**: You can loop 10 times. The 1st odd is 1, the 2nd is 3, the 3rd is 5—so the **i-th** odd number is `2 * i - 1` (when i is 1, 2, 3, …). Add each to a running total.

**Check Your Logic**:
- First 3 odds: **9**.
- First 5 odds: **25** (1+3+5+7+9).
- First 10 odds: **100**.

```python
# Starting Code
total = 0

for i in range(1, 11):
    # The i-th odd number is (2 * i - 1). Add it to total.
    pass

print(f"Sum of first 10 odd numbers: {total}")
```
