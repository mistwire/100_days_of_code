# Day 11: Blackjack Game - Game Algorithms & Complex Logic

## What You Learned
Today you built a complete Blackjack game, mastering complex game logic with multiple conditions, state management, and AI decision-making. The key insight is that games require careful sequencing: deal phase → player phase → dealer phase → comparison. You also learned how to handle the Ace's dual nature (11 or 1) and detect special cases like blackjack.

---

## Key Concepts

### 1. Game Phases and Control Flow
Blackjack has distinct phases that must happen in order:

```python
# PHASE 1: INITIAL DEAL (both get 2 cards)
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

# PHASE 2: PLAYER TURN (user hits or stands)
while not is_game_over:
    # Show hand, ask to hit/stand, adjust cards
    if hit_again == 'y':
        user_cards.append(deal_card())

# PHASE 3: DEALER TURN (auto-plays following rules)
while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())

# PHASE 4: COMPARE (determine winner)
print(compare(user_score, computer_score))
```

### 2. Ace Handling (Multi-valued Card)
The Ace is the tricky card - it's worth 11 or 1 depending on situation:

```python
def calculate_score(cards):
    # Try to use Ace as 11
    # If that causes bust (>21), convert to 1 instead
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)  # Now worth 1 instead of 11
    return sum(cards)

# Examples:
# [11, 5] → 11 + 5 = 16 (Ace as 11)
# [11, 10] → 11 + 10 = 21 (Ace as 11) - BLACKJACK
# [11, 10, 5] → 11 + 10 + 5 = 26 > 21, so convert Ace
#            → 1 + 10 + 5 = 16 (Ace as 1)
```

### 3. Blackjack Detection (Special Code)
Blackjack is exactly 21 with exactly 2 cards - it's special because:
- It wins immediately (even beats 21 with 3+ cards)
- It pays extra in real casinos (3:2 instead of 1:1)

Using 0 as a special code:
```python
if sum(cards) == 21 and len(cards) == 2:
    return 0  # Signal "BLACKJACK" with special value

# In game logic:
if user_score == 0:  # User has blackjack
    print("You win!")
elif user_score == 21:  # 21 but not blackjack (3+ cards)
    # Not an immediate win - dealer might also have cards
```

### 4. Dealer AI (Deterministic Rules)
Unlike a real dealer who can bluff, computer dealer follows strict rules:

```python
# Dealer must hit if under 17, stand at 17 or more
while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
```

This is **deterministic** - always the same given the same cards. Real players can deviate (strategic bluffing), but this algorithm is predictable.

### 5. Game State Variables
Tracking multiple pieces of state:

```python
user_cards = []         # Player's hand
computer_cards = []     # Dealer's hand
is_game_over = False    # Loop control

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
```

These variables work together to create the game state at each moment.

### 6. Multiple Exit Conditions
The player turn ends when ANY of these is true:

```python
if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True
# Blackjack (user) OR Blackjack (computer) OR Bust (user)
```

### 7. Win/Loss Comparison Logic
Many conditions to check, in order of priority:

```python
def compare(user_score, computer_score):
    # 1. Check special cases first (blackjack)
    if computer_score == 0:
        return "Computer has blackjack, you lose!"
    elif user_score == 0:
        return "Player has blackjack, you win!"

    # 2. Check bust conditions
    elif user_score > 21:
        return "Player busted, you lose!"
    elif computer_score > 21:
        return "Computer busted, you win!"

    # 3. Compare scores (who's closer to 21)
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"
```

**Order matters!** If you check `user_score > 21` before checking for player blackjack (0), blackjack would never win.

---

## Common Pitfalls

- **Wrong comparison order:** Check special cases (blackjack, bust) BEFORE comparing scores
- **Forgetting Ace conversion:** Ace stays as 11 even after bust, causing wrong scores
- **Only one Ace conversion:** What if player has two Aces? (11 + 11 = 22 → need to convert both)
- **Showing dealer hole card:** Revealing dealer's hole card breaks the game
- **Not checking win conditions correctly:** Player can win by bust if dealer also busts (game logic)
- **Infinite loops:** If dealer AI condition is wrong (e.g., `<=` instead of `<`), game hangs
- **Forgetting player_score must be recalculated:** After hitting, need `user_score = calculate_score(user_cards)` again

---

## Connections to Other Days

| Day | Connection |
|-----|-----------|
| **Day 5** | Random card dealing (random.choice) |
| **Day 7** | Game loop structure and state tracking |
| **Day 10** | Functions with return values (calculate_score, compare) |
| **Day 12** | Global vs local scope (game state) |
| **Day 14+** | Similar game logic (Higher/Lower) |

---

## Before You Move On
Make sure you can:
- [ ] Trace through a game: deal → player hits twice → stand → dealer plays
- [ ] Explain why Ace is 11, but converts to 1 when needed
- [ ] Explain why returning 0 for blackjack is a good design choice
- [ ] List all win/loss conditions in the compare() function
- [ ] Explain the dealer AI rule (must hit under 17)
- [ ] Modify the game rules (e.g., dealer hits on soft 17)

---

## Practice Prompt
**Enhancement Challenge:**
1. Add betting: track player's money and adjust based on wins/losses
2. Modify dealer rule: currently hits on hard 17, make it "hit on soft 17" (Ace counts as 11)
3. Add split: if first two cards match, allow player to split into two hands
4. Add double down: player can double bet and receive exactly one more card
5. Prevent Ace conversion loop: handle multiple Aces correctly

**Soft 17 Example:**
```python
# Soft 17: Has an Ace counting as 11
# [6, 11] = 17 (Ace as 11 is "soft")
# Dealer should hit on soft 17 (might make hand better)

# Hard 17: No Aces, or Aces count as 1
# [10, 7] = 17 (no Aces, "hard")
# Dealer should stand on hard 17
```

**Multi-Ace Handling:**
```python
# [11, 11, 5] = 27 (bust)
# Convert: 1 + 11 + 5 = 17 (one Ace becomes 1)
# But current code only converts once!
# Fix: Use a loop to convert ALL Aces if needed

while 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
```

**Bonus:** Add a hand history/replay: "Deal → Player hits → Dealer shows → Player stands → Dealer plays" as narrated log

**Bonus 2:** Implement split: if first two cards match, player can play two separate hands simultaneously
