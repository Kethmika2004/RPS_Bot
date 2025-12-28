# ⚫📄✂️ Rock Paper Scissors – Intelligent Bot (Python)

A **smart Rock–Paper–Scissors player** that learns, adapts, and wins.
Built to defeat multiple strategies with **≥75% win rate** against every opponent.

---

## 🚀 Project Overview

This project implements an **adaptive Rock–Paper–Scissors bot** in Python that competes against **four different bots**, each with unique play styles.

Unlike random play (≈50% win rate), this bot:

- **Analyzes opponent behavior**
- **Detects patterns**
- **Switches strategies dynamically**
- **Consistently wins 75%+ of games per match**

---

## 🧠 How It Works

The bot is implemented inside the `player()` function in `RPS.py`.

**Key Ideas**:

- 📊 State memory using function arguments
- 🔍 Opponent move tracking
- 🔁 Pattern detection
- 🧪 Multiple strategies, selected based on opponent behavior

The bot adapts its strategy mid-game depending on whether the opponent:

- Repeats moves
- Cycles predictably
- Plays randomly
- Tries to counter your last move

---

## 🗂️ Project Structure

```text
.
├── RPS.py          # 🤖 Main intelligent player logic
├── RPS_game.py     # 🎮 Game engine & opponent bots (don't change)
├── main.py         # 🧪 Local testing playground
└── README.md       # 📘 You are here
```
---

## ▶️ How to Run & Test

Use `main.py` to test your bot against built-in opponents.

**Example Test:**
```python
play(player, quincy, 1000, verbose=True)
```
**Function Signature:**
```python
play(player1, player2, num_games, verbose=False)
```
- `player1`, `player2` → bot functions
- `num_games` → number of rounds
- `verbose=True` → shows every move

---

## 🧪 Strategy Highlights

- 📈 Tracks opponent history
- 🧩 Recognizes repeating & cyclic patterns
- 🔄 Switches counter-strategies dynamically
- 🎯 Exploits predictable bots
- 🎲 Falls back to probabilistic play when needed

---

## 🛠️ Tech Stack

- **Language:** *Python* 🐍

- **Concepts Used:**

  - State persistence
  - Pattern recognition
  - Game theory basics
  - Adaptive algorithms
 
---

## 🌟 Final Thoughts

This project demonstrates how **simple machine-learning ideas** like memory, pattern detection, and adaptation can dramatically outperform randomness—even in a classic game like Rock–Paper–Scissors.

If you like this project, feel free to ⭐ star the repo!
