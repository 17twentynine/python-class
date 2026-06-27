# Build a Snake Game — Step by Step
Date: 27th Jun 2026
Topic: Lists & Dictionaries — Applied to a Real Game

*You know lists and dictionaries. Today you'll use both to build the Snake game from scratch — one small piece at a time. Each puzzle builds on the previous one. By the end you'll have a working game engine: a board, a moving snake, food, growing, scoring, and game-over detection.*

---

## Puzzle 1: The Grid (Easy)
**The Story**: Every game needs a board. The Snake board is a 10×10 grid of cells. In Python we store it as a **list of rows**, where each row is a **list of cells**. Every cell starts as `"."` (empty).

**The Question**: Build `board` as a 10×10 grid where every cell is `"."`. Then print it — each row on its own line, cells separated by a space.

**Example Test Case**:
- A 3×3 board prints as:
```
. . .
. . .
. . .
```

**Hint**: `["."] * 10` creates a list of 10 dots in one line. To print a row neatly, use `" ".join(row)`.

**Check Your Logic**:
- Your output should be **10 lines**, each with **10 dots**.
- `board[0]` is the first row — a list of 10 dots.
- `board[5][3]` is row 5, column 3 — it should be `"."`.

```python
# Starting Code
board = []

for r in range(10):
    row = ["."] * 10
    board.append(row)

# Print the board — each row on its own line, cells separated by spaces
for row in board:
    # Use join to print the row
    pass
```

---

## Puzzle 2: Place the Snake (Easy–Medium)
**The Story**: The snake is a **list of positions**. Each position is a `[row, col]` pair. The **first item** is the snake's **head**; the **last item** is the **tail**.

**The Question**: Given the snake below, mark each position on the board with `"S"`, then print the board.

**Example Test Case**:
- Snake `[[2, 3], [2, 2]]` on a 5×5 board → row 2 prints as `". . . S S ."` ... wait, 5 cols: `". . . S S"` — columns 3 and 4 are `"S"`.

**Hint**: `board[row][col] = "S"` changes one cell. Loop over `snake` — each item `pos` gives you `pos[0]` (row) and `pos[1]` (col).

**Check Your Logic**:
- Exactly **3** cells show `"S"` — all in row 5.
- `board[5][5]` → `"S"` (head).
- `board[5][4]` → `"S"` (middle).
- `board[5][3]` → `"S"` (tail).

```python
# Starting Code
board = []
for r in range(10):
    board.append(["."] * 10)

snake = [[5, 5], [5, 4], [5, 3]]   # head at [5,5], tail at [5,3]

# Mark each snake position on the board with "S"
for pos in snake:
    row = pos[0]
    col = pos[1]
    # Set board[row][col] to "S"
    pass

# Print the board
for row in board:
    print(" ".join(row))
```

---

## Puzzle 3: Move the Snake (Medium)
**The Story**: The snake moves by adding a **new head** in the direction of travel, then removing the **tail**. Direction is stored as a dictionary with `"row"` and `"col"` offsets.

| Direction | Dictionary |
|-----------|------------|
| Right     | `{"row": 0, "col": 1}` |
| Left      | `{"row": 0, "col": -1}` |
| Down      | `{"row": 1, "col": 0}` |
| Up        | `{"row": -1, "col": 0}` |

**The Question**: Move the snake one step to the **right**. Print the snake before and after.

**Example Test Case**:
- Snake `[[5, 5], [5, 4], [5, 3]]`, direction right → `[[5, 6], [5, 5], [5, 4]]`.

**Hint**:
1. New head row = `snake[0][0] + direction["row"]`, new head col = `snake[0][1] + direction["col"]`.
2. `snake.insert(0, new_head)` — adds the new head at the **front**.
3. `snake.pop()` — removes the last item (the old tail).

**Check Your Logic**:
- Before: `[[5, 5], [5, 4], [5, 3]]`
- After:  `[[5, 6], [5, 5], [5, 4]]` — the snake slid one step right; length stays 3.

```python
# Starting Code
snake = [[5, 5], [5, 4], [5, 3]]
direction = {"row": 0, "col": 1}   # moving right

print("Before:", snake)

# Step 1: Calculate the new head position
new_head = [snake[0][0] + direction["row"], snake[0][1] + direction["col"]]

# Step 2: Add the new head to the FRONT of the snake
# snake.insert(...)
pass

# Step 3: Remove the tail
# snake.pop()
pass

print("After: ", snake)
```

---

## Puzzle 4: Add Food (Medium)
**The Story**: Food appears at a position on the board, marked `"F"`. Each time the snake moves, we check if the snake's **head** landed on the food.

**The Question**: Place food at `[2, 7]`. Mark it on the board. Check if the snake ate it (the head starts at `[5, 5]` — not there yet). Then move the snake right and check again.

**Example Test Case**:
- Head `[2, 7]`, food `[2, 7]` → **ate it!**
- Head `[5, 5]`, food `[2, 7]` → not eaten.

**Hint**: `snake[0]` is the head. Two lists are equal when both values match: `[2, 7] == [2, 7]` is `True`.

**Check Your Logic**:
- Before moving: head is `[5, 5]` → **not eaten**.
- After moving right: head is `[5, 6]` → **still not eaten** (food is far away — that's fine!).

```python
# Starting Code
board = []
for r in range(10):
    board.append(["."] * 10)

snake = [[5, 5], [5, 4], [5, 3]]
direction = {"row": 0, "col": 1}
food = [2, 7]

# Mark snake and food on the board
for pos in snake:
    board[pos[0]][pos[1]] = "S"
board[food[0]][food[1]] = "F"

# Print board
for row in board:
    print(" ".join(row))
print()

# Check: did the snake eat the food before moving?
if snake[0] == food:
    print("Yum! Snake ate the food!")
else:
    print(f"Head is at {snake[0]}, food is at {food} — not eaten yet.")

# Move the snake one step right
new_head = [snake[0][0] + direction["row"], snake[0][1] + direction["col"]]
snake.insert(0, new_head)
snake.pop()

# Check again after moving
if snake[0] == food:
    # print a "Yum!" message
    pass
else:
    # print where the head is now
    pass
```

---

## Puzzle 5: Grow & Keep Score (Medium–Hard)
**The Story**: When the snake eats food, it **grows** — we add the new head but do **NOT** remove the tail. We track everything in a game state dictionary: `game = {"score": 0, "alive": True}`.

**The Question**: The snake is one step away from the food. Move it, detect the eat, grow it, and update the score.

**Example Test Case**:
- Snake length 3, eats food → length becomes **4**, score goes from **0** to **1**.

**Hint**: The only difference from a normal move is the `if`:
- Normal move → `insert` **and** `pop`.
- Eating move → `insert` **only** (no `pop`). Then add 1 to `game["score"]`.

**Check Your Logic**:
- Start: length = **3**, score = **0**.
- After eating: length = **4**, score = **1**.
- `snake[0]` is the new head `[2, 7]`; `snake[1]` is the old head `[2, 6]`.

```python
# Starting Code
snake = [[2, 6], [2, 5], [2, 4]]   # heading right, one step from food
direction = {"row": 0, "col": 1}
food = [2, 7]
game = {"score": 0, "alive": True}

print(f"Before — length: {len(snake)}, score: {game['score']}")

# Calculate new head
new_head = [snake[0][0] + direction["row"], snake[0][1] + direction["col"]]

# Add new head to the front
snake.insert(0, new_head)

# Did we eat the food?
if new_head == food:
    # Snake grows — do NOT pop. Update the score.
    pass
else:
    # Normal move — remove the tail
    pass

print(f"After  — length: {len(snake)}, score: {game['score']}")
print(f"Snake: {snake}")
```

---

## Puzzle 6: Game Over (Medium–Hard)
**The Story**: The game ends in two ways — the snake hits a **wall** (goes outside the 10×10 grid) or hits **itself** (the new head lands on a body cell). Write a function that detects both.

**The Question**: Write `is_game_over(head, snake, size)` and test it on three cases.

**Example Test Case**:
- Head `[0, -1]` → out of bounds → **True**
- Head `[5, 3]`, body has `[5, 3]` → self-collision → **True**
- Head `[3, 4]`, body is `[[3, 5], [3, 6]]` → safe → **False**

**Hint**:
- Wall check: `head[0] < 0 or head[0] >= size or head[1] < 0 or head[1] >= size`
- Self check: `head in snake[1:]` — `snake[1:]` is the body without the head.

**Check Your Logic**:
- Case 1 (wall): **True**
- Case 2 (self-hit): **True**
- Case 3 (safe move): **False**

```python
# Starting Code
def is_game_over(head, snake, size):
    # Check 1: did the head go out of bounds?
    if head[0] < 0 or head[0] >= size or head[1] < 0 or head[1] >= size:
        return True

    # Check 2: did the head hit the snake's own body?
    if head in snake[1:]:
        # return True
        pass

    # Safe — the game continues
    return False


# Test Case 1: head hits the left wall
head1 = [5, -1]
snake1 = [[5, 0], [5, 1], [5, 2]]
print("Case 1 (wall):     ", is_game_over(head1, snake1, 10))   # Expected: True

# Test Case 2: head hits its own body
head2 = [5, 3]
snake2 = [[5, 4], [5, 3], [5, 2]]   # [5,3] is already in the body
print("Case 2 (self-hit): ", is_game_over(head2, snake2, 10))   # Expected: True

# Test Case 3: safe move
head3 = [3, 4]
snake3 = [[3, 5], [3, 6], [3, 7]]
print("Case 3 (safe):     ", is_game_over(head3, snake3, 10))   # Expected: False
```

---

## Bonus: Put It All Together
*Finished all 6? Connect every piece into one running game. The snake moves on its own — watch it go!*

```python
import time, os

def is_game_over(head, snake, size):
    if head[0] < 0 or head[0] >= size or head[1] < 0 or head[1] >= size:
        return True
    if head in snake[1:]:
        return True
    return False

# Setup
SIZE = 10
snake = [[5, 5], [5, 4], [5, 3]]
direction = {"row": 0, "col": 1}   # start moving right
food = [2, 7]
game = {"score": 0, "alive": True}

while game["alive"]:
    # Build a fresh board
    board = []
    for r in range(SIZE):
        board.append(["."] * SIZE)

    # Mark snake and food
    for pos in snake:
        board[pos[0]][pos[1]] = "S"
    board[food[0]][food[1]] = "F"

    # Display
    os.system("clear")
    for row in board:
        print(" ".join(row))
    print(f"Score: {game['score']}")

    # Calculate new head
    new_head = [snake[0][0] + direction["row"], snake[0][1] + direction["col"]]

    # Check game over
    if is_game_over(new_head, snake, SIZE):
        game["alive"] = False
        print("Game Over!")
        break

    # Move or grow
    snake.insert(0, new_head)
    if new_head == food:
        game["score"] += 1
        food = [1, 2]   # new food position — try using random later!
    else:
        snake.pop()

    time.sleep(0.4)
```
