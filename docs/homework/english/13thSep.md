# Touch Screen Games — Snake Buttons & Tic Tac Toe
Date: 13th Sep 2026
Topic: Dictionaries of Dictionaries, Lists of Lists & Tapping the Screen

*Our Raspberry Pi has a 7-inch touch screen. Today we make games you can play with just your finger! First we add touch buttons to the Snake game, then you build Tic Tac Toe from scratch. These puzzles give you fewer answers than before: work things out on paper first, and only read the hints when you're stuck.*

---

## Before You Start: The Pi Screen

- The screen is **1024×600** pixels. After the taskbar and the window's title bar, a game window can be about **500 pixels tall** at most — so every window today is **480** pixels tall.
- A **tap** on the touch screen works just like a **mouse click**. `screen.onclick(fn)` handles both.
- Your Snake game from 27th Jun used `CELL = 40` (640×640). On the Pi, change it to `CELL = 30`.

---

# Part 1: Snake Gets Touch Buttons

## Puzzle 1: On-Screen Arrow Buttons (Medium–Hard)
**The Story**: Our Raspberry Pi has a **touch screen** — so why not play without a keyboard? Let's draw four big arrow buttons on the screen. When you **tap** a button (or press the matching arrow key), it lights up yellow. We store the buttons in a **dictionary of dictionaries**: each button's name points to another dictionary with its position and arrow symbol.

**New in this puzzle:**
| What | What it does |
|------|-------------|
| `buttons["Up"]["x"]` | a dictionary inside a dictionary — first pick the button, then pick its `x` |
| `for name in buttons:` | looping over a dictionary gives you each **key** (`"Up"`, `"Left"`, …) |
| `screen.onclick(fn)` | calls `fn(x, y)` when you click or **tap** the screen — `x` and `y` are where you touched |
| `abs(number)` | distance from zero, always positive: `abs(-7)` is `7`, `abs(7)` is `7` |
| `def press(name):` | one function with a parameter does the work; four tiny functions call it for each key |

**The Question**: Finish the program so all **four** buttons appear in an upside-down T (like the arrow keys on a keyboard), the pressed button turns **yellow**, and tapping a button works just like pressing its arrow key.

**Example Test Case**:
- Tap the **→** button → it turns yellow, the title says `You pressed: Right`.
- Press the **Up** arrow key → **↑** turns yellow, **→** goes back to grey.
- Tap an empty part of the screen → nothing changes.

**Hint** (think first, peek later!):
- Work out the positions yourself: **↓** sits exactly under **↑**. **→** is as far to the right of **↓** as **←** is to the left.
- For the colour, remember the one-line `if … else` from the Snake game (27th Jun, Puzzle 4): `"green" if i == 0 else "lime green"`.
- Is a tap at `(130, -40)` on the **→** button at `(110, -60)`? The button is `100` wide, so it reaches `50` pixels each way. How far away is the tap left-to-right? And up-and-down? Both need to be close enough.
- Use `abs()` so it doesn't matter if the tap is left **or** right of the centre.

**Check Your Logic**:
- Four round grey buttons: ↑ on top, ← ↓ → underneath, not overlapping.
- Only one button is yellow at a time.
- Tapping just outside a button's edge does nothing — even in the corners.
- If an arrow is not in the middle of its button, change the `- 28` in `draw_button`.

```python
# Starting Code
import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(480, 480)
screen.title("Arrow Buttons")
screen.tracer(0)

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.speed(0)

BUTTON = 100   # size of each round button in pixels

# A dictionary of dictionaries: where each button sits, and its arrow
buttons = {
    "Up":    {"x": 0,    "y": 50,  "arrow": "↑"},
    "Left":  {"x": -110, "y": -60, "arrow": "←"},
    # add "Down"  — arrow "↓"
    # add "Right" — arrow "→"
}
pressed = {"name": ""}   # the button pressed last

def draw_button(name):
    info = buttons[name]
    colour = "light gray"   # make it "yellow" if this is the pressed button
    pen.goto(info["x"], info["y"])
    pen.dot(BUTTON, colour)
    pen.goto(info["x"], info["y"] - 28)   # text sits above the pen, so start lower
    pen.color("black")
    pen.write(info["arrow"], align="center", font=("Arial", 36, "bold"))

def draw_all():
    pen.clear()
    pen.goto(0, 160)
    pen.color("white")
    pen.write("Tap a button or press an arrow key!", align="center", font=("Arial", 16, "bold"))
    for name in buttons:
        draw_button(name)
    screen.update()

def press(name):
    pressed["name"] = name
    screen.title(f"You pressed: {name}")
    draw_all()

def up_pressed():
    press("Up")

def left_pressed():
    press("Left")

def down_pressed():
    # fill in
    pass

def right_pressed():
    # fill in
    pass

def on_tap(x, y):
    for name in buttons:
        info = buttons[name]
        # Is (x, y) on this button? If yes, press it.
        pass

screen.listen()
screen.onkeypress(up_pressed,    "Up")
screen.onkeypress(down_pressed,  "Down")
screen.onkeypress(left_pressed,  "Left")
screen.onkeypress(right_pressed, "Right")
screen.onclick(on_tap)

draw_all()
screen.mainloop()
```

---

## Puzzle 2: Snake with Touch Buttons (Hard)
**The Story**: Now let's put the buttons **next to** the snake board, so the whole game can be played on the touch screen — no keyboard needed! The window gets wider by `PANEL` pixels, and the board has to slide left to make room. When the game ends, **tapping anywhere** starts a new game.

**New in this puzzle:**
| What | What it does |
|------|-------------|
| `screen.setup(SIZE * CELL + PANEL, SIZE * CELL)` | a wider window: the board plus a side panel |
| `PANEL_X = SIZE * CELL / 2` | the x position of the middle of the panel |
| `snake.clear()` | removes everything from a list |
| `snake.extend([...])` | adds all items from another list to the end |

**The Question**: Make the snake game playable with only your finger:
1. Fix `to_xy` so the board doesn't cover the buttons.
2. Show the panel on screen.
3. Make the button you pressed light up — for keys **and** taps.
4. Finish `on_tap` so every button steers the snake.
5. Write `restart()` so tapping after "GAME OVER" starts a fresh game.

**Example Test Case**:
- Game starts — board on the left, score and four buttons on the right.
- Tap **↑** → it lights up yellow and the snake turns up.
- Tap **↓** while going up → it lights up but the snake does **not** reverse.
- Snake crashes → "GAME OVER — Tap to play again". Tap → new game, score 0, snake back in the middle, moving right.

**Hint** (think first, peek later!):
- Run the starting code first and look at what's wrong.
- The window grew by `PANEL` pixels, but it grew on **both** sides of the centre. How far must the board slide left so all the extra space ends up on the right?
- Puzzle 1's `on_tap` finds **which** button was tapped. Now, instead of `press(name)`, call the right `go_...` function.
- For `restart()`: make a list of every variable that changes while you play. Each one must go back to how it was at the start. And don't forget the game loop has stopped!
- Why `snake.clear()` and not `snake = [[8, 8], [8, 7], [8, 6]]`? Try the second way and see what happens.

**Check Your Logic**:
- The window is 700×480 — it fits on the 7-inch Pi screen (1024×600).
- The grey grid stops before the buttons, and the board fills the left edge exactly.
- Eating food makes the panel score go up.
- After a restart the snake doesn't move twice as fast (if it does — why?).

```python
# Starting Code
import turtle, random

SIZE   = 16
CELL   = 30          # 16 x 30 = 480 pixels — fits the 7-inch Pi screen
PANEL  = 220         # extra space on the right for the buttons
BUTTON = 64

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(SIZE * CELL + PANEL, SIZE * CELL)
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

PANEL_X = SIZE * CELL / 2          # centre of the panel
buttons = {
    "Up":    {"x": PANEL_X,      "y": -40,  "arrow": "↑"},
    "Left":  {"x": PANEL_X - 70, "y": -110, "arrow": "←"},
    "Down":  {"x": PANEL_X,      "y": -110, "arrow": "↓"},
    "Right": {"x": PANEL_X + 70, "y": -110, "arrow": "→"},
}
pressed = {"name": ""}

def to_xy(row, col):
    x = col * CELL - (SIZE * CELL) / 2 + CELL / 2   # 1. slide the board left
    y = (SIZE * CELL) / 2 - row * CELL - CELL / 2
    return x, y

def draw_button(name):
    info = buttons[name]
    colour = "yellow" if name == pressed["name"] else "light gray"
    pen.goto(info["x"], info["y"])
    pen.dot(BUTTON, colour)
    pen.goto(info["x"], info["y"] - 20)
    pen.color("black")
    pen.write(info["arrow"], align="center", font=("Arial", 26, "bold"))

def draw_panel():
    pen.goto(PANEL_X, 150)
    pen.color("white")
    pen.write(f"Score: {game['score']}", align="center", font=("Arial", 22, "bold"))
    for name in buttons:
        draw_button(name)

def draw():
    pen.clear()
    for r in range(SIZE):
        for c in range(SIZE):
            x, y = to_xy(r, c)
            pen.goto(x, y)
            pen.dot(5, "gray")
    for i in range(len(snake)):
        pos = snake[i]
        x, y = to_xy(pos[0], pos[1])
        pen.goto(x, y)
        pen.dot(CELL - 4, "green" if i == 0 else "lime green")
    x, y = to_xy(food[0], food[1])
    pen.goto(x, y)
    pen.dot(CELL - 4, "red")
    # 2. show the panel
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

    new_head = [snake[0][0] + direction["row"], snake[0][1] + direction["col"]]

    if is_game_over(new_head):
        game["alive"] = False
        draw()
        pen.goto(-PANEL / 2, 0)
        pen.color("white")
        pen.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
        pen.goto(-PANEL / 2, -40)
        pen.write("Tap to play again", align="center", font=("Arial", 16, "normal"))
        screen.update()
        return

    snake.insert(0, new_head)

    if new_head == food:
        game["score"] += 1
        screen.title(f"Snake — Score: {game['score']}")
        food[0] = random.randint(0, SIZE - 1)
        food[1] = random.randint(0, SIZE - 1)
    else:
        snake.pop()

    draw()
    screen.ontimer(tick, 200)

# --- Keys and buttons ---
# 3. each of these should remember which button was pressed
def go_right():
    if direction["col"] != -1:
        direction["row"] = 0
        direction["col"] = 1

def go_left():
    if direction["col"] != 1:
        direction["row"] = 0
        direction["col"] = -1

def go_up():
    if direction["row"] != 1:
        direction["row"] = -1
        direction["col"] = 0

def go_down():
    if direction["row"] != -1:
        direction["row"] = 1
        direction["col"] = 0

def restart():
    # 5. put everything back to how the game started
    pass

def on_tap(x, y):
    if not game["alive"]:
        restart()
        return
    # 4. find which button was tapped and steer the snake

screen.listen()
screen.onkeypress(go_right, "Right")
screen.onkeypress(go_left,  "Left")
screen.onkeypress(go_up,    "Up")
screen.onkeypress(go_down,  "Down")
screen.onclick(on_tap)

draw()
screen.ontimer(tick, 200)
screen.mainloop()
```

**Extra Challenges**:
- Make a blocked button (like ↓ while going up) light up **red** instead of yellow.
- Make the snake a little faster every time it eats. (Hint: store the speed in the `game` dictionary.)

---

# Part 2: Tic Tac Toe

## How the Board Works

The board is **3×3** cells. Each cell is **160** pixels, so the window is **480×480**. The window goes from `-240` to `240` in both directions — we call that number `EDGE`.

We store the board as a **list of lists** — a list of 3 rows, and each row is a list of 3 cells. An empty cell is `""`.
```python
board = [["X", "",  "O"],     # row 0 (top)
         ["",  "X", ""],      # row 1
         ["O", "",  ""]]      # row 2 (bottom)
```
`board[0][2]` means **row 0, column 2** → the top-right cell → `"O"`.

To find the centre of a cell on screen, use the same idea as Snake:
```
x = col * CELL - EDGE + CELL / 2
y = EDGE - row * CELL - CELL / 2
```

---

## Puzzle 3: Draw the Board (Medium)
**The Story**: A Tic Tac Toe board is two vertical lines and two horizontal lines — like a `#`. Up to now we only drew dots. To draw a **line**, put the pen **down**, move it, then lift it **up** again.

**New in this puzzle:**
| What | What it does |
|------|-------------|
| `pen.pendown()` | puts the pen on the paper — moving now draws a line |
| `pen.pensize(6)` | makes lines 6 pixels thick |
| `pen.color("white")` | the colour for lines and text |
| `for i in range(1, SIZE):` | counts `1, 2` — starts at 1, stops **before** `SIZE` |

**The Question**:
1. Write `draw_line(x1, y1, x2, y2)` that draws one straight line from `(x1, y1)` to `(x2, y2)` — and leaves the pen **up** afterwards.
2. Use **one loop** to draw the whole `#`: each time round, draw one vertical and one horizontal line. Every line goes from edge to edge.

**Example Test Case**:
- The vertical lines are at `x = -80` and `x = 80`.
- The horizontal lines are at `y = -80` and `y = 80`.
- `draw_line(-80, 240, -80, -240)` is the left vertical line.

**Hint** (think first, peek later!):
- Why must the pen go **up** before moving to the start of the line?
- The first line is **1 cell** in from the left edge (`-240`). The second line is **2 cells** in. Can you write where line `i` is using `i`, `CELL` and `EDGE`?
- A vertical line at `pos` goes from `(pos, EDGE)` to `(pos, -EDGE)`. What about a horizontal line?

**Check Your Logic**:
- A white `#` with 9 equal squares.
- No extra diagonal line from the centre (if you see one — why?).
- Change `CELL = 160` to `CELL = 100` — the board should still be perfect, just smaller.

```python
# Starting Code
import turtle

SIZE = 3
CELL = 160
EDGE = SIZE * CELL / 2   # 240

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(SIZE * CELL, SIZE * CELL)
screen.title("Tic Tac Toe")
screen.tracer(0)

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.speed(0)

def draw_line(x1, y1, x2, y2):
    # fill in
    pass

pen.color("white")
pen.pensize(6)

for i in range(1, SIZE):
    pos = 0   # where is line number i?
    # draw a vertical line at x = pos
    # draw a horizontal line at y = pos
    pass

screen.update()
screen.exitonclick()
```

---

## Puzzle 4: Draw the X's and O's (Medium)
**The Story**: The board list says what's in each cell. Now draw it! An **X** is two lines that cross. An **O** is a ring — and a ring is just a big dot with a smaller black dot on top.

**New in this puzzle:**
| What | What it does |
|------|-------------|
| `board[r][c]` | row `r`, column `c` of a list of lists |
| `pen.dot(80, "black")` | drawing a black dot on a coloured dot makes a ring |

**The Question**:
1. Write `to_xy(row, col)` — it returns the centre of a cell.
2. Write `draw_x(x, y)` — two pink lines crossing at `(x, y)`, reaching **45** pixels from the centre in each direction.
3. Write `draw_o(x, y)` — a turquoise ring, size **110**, with a black hole of size **80**.
4. Loop over the board and draw each X and O in the right cell.

**Example Test Case**:
- `to_xy(0, 0)` → `(-160, 160)`, `to_xy(1, 1)` → `(0, 0)`, `to_xy(2, 1)` → `(0, -160)`.
- The board below → X's on the diagonal from top-left to bottom-right, O's in the other two corners.

**Hint** (think first, peek later!):
- Draw the X on paper with its centre at `(x, y)`. What are the coordinates of its 4 corners?
- One line goes from bottom-left to top-right. The other from top-left to bottom-right.
- For the loop: `if board[r][c] == "X":` … `elif` … — what should happen for `""`?

**Check Your Logic**:
- Three pink X's from top-left to bottom-right, two turquoise O's in the other corners.
- Every mark is in the **middle** of its square.
- Change the board list — the picture changes to match.

```python
# Starting Code
import turtle

SIZE = 3
CELL = 160
EDGE = SIZE * CELL / 2

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(SIZE * CELL, SIZE * CELL)
screen.title("Tic Tac Toe")
screen.tracer(0)

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.speed(0)

board = [["X", "",  "O"],
         ["",  "X", ""],
         ["O", "",  "X"]]

def draw_line(x1, y1, x2, y2):
    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()
    pen.goto(x2, y2)
    pen.penup()

def draw_grid():
    pen.color("white")
    pen.pensize(6)
    for i in range(1, SIZE):
        pos = i * CELL - EDGE
        draw_line(pos, EDGE, pos, -EDGE)
        draw_line(-EDGE, pos, EDGE, pos)

def to_xy(row, col):
    # return the centre of the cell
    return 0, 0

def draw_x(x, y):
    pen.color("hot pink")
    pen.pensize(12)
    # two lines crossing at (x, y)
    pass

def draw_o(x, y):
    # a turquoise ring
    pass

print(to_xy(0, 0))   # Expected: (-160.0, 160.0)
print(to_xy(2, 1))   # Expected: (0.0, -160.0)

draw_grid()
for r in range(SIZE):
    for c in range(SIZE):
        # draw an X or an O if this cell has one
        pass

screen.update()
screen.exitonclick()
```

---

## Puzzle 5: Which Cell Did I Tap? (Hard)
**The Story**: When you tap the screen, turtle tells you the tap's `(x, y)`. But the game needs to know the **row and column**. So we need `to_cell(x, y)` — `to_xy` **backwards**!

**New in this puzzle:**
| What | What it does |
|------|-------------|
| `a // b` | **floor division** — divides and throws away the leftover: `7 // 2` is `3`, `350 // 160` is `2` |
| `int(2.0)` | turns `2.0` into the whole number `2` (lists need whole numbers) |
| `screen.onclick(on_tap)` | calls `on_tap(x, y)` whenever you tap or click |
| `screen.mainloop()` | keeps the window open and listening for taps |

**The Question**: Write `to_cell(x, y)` so it returns `(row, col)` for any point inside the board. Then tapping a cell draws a yellow dot in the **centre** of that cell.

**Example Test Case**:
- `to_cell(0, 0)` → `(1, 1)` — the middle cell.
- `to_cell(-200, 200)` → `(0, 0)` — top-left.
- `to_cell(100, -20)` → `(1, 2)`.
- `to_cell(-81, -239)` → `(2, 0)` — right in the corner of the bottom-left cell.

**Hint** (think first, peek later!):
- Do it in two steps for `col`. Step 1: `x + EDGE` changes the range `-240 … 240` into `0 … 480`. Step 2: how many **whole** cells fit into that number?
- Try it on paper for `x = 100`: `100 + 240 = 340`. How many whole 160s fit in 340?
- For `row`, be careful: row 0 is at the **top**, where `y` is **biggest**. So start with `EDGE - y`, not `y + EDGE`.

**Check Your Logic**:
- All four test cases print what's expected.
- Tap near the **corner** of a square — the yellow dot still lands in the middle of **that** square.
- Tap exactly on a line between squares — the dot picks one of the two squares.

```python
# Starting Code
import turtle

SIZE = 3
CELL = 160
EDGE = SIZE * CELL / 2

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(SIZE * CELL, SIZE * CELL)
screen.title("Tap a square!")
screen.tracer(0)

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.speed(0)

def draw_line(x1, y1, x2, y2):
    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()
    pen.goto(x2, y2)
    pen.penup()

def draw_grid():
    pen.color("white")
    pen.pensize(6)
    for i in range(1, SIZE):
        pos = i * CELL - EDGE
        draw_line(pos, EDGE, pos, -EDGE)
        draw_line(-EDGE, pos, EDGE, pos)

def to_xy(row, col):
    x = col * CELL - EDGE + CELL / 2
    y = EDGE - row * CELL - CELL / 2
    return x, y

def to_cell(x, y):
    # turn a tap position into (row, col)
    col = 0
    row = 0
    return row, col

print(to_cell(0, 0))       # Expected: (1, 1)
print(to_cell(-200, 200))  # Expected: (0, 0)
print(to_cell(100, -20))   # Expected: (1, 2)
print(to_cell(-81, -239))  # Expected: (2, 0)

def on_tap(x, y):
    row, col = to_cell(x, y)
    screen.title(f"You tapped row {row}, col {col}")
    cx, cy = to_xy(row, col)
    pen.goto(cx, cy)
    pen.dot(30, "yellow")
    screen.update()

draw_grid()
screen.update()
screen.onclick(on_tap)
screen.mainloop()
```

---

## Puzzle 6: Take Turns (Medium–Hard)
**The Story**: Time to play! Tap an empty square to put your mark there. Then it's the other player's turn. We keep whose turn it is in a dictionary: `game = {"turn": "X"}`.

**New in this puzzle:**
| What | What it does |
|------|-------------|
| `game["turn"]` | `"X"` or `"O"` — whose turn it is |
| `board[row][col] = "X"` | changes one cell of the list of lists |
| `return` (with nothing after it) | leaves the function straight away — handy to ignore a bad tap |

**The Question**: Write `on_tap(x, y)` so that:
1. The mark goes into the tapped square — but **only if that square is empty**.
2. After a good move, the turn switches from X to O (or O to X).
3. The window title always says whose turn it is.
4. The game **never crashes**, wherever you tap.

**Example Test Case**:
- Tap the middle → pink X. Title: `O's turn`.
- Tap the middle **again** → nothing happens, still `O's turn`.
- Tap the top-left → turquoise O. Title: `X's turn`.

**Hint** (think first, peek later!):
- Remember the one-line `if … else`: `"O" if game["turn"] == "X" else "X"`.
- What does `to_cell(240, 0)` give? Is there a column 3 on the board? What would `board[1][3]` do? How can you stop that?
- Draw **after** you change the board, not before.

**Check Your Logic**:
- X and O take turns.
- A full square can't be changed.
- Tapping right on the edge of the window doesn't crash the game (check Thonny for red error text).

```python
# Starting Code
import turtle

SIZE = 3
CELL = 160
EDGE = SIZE * CELL / 2

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(SIZE * CELL, SIZE * CELL)
screen.title("X's turn")
screen.tracer(0)

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.speed(0)

board = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]
game  = {"turn": "X"}

def to_xy(row, col):
    x = col * CELL - EDGE + CELL / 2
    y = EDGE - row * CELL - CELL / 2
    return x, y

def to_cell(x, y):
    col = int((x + EDGE) // CELL)
    row = int((EDGE - y) // CELL)
    return row, col

def draw_line(x1, y1, x2, y2):
    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()
    pen.goto(x2, y2)
    pen.penup()

def draw_x(x, y):
    pen.color("hot pink")
    pen.pensize(12)
    draw_line(x - 45, y - 45, x + 45, y + 45)
    draw_line(x - 45, y + 45, x + 45, y - 45)

def draw_o(x, y):
    pen.goto(x, y)
    pen.dot(110, "turquoise")
    pen.dot(80, "black")

def draw_board():
    pen.clear()
    pen.color("white")
    pen.pensize(6)
    for i in range(1, SIZE):
        pos = i * CELL - EDGE
        draw_line(pos, EDGE, pos, -EDGE)
        draw_line(-EDGE, pos, EDGE, pos)
    for r in range(SIZE):
        for c in range(SIZE):
            x, y = to_xy(r, c)
            if board[r][c] == "X":
                draw_x(x, y)
            elif board[r][c] == "O":
                draw_o(x, y)
    screen.update()

def on_tap(x, y):
    row, col = to_cell(x, y)
    # 1. ignore taps that are not on the board
    # 2. ignore taps on a square that is not empty
    # 3. put the mark in, switch turns, update the title, redraw
    pass

draw_board()
screen.onclick(on_tap)
screen.mainloop()
```

---

## Puzzle 7: Who Won? (Hard)
**The Story**: A player wins with **three in a row**. This puzzle has no screen at all — just logic. We test `winner(board)` on lots of boards before we trust it in the game.

**New in this puzzle:**
| What | What it does |
|------|-------------|
| `a == b == c` | `True` only if **all three** are the same |
| `"" in row` | `True` if the list `row` has an empty cell in it |
| `return` inside a loop | leaves the whole function immediately — even in the middle of a loop |

**The Question**:
1. Write `winner(board)` — it returns `"X"` or `"O"` if that player has three in a row, and `""` if nobody has.
2. Write `is_full(board)` — it returns `True` if there are no empty cells left.

**Example Test Case**: Run the program — every line should match its `Expected`.

**Hint** (think first, peek later!):
- How many different ways are there to get three in a row? Count them on paper. (It's more than 3!)
- Look at `empty` in the tests. All three cells in the top row are `""` — so they **are** all the same. Why is that a problem? How do you fix it?
- **Challenge**: check all the rows with one `for` loop, and all the columns with another `for` loop. Then you only need two extra `if`s for the diagonals.

**Check Your Logic**:
- All 9 tests match.
- Make up your own tricky board and test it too.

```python
# Starting Code
def winner(board):
    # return "X" or "O" if they have three in a row, otherwise ""
    return ""

def is_full(board):
    # return True if there are no empty cells left
    return False

row_win  = [["X", "X", "X"],
            ["O", "O", ""],
            ["",  "",  ""]]
col_win  = [["X", "O", ""],
            ["X", "O", ""],
            ["",  "O", "X"]]
diag_win = [["X", "O", "O"],
            ["",  "X", ""],
            ["O", "",  "X"]]
back_win = [["X", "X", "O"],
            ["",  "O", ""],
            ["O", "",  "X"]]
draw     = [["X", "O", "X"],
            ["X", "O", "O"],
            ["O", "X", "X"]]
empty    = [["",  "",  ""],
            ["",  "",  ""],
            ["",  "",  ""]]

print("row_win: ", winner(row_win))    # Expected: X
print("col_win: ", winner(col_win))    # Expected: O
print("diag_win:", winner(diag_win))   # Expected: X
print("back_win:", winner(back_win))   # Expected: O
print("draw:    ", winner(draw))       # Expected: (nothing)
print("empty:   ", winner(empty))      # Expected: (nothing)

print("draw full?    ", is_full(draw))      # Expected: True
print("empty full?   ", is_full(empty))     # Expected: False
print("row_win full? ", is_full(row_win))   # Expected: False
```

---

## Puzzle 8: The Full Game (Hard)
**The Story**: Put it all together! When someone wins or the board fills up, show a message, count the score, and let the next tap start a new game. The **score** lives in its own dictionary, so it survives when the board is cleared.

**New in this puzzle:**
| What | What it does |
|------|-------------|
| `score = {"X": 0, "O": 0, "Draw": 0}` | the score for many games |
| `score[w] += 1` | if `w` is `"X"`, this adds 1 to `score["X"]` — the key comes from a variable |
| `game["over"]` | `True` when a game has ended and we are waiting for a tap to restart |

**The Question**: Paste in your `winner` and `is_full` from Puzzle 7. Then:
1. Finish `place(row, col)`: after a move, check for a **winner**, then a **draw**, and only if neither happened, switch turns.
2. Write `restart()`: empty board, X starts, game not over.
3. In `on_tap`: if the game is over, a tap starts a new game (and does **not** put a mark down).

**Example Test Case**:
- X gets three in a row → band across the middle says `X wins!` Title: `X: 1   O: 0   Draw: 0`.
- Tap → empty board, X's turn, score still `X: 1`.
- A game where the board fills with no winner → `Draw!` and the draw count goes up.

**Hint** (think first, peek later!):
- What should happen if the **last** square gives someone three in a row — is it a win or a draw? Which check must come first?
- Why must `restart()` change the cells one by one (with a loop) instead of `board = [["", "", ""], ...]`? Think about Snake's `restart()`.
- Before your step 3 works, try tapping after `X wins!` — what goes wrong?

**Check Your Logic**:
- Win across, down and diagonally — all show the message.
- Nobody can move after the game is over.
- Scores keep counting over many games.

```python
# Starting Code
import turtle

SIZE = 3
CELL = 160
EDGE = SIZE * CELL / 2

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(SIZE * CELL, SIZE * CELL)
screen.title("Tic Tac Toe")
screen.tracer(0)

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.speed(0)

board = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]
game  = {"turn": "X", "over": False}
score = {"X": 0, "O": 0, "Draw": 0}

def to_xy(row, col):
    x = col * CELL - EDGE + CELL / 2
    y = EDGE - row * CELL - CELL / 2
    return x, y

def to_cell(x, y):
    col = int((x + EDGE) // CELL)
    row = int((EDGE - y) // CELL)
    return row, col

def draw_line(x1, y1, x2, y2):
    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()
    pen.goto(x2, y2)
    pen.penup()

def draw_x(x, y):
    pen.color("hot pink")
    pen.pensize(12)
    draw_line(x - 45, y - 45, x + 45, y + 45)
    draw_line(x - 45, y + 45, x + 45, y - 45)

def draw_o(x, y):
    pen.goto(x, y)
    pen.dot(110, "turquoise")
    pen.dot(80, "black")

def draw_board():
    pen.clear()
    pen.color("white")
    pen.pensize(6)
    for i in range(1, SIZE):
        pos = i * CELL - EDGE
        draw_line(pos, EDGE, pos, -EDGE)
        draw_line(-EDGE, pos, EDGE, pos)
    for r in range(SIZE):
        for c in range(SIZE):
            x, y = to_xy(r, c)
            if board[r][c] == "X":
                draw_x(x, y)
            elif board[r][c] == "O":
                draw_o(x, y)
    screen.update()

def winner(board):
    # paste your answer from Puzzle 7
    return ""

def is_full(board):
    # paste your answer from Puzzle 7
    return False

def show_message(text):
    pen.color("black")
    pen.pensize(100)
    draw_line(-EDGE, 0, EDGE, 0)        # a thick black band across the middle
    pen.color("yellow")
    pen.goto(0, -5)
    pen.write(text, align="center", font=("Arial", 32, "bold"))
    pen.color("white")
    pen.goto(0, -40)
    pen.write("Tap to play again", align="center", font=("Arial", 14, "normal"))
    screen.update()

def update_title():
    screen.title(f"X: {score['X']}   O: {score['O']}   Draw: {score['Draw']}   —   {game['turn']}'s turn")

def place(row, col):
    board[row][col] = game["turn"]
    draw_board()
    # 1. winner? -> add to score, game over, show_message(...)
    # 2. board full? -> count a draw, game over, show_message("Draw!")
    # 3. otherwise -> switch turns
    game["turn"] = "O" if game["turn"] == "X" else "X"
    update_title()

def restart():
    # 2. empty every cell, X starts, the game is not over — then redraw
    pass

def on_tap(x, y):
    # 3. if the game is over, start a new one instead
    row, col = to_cell(x, y)
    if row < 0 or row >= SIZE or col < 0 or col >= SIZE:
        return
    if board[row][col] == "":
        place(row, col)

screen.onclick(on_tap)
draw_board()
update_title()
screen.mainloop()
```

---

## Puzzle 9: Play Against the Computer (Hard)
**The Story**: No one to play with? Let the computer be **O**! To start, the computer just picks a **random empty square**. We wait a moment before it moves, so it looks like it's thinking.

**New in this puzzle:**
| What | What it does |
|------|-------------|
| `random.choice(my_list)` | picks one random item from a list |
| `empty.append([r, c])` | builds a list of `[row, col]` pairs |
| `screen.ontimer(computer_move, 600)` | runs `computer_move()` once, after 600 milliseconds |

**The Question**: Start from your finished Puzzle 8.
1. Write `computer_move()`: make a list of every empty square, pick one at random, and `place` an O there.
2. In `on_tap`: after **your** move, if the game isn't over, ask the computer to move in 600 ms.
3. While the computer is "thinking", taps must be ignored.

**Example Test Case**:
- Tap a square → pink X. A moment later, a turquoise O appears somewhere else.
- Tap very fast, twice → only **one** X appears before the computer's O.
- You win with your last X → the computer does **not** move afterwards.

**Hint** (think first, peek later!):
- You already loop over every `r` and `c` in `draw_board`. Do the same, but `append` the empty ones.
- How can `on_tap` tell that it is the computer's turn? Look at `game`.
- Why is `if game["over"]: return` at the top of `computer_move` a good idea?

**Check Your Logic**:
- You are always X, the computer is always O.
- The computer never picks a full square.
- The score counts wins for both of you, and draws.

```python
# Starting Code — add these to your Puzzle 8 game

import random   # put this at the top, next to import turtle

def computer_move():
    if game["over"]:
        return
    empty = []
    # 1. add every empty [row, col] to the list
    # 2. pick one at random
    # 3. place an "O" there
    pass

def on_tap(x, y):
    if game["over"]:
        restart()
        return
    # 3. ignore taps while it's the computer's turn
    row, col = to_cell(x, y)
    if row < 0 or row >= SIZE or col < 0 or col >= SIZE:
        return
    if board[row][col] == "":
        place(row, col)
        # 2. if the game isn't over, the computer moves in 600 ms
```

**Extra Challenges** (really hard!):
- **A smarter computer**: before picking at random, check each empty square — if an O there would **win**, go there. (Hint: put `"O"` in the square, call `winner(board)`, then put `""` back.)
- Even smarter: if an **X** there would win, go there to **block** it.
- Let the **loser** start the next game.
- Draw a line through the three winning squares.
