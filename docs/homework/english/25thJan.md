# Logic Puzzles: Loops & Logic (Level 2)
Date: 25th Jan 2026
Topic: Loops & Modulo

*Three new puzzles to test your skills.*

## Puzzle 1: The Rocket Countdown (Easy)
**The Story**: SpaceX is launching a new "Starship". The crowds are waiting.
You need to build the computer system that counts down from 10 to 1, and then shouts "BLAST OFF!".

**The Question**: Use a loop to print exact numbers 10 down to 1.
*Note*: It must stop AT 1, not 0.

**Example Test Case**:
- Input: `Start 5`
- Output: `5, 4, 3, 2, 1, BLAST OFF!`

**Hint**: You can use `range(10, 0, -1)`. The `-1` means "count backwards".

**Check Your Logic**:
- If you use `range(10, 0, -1)`, does it print 0? (It shouldn't).

```python
# Starting Code
import time

print("Initiating Launch Sequence...")

# Loop goes here
for t in range(10, 0, -1):
    # Print 't'
    # Maybe sleep for 1 second?
    pass

print("BLAST OFF! 🚀")
```

---

## Puzzle 2: The "Viral" Video (Recent Events)
**The Story**: You posted a funny video on Instagram.
- At Hour 0, you have **10 views**.
- Every hour, your views **TRIPLE** (x3).
- **BUT**, every hour, **50 people** get bored and leave (click away).

**The Question**: How many hours until you are "Famous" (reach 10,000 views)?

**Example Test Case**:
- Hour 1: (10 * 3) - 50 = ... Wait, that's negative! (Let's say minimum is 0).
- *Correction*: Let's start with **100 views**.
- Input: `Start 100` -> Goal `1000`
- Hour 1: (100 * 3) - 50 = 250
- Hour 2: (250 * 3) - 50 = 700
- Hour 3: (700 * 3) - 50 = 2050 (Goal!) -> Answer: 3 Hours

**Hint**: Use a `while views < 10000:` loop. Inside, do the math `views = (views * 3) - 50`.

**Verify Your Logic**:
- Input: `Start 25` (Tricky!)
- Hour 1: 25 * 3 - 50 = 25.
- Hour 2: 25.
- Answer: **Forever** (It never grows!). The loop might run forever (Infinite Loop).
- *Code Tip*: Add `if hours > 100: break` to save your computer!

```python
# Starting Code
views = 100
hours = 0

while views < 10000:
    # 1. Count hour
    # 2. Update views (x3 then -50)
    # 3. Print status
    pass
```

---

## Puzzle 3: The Warehouse Robot (Challenging)
**The Story**: An Amazon robot needs to move a package across the floor.
- The floor is **20 meters** long.
- The robot moves **1 meter** every second.
- **BUT**: Every **3rd second** (3, 6, 9...), the robot must STOP to charge its battery. It moves **0 meters** that second.

**The Question**: How many seconds does it take to cross 20 meters?

**Example Test Case**:
- Distance: `5 meters`
- Sec 1: Move (at 1m)
- Sec 2: Move (at 2m)
- Sec 3: **Charge** (still at 2m)
- Sec 4: Move (at 3m)
- Sec 5: Move (at 4m)
- Sec 6: **Charge** (still at 4m)
- Sec 7: Move (at 5m) -> DONE!
- Answer: **7 seconds**

**Hint**: You need a loop (counting seconds). Inside, use checking `if time % 3 == 0:` to verify if it's a charging second.

**Small Syntax Hint**: `x % 3 == 0` means "x is divisible by 3".

```python
# Starting Code
distance = 0
seconds = 0
target = 20

while distance < target:
    seconds = seconds + 1
    
    # Check if charging time (3, 6, 9...)
    if seconds % 3 == 0:
        print(f"Sec {seconds}: Charging...")
    else:
        distance = distance + 1
        print(f"Sec {seconds}: Moved to {distance}m")

print(f"Done in {seconds} seconds!")
```
