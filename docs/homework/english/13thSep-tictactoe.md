# Build Tic Tac Toe — Step by Step with Turtle
Date: 13th Sep 2026
Topic: Lists of Lists & Tapping the Screen

*Our Raspberry Pi has a 7-inch touch screen. Today you build Tic Tac Toe from scratch — a game you play by tapping the squares, against a friend or against the computer. There is **no starting code**. Read the puzzle, plan it on paper, then write the program yourself. Only read the hints when you're stuck.*

---

## Before You Start

- The Pi screen is **1024×600** pixels, so our board is **480×480** — it fits with room to spare.
- A **tap** on the touch screen works just like a **mouse click**. `screen.onclick(fn)` handles both.
- Each puzzle builds on the one before. Save each one as its own file (`ttt1.py`, `ttt2.py`, …) and start the next puzzle from a copy.

---

## How the Board Works

The board is **3×3** cells. Each cell is **160** pixels, so the window is **480×480**. The window goes from `-240` to `240` in both directions — call that number `EDGE`.

```
SIZE = 3      CELL = 160      EDGE = SIZE * CELL / 2  →  240
```

We store the board as a **list of lists**: a list of 3 rows, and each row is a list of 3 cells. An empty cell is `""`.

| | col 0 | col 1 | col 2 |
|---|---|---|---|
| **row 0** (top) | `"X"` | `""` | `"O"` |
| **row 1** | `""` | `"X"` | `""` |
| **row 2** (bottom) | `"O"` | `""` | `""` |

`board[0][2]` means **row 0, column 2** → the top-right cell → `"O"`.

To find the centre of a cell on screen, use the same idea as Snake:
```
x = col * CELL - EDGE + CELL / 2
y = EDGE - row * CELL - CELL / 2
```

---

## Puzzle 1: Draw the Board (Medium)
**The Story**: A Tic Tac Toe board is two vertical lines and two horizontal lines — like a `#`. Up to now we only drew dots. To draw a **line**, put the pen **down**, move it, then lift it **up** again.

**New in this puzzle:**
| What | What it does |
|------|-------------|
| `pen.pendown()` | puts the pen on the paper — moving now draws a line |
| `pen.penup()` | lifts the pen — moving now draws nothing |
| `pen.pensize(6)` | makes lines 6 pixels thick |
| `pen.color("white")` | the colour for lines and text |
| `for i in range(1, SIZE):` | counts `1, 2` — starts at 1, stops **before** `SIZE` |

**The Question**: Write a program that:
1. Opens a black **480×480** window, using `SIZE`, `CELL` and `EDGE` (no plain `480` or `240` in your code!).
2. Has a function `draw_line(x1, y1, x2, y2)` that draws one straight line — and leaves the pen **up** when it's done.
3. Uses **one loop** to draw the white `#` (thickness 6): each time round, one vertical and one horizontal line, from edge to edge.

**Example Test Case**:
- The vertical lines are at `x = -80` and `x = 80`.
- The horizontal lines are at `y = -80` and `y = 80`.
- The left vertical line goes from `(-80, 240)` to `(-80, -240)`.

**Hint** (think first, peek later!):
- Why must the pen go **up** before moving to the start of a line?
- The first line is **1 cell** in from the left edge (`-EDGE`). The second is **2 cells** in. Write the position of line `i` using `i`, `CELL` and `EDGE`.
- A vertical line at `pos` goes from `(pos, EDGE)` to `(pos, -EDGE)`. What about a horizontal line?

**Check Your Logic**:
- A white `#` with 9 equal squares.
- No extra line from the centre of the window (if there is one — why?).
- Change `CELL` to `100` — the board is smaller but still perfect.

---

## Puzzle 2: Draw the X's and O's (Medium)
**The Story**: The board list says what is in each cell. Now draw it! An **X** is two lines that cross. An **O** is a ring — and a ring is just a big dot with a smaller black dot on top.

**New in this puzzle:**
| What | What it does |
|------|-------------|
| `board[r][c]` | row `r`, column `c` of a list of lists |
| `pen.dot(80, "black")` | a black dot on top of a coloured dot makes a ring |

**The Question**: Starting from Puzzle 1, add:
1. A `board` variable holding the example board from **How the Board Works**, plus an `"X"` in the bottom-right corner.
2. `to_xy(row, col)` — returns the centre `(x, y)` of a cell.
3. `draw_x(x, y)` — two **hot pink** lines, thickness **12**, crossing at `(x, y)` and reaching **45** pixels from the centre in every direction.
4. `draw_o(x, y)` — a **turquoise** ring: outside size **110**, black hole size **80**.
5. A loop that goes over every cell and draws an X or an O where the board has one.

**Example Test Case**:
- `to_xy(0, 0)` → `(-160.0, 160.0)`
- `to_xy(1, 1)` → `(0.0, 0.0)`
- `to_xy(2, 1)` → `(0.0, -160.0)`
- On screen: X's from top-left to bottom-right, O's in the other two corners.

**Hint** (think first, peek later!):
- Draw an X on paper with its centre at `(x, y)`. What are the coordinates of its four ends?
- One line goes bottom-left → top-right, the other top-left → bottom-right.
- You need a loop inside a loop — one for rows, one for columns. What should happen when the cell is `""`?
- If your X's are thin, where did `pensize` get changed?

**Check Your Logic**:
- Every mark is in the **middle** of its square.
- Change the board list — the picture changes to match.

---

## Puzzle 3: Which Cell Did I Tap? (Hard)
**The Story**: When you tap the screen, turtle gives you the tap's `(x, y)`. But the game needs the **row and column**. So we need `to_cell(x, y)` — `to_xy` **backwards**!

**New in this puzzle:**
| What | What it does |
|------|-------------|
| `a // b` | **floor division** — divides and throws away the leftover: `7 // 2` is `3`, `340 // 160` is `2` |
| `int(2.0)` | turns `2.0` into the whole number `2` (list positions must be whole numbers) |
| `screen.onclick(on_tap)` | calls `on_tap(x, y)` every time you tap or click |
| `screen.mainloop()` | keeps the window open and listening for taps |

**The Question**: Start from Puzzle 1 (the empty `#` board) and add:
1. `to_xy(row, col)` from Puzzle 2.
2. `to_cell(x, y)` — returns `(row, col)` for any point on the board.
3. Print the four test cases below, so you can check `to_cell` before you tap anything.
4. When you tap, draw a **yellow** dot (size 30) in the **centre** of the tapped cell and show `You tapped row 1, col 2` in the title.

**Example Test Case**:
- `to_cell(0, 0)` → `(1, 1)` — the middle cell
- `to_cell(-200, 200)` → `(0, 0)` — top-left
- `to_cell(100, -20)` → `(1, 2)`
- `to_cell(-81, -239)` → `(2, 0)` — deep in the corner of the bottom-left cell

**Hint** (think first, peek later!):
- Do `col` in two steps. Step 1: `x + EDGE` turns the range `-240 … 240` into `0 … 480`. Step 2: how many **whole** cells fit into that?
- Try it on paper for `x = 100`: `100 + 240 = 340`. How many whole 160s fit in 340?
- For `row`, careful: row 0 is at the **top**, where `y` is **biggest**. What should you start with instead of `y + EDGE`?

**Check Your Logic**:
- All four test cases print the expected answers.
- Tap near the **corner** of a square — the yellow dot still lands in the middle of **that** square.

---

## Puzzle 4: Take Turns (Medium–Hard)
**The Story**: Time to play with a friend! Tap an empty square to put your mark there, then it's the other player's turn. Keep whose turn it is in a dictionary: `game = {"turn": "X"}`.

**New in this puzzle:**
| What | What it does |
|------|-------------|
| `board[row][col] = "X"` | changes one cell of the list of lists |
| `return` (with nothing after it) | leaves the function straight away — handy to ignore a bad tap |
| `pen.clear()` | wipes the screen so you can draw everything again |

**The Question**: Using your code from Puzzles 1–3, make a two-player game:
1. The board starts **empty**.
2. Write `draw_board()` that clears the screen and draws the `#` **and** every X and O.
3. A tap puts the current player's mark in the tapped square — but **only if it is empty**.
4. After a good move, the turn switches from X to O (or O to X).
5. The window title always says whose turn it is: `X's turn`.
6. The game **never crashes**, wherever you tap.

**Example Test Case**:
- Tap the middle → pink X. Title: `O's turn`.
- Tap the middle **again** → nothing happens, still `O's turn`.
- Tap the top-left → turquoise O. Title: `X's turn`.

**Hint** (think first, peek later!):
- Remember the one-line `if … else` from Snake: `"green" if i == 0 else "lime green"`. How can it switch X and O?
- What does `to_cell(240, 0)` give? Is there a column 3? What would `board[1][3]` do? How can you stop that?
- Change the board **first**, then draw.

**Check Your Logic**:
- X and O take turns.
- A full square can't be changed.
- Tapping right on the edge of the window doesn't show red error text in Thonny.

---

## Puzzle 5: Who Won? (Hard)
**The Story**: A player wins with **three in a row**. This puzzle has no turtle at all — just logic. Test `winner(board)` on lots of boards before you trust it in the game.

**New in this puzzle:**
| What | What it does |
|------|-------------|
| `a == b == c` | `True` only if **all three** are the same |
| `"" in row` | `True` if the list `row` has an empty cell in it |
| `return` inside a loop | leaves the whole function immediately — even in the middle of a loop |

**The Question**: In a **new file**, write:
1. `winner(board)` — returns `"X"` or `"O"` if that player has three in a row, and `""` if nobody does.
2. `is_full(board)` — returns `True` if there are no empty cells left.
3. Make each test board below as a list of lists, and print the results.

**Example Test Case**:
| Board name | Row 0 | Row 1 | Row 2 | `winner` | `is_full` |
|---|---|---|---|---|---|
| `row_win` | X X X | O O _ | _ _ _ | `"X"` | `False` |
| `col_win` | X O _ | X O _ | _ O X | `"O"` | `False` |
| `diag_win` | X O O | _ X _ | O _ X | `"X"` | `False` |
| `back_win` | X X O | _ O _ | O _ X | `"O"` | `False` |
| `draw` | X O X | X O O | O X X | `""` | `True` |
| `empty` | _ _ _ | _ _ _ | _ _ _ | `""` | `False` |

(`_` means an empty cell `""`.)

**Hint** (think first, peek later!):
- How many different ways are there to get three in a row? Count them on paper. (It's more than 3!)
- Look at `empty`. All three cells in the top row are `""` — so they **are** all the same. Why is that a problem? How do you fix it?
- **Challenge**: check all rows with one `for` loop and all columns with another. Then you only need two more `if`s for the diagonals.

**Check Your Logic**:
- Every row of the table matches.
- Make up your own tricky board and test that too.

---

## Puzzle 6: The Full Game (Hard)
**The Story**: Put it all together! When someone wins or the board fills up, show a message, count the score, and let the next tap start a new game. The **score** lives in its own dictionary so it survives when the board is cleared.

**New in this puzzle:**
| What | What it does |
|------|-------------|
| `score = {"X": 0, "O": 0, "Draw": 0}` | the score across many games |
| `score[w] += 1` | if `w` is `"X"`, this adds 1 to `score["X"]` — the key comes from a variable |
| `game["over"]` | `True` when a game has ended and we're waiting for a tap to restart |

**The Question**: Start from Puzzle 4 and add your `winner` and `is_full` from Puzzle 5. Then:
1. After every move, check for a **winner**, then for a **draw**. Only if neither happened, switch turns.
2. When the game ends, draw a thick **black** band across the middle of the board (a line with pen size **100**), write the message — `X wins!`, `O wins!` or `Draw!` — in **yellow**, and `Tap to play again` in smaller white text below it.
3. Show the score and whose turn it is in the title: `X: 1   O: 0   Draw: 0   —   O's turn`.
4. After the game ends, the next tap starts a new game: empty board, X starts. It must **not** also put down a mark.
5. The score keeps counting over many games.

**Example Test Case**:
- X gets three in a row → `X wins!` banner. Title: `X: 1   O: 0   Draw: 0`.
- Tap → empty board, X's turn, score still `X: 1`.
- The board fills with no winner → `Draw!` and the draw count goes up.

**Hint** (think first, peek later!):
- A good plan: a function `place(row, col)` that puts the mark down, redraws, and checks for win/draw. Then `on_tap` only has to work out **where** you tapped.
- If the **last** square gives someone three in a row, is it a win or a draw? Which check must come first?
- Why must `restart()` empty the cells one by one (with loops) instead of `board = [["", "", ""], ...]`? Think about the Snake touch-buttons game.
- Before you do step 4, try tapping after `X wins!` — what goes wrong?

**Check Your Logic**:
- Wins across, down and diagonally all show the message.
- Nobody can move after the game is over.
- The score keeps counting over many games.

---

## Puzzle 7: Play Against the Computer (Hard)
**The Story**: No one to play with? Let the computer be **O**! To start, the computer just picks a **random empty square**. It waits a moment before moving, so it looks like it's thinking.

**New in this puzzle:**
| What | What it does |
|------|-------------|
| `random.choice(my_list)` | picks one random item from a list |
| `empty.append([r, c])` | builds a list of `[row, col]` pairs |
| `screen.ontimer(computer_move, 600)` | runs `computer_move()` once, after 600 milliseconds |

**The Question**: Start from Puzzle 6. You are always **X**, the computer is always **O**.
1. Write `computer_move()`: make a list of every empty square, pick one at random, and put an O there (with the same win/draw checks as your moves).
2. After **your** move, if the game isn't over, the computer moves **600 ms** later.
3. While the computer is "thinking", your taps are ignored.

**Example Test Case**:
- Tap a square → pink X. A moment later a turquoise O appears somewhere else.
- Tap two squares very fast → only **one** X appears before the computer's O.
- You win with your last X → the computer does **not** move afterwards.

**Hint** (think first, peek later!):
- You already loop over every `r` and `c` in `draw_board`. Do the same, but `append` the empty ones.
- How can `on_tap` tell that it's the computer's turn? Look inside `game`.
- What could go wrong if `computer_move` runs after the game is already over? How do you stop it?

**Check Your Logic**:
- The computer never picks a full square.
- Wins, losses and draws are all counted.
- You can play game after game with only your finger.

**Extra Challenges** (really hard!):
- **A smarter computer**: before picking at random, check each empty square — if an O there would **win**, go there. (Hint: put `"O"` in the square, call `winner(board)`, then put `""` back.)
- Even smarter: if an **X** there would win, go there to **block** it.
- Let the **loser** start the next game.
- Draw a line through the three winning squares.
