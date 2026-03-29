# Logic Puzzles: Maps (Dictionaries)
Date: 29th Mar 2026
Topic: Dictionaries — Keys, Values & Lookups

*Five puzzles to introduce the **dictionary** (`dict`), Python’s built-in **map**: each **key** maps to exactly one **value**. Use curly braces: `prices = {"apple": 50}`; read with `prices["apple"]`; add or change with `prices["pear"] = 40`. Keys must be unique; values can be anything (numbers, strings, even lists).*

---

## Puzzle 1: The Snack Price List (Easy)
**The Story**: A small shop keeps snack prices in a dictionary. The key is the snack name (string); the value is the price in cents.

**The Question**: Build `prices` with: apple → 50, banana → 30, orange → 45. Then print the price of **banana** and the price of **orange**.

**Example Test Case**:
- If `prices = {"milk": 120, "water": 80}`, then `prices["water"]` is **80**.

**Hint**: `prices = {"apple": 50, ...}`. Use square brackets to read: `prices["banana"]`.

**Check Your Logic**:
- Banana: **30** cents.
- Orange: **45** cents.

```python
# Starting Code
prices = {
    # Add apple, banana, orange with the prices above
}

print(f"Banana: {prices['banana']} cents")
print(f"Orange: {prices['orange']} cents")
```

---

## Puzzle 2: The Attendance Roster (Easy–Medium)
**The Story**: Three students are in class today: `"Ada"`, `"Bob"`, and `"Chen"`. You start with everyone marked absent (`False`). Then Ada and Chen arrive — set their values to `True` (present).

**The Question**: Build `attendance` with all three names as keys. After updates, how many students are present? (Count by looping or by checking each name — your choice.)

**Example Test Case**:
- Only `{"Zoe": True, "Max": False}` → **1** present.

**Hint**: Start with `{"Ada": False, "Bob": False, "Chen": False}`, then assign `attendance["Ada"] = True` and the same for Chen.

**Check Your Logic**:
- Present: Ada and Chen → **2** present; Bob stays **False**.

```python
# Starting Code
attendance = {
    "Ada": False,
    "Bob": False,
    "Chen": False,
}

# Mark Ada and Chen as present
# attendance["Ada"] = ...

present_count = 0
for name in attendance:
    # If this student is True, add 1 to present_count
    pass

print(f"Attendance map: {attendance}")
print(f"Number present: {present_count}")
```

---

## Puzzle 3: The Letter Counter (Medium)
**The Story**: You have a word (all lowercase). You want a dictionary `counts` where each **letter** is a key and the **value** is how many times that letter appears.

**The Question**: For `word = "banana"`, build `counts`. What is `counts["a"]`? What is `counts["b"]`?

**Example Test Case**:
- Word `"egg"` → `counts = {"e": 1, "g": 2}`.

**Hint**: Loop `for ch in word:`. If `ch` is not in `counts` yet, set `counts[ch] = 1`. Else, add 1: `counts[ch] = counts[ch] + 1`.

**Check Your Logic**:
- `"banana"` → `a`: **3**, `b`: **1**, `n`: **2**.

```python
# Starting Code
word = "banana"
counts = {}

for ch in word:
    # Update counts for this character
    pass

print(f"Letter counts: {counts}")
print(f"How many 'a'? {counts['a']}")
print(f"How many 'b'? {counts['b']}")
```

---

## Puzzle 4: The Country Codebook (Medium–Hard)
**The Story**: You have two parallel lists: country names and their dialing codes (same order). Build a single dictionary `dial` mapping **country name → code** (integer).

**The Question**: Using a loop with index `i` (or `zip`), build `dial` from the lists below. What is `dial["Japan"]`? What is `dial["Brazil"]`?

**Example Test Case**:
- `names = ["X", "Y"]`, `codes = [1, 2]` → `dial["Y"]` is **2**.

**Hint**: `for i in range(len(names)):` then `dial[names[i]] = codes[i]`. Or: `for name, code in zip(names, codes):`.

**Check Your Logic**:
- Japan → **81**, Brazil → **55**.

```python
# Starting Code
names = ["France", "Japan", "Brazil", "Kenya"]
codes = [33, 81, 55, 254]

dial = {}

# Fill dial from names and codes
for i in range(len(names)):
    # Map names[i] to codes[i]
    pass

print(f"Dial codes: {dial}")
print(f"Japan: {dial['Japan']}")
print(f"Brazil: {dial['Brazil']}")
```

---

## Puzzle 5: The Scoreboard Invert (Challenging)
**The Story**: You start with `player_scores` mapping **player name → score** (integer). You must build a **new** dictionary `score_to_players` mapping **each score → list of player names** who have that score. Players with the same score go in the same list.

**The Question**: For the data below, what is `score_to_players[10]`? What is `score_to_players[25]`? What keys appear in `score_to_players`?

**Example Test Case**:
- `{"A": 5, "B": 5, "C": 7}` → `score_to_players[5]` is `["A", "B"]` (order of names can vary if you append in loop order).

**Hint**: Loop `for player, score in player_scores.items():`. If `score` is not yet a key in `score_to_players`, set it to `[player]`. Otherwise, `append` the player to the existing list.

**Check Your Logic**:
- Score **10**: `["Eve", "Dan"]` (or `["Dan", "Eve"]` depending on loop order).
- Score **25**: `["Amy"]`.
- Keys in `score_to_players`: **10, 15, 20, 25** (four different scores).

```python
# Starting Code
player_scores = {
    "Amy": 25,
    "Ben": 15,
    "Chen": 20,
    "Dan": 10,
    "Eve": 10,
}

score_to_players = {}

for player, score in player_scores.items():
    # Add player to the list for this score
    pass

print(f"Score → players: {score_to_players}")
print(f"Who scored 10? {score_to_players[10]}")
print(f"Who scored 25? {score_to_players[25]}")
```
