# Rhythm Reaction Game (Python)

A simple terminal-based rhythm reaction game written in Python.  
The game challenges players to quickly press displayed keys within a time limit, featuring two different modes and multiple difficulty levels.

---

## Game Modes

- Classic Mode  
  Limited to 3 misses.  
  Game ends once all tries are used.  
  Final score is displayed at the end.  

- Timed Mode  
  30-second countdown.  
  Score as many points as possible within the time limit.  

---

## Difficulty Levels

- Easy: 1.5s reaction time, ×1 score multiplier  
- Medium: 1.0s reaction time, ×1.5 score multiplier  
- Hard: 0.7s reaction time, ×2 score multiplier  

---

## Features

- Real-time key press detection (W, A, S, D, Z, X, C)  
- Combo system: consecutive correct presses increase score multiplier  
- Scoring and feedback system with instant response  
- Two modes to test either endurance (Classic) or speed (Timed)  

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yankyang/rhythm-reaction.git
   cd rhythm-reaction
   ## How to Run

2. Run the game
   python main.py
