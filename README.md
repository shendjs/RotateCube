# Rotating 3D Cube Simulation

This project is a Python application that simulates a rotating 3D cube using the Pygame library. The cube rotates smoothly and demonstrates basic 3D transformations and rendering in a 2D environment.

## Features
- Real-time rendering of a rotating 3D cube.
- Configurable rotation speeds.
- Customizable cube size and colors.
- Lightweight and easy to run on most systems.

## Requirements
- Python 3.8 or higher
- Pygame library

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/shendjs/RotateCube.git
   cd RotateCube
   ```
2. Install the required library:
   ```bash
   pip install pygame
   ```

## Usage
Run the application by executing the Python script:
```bash
python cube.py
```

### Controls
Currently, there are no interactive controls, but the script can be customized by modifying the parameters in the code:
- **Rotation speed**: Adjust the `angle_x`, `angle_y`, and `angle_z` increments in the main loop.
- **Cube size**: Change the `scale` variable.
- **Colors**: Modify the `cube_color` variable.

## File Structure
- `cube.py`: Main script to run the simulation.
- `README.md`: Documentation for the project.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---
