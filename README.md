# Open-World Map Simulation — Python and C++ prototypes

A small 2D open-world map simulation inspired by large city game environments. The repository contains two separate prototype implementations.

## Implementations
- `gtav.py` — Python implementation using Pygame
- `gtavcpp.cpp` — C++ implementation using SDL2

The Python source creates a large scrolling world with roads, buildings, trees, vehicles and a player-controlled camera/world view. The C++ source is an SDL2 prototype and may require additional build setup.

## Python version: requirements and run
Requirements:
- Python 3.9 or newer
- Pygame

```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows PowerShell
.venv\\Scripts\\Activate.ps1
python -m pip install pygame
python gtav.py
```

## C++ version
The C++ prototype includes SDL2 headers. Install the SDL2 development package for your operating system, then compile with the appropriate SDL2 compiler and linker flags. A portable build command is not yet provided in this repository.

## Scope
This is an educational 2D simulation prototype, not a complete GTA V map, navigation service or production game. It does not use official GTA V assets or provide real-world map data.

## Next improvements
- Add a documented C++ build configuration
- Separate world data, rendering and input handling
- Add reproducible world generation and configuration
- Add tests for camera bounds and world-coordinate calculations
