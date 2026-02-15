# Logic Puzzles: Game Theory (Challenging)
Date: 22nd Feb 2026
Topic: Simulation, Strategy & Randomness

*Three puzzles inspired by classic game theory. Track state, payoffs, and outcomes.*

## Puzzle 1: The Iterated Prisoner's Dilemma
**The Story**: Two suspects are questioned separately every round. Each round, each player can **Cooperate (C)** or **Defect (D)**. The payoffs (points) for each round are:

|               | Other: C | Other: D |
|---------------|----------|----------|
| **You: C**    | 3, 3     | 0, 5     |
| **You: D**    | 5, 0     | 1, 1     |

(First number = your points, second = opponent's.)

- **Player A** uses **Tit-for-Tat**: first round Cooperate; then each round, do whatever the opponent did last round.
- **Player B** uses **Always Defect**: every round, Defect.

**The Question**: Simulate **20 rounds**. Track each player's total score. What are the final scores for Player A and Player B?

**Example Test Case** (first 3 rounds):
- Round 1: A plays C, B plays D → A gets 0, B gets 5.
- Round 2: A (tit-for-tat) copies B's last move → A plays D. B plays D. → A gets 1, B gets 1.
- Round 3: A copies D, B plays D. → A gets 1, B gets 1.
- So after 3 rounds: A = 2, B = 7.

**Hint**: You need variables for `score_a`, `score_b`, and `last_move_b` (what B did last time—B always D, so it's always "D" after round 1). For A you need `last_move_b` to decide A's move. In each round: decide A's move, B's move is always D, then use the payoff table to add points.

**Check Your Logic**:
- After 1 round: A = 0, B = 5.
- After 20 rounds: A = 19, B = 24.

```python
# Starting Code
score_a = 0
score_b = 0
last_move_b = "C"  # Before round 1, we pretend B "cooperated" so A starts with C

for round_num in range(1, 21):
    # 1. A's move: Tit-for-Tat = copy last_move_b
    move_a = last_move_b
    move_b = "D"  # Always Defect

    # 2. Payoffs: (C,C)=3,3  (C,D)=0,5  (D,C)=5,0  (D,D)=1,1
    #    Add the right points to score_a and score_b
    # 3. Update last_move_b for next round (for Tit-for-Tat)
    pass

print(f"Player A (Tit-for-Tat): {score_a} points")
print(f"Player B (Always Defect): {score_b} points")
```

---

## Puzzle 2: The St. Petersburg Lottery
**The Story**: A fair coin is flipped. If it's **Heads** on the 1st flip, you win **1** point and stop. If **Tails**, flip again; if **Heads** on the 2nd flip, you win **2** points and stop. If Tails again, flip again; **Heads** on the 3rd flip wins **4** points, and so on. So **Heads on flip n** pays **2^(n-1)** (1, 2, 4, 8, 16, ...).

**The Question**: Simulate this game **1000 times**. What is the **average** payout per game (total winnings ÷ 1000)?

**Example Test Case** (one game):
- Flip 1: Tails. Flip 2: Tails. Flip 3: Heads → payout = 4. So this game pays 4.

**Hint**: Use `import random`. In one game: loop (or while) flipping until `random.random() < 0.5` (Heads). Count flips; payout = 2**(flips - 1). Add payout to a running total. After 1000 games, average = total / 1000.

**Check Your Logic**:
- Average should be around 5–15 (it varies a lot because of randomness). Run a few times to see.
- If you simulate only 10 games, the average can be very different; 1000 gives a more stable number.

```python
# Starting Code
import random

total_payout = 0
num_games = 1000

for game in range(num_games):
    flips = 0
    # Keep flipping until Heads (random.random() < 0.5 means Heads)
    # Count flips; when you get Heads, payout = 2 ** (flips - 1)  (if 1st flip = 1, 2nd = 2, 3rd = 4)
    # Add payout to total_payout
    pass

average = total_payout / num_games
print(f"Average payout over {num_games} games: {average:.2f}")
```

---

## Puzzle 3: The Ultimatum Game
**The Story**: In each round, a **Proposer** splits 100 coins: they offer the **Responder** some amount from 0 to 100 (the rest they keep). The Responder has a rule: **accept** if the offer is **≥ 40**, otherwise **reject**. If accepted, the Proposer gets (100 - offer) and the Responder gets (offer). If rejected, both get 0.

**The Question**: Simulate **100 rounds**. In each round, the Proposer makes a **random** offer (an integer from 0 to 100). Count how many offers are **accepted** and what the **total coins** received by the Responder are.

**Example Test Case**:
- Offer 35 → Rejected. Proposer 0, Responder 0.
- Offer 40 → Accepted. Proposer 60, Responder 40.
- Offer 50 → Accepted. Proposer 50, Responder 50.

**Hint**: Use `random.randint(0, 100)` for the offer. If `offer >= 40`, add 1 to an `accepted_count` and add `offer` to `responder_total`. Loop 100 times.

**Check Your Logic**:
- About half the random offers will be below 40 (0–39) and half 40–100, so you should see roughly 60–65 accepts out of 100 (since 40–100 is 61 integers).
- Responder total will be the sum of all accepted offers; it will vary each run.

```python
# Starting Code
import random

accepted_count = 0
responder_total = 0

for round_num in range(100):
    offer = random.randint(0, 100)

    # If offer >= 40: accept → count it and add offer to responder_total
    # Otherwise: reject → nothing to add
    pass

print(f"Accepted: {accepted_count} out of 100")
print(f"Responder total coins: {responder_total}")
```
