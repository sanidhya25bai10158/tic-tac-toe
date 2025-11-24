# Python Tic-Tac-Toe

## Overview of the Project

This is a simple, command-line implementation of the classic Tic-Tac-Toe game built using Python. Two players take turns marking spaces in a 3x3 grid (using X and O). The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner.

## Features

- **Two-Player Mode**: Play against a friend on the same computer.
- **Randomized Start**: A digital "coin toss" decides whether X or O goes first.
- **Clean Interface**: The screen clears automatically after every turn to keep the board view clean.
- **Input Validation**: Prevents players from entering invalid numbers or selecting spots that are already taken.
- **Win & Tie Detection**: Automatically detects when a player wins or if the game ends in a draw.

## Technologies/Tools Used

- **Programming Language**: Python 3.x
- **Standard Libraries**:
  - `os` (for clearing the terminal screen)
  - `sys` (for exiting the game)
  - `random` (for the coin toss logic)
  - `time` (for user experience delays)
  - `itertools` (for cycling player turns)

## Steps to Install & Run the Project

1. **Prerequisites**: Ensure you have Python installed on your machine. You can check this by typing `python --version` in your terminal.
2. **Download**: Save the provided Python code into a file named `tic_tac_toe.py`.
3. **Run the Game**:
   Open your terminal or command prompt, navigate to the folder where you saved the file, and run:

   ```bash
   python tic_tac_toe.py
## References

*   [**freeCodeCamp's Tic-Tac-Toe Project**](https://github.com/freeCodeCamp/boilerplate-tic-tac-toe/) - A foundational boilerplate for building Tic-Tac-Toe, often used in curricula.
*   [**knightdave/tic_tac_toe.py**](https://gist.github.com/knightdave/1c4b0f722d8e7f5e6e8a27d3b55c3a47) - A clean, well-documented command-line Tic-Tac-Toe game in Python.
*   [**Ascii Tic-Tac-Toe by donno2048**](https://github.com/donno2048/tic-tac-toe) - A simple terminal-based game with an ASCII interface, similar to this project.
