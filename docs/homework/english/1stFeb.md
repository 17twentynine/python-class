# Logic Puzzles: Mastery level
Date: 1st Feb 2026
Topic: Accumulation, Sequences & Nested Loops

*Three advanced puzzles to push your Python skills to the limit.*

## Puzzle 1: The Greedy Baker (Accumulation)
**The Story**: A baker is very happy. To celebrate his 1-month anniversary, he decides to give away cookies.
- On **Day 1**, he gives away **1 cookie**.
- On **Day 2**, he gives away **2 cookies**.
- On **Day 3**, he gives away **3 cookies**.
- This continues for **30 days**.

**The Question**: How many total cookies did the baker give away by the end of Day 30?

**Example Test Case**:
- Input: `5 days`
- Logic: 1 + 2 + 3 + 4 + 5 = 15
- Output: `15 cookies`

**Hint**: You need a variable `total_cookies = 0`. Inside a loop that runs 30 times, keep adding the `day` number to your `total_cookies`.

```python
# Starting Code
total_cookies = 0

for day in range(1, 31):
    # Your logic here
    pass

print(f"Total cookies: {total_cookies}")
```

**Check Your Logic**:
- If you check for 10 days, the answer should be **55**.
- If you check for 20 days, the answer should be **210**.
- What is the answer for **30 days**?

---

## Puzzle 2: The Fibonacci Rabbits (Sequences)
**The Story**: You have a pair of legendary Fibonacci rabbits. 
- In **Month 1**, you have **1 pair**.
- In **Month 2**, you still have **1 pair**.
- From **Month 3** onwards, the number of pairs is the sum of the two previous months!
- (Month 3 = Month 1 + Month 2 = 1 + 1 = 2)
- (Month 4 = Month 2 + Month 3 = 1 + 2 = 3)

**The Question**: How many pairs of rabbits will you have at **Month 12**?

**Example Sequence**: `1, 1, 2, 3, 5, 8, 13...`

**Hint**: You need two variables to remember the "last month" and the "month before that".

```python
# Starting Code
a = 1 # Month 1
b = 1 # Month 2

# We already have 2 months, so loop from 3 to 12
for month in range(3, 13):
    new_pairs = a + b
    # Now, update 'a' and 'b' for the next month!
    # a becomes what b was
    # b becomes the new_pairs
    pass

print(f"Month 12: {b} pairs")
```

**Check Your Logic**:
- Month 5: **5 pairs**
- Month 7: **13 pairs**
- Month 10: **55 pairs**

---

## Puzzle 3: The Digital Clock (Triple Nested Loops)
**The Story**: You are building the software for a high-tech digital clock.
It needs to count every single second of the day, from `00:00:00` to `23:59:59`.

**The Question**: Use **three** loops (one inside the other) to print the time in the format `HH:MM:SS`. 

**Example Output**:
```
00:00:00
00:00:01
00:00:02
...
23:59:59
```

**Hint**: 
- The outer loop is for **Hours** (0 to 23).
- The middle loop is for **Minutes** (0 to 59).
- The inner loop is for **Seconds** (0 to 59).
- Use `f"{h:02}:{m:02}:{s:02}"` to make sure 7 becomes `07`.
- **Power Hint**: Use `print(time_string, end="\r")` to print on the same line again and again!

```python
# Starting Code
import time

for h in range(24):
    for m in range(60):
        for s in range(60):
            # 1. Create the time string (HH:MM:SS)
            # 2. Print it!
            # 3. Optional: add a sleep if you want to see it tick
            # time.sleep(1) 
            pass

print("End of the day!")
```

**Check Your Logic**:
- If you change hours to `range(1)`, it should print 3600 lines (60 * 60).
- The very last line printed should be `23:59:59`.
