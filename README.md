# Vampire Survivor

This repository contains an extremely small proof-of-concept version of a Vampire Survivor style game written with Pygame.

## Directory structure

- `src/` - source code for the game
  - `main.py` - entry point that launches the game window
  - `game/` - basic game objects (`player`, `enemy`, `bullet`, `constants`)
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

Use the arrow keys to move the player. The player automatically shoots projectiles to the right. Enemies spawn from the screen edges and move toward the player. Survive as long as possible and keep track of your score in the top-left corner.
