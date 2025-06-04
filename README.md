# Vampire Survivor

This repository contains a basic project setup for a simple Vampire Survivor style game written in Python using Pygame.  It is a very small MVP where enemies spawn over time and the player automatically fires small bullets.

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

Use the arrow keys to move the player.  Enemies spawn from the edges of the
screen and chase you while bullets are fired automatically.  Each defeated enemy
adds to your score displayed in the corner.  Colliding with an enemy ends the
game.
