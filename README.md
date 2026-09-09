# Asteroids

A small Asteroids-style game built with Python and Pygame.

## Requirements

- Python 3.13 or newer
- [uv](https://docs.astral.sh/uv/)

## Run the game

From the project directory:

```bash
uv sync
uv run main.py
```

The game opens a 1280x720 window and runs at 60 FPS.

## Controls

| Key | Action |
| --- | --- |
| `A` | Rotate left |
| `D` | Rotate right |
| `W` | Move forward |
| `S` | Move backward |
| `Space` | Fire |
| Close window | Quit |

## Gameplay

- Asteroids spawn continuously from the edges of the screen.
- Shooting an asteroid destroys it and splits larger asteroids into smaller ones.
- The player loses when colliding with an asteroid.
- Shots have a short cooldown to limit the firing rate.

## Project structure

- `main.py` - Initializes Pygame, creates sprite groups, and runs the game loop.
- `player.py` - Player movement, rotation, and shooting.
- `asteroid.py` - Asteroid movement, drawing, collision splitting, and removal.
- `asteroidfield.py` - Timed asteroid spawning.
- `shot.py` - Projectile behavior.
- `circleshape.py` - Shared circular sprite and collision logic.
- `constants.py` - Screen size, movement speeds, radii, and gameplay settings.
- `logger.py` - Writes periodic state snapshots and gameplay events.

## Logs

While the game runs, it writes diagnostic data to:

- `game_state.jsonl` - Periodic snapshots of sprite positions and velocities.
- `game_events.jsonl` - Collision and asteroid-splitting events.
