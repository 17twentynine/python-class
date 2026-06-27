# Build a Snake Game — Step by Step with Turtle
Date: 27th Jun 2026
Topic: Lists & Dictionaries — Applied to a Real Game

*You know lists and dictionaries. Today you'll use both to build the Snake game — one small piece at a time. Every puzzle is runnable: you'll see something on screen after each step. By the end you'll have a fully playable Snake game with arrow-key controls.*

---

## How Turtle Coordinates Work

The turtle screen puts `(0, 0)` at the **centre**. x goes right, y goes up.

To convert a grid `[row, col]` into a turtle `(x, y)` position, use this formula:
```
x = col * CELL - (SIZE * CELL / 2) + CELL / 2
y = (SIZE * CELL / 2) - row * CELL - CELL / 2
```

We will use `SIZE = 16` (16×16 grid) and `CELL = 40` (each cell is 40 pixels) — giving a **640×640** window.

---

## Puzzle 1: Hello Turtle (Easy)
**The Story**: Before drawing a game, let's learn the basics. `turtle` is a built-in Python module — no install needed. You create a **Screen** (the window) and a **Turtle** (the pen that draws).

**New in this puzzle:**
| What | What it does |
|------|-------------|
| `import turtle` | loads the built-in drawing module |
| `turtle.Screen()` | opens the game window |
| `screen.bgcolor("black")` | sets background colour |
| `screen.setup(w, h)` | sets window size in pixels |
| `turtle.Turtle()` | creates a drawing pen |
| `pen.penup()` | lifts the pen so moving leaves no line |
| `pen.hideturtle()` | hides the arrow cursor |
| `pen.speed(0)` | fastest drawing speed |
| `pen.goto(x, y)` | moves the pen to a position |
| `pen.dot(size, colour)` | draws a filled circle |
| `screen.exitonclick()` | keeps window open until you click it |

**The Question**: Open a black window (640×640 pixels) and draw one **green dot** of size 30 in the centre of the screen. Keep the window open until you click it.

**Example Test Case**:
- Running the code opens a black window with one green dot in the middle.

**Hint**:
- `screen = turtle.Screen()` creates the window.
- `screen.bgcolor("black")` sets the background colour.
- `screen.setup(640, 640)` sets the size.
- `pen = turtle.Turtle()` creates the drawing pen.
- `pen.penup()` lifts the pen so moving doesn't draw a line.
- `pen.goto(0, 0)` moves to the centre.
- `pen.dot(30, "green")` draws a filled circle of size 30.
- `screen.exitonclick()` keeps the window open until clicked.

**Check Your Logic**:
- A black window appears — size 640×640.
- One green dot is visible in the exact centre.

```python
# Starting Code
import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(640, 640)
screen.title("Hello Turtle")

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.speed(0)

# Move to the centre and draw a green dot of size 30
pen.goto(0, 0)
# pen.dot(...)
pass

screen.exitonclick()
```

---

## Puzzle 2: Draw the Grid (Easy–Medium)
**The Story**: The Snake board is a 16×16 grid. We'll draw it as a grid of small grey dots — one dot per cell. To place each dot correctly we need to convert `[row, col]` into turtle `(x, y)` coordinates.

**New in this puzzle:**
| What | What it does |
|------|-------------|
| `screen.tracer(0)` | turns off auto-drawing so the whole frame appears at once (no flickering) |
| `screen.update()` | manually pushes the finished frame to the screen |
| `return x, y` | a function can return two values at once |
| `x, y = to_xy(r, c)` | unpack two return values into two variables |

**The Question**: Complete `to_xy(row, col)` so it returns the correct turtle position for any grid cell. Then loop over all rows and columns and draw a small grey dot at each position.

**Example Test Case**:
- `to_xy(0, 0)` → top-left cell → `(-300, 300)`.
- `to_xy(15, 15)` → bottom-right cell → `(300, -300)`.
- `to_xy(8, 8)` → just right of centre → `(20, -20)`.

**Hint**: Use `SIZE = 16` and `CELL = 40`. The formula is in the intro above. `pen.dot(6, "gray")` draws a tiny grey dot as a grid marker.

**Check Your Logic**:
- 256 grey dots appear in a 16×16 pattern filling the black window.
- Top-left dot is at `(-300, 300)`, bottom-right is at `(300, -300)`.

```python
# Starting Code
import turtle

SIZE = 16
CELL = 40

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(SIZE * CELL, SIZE * CELL)
screen.title("Grid")
screen.tracer(0)   # draw everything at once — no slow animation

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.speed(0)

def to_xy(row, col):
    x = col * CELL - (SIZE * CELL) / 2 + CELL / 2
    y = (SIZE * CELL) / 2 - row * CELL - CELL / 2
    # return x and y
    pass

# Draw a small grey dot at every grid position
for r in range(SIZE):
    for c in range(SIZE):
        x, y = to_xy(r, c)
        pen.goto(x, y)
        # Draw a grey dot of size 6
        pass

screen.update()
screen.exitonclick()
```

---

## Puzzle 3: Place the Snake & Food (Easy–Medium)
**The Story**: Now we add the snake and food on top of the grey grid. The snake is a **list of `[row, col]` positions** — draw each one as a large green dot. The food is a single `[row, col]` position — draw it as a red dot.

**New in this puzzle:**
| What | What it does |
|------|-------------|
| `for i in range(len(snake)):` | loop with an index so you know which segment is the head (`i == 0`) |
| `CELL - 4` | large dot size — slightly smaller than the cell so there's a gap between segments |
| draw order matters | drawing a large dot last covers the small grey dot underneath |

**The Question**: Draw the full grid (grey dots), then the snake (green dots), then the food (red dot). The head of the snake is always `snake[0]`.

**Example Test Case**:
- Snake `[[8, 8], [8, 7], [8, 6]]` → three green dots in a horizontal row near the centre.
- Food `[3, 12]` → one red dot near the top-right.

**Hint**: Draw grey dots first (small, size 6), then draw snake dots on top (large, size `CELL - 4`). The large dot covers the grey one underneath. Use `"lime green"` for the snake body and `"green"` for the head.

**Check Your Logic**:
- Grey grid fills the screen.
- Three green dots appear in a row around the middle.
- `snake[0]` (the head at `[8, 8]`) is drawn in a slightly different green.
- One red dot appears at row 2, column 7.

```python
# Starting Code
import turtle

SIZE = 16
CELL = 40

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(SIZE * CELL, SIZE * CELL)
screen.title("Snake")
screen.tracer(0)

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.speed(0)

snake = [[8, 8], [8, 7], [8, 6]]
food  = [3, 12]

def to_xy(row, col):
    x = col * CELL - (SIZE * CELL) / 2 + CELL / 2
    y = (SIZE * CELL) / 2 - row * CELL - CELL / 2
    return x, y

# 1. Draw the grey grid
for r in range(SIZE):
    for c in range(SIZE):
        x, y = to_xy(r, c)
        pen.goto(x, y)
        pen.dot(6, "gray")

# 2. Draw each snake segment — use "green" for the head, "lime green" for the rest
for i in range(len(snake)):
    pos = snake[i]
    x, y = to_xy(pos[0], pos[1])
    pen.goto(x, y)
    if i == 0:
        # Draw the head in "green"
        pass
    else:
        # Draw the body in "lime green"
        pass

# 3. Draw the food in red
x, y = to_xy(food[0], food[1])
pen.goto(x, y)
# pen.dot(...)
pass

screen.update()
screen.exitonclick()
```

---

## Puzzle 4: Move One Step & Redraw (Medium)
**The Story**: Moving the snake means: calculate the new head, `insert` it at the front, `pop` the tail — then **clear the screen and redraw everything**. `pen.clear()` erases all dots so we can draw a fresh frame.

**New in this puzzle:**
| What | What it does |
|------|-------------|
| `pen.clear()` | erases everything the pen has drawn — used at the start of each frame |
| `import turtle, time` | you can import two modules on one line |
| `time.sleep(0.8)` | pauses the program for 0.8 seconds |
| `def draw():` | wrapping draw code in a function lets you call it multiple times |

**The Question**: Move the snake one step to the **right**, then redraw the board. Print a short pause between frames so you can see both positions.

**Example Test Case**:
- Snake `[[8, 8], [8, 7], [8, 6]]`, direction right → after move: `[[8, 9], [8, 8], [8, 7]]`.
- The drawing shifts one cell to the right.

**Hint**:
- `direction = {"row": 0, "col": 1}` means right.
- `new_head = [snake[0][0] + direction["row"], snake[0][1] + direction["col"]]`
- Call `pen.clear()` before redrawing to wipe the previous frame.
- Put your draw code in a `def draw():` function so you can call it twice easily.

**Check Your Logic**:
- First frame: snake at columns 6, 7, 8.
- After a short pause, snake shifts to columns 7, 8, 9.
- Food stays in place.

```python
# Starting Code
import turtle, time

SIZE = 16
CELL = 40

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(SIZE * CELL, SIZE * CELL)
screen.title("Move!")
screen.tracer(0)

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.speed(0)

snake     = [[8, 8], [8, 7], [8, 6]]
direction = {"row": 0, "col": 1}
food      = [3, 12]

def to_xy(row, col):
    x = col * CELL - (SIZE * CELL) / 2 + CELL / 2
    y = (SIZE * CELL) / 2 - row * CELL - CELL / 2
    return x, y

def draw():
    pen.clear()
    # Draw grey grid
    for r in range(SIZE):
        for c in range(SIZE):
            x, y = to_xy(r, c)
            pen.goto(x, y)
            pen.dot(6, "gray")
    # Draw snake
    for i in range(len(snake)):
        pos = snake[i]
        x, y = to_xy(pos[0], pos[1])
        pen.goto(x, y)
        colour = "green" if i == 0 else "lime green"
        pen.dot(CELL - 4, colour)
    # Draw food
    x, y = to_xy(food[0], food[1])
    pen.goto(x, y)
    pen.dot(CELL - 4, "red")
    screen.update()

# Draw the first frame
draw()
time.sleep(0.8)   # pause so you can see the starting position

# Move the snake one step in the direction
new_head = [snake[0][0] + direction["row"], snake[0][1] + direction["col"]]

# Add the new head and remove the tail
# snake.insert(...)
# snake.pop()
pass

# Redraw the second frame
draw()

screen.exitonclick()
```

---

## Puzzle 5: Eat Food & Keep Score (Medium)
**The Story**: When the snake's new head lands on the food: the snake **grows** (no `pop`), the score goes up, and new food appears somewhere random. We store the game state in a dictionary: `game = {"score": 0, "alive": True}`.

**New in this puzzle:**
| What | What it does |
|------|-------------|
| `game = {"score": 0, "alive": True}` | a dictionary as a game-state container — one place for all game variables |
| `game["score"] += 1` | increment a value stored inside a dict |
| `screen.title(f"Snake — Score: {game['score']}")` | update the window title bar text at any time |
| `food[0] = ...` | change one part of a two-element list to move food |

**The Question**: The snake starts one step away from the food. Move it into the food, grow the snake, update the score, and place new food at `[12, 3]`. Update the window title to show the score.

**Example Test Case**:
- Snake length 3, eats food → length **4**, score **1**, new food at `[12, 3]`.

**Hint**:
- Check `if new_head == food:` after calculating the new head.
- If eating: `insert` but **no** `pop`. Then `game["score"] += 1`. Then move `food` to a new position.
- `screen.title(f"Snake — Score: {game['score']}")` updates the window title.

**Check Your Logic**:
- Before: snake has **3** segments, score is **0**, red dot at `[3, 12]`.
- After: snake has **4** segments, score is **1**, red dot moved to `[12, 3]`.
- Window title reads `"Snake — Score: 1"`.

```python
# Starting Code
import turtle

SIZE = 16
CELL = 40

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(SIZE * CELL, SIZE * CELL)
screen.title("Snake — Score: 0")
screen.tracer(0)

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.speed(0)

snake     = [[3, 11], [3, 10], [3, 9]]   # one step away from food
direction = {"row": 0, "col": 1}
food      = [3, 12]
game      = {"score": 0, "alive": True}

def to_xy(row, col):
    x = col * CELL - (SIZE * CELL) / 2 + CELL / 2
    y = (SIZE * CELL) / 2 - row * CELL - CELL / 2
    return x, y

def draw():
    pen.clear()
    for r in range(SIZE):
        for c in range(SIZE):
            x, y = to_xy(r, c)
            pen.goto(x, y)
            pen.dot(6, "gray")
    for i in range(len(snake)):
        pos = snake[i]
        x, y = to_xy(pos[0], pos[1])
        pen.goto(x, y)
        pen.dot(CELL - 4, "green" if i == 0 else "lime green")
    x, y = to_xy(food[0], food[1])
    pen.goto(x, y)
    pen.dot(CELL - 4, "red")
    screen.update()

draw()

print(f"Before — length: {len(snake)}, score: {game['score']}")

# Calculate new head
new_head = [snake[0][0] + direction["row"], snake[0][1] + direction["col"]]

# Add the new head
snake.insert(0, new_head)

# Did we eat the food?
if new_head == food:
    # Grow: no pop. Update score. Update title. Move food to [12, 3].
    pass
else:
    # Normal move: remove the tail
    pass

print(f"After  — length: {len(snake)}, score: {game['score']}")

draw()
screen.exitonclick()
```

---

## Puzzle 6: Game Over Detection (Medium–Hard)
**The Story**: The game ends when the snake hits a **wall** or hits **itself**. We write a function `is_game_over(head)` that checks both. When it triggers, we display a "GAME OVER" message on screen.

**New in this puzzle:**
| What | What it does |
|------|-------------|
| `head in snake[1:]` | checks if `head` appears anywhere in the body (skips index 0 which is the head itself) |
| `pen.color("white")` | sets the pen colour for writing text |
| `pen.write("text", align=, font=)` | draws text on the turtle screen at the pen's current position |
| `return True` inside a function | stops the function immediately and sends back `True` |

**The Question**: Write `is_game_over(head)`, test it on three cases, and display the message when the game ends.

**Example Test Case**:
- Head `[0, -1]` → out of bounds → **True**
- Head `[5, 3]` when body has `[5, 3]` → self-collision → **True**
- Head `[3, 4]` with body `[[3, 5], [3, 6]]` → safe → **False**

**Hint**:
- Wall: `head[0] < 0 or head[0] >= SIZE or head[1] < 0 or head[1] >= SIZE`
- Self: `head in snake[1:]`
- To write text: `pen.goto(0, 0)`, `pen.color("white")`, `pen.write("GAME OVER", align="center", font=("Arial", 24, "bold"))`.

**Check Your Logic**:
- Case 1 prints **True** and shows "GAME OVER" on screen.
- Case 2 prints **True**.
- Case 3 prints **False**.

```python
# Starting Code
import turtle

SIZE = 16
CELL = 40

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(SIZE * CELL, SIZE * CELL)
screen.title("Game Over Test")
screen.tracer(0)

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.speed(0)

snake = [[8, 7], [8, 6], [8, 5]]

def to_xy(row, col):
    x = col * CELL - (SIZE * CELL) / 2 + CELL / 2
    y = (SIZE * CELL) / 2 - row * CELL - CELL / 2
    return x, y

def is_game_over(head):
    # Check 1: out of bounds
    if head[0] < 0 or head[0] >= SIZE or head[1] < 0 or head[1] >= SIZE:
        return True
    # Check 2: hit own body
    if head in snake[1:]:
        # return True
        pass
    return False

def show_game_over():
    pen.goto(0, 0)
    pen.color("white")
    pen.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
    screen.update()

# Test Case 1: wall (left boundary)
head1 = [8, -1]
result1 = is_game_over(head1)
print("Case 1 (wall):     ", result1)   # Expected: True
if result1:
    show_game_over()

# Test Case 2: self-collision
head2 = [8, 6]
print("Case 2 (self-hit): ", is_game_over(head2))   # Expected: True

# Test Case 3: safe
head3 = [5, 5]
print("Case 3 (safe):     ", is_game_over(head3))   # Expected: False

screen.exitonclick()
```

---

## Puzzle 7: Arrow Keys — Change Direction (Medium–Hard)
**The Story**: `screen.onkeypress(function, "Key")` calls a function the instant a key is pressed. We use this to update the `direction` dictionary when an arrow key is pressed. One rule: you cannot reverse direction (going left while moving right would instantly hit yourself).

**New in this puzzle:**
| What | What it does |
|------|-------------|
| `screen.listen()` | tells the window to start watching for key presses |
| `screen.onkeypress(fn, "Right")` | calls `fn()` every time the Right arrow key is pressed |
| `screen.mainloop()` | keeps the window open and responsive (replaces `exitonclick`) |
| key names | `"Right"`, `"Left"`, `"Up"`, `"Down"` for arrow keys |

**The Question**: Wire up all four arrow keys. Each one updates `direction` — but only if the new direction is not the opposite of the current one.

**Example Test Case**:
- Currently moving right `{"row": 0, "col": 1}`. Press **Left** → no change (opposite direction blocked).
- Currently moving right. Press **Up** → `{"row": -1, "col": 0}` ✓

**Hint**:
- `screen.listen()` must be called so the window pays attention to keys.
- Opposite of right `col=1` is left `col=-1`. Check `direction["col"] != -1` before allowing left.
- Each function only changes `direction` — it does not move the snake. Movement happens in the game loop.

**Check Your Logic**:
- Press **Right** → title updates to show direction `(0, 1)`.
- Press **Up** → title updates to `(-1, 0)`.
- Press **Left** while moving right → title does NOT update (blocked).
- Press **Left** while moving up → title updates to `(0, -1)`.

```python
# Starting Code
import turtle

SIZE = 16
CELL = 40

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(SIZE * CELL, SIZE * CELL)
screen.title("Press arrow keys!")
screen.tracer(0)

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()

direction = {"row": 0, "col": 1}   # start: moving right

def go_right():
    if direction["col"] != -1:     # not already going left
        direction["row"] = 0
        direction["col"] = 1
    screen.title(f"Direction: row={direction['row']} col={direction['col']}")

def go_left():
    if direction["col"] != 1:      # not already going right
        # set direction to left
        pass
    screen.title(f"Direction: row={direction['row']} col={direction['col']}")

def go_up():
    if direction["row"] != 1:      # not already going down
        # set direction to up
        pass
    screen.title(f"Direction: row={direction['row']} col={direction['col']}")

def go_down():
    if direction["row"] != -1:     # not already going up
        # set direction to down
        pass
    screen.title(f"Direction: row={direction['row']} col={direction['col']}")

screen.listen()
screen.onkeypress(go_right, "Right")
screen.onkeypress(go_left,  "Left")
screen.onkeypress(go_up,    "Up")
screen.onkeypress(go_down,  "Down")

screen.mainloop()
```

---

## Puzzle 8: The Full Snake Game — Timer Loop (Medium–Hard)
**The Story**: `screen.ontimer(function, ms)` calls a function after `ms` milliseconds. If the `tick` function schedules itself at the end, it runs forever — that's our game loop. Combine everything: draw → move → check game over → schedule next tick.

**New in this puzzle:**
| What | What it does |
|------|-------------|
| `screen.ontimer(fn, 200)` | calls `fn()` after 200 milliseconds — use inside `tick()` to keep scheduling itself |
| `import random` | built-in module for random numbers |
| `random.randint(0, SIZE - 1)` | returns a random integer between 0 and 15 (inclusive) |
| `if not game["alive"]: return` | early exit — stops the tick function if the game has ended |

**The Question**: Fill in the missing parts of `tick()` to complete the game. The snake should move on its own every 200 ms, grow when it eats food, and stop with a "GAME OVER" message on collision.

**Example Test Case**:
- Game starts. Snake moves right on its own.
- Press **Up** — snake curves upward.
- Snake reaches the red dot — grows by one, score increases, new food appears.
- Snake hits the wall — "GAME OVER" appears.

**Hint**:
- `tick()` should: calculate new head → check game over → move/grow → draw → `screen.ontimer(tick, 200)`.
- `screen.tracer(0)` + `screen.update()` inside `draw()` gives smooth redraws.
- `random.randint(0, SIZE - 1)` gives a random row or column for new food.

**Check Your Logic**:
- Snake moves automatically without any key press.
- Arrow keys change direction smoothly.
- Eating food: snake grows by 1, window title score increases.
- Wall or self-hit: "GAME OVER" text appears on screen, movement stops.

```python
# Starting Code
import turtle, random

SIZE = 16
CELL = 40

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(SIZE * CELL, SIZE * CELL)
screen.title("Snake — Score: 0")
screen.tracer(0)

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.speed(0)

snake     = [[8, 8], [8, 7], [8, 6]]
direction = {"row": 0, "col": 1}
food      = [random.randint(0, SIZE - 1), random.randint(0, SIZE - 1)]
game      = {"score": 0, "alive": True}

def to_xy(row, col):
    x = col * CELL - (SIZE * CELL) / 2 + CELL / 2
    y = (SIZE * CELL) / 2 - row * CELL - CELL / 2
    return x, y

def draw():
    pen.clear()
    for r in range(SIZE):
        for c in range(SIZE):
            x, y = to_xy(r, c)
            pen.goto(x, y)
            pen.dot(6, "gray")
    for i in range(len(snake)):
        pos = snake[i]
        x, y = to_xy(pos[0], pos[1])
        pen.goto(x, y)
        pen.dot(CELL - 4, "green" if i == 0 else "lime green")
    x, y = to_xy(food[0], food[1])
    pen.goto(x, y)
    pen.dot(CELL - 4, "red")
    screen.update()

def is_game_over(head):
    if head[0] < 0 or head[0] >= SIZE or head[1] < 0 or head[1] >= SIZE:
        return True
    if head in snake[1:]:
        return True
    return False

def tick():
    if not game["alive"]:
        return

    # Calculate the new head
    new_head = [snake[0][0] + direction["row"], snake[0][1] + direction["col"]]

    # Check game over
    if is_game_over(new_head):
        game["alive"] = False
        draw()
        pen.goto(0, 0)
        pen.color("white")
        pen.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
        screen.update()
        return

    # Move the snake — insert new head
    snake.insert(0, new_head)

    # Did we eat the food?
    if new_head == food:
        # Update score, update title, place new food randomly
        game["score"] += 1
        screen.title(f"Snake — Score: {game['score']}")
        food[0] = random.randint(0, SIZE - 1)
        food[1] = random.randint(0, SIZE - 1)
        # No pop — snake grows
    else:
        # Normal move — remove the tail
        # snake.pop()
        pass

    draw()
    screen.ontimer(tick, 200)   # schedule the next tick

# --- Key bindings ---
def go_right():
    if direction["col"] != -1:
        direction["row"] = 0
        direction["col"] = 1

def go_left():
    if direction["col"] != 1:
        # fill in
        pass

def go_up():
    if direction["row"] != 1:
        # fill in
        pass

def go_down():
    if direction["row"] != -1:
        # fill in
        pass

screen.listen()
screen.onkeypress(go_right, "Right")
screen.onkeypress(go_left,  "Left")
screen.onkeypress(go_up,    "Up")
screen.onkeypress(go_down,  "Down")

draw()
screen.ontimer(tick, 200)   # start the first tick
screen.mainloop()           # keep the window open
```
