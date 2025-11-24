# Project Statement: Python Tic-Tac-Toe

## Problem Statement

In digital environments, users often seek quick, lightweight forms of entertainment to pass time or simple methods to make binary decisions (similar to flipping a coin) without requiring physical materials like pen and paper. While many complex games exist, there is a need for a minimalist, distraction-free strategy game that runs natively in a developer's primary workspace—the command line—without requiring heavy installations, internet access, or graphical user interfaces.

## Scope of the Project

The scope of this project is limited to a text-based console application.

### In Scope:
- Implementation of the standard 3x3 grid Tic-Tac-Toe rules
- Local multiplayer functionality (Hotseat: two players sharing one keyboard)
- Basic command-line interface (CLI) visualization
- Input validation and game state management (win/loss/draw detection)

### Out of Scope:
- Artificial Intelligence (AI) or single-player mode against the computer
- Networked multiplayer over the internet or LAN
- Graphical User Interface (GUI) using libraries like PyGame or Tkinter
- Persistent data storage (leaderboards or save files)

## Target Users

- **Developers & Programmers**: Individuals who spend significant time in the terminal and want a quick, low-resource diversion
- **Python Students**: Beginners looking for a clear, readable example of game logic, list manipulation, and control flow
- **Casual Gamers**: Users looking for a classic game that requires no setup or internet connection
- **Educators**: Teachers requiring a simple codebase to demonstrate basic programming concepts such as loops, exception handling, and standard library usage (os, random, sys)

## High-Level Features

- **Randomized First Mover**: Utilizes a digital coin toss (random module) to fairly decide whether Player X or Player O starts the game
- **Dynamic Interface**: Features a self-clearing terminal display (os module) that refreshes the board after every move, ensuring the game remains visually clean and easy to follow
- **Robust Input Handling**: Includes error catching to handle non-numeric inputs or out-of-bound coordinates, preventing the application from crashing due to user error
- **Win Condition Logic**: Automatically checks rows, columns, and diagonals after every turn to declare a winner or identify a stalemate (tie) immediately
