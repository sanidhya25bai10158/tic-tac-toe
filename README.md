# Tic Tac Toe Python

## Overview
This project is an application of the classic **Tic Tac Toe** game, built entirely in Python. It is designed to run in a command-line interface (terminal) environment, focusing on clean logic, user interaction, and efficiency.

This game has a **two-player system** where two users share a single terminal window and keyboard to play. The application manages the game state, validates user inputs, detects win situations, and provides a clean user experience through automatic screen clearing and status updates. It gives an excellent demonstration of Python control flow, list manipulation, and modular programming using the standard library.

## Features
* **Coin Toss Mechanism:** The game uses the `random` module to simulate a coin toss at the start of every session. This ensures that the starting player (Player X or Player O) is chosen fairly and unpredictably, removing the advantage of always going first.
* **Clean and Responsive Interface:** To maintain a clutter-free environment, the game uses the `os` module to detect the operating system and execute the appropriate terminal clear command (`cls` for Windows, `clear` for Unix/Linux/macOS). This makes sure that the board is always generated at the top of the screen after every turn.
* **Robust Input Validation and Error Handling:**
    * **Type Safety:** The game uses `try-except` blocks to catch `ValueError` exceptions, preventing the application from crashing if a user enters non-numeric characters.
    * **Range Checking:** Logic is in place to ensure users select a number strictly between **1 and 9**.
    * **Collision Detection:** The game checks the state of the board before confirming a move, ensuring players cannot use a position that has already been taken.
* **Comprehensive Win Logic:** The game uses a predefined tuple of tuples representing all possible winning combinations. After every move, the game circulates through these combinations to check for a victory state.
* **Tie Detection:** The game tracks the number of moves and the state of the board. If all 9 grid positions are filled without a winning condition being met, the game correctly declares a draw.

## Educational Value
This project serves as a practical example for several core programming concepts:
* **Game Loops:** Implementing a `while` loop that continues until a win or tie is reached.
* **State Management:** Tracking the game board using a list data structure and modifying it based on user input.
* **Exception Handling:** Using `try-except` blocks to handle invalid user input without crashing the program.
* **Iterators:** Utilizing `itertools.cycle` for efficient player turn changing.

## Technologies and Tools Used
The project is built using **Python 3**. It relies exclusively on Python's **standard library**, ensuring portability and removing the need for external package managers like `pip`.

### Standard Modules:
* `os`: Used for cross-platform system capability, specifically to clear the terminal window.
* `sys`: Used to call `sys.exit()` for a clean and immediate program termination when the game is over.
* `random`: Used to generate random choices for the initial player selection.
* `time`: Used to introduce delays.
* `itertools`: Used to create an infinite iterator that cycles between player X and O, simplifying the logic required to switch turns.

## Code Structure and Logic
The entire game logic is encapsulated within a single `play()` function to maintain simplicity.

1.  **Board Representation:** The board is initialized as a list comprehension: `[" " for _ in range(9)]`. This creates a mutable list of 9 empty strings.
2.  **Coordinate Mapping:** The User Interface prompts for input ranging from **1 to 9**. The code adjusts this input (`input - 1`) to map to Python's 0-based list indices (0-8).
3.  **Turn Management:** Rather than using conditional `if-else` statements to swap players, the code creates an iterator `player_cycle = itertools.cycle(["X", "O"])`. Calling `next(player_cycle)` selects the next player automatically.

## Steps to Install and Run

### Prerequisites
* **Python 3.13.7** (or newer) installed on your PC.
* A command-line terminal (Command Prompt, PowerShell, Terminal, or Bash).

### Installation
1.  **Clone the Repository** (or download the source code):
2.  **Navigate to the directory:**
3.  **Verify the script:** Ensure the file `tictactoe.py` is present.

### Running the Game
Execute the script using the Python interpreter:
python tictactoe.py
## Testing Instructions

### Verification Test Cases

To verify the game works as intended, perform the following test cases:

### Initialization Test
- Run the script and observe the "Coin toss..." message
- Confirm that the delay occurs and a starting player is assigned

### Standard Gameplay
- The grid layout corresponds to numbers 1 through 9
- Enter valid numbers and ensure the board updates correctly with X or O

### Edge Case and Error Testing
- **Non-Numeric Input**: Enter a character like A or a symbol like #. The game should catch the error and prompt "Please enter a number."
- **Occupied Cell**: Attempt to choose a number that already has an X or O. The game should display "Invalid move. Try again."
- **Range Error**: Enter 0 or 10. The game should display "Invalid move."

### Termination Tests
- **Win Condition**: Intentionally play a winning line. Verify the "Jeet gaya" message appears and the program exits
- **Tie Condition**: Intentionally fill the board without creating a line. Verify the "Tie hogya" message appears

## Future Improvements

The following features are planned for future releases to enhance the application:

- **Single Player AI**: Implement a Minimax algorithm to allow a single user to play against an unbeatable computer opponent
- **Persistent Scoreboard**: Use file I/O (handling .txt or .json files) to save win/loss records across multiple games
- **Replay Loop**: Encapsulate the main logic in a while True loop to allow players to restart the game immediately without re-running the script
- **Graphical User Interface**: Port the game logic to a GUI framework such as Tkinter or PyGame for a windowed experience

## Screenshots
<img width="477" height="333" alt="Screenshot 2025-11-24 231638" src="https://github.com/user-attachments/assets/8fb8ceb5-db1d-407d-a1fd-7834d560ac5b" />
<img width="503" height="417" alt="Screenshot 2025-11-24 231737" src="https://github.com/user-attachments/assets/8133e444-cbf5-4e76-9793-b99891ca8652" />
<img width="539" height="401" alt="Screenshot 2025-11-24 231814" src="https://github.com/user-attachments/assets/aa4cd500-638c-463b-b97e-38570f3edd06" />

