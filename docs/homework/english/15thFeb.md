# Logic Puzzle: One for Today
Date: 15th Feb 2026
Topic: Loops & Conditions

*One short puzzle—simpler than next week's game theory set.*

## Puzzle: The Even Number Collector
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
