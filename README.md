# Space Battle Game

A simple two-player spaceship battle game built using Python and Pygame. Players control spaceships and attempt to shoot each other while avoiding enemy fire. The first player to deplete the other's health wins the game.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Controls](#controls)
- [Assets](#assets)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Two-Player Gameplay:** Control two spaceships on a single keyboard.
- **Bullet Shooting:** Each player can shoot bullets to reduce the opponent's health.
- **Health Display:** Health is displayed at the top of the screen for each player.
- **Winning Screen:** A winning message is displayed when a player wins.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/space-battle-game.git
   cd space-battle-game
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the game assets:**

   Ensure that you have the following assets in the `Assets` directory:
   - `spaceship_yellow.png`
   - `spaceship_red.png`
   - `space2.png`
   - `Grenade+1.mp3`
   - `Gun+Silencer.mp3`

   You can download or create your own assets and place them in the `Assets` directory.

## Usage

To start the game, run the `main.py` file:

```bash
python main.py
```

## Project Structure

The project is structured as follows:

```
space-battle-game/
│
├── Assets/                      # Directory containing game assets
│   ├── spaceship_yellow.png
│   ├── spaceship_red.png
│   ├── space2.png
│   ├── Grenade+1.mp3
│   └── Gun+Silencer.mp3
│
├── config.py                    # Configuration constants for the game
├── assets.py                    # Loading and managing game assets
├── handlers.py                  # Functions to handle movement, bullets, and events
├── utils.py                     # Utility functions for drawing the window and winner
├── main.py                      # Main game loop and entry point
├── requirements.txt             # Python dependencies
└── README.md                    # Project overview and instructions
```

### Controls

- **Yellow Spaceship:**
  - Move Up: `W`
  - Move Down: `S`
  - Move Left: `A`
  - Move Right: `D`
  - Shoot: `Left Ctrl`
  
- **Red Spaceship:**
  - Move Up: `Up Arrow`
  - Move Down: `Down Arrow`
  - Move Left: `Left Arrow`
  - Move Right: `Right Arrow`
  - Shoot: `Right Ctrl`

### Assets

The game uses custom images and sound effects stored in the `Assets` directory. You can replace these files with your own to customize the game's appearance and sound.

### Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue on GitHub if you have any suggestions or improvements.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
