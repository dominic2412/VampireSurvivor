# Vampire Survivor

This repository contains a basic project setup for a simple Vampire Survivor style game written in Python using Pygame.  It is a very small MVP where enemies spawn over time and the player automatically fires small bullets that can now travel in any direction.

## Directory structure

- `src/` - source code for the game
  - `main.py` - entry point that launches the game window
  - `game/` - package containing game modules such as `player` and `enemy`
- `assets/` - placeholder folder for sprites and sounds
- `tests/` - unit tests

## Setup

Install dependencies. Using `python -m pip` ensures the packages install into the
same interpreter you will use to launch the game:

```bash
python -m pip install -r requirements.txt
```

Run the game:

```bash
python src/main.py
```

Use the arrow keys to move the player.  Enemies spawn from the edges of the
screen and chase you while bullets are fired automatically.  Each defeated enemy
adds to your score displayed in the corner.  The player starts with three health
points. Colliding with an enemy removes one health; the game ends when your
health reaches zero.

Yellow power-ups occasionally appear and restore one health when collected.
Blue power-ups grant a temporary shield that prevents damage for a few seconds.
Orange power-ups briefly boost your movement speed, shown with a timer when active.
Pink power-ups activate a triple-shot mode letting you fire three bullets at once for a short time.
Light-blue power-ups slow all enemies for a few seconds, displayed with its own timer.
Purple power-ups let your bullets pierce through enemies for a few seconds.
Gold power-ups cause bullets to home in on the nearest enemy for a short time, letting you attack foes in any direction.
Silver power-ups temporarily increase the speed of your bullets, displayed with its own timer.
Magenta power-ups permanently raise your maximum health by one and heal you.


Enemy spawn frequency increases slightly as you rack up kills, but the game is
still very minimal.
Press the `P` key to pause or resume. After your score reaches 10, faster blue
enemies sometimes appear to keep things interesting. Once you hit a score of 20,
larger dark-red enemies spawn that take several hits before they go down. When
your score climbs above 30, bullets fire a little faster, and after score 40,
a huge purple boss enemy occasionally appears and requires even more hits to
defeat.
While a shield is active, the remaining time in seconds is displayed below your
health counter.
