# Object-Oriented Ball Bounce Program  
A tiny Pygame playground that spawns multiple bouncing **Ball** objects (and optional **Drop** objects) using an object-oriented design.  
Press keys during runtime to add more objects and watch them animate.
## Demo Features
- Object-oriented design with `Ball` and `Drop` classes
- Keyboard controls to spawn new objects at runtime
- Fixed timestep loop with configurable FPS
- Lightweight assets (single `images/instructions.jpg` overlay)

## Controls
- **B** — add a new **Ball**
- **D** — add a new **Drop**
- **Window close** — exit

---

## Project Structure
- `main.py` – the game loop (provided below)
- `Ball.py` – defines the `Ball` class with `update()` and `draw()` methods
- `Drop.py` – defines the `Drop` class with `update()` and `draw()` methods
- `images/instructions.jpg` – an overlay shown at the bottom of the window

---

## Requirements
- Python 3.8+
- [Pygame](https://www.pygame.org/news)

### Install
```bash
# (optional) create a virtual environment
python -m venv .venv
# activate it
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# install pygame
pip install pygame

### Run it
python main.py

### Credits
Built with Pygame https://www.pygame.org/news
Author: Tanxin (Tracy) — 2025
