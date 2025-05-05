#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] != " " and row.count(row[0]) == len(row):
            return True

    # Check columns
    for col in range(3):
        if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:
            return True

    # Check diagonals
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return True

    return False

def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"
    move_count = 0

    while True:
        print_board(board)

        # Draw if all 9 moves have been made
        if move_count == 9:
            print("It's a draw!")
            break

        # Read and validate user input
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
        except ValueError:
            print("Invalid input. Please enter integers 0, 1, or 2.")
            continue

        if not (0 <= row < 3 and 0 <= col < 3):
            print("Coordinates out of range. Must be 0, 1, or 2.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # Make move
        board[row][col] = player
        move_count += 1

        # Win check
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Switch player
        player = "O" if player == "X" else "X"

    print("Game over.")

if __name__ == "__main__":
    tic_tac_toe()
