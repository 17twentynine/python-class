# Real-World Logic: Lists & Maps (Dictionaries)
Date: 17th May 2026
Topic: Lists and Dictionaries — Practical Simulations & Calculators

*This week, we move beyond pure logic puzzles and apply Lists and Dictionaries to real-world scenarios. We will simulate a traffic light, calculate a grocery bill, and track temperatures. These are the building blocks of real software.*

---

## Puzzle 1: The Flight Router (Connecting Flights)
**The Story**: You are building a travel app. You have a dictionary of direct flights. The keys are departure cities, and the values are **lists** of cities you can fly directly to.

**The Question**: A user wants to start in **Amsterdam** and take exactly **TWO** flights (one layover). What are all the unique final destinations they can reach?

**Example Test Case**:
- `{"A": ["B", "C"], "B": ["D"], "C": ["D", "E"]}`. Start "A" → Layover "B" or "C" → Final "D", "E".

**Hint**: You need a nested loop. First, loop through the cities you can reach directly from Amsterdam (these are your layovers). Then, for each layover, loop through the cities you can reach from *there* (your final destinations). Add them to a `possible_destinations` list if they aren't already in it.

**Check Your Logic**:
- From London: New York, Madrid, Paris
- From Paris: Madrid, Rome, Amsterdam
- From Berlin: Rome, Warsaw
- Final Unique List: **['New York', 'Madrid', 'Paris', 'Rome', 'Amsterdam', 'Warsaw']**

```python
# Starting Code
flights = {
        "Amsterdam": ["London", "Paris", "Berlin"],
        "London":    ["New York", "Madrid", "Paris"],
        "Paris":     ["Madrid", "Rome", "Amsterdam"],
        "Berlin":    ["Rome", "Warsaw"],
        "Madrid":    ["Rome"],
        "Rome":      ["Athens"],
        "New York":  ["Toronto"]
}

start_city = "Amsterdam"
possible_destinations = []

# 1. Loop through the layover cities from the start_city
# 2. For each layover, loop through ITS destinations
# 3. Add to possible_destinations if not already there
pass

print(f"Starting from {start_city} with 1 layover, you can reach:")
print(possible_destinations)
```


---

## Puzzle 2: The Shopping Cart Total (Medium)
**The Story**: You have a price list (a dictionary) and a shopping cart (a list of items you want to buy). You need to calculate the total cost of all items in the cart.

**The Question**: If your cart has `["Milk", "Bread", "Milk", "Eggs"]`, what is the total cost based on the prices below?

**Example Test Case**:
- Prices: `{"A": 1, "B": 2}`, Cart: `["A", "A", "B"]` → Total: **4**.

**Hint**: Loop through the `cart` list. for each `item`, look up its price in the `prices` dictionary and add it to a `total` variable.

**Check Your Logic**:
- Milk (2.50) + Bread (1.50) + Milk (2.50) + Eggs (3.00) = **9.50**.

```python
# Starting Code
prices = {
    "Milk":  2.50,
    "Bread": 1.50,
    "Eggs":  3.00,
    "Apple": 0.75
}

cart = ["Milk", "Bread", "Milk", "Eggs"]
total = 0

for item in cart:
    # Look up price and add to total
    pass

print(f"Total cart cost: ${total:.2f}")
```

---

## Puzzle 3: The Temperature Tracker (Medium)
**The Story**: You recorded the high temperature for each day of the week in a dictionary. You want to find the **average** temperature and the **hottest day**.

**The Question**: What was the average temperature for the week, and which day was the hottest?

**Example Test Case**:
- `{"Mon": 20, "Tue": 22}` → Average: **21**, Hottest: **Tue**.

**Hint**: To find the average, sum all values and divide by the count. To find the hottest day, use a "best so far" loop like we did in previous puzzles.

**Check Your Logic**:
- Average: `(18+20+25+22+19+15+17) / 7` ≈ **19.43**.
- Hottest: **Wednesday** (25).

```python
# Starting Code
temps = {
    "Monday":    18,
    "Tuesday":   20,
    "Wednesday": 25,
    "Thursday":  22,
    "Friday":    19,
    "Saturday":  15,
    "Sunday":    17
}

total_temp = 0
hottest_day = ""
max_temp = -100 # Start very low

for day, temp in temps.items():
    # 1. Add to total_temp
    # 2. Check if this is the hottest day so far
    pass

average = total_temp / len(temps)
print(f"Average temperature: {average:.2f}")
print(f"The hottest day was {hottest_day} at {max_temp} degrees.")
```

---

## Puzzle 4: Attendance Checker (Easy–Medium)
**The Story**: You have a list of students who are "Present". You need to check if a list of "Expected" students actually showed up.

**The Question**: For each student in the `expected` list, print whether they are "Present" or "Absent".

**Example Test Case**:
- Present: `["Ali", "Bo"]`, Expected: `["Ali", "Bo", "Cal"]` → Cal is **Absent**.

**Hint**: Use the `in` keyword to check if a name exists in the `present` list: `if name in present:`.

**Check Your Logic**:
- Alice: **Present**
- Bob: **Absent**
- Charlie: **Present**
- Dave: **Absent**

```python
# Starting Code
present = ["Alice", "Charlie", "Eve", "Frank"]
expected = ["Alice", "Bob", "Charlie", "Dave"]

for student in expected:
    # Check if student is in the 'present' list
    if student in present:
        print(f"{student}: Present")
    else:
        print(f"{student}: Absent")
```

---

## Puzzle 5: The Bank Statement (Medium)
**The Story**: A bank statement is a list of transactions. Positive numbers are deposits (+), and negative numbers are withdrawals (-). You want to know your final balance and how many of each type of transaction occurred.

**The Question**: Starting with a balance of `$100`, what is the final balance after the transactions below? How many withdrawals were made?

**Example Test Case**:
- Start: 100, Trans: `[20, -10]` → Balance: **110**, Withdrawals: **1**.

**Hint**: Loop through `transactions`. Add each value to `balance`. If the value is less than 0, increment a `withdrawal_count`.

**Check Your Logic**:
- Balance: 100 + 50 - 20 - 10 + 100 - 40 = **180**.
- Withdrawals: **3** (-20, -10, -40).

```python
# Starting Code
balance = 100
transactions = [50, -20, -10, 100, -40]
withdrawals = 0

for t in transactions:
    # Update balance and count withdrawals
    pass

print(f"Final Balance: ${balance}")
print(f"Number of withdrawals: {withdrawals}")
```

---

## Puzzle 6: Category Spending Tracker (Medium–Hard)
**The Story**: You have a list of transactions, where each transaction is a dictionary containing an "amount" and a "category" (like "Food", "Transport", or "Rent"). You want to know how much you spent in **each** category.

**The Question**: For the transactions below, what is the total spent in the "Food" category? What is the total for "Transport"?

**Example Test Case**:
- `[{"cat": "A", "amt": 10}, {"cat": "A", "amt": 5}]` → `{"A": 15}`.

**Hint**: Create an empty dictionary `totals = {}`. Loop through the `transactions`. For each one, get the category. If the category is **not** in `totals`, add it with the current amount. If it **is** already in `totals`, add the current amount to the existing value.

**Check Your Logic**:
- Food: 20 + 15 = **35**.
- Transport: 10 + 25 = **35**.
- Rent: **500**.

```python
# Starting Code
transactions = [
    {"category": "Food",      "amount": 20},
    {"category": "Transport", "amount": 10},
    {"category": "Food",      "amount": 15},
    {"category": "Rent",      "amount": 500},
    {"category": "Transport", "amount": 25},
]

category_totals = {}

for t in transactions:
    cat = t["category"]
    amt = t["amount"]
    
    # If category not in category_totals, set it to amt
    # Else, add amt to existing category_totals[cat]
    pass

print(f"Spending by category: {category_totals}")
```

