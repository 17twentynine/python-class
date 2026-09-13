# Snake on the Touch Screen
Date: 13th Sep 2026
Topic: Dictionaries of Dictionaries & Tapping the Screen

*Our Raspberry Pi has a 7-inch touch screen. Today we add big arrow buttons to the Snake game so you can play with just your finger — no keyboard! This time there is **no starting code**. Read the puzzle, plan it on paper, then write the whole program yourself. Only read the hints when you're stuck.*

---

## Before You Start: The Pi Screen

- The screen is **1024×600** pixels. After the taskbar and the window's title bar, a game window can be about **500 pixels tall** at most — so every window today is **480** pixels tall.
- A **tap** on the touch screen works just like a **mouse click**. `screen.onclick(fn)` handles both.
- Your Snake game from 27th Jun used `CELL = 40` (640×640). On the Pi, change it to `CELL = 30`.
- Save each puzzle as its own file (`touch1.py`, `touch2.py`) so you can go back to it.

---

## Puzzle 1: On-Screen Arrow Buttons (Medium–Hard)
**The Story**: Why play with a keyboard when you have a touch screen? Draw four big round arrow buttons. When you **tap** a button — or press the matching arrow key — it lights up yellow. Store the buttons in a **dictionary of dictionaries**: each button's name points to another dictionary with its position and arrow symbol.

**New in this puzzle:**
| What | What it does |
|------|-------------|
| `buttons["Up"]["x"]` | a dictionary inside a dictionary — first pick the button, then pick its `x` |
| `for name in buttons:` | looping over a dictionary gives you each **key** (`"Up"`, `"Left"`, …) |
| `screen.onclick(fn)` | calls `fn(x, y)` when you click or **tap** — `x` and `y` are where you touched |
| `abs(number)` | distance from zero, always positive: `abs(-7)` is `7`, `abs(7)` is `7` |
| `pen.write(text, align="center", font=("Arial", 36, "bold"))` | writes text; it appears **above** the pen's position |

**The Question**: Write a program that:
1. Opens a black **480×480** window.
2. Draws four round **light gray** buttons, size **100**, in an upside-down T like the arrow keys on a keyboard. **↑** is at `(0, 50)` and **←** is at `(-110, -60)` — you work out where **↓** and **→** go.
3. Writes the arrow `↑ ← ↓ →` in black in the middle of each button.
4. Lights up the **last pressed** button in **yellow** — only one at a time.
5. Works with the **arrow keys** and with **taps** on the buttons. Taps that miss every button do nothing.
6. Shows `You pressed: Right` (or Up, Down, Left) in the window title.

**Example Test Case**:
- Tap **→** → it turns yellow, title says `You pressed: Right`.
- Press the **Up** key → **↑** turns yellow, **→** goes back to gray.
- Tap an empty corner of the window → nothing changes.

**Hint** (think first, peek later!):
- **↓** sits exactly under **↑**. **→** is as far to the right of **↓** as **←** is to the left.
- Plan your functions first: one to draw **one** button, one to redraw **everything**, one called `press(name)` that remembers the button and redraws. Why is `press(name)` better than writing the same code four times?
- `screen.onkeypress` needs a function with **no** parameters. How can a tiny function like `up_pressed()` use `press(name)`?
- Is a tap at `(130, -40)` on the **→** button at `(110, -60)`? The button reaches **50** pixels each way. How far is the tap left-to-right? Up-and-down? **Both** need to be close enough.
- To remember the last button inside a function, use a dictionary like `pressed = {"name": ""}` — just like `direction` in Snake.
- The arrow text appears above the pen. Start writing about **28** pixels lower than the button's centre — then adjust until it looks right.

**Check Your Logic**:
- Four buttons, not overlapping, in an upside-down T.
- Only one button is yellow at a time.
- Tapping just outside a button — even diagonally near its corner — does nothing.

---

## Puzzle 2: Snake with Touch Buttons (Hard)
**The Story**: Put the buttons **next to** the snake board so the whole game can be played on the touch screen. The window gets wider to make a side panel, and the board slides to the left. When the game ends, **tapping anywhere** starts a new game — no keyboard needed at all.

**New in this puzzle:**
| What | What it does |
|------|-------------|
| `snake.clear()` | removes everything from a list |
| `snake.extend([[8, 8], [8, 7]])` | adds all the items from another list to the end |
| `name == "Up"` … `elif` | choose which function to call for the button that was tapped |

**The Question**: Start from your finished Snake game (27th Jun, Puzzle 8) with `CELL = 30`. Change it so that:
1. The window is the board plus a panel **220** pixels wide on the right: **700×480**.
2. The board sits on the left, touching the left edge, and **doesn't cover** the panel.
3. The panel shows `Score: 0` near the top and four arrow buttons (size **64**) below it. Put the middle of the panel at `PANEL_X = SIZE * CELL / 2`. **↑** is at `(PANEL_X, -40)`, **←** at `(PANEL_X - 70, -110)` — work out the other two.
4. The last button pressed — by key **or** tap — is yellow.
5. Tapping a button steers the snake (and still can't reverse it).
6. "GAME OVER" is written in the middle of the **board** (not the window), with `Tap to play again` below it.
7. After Game Over, a tap starts a completely fresh game: score 0, snake back in the middle, moving right.

**Example Test Case**:
- Board on the left, score and four buttons on the right.
- Tap **↑** → it lights up and the snake turns up.
- Tap **↓** while going up → it lights up, but the snake does **not** reverse.
- Crash → `GAME OVER` / `Tap to play again`. Tap → new game.

**Hint** (think first, peek later!):
- The window grew by 220 pixels, but `(0, 0)` is still in the **middle** of the window — so the window grew by 110 on **each** side. How far must every snake dot move left? Which **one** function do you need to change to move them all?
- Where is the middle of the board now? That's where "GAME OVER" goes.
- Puzzle 1 found **which** button was tapped. Now, instead of `press(name)`, call `go_up()`, `go_down()`, …
- For the restart, list **every** variable that changes while you play. Each one must go back to how it started. And the game loop stopped when you crashed — how do you start it again?
- Why use `snake.clear()` and `snake.extend(...)` instead of `snake = [[8, 8], [8, 7], [8, 6]]`? Try the second way and see what happens.

**Check Your Logic**:
- The gray grid starts at the left edge and stops before the buttons.
- Eating food makes the panel score go up.
- After a restart the snake moves at normal speed — not twice as fast (if it's faster, why?).
- You can play game after game using **only your finger**.

**Extra Challenges**:
- Make a blocked button (like ↓ while going up) light up **red** instead of yellow.
- Make the snake a little faster every time it eats. (Store the speed in the `game` dictionary.)
