# Logic Puzzles: Maps (Dictionaries) — Round 2
Date: 19th Apr 2026
Topic: Dictionaries — Merging, Filtering, Nested Dicts & Finding Extremes

*You already know how to build a dict and look up values. These puzzles push further: you will **merge** two dicts, **filter** entries, **navigate nested dicts**, **count words**, and **find the key with the highest value**. Same tool (`dict`), sharper use.*

---

## Puzzle 1: Word Frequency (Medium)
**The Story**: A sentence is a string of words separated by spaces. You want to know how often each word appears — similar to the letter counter from last time, but now each **word** (not letter) is the key.

**The Question**: For `sentence = "the cat sat on the mat the cat"`, build `word_counts` where each word maps to the number of times it appears. What is `word_counts["the"]`? What is `word_counts["cat"]`?

**Example Test Case**:
- `"hi hi bye"` → `{"hi": 2, "bye": 1}` → `word_counts["hi"]` is **2**.

**Hint**: Split the sentence into a list first: `words = sentence.split()`. Then loop over `words` exactly like you looped over letters in the letter-counter puzzle.

**Check Your Logic**:
- `"the"` appears **3** times.
- `"cat"` appears **2** times.

```python
# Starting Code
sentence = "the cat sat on the mat the cat"
word_counts = {}

words = sentence.split()   # ["the", "cat", "sat", ...]

for word in words:
    # Update word_counts for this word
    pass

print(f"Word counts: {word_counts}")
print(f"'the' appears: {word_counts['the']} times")
print(f"'cat' appears: {word_counts['cat']} times")
```

---

## Puzzle 2: Inventory Merge (Medium)
**The Story**: Two warehouses each track stock as a dictionary `{item: quantity}`. You need to combine them into one `combined` dict. If both warehouses have the **same item**, **add** their quantities.

**The Question**: Merge `warehouse_a` and `warehouse_b` below. What is `combined["apples"]`? What is `combined["grapes"]`?

**Example Test Case**:
- `a = {"x": 3}`, `b = {"x": 2, "y": 5}` → `combined = {"x": 5, "y": 5}`.

**Hint**: Start by copying `warehouse_a` into `combined`. Then loop `for item, qty in warehouse_b.items():`. If the item already exists in `combined`, add to it; otherwise, set it fresh.

**Check Your Logic**:
- `"apples"`: 30 + 15 = **45**.
- `"grapes"`: only in warehouse_b → **20**.

```python
# Starting Code
warehouse_a = {"apples": 30, "bananas": 50, "mangoes": 10}
warehouse_b = {"apples": 15, "bananas": 25, "grapes": 20}

combined = {}

# First, copy everything from warehouse_a
for item, qty in warehouse_a.items():
    combined[item] = qty

# Then merge warehouse_b
for item, qty in warehouse_b.items():
    # If item already in combined, add quantities; else set it
    pass

print(f"Combined inventory: {combined}")
print(f"Apples: {combined['apples']}")
print(f"Grapes: {combined['grapes']}")
```

---

## Puzzle 3: Find the Top Scorer (Medium)
**The Story**: A dict maps player names to scores. You must find the **name** of the player with the **highest** score — without using `max()` on the dict directly. Loop through the entries yourself.

**The Question**: For the scores below, which player won, and what was their score?

**Example Test Case**:
- `{"Ali": 8, "Bo": 15, "Cal": 11}` → winner is `"Bo"` with score **15**.

**Hint**: Start with `best_name = None` and `best_score = -1`. Loop `for name, score in scores.items():`. If `score > best_score`, update both variables.

**Check Your Logic**:
- Winner: **"Maya"** with score **98**.

```python
# Starting Code
scores = {
    "Liam": 72,
    "Maya": 98,
    "Noah": 85,
    "Ava":  91,
    "Ethan": 60,
}

best_name = None
best_score = -1

for name, score in scores.items():
    # Update best_name and best_score if this score is higher
    pass

print(f"Top scorer: {best_name} with {best_score} points")
```

---

## Puzzle 4: The Nested Gradebook (Medium–Hard)
**The Story**: A gradebook is a dict of dicts. Each student name maps to **another dict** that maps subject → score: `{"Ada": {"Math": 90, "Science": 85}}`. You read a nested value with two bracket lookups: `gradebook["Ada"]["Math"]`.

**The Question**: Using the gradebook below —
1. Print Ada's Science score.
2. Find Ada's **average** score across all her subjects.

**Example Test Case**:
- `{"Zoe": {"Art": 80, "PE": 60}}` → Zoe's average is `(80 + 60) / 2` = **70.0**.

**Hint**: `gradebook["Ada"]` gives you the inner dict `{"Math": 90, ...}`. To average, sum the `.values()` of that inner dict and divide by its length.

**Check Your Logic**:
- Ada's Science score: **78**.
- Ada's average: `(90 + 78 + 95) / 3` = **87.67** (rounded to 2 decimal places).

```python
# Starting Code
gradebook = {
    "Ada":  {"Math": 90, "Science": 78, "English": 95},
    "Ben":  {"Math": 65, "Science": 80, "English": 70},
    "Cara": {"Math": 88, "Science": 92, "English": 76},
}

# 1. Print Ada's Science score
ada_science = gradebook["Ada"]["Science"]
print(f"Ada's Science score: {ada_science}")

# 2. Compute Ada's average
ada_scores = gradebook["Ada"]   # inner dict
total = 0
for subject in ada_scores:
    # Add each score to total
    pass

average = total / len(ada_scores)
print(f"Ada's average: {round(average, 2)}")
```

---

## Puzzle 5: Budget Filter (Medium–Hard)
**The Story**: A shop has a menu dict `{item: price}`. A customer has a fixed budget. You must build a **new** dict `affordable` containing only the items whose price is **less than or equal to** the budget. Then print the affordable items sorted by price (cheapest first).

**The Question**: With `budget = 40`, which items can the customer afford? What is the cheapest affordable item and its price?

**Example Test Case**:
- `menu = {"tea": 10, "cake": 50, "juice": 30}`, `budget = 35` → `affordable = {"tea": 10, "juice": 30}`.

**Hint**: Loop `for item, price in menu.items():` and add to `affordable` only when `price <= budget`. To sort, use: `sorted(affordable.items(), key=lambda x: x[1])` — this gives a list of `(item, price)` pairs sorted by price.

**Check Your Logic**:
- Affordable items (budget 40): **sandwich (35), coffee (25), water (15)** — three items.
- Cheapest: **water** at **15**.

```python
# Starting Code
menu = {
    "coffee":    25,
    "cake":      55,
    "sandwich":  35,
    "smoothie":  60,
    "water":     15,
    "salad":     45,
}
budget = 40

affordable = {}

for item, price in menu.items():
    # Add to affordable if within budget
    pass

print(f"Affordable items: {affordable}")

# Sort by price and print
sorted_items = sorted(affordable.items(), key=lambda x: x[1])
print("Sorted by price:")
for item, price in sorted_items:
    print(f"  {item}: {price}")

print(f"Cheapest: {sorted_items[0][0]} at {sorted_items[0][1]}")
```
