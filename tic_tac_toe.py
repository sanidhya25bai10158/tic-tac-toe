import os          # Module 1: Handles the Operating System (screen clearing)
import sys         # Module 2: Handles System exit
import random      # Module 3: Handles Random choices
import time        # Module 4: Handles Time delays
import itertools   # Module 5: Handles iterating/cycling through players

def play():
    
    board = [" " for _ in range(9)]

    winners = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Columns
        (0, 4, 8), (2, 4, 6)             # Diagonals
    )

    # using random module for first play
    starter = random.choice(["X", "O"])
    print(f"Coin toss... {starter} goes first!")

    # addint time delay using time module 
    time.sleep(1.5)

    # to cycle through players we use interools 
    player_cycle = itertools.cycle(["X", "O"])

    if starter == "O":
        next(player_cycle)

    for _ in range(9): 
        current_player = next(player_cycle)

        # using os module for terminal clearing 
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"\n {board[0]} | {board[1]} | {board[2]} ")
        print("---+---+---")
        print(f" {board[3]} | {board[4]} | {board[5]} ")
        print("---+---+---")
        print(f" {board[6]} | {board[7]} | {board[8]} \n")
        print(f"Player {current_player}'s turn.")

        while True:
            try:
                choice = int(input("Enter position (1-9): ")) - 1
                if 0 <= choice <= 8 and board[choice] == " ":
                    board[choice] = current_player
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Please enter a number.")

        for combo in winners:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] == current_player:
 
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"\n {board[0]} | {board[1]} | {board[2]} ")
                print("---+---+---")
                print(f" {board[3]} | {board[4]} | {board[5]} ")
                print("---+---+---")
                print(f" {board[6]} | {board[7]} | {board[8]} \n")

                print(f"Khel khatam: Player {current_player} jeet gaya")

                # using sys to stop the game 
                sys.exit()

    print("Khel khatam: Tie hogya")

if __name__ == "__main__":
    play()