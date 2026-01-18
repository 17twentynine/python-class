# Logic Puzzles with Loops

Date: 18th Jan 2026
Topic: Loops

*Three curious questions to solve using Python.*

## Puzzle 1: The Unstoppable Number (The 3n+1 Mystery)
**The Story**: Mathematicians have found a magic rule. Pick **ANY** number (like 10 or 27 or 500).
- If the number is **Even**: Divide it by 2.
- If the number is **Odd**: Multiply by 3 and add 1.
- Repeat!

**The Mystery**: It seems to *always* eventually crash down to the number **1**. Nobody knows why!

**The Question**: Start with the number **27**. How many steps does it take to reach 1? (It's more than you think!)

**Example Test Case**:
- Input: `6`
- Logic: `6` (even) -> `3` (odd) -> `10` -> `5` -> `16` -> `8` -> `4` -> `2` -> `1`
- Output: `8 steps`

**Hint**: You need a loop that keeps going *while* the number is not 1. Inside, check if it's even or odd and change the number accordingly.

**Small Syntax Hint**: `number % 2 == 0` is `True` if a number is **Even**.

```python
# Starting code
number = 27
steps = 0

while number > 1:
    # Your logic here!
    # Remember to count the steps
    pass
```

### Verify Your Logic
Try changing `number` to these values and see if you get the right answer:
- **Input: 9** -> Answer: **19 steps**
- **Input: 12** -> Answer: **9 steps**
- **Input: 15** -> Answer: **17 steps**
- **Input: 27** -> Answer: **111 steps** (It takes a long time!)

---

## Puzzle 2: The Magic Penny (Exponential Growth)
**The Story**: A slightly evil genie offers you a deal. You can have:
1.  **$1,000,000** (1 Million Dollars) right now.
2.  **A Magic Penny** ($0.01) that doubles in value every day for 30 days. (Day 1: $0.01, Day 2: $0.02, Day 3: $0.04...)

**The Question**: Which one is worth more on Day 30? Write a loop to prove it.

**Example Test Case**:
- Input: `Day 5`
- Logic: Day 1 (`0.01`), Day 2 (`0.02`), Day 3 (`0.04`), Day 4 (`0.08`), Day 5 (`0.16`)
- Output: `$0.16`

**Hint**: Don't try to calculate 2^30 in your head! Use a loop to update the `penny` value 30 times.

**Small Syntax Hint**: To double a number, use line `penny = penny * 2`.

```python
# Starting code
money = 0.01

# Loop for 30 days
for day in range(1, 31):
    # Update 'money' here
    pass
```

### Verify Your Logic
Try changing the loop range to check these days:
- **Day 10**: `$5.12`
- **Day 20**: `$5,242.88` (Already 5 thousand!)
- **Day 30**: `$5,368,709.12` (5 Million!)

---

## Puzzle 3: The Frog in the Well (Logic Trap)
**The Story**: A frog falls into a well that is **20 meters deep**.
- Every **morning**, the frog jumps **UP 5 meters**.
- Every **night** while sleeping, the frog slides **DOWN 4 meters**.

**The Question**: How many days does it take to get out?

**Example Test Case**:
- Input: `Depth 10 meters`
- Logic:
  - Day 1: Climinb 0 -> 5. Slide to 1.
  - Day 2: Climb 1 -> 6. Slide to 2. ...
  - Day 6: Climb 5 -> 10 (OUT!)
- Output: `6 Days`

**The Trap**: It is NOT 20 days!
*Think about it*: Once he reaches the top (20m) during the day, does he slide back down that night? No, he's out!

**Hint**: Be careful! Simulating this day-by-day is safer than math. Remember: he jumps *during the day*.

**Small Syntax Hint**: Use `if depth >= 20: break` to stop the loop immediately when he escapes.

```python
# Starting code
depth = 0
days = 0

while True:
    days = days + 1
    # 1. He jumps up 5m
    # 2. Check: Is he out? (>= 20). If yes, break!
    # 3. If not out, he slides down 4m
    pass
```

### Verify Your Logic
Change the well depth logic to `if depth >= 50:` etc. to test:
- **Depth 10m** -> Answer: **6 days**
- **Depth 20m** -> Answer: **16 days**
- **Depth 50m** -> Answer: **46 days**
- **Depth 100m** -> Answer: **96 days**
