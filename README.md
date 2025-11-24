# Python Tic Tac Toe

## Overview 

This is a simple Tic Tac Toe game you can play right in the command line (terminal). It’s written in Python and lets two players take turns placing X and O on a 3×3 grid. The goal is straightforward: get three of your symbols in a row—horizontally, vertically, or diagonally—before the other player does. Whoever manages that first wins the game.

## Features

- **Two-Player Mode**: Play against a friend on the same computer.
- **Randomized Start**: A digital coin toss decides whether player X or O goes first.
- **Clean Interface**: The terminal screen clears automatically after every turn to keep the board view clean.
- **Input Validation**: Prevents players from entering invalid numbers or selecting spots that are already taken.
- **Win & Tie Detection**: Automatically detects when a player wins or if the game ends in a draw.

## Tools Used

- **Programming Language**: Python 3.13.7
- **Standard Libraries**:
  - `os` (for clearing the terminal screen)
  - `sys` (for exiting the game)
  - `random` (for the coin toss)
  - `time` (for delays)
  - `itertools` (for player turns)

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
