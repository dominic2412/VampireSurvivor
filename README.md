# Vampire Survivor

This repository contains a basic project setup for a simple Vampire Survivor style game written in Python using Pygame.

## Directory structure

- `src/` - source code for the game
  - `main.py` - entry point that launches the game window
  - `game/` - package containing game modules such as `player` and `enemy`
- `assets/` - placeholder folder for sprites and sounds
- `tests/` - unit tests

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the game:

```bash
python src/main.py
```

## Gameplay

Use the arrow keys to move the red square representing the player. Blue squares
spawn every second and move slowly toward the player. Colliding with an enemy
ends the game.
