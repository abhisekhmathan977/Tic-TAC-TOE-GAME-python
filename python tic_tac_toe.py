# Function to display the board in a clean format
def show_board(board):
    for row in board:
        print("| " + " | ".join(row) + " |")
    print()


# Function to check if a player has won
def has_won(board, symbol):
    # Check rows
    for r in range(3):
        if board[r] == [symbol, symbol, symbol]:
            return True

    # Check columns
    for c in range(3):
        if board[0][c] == symbol and board[1][c] == symbol and board[2][c] == symbol:
            return True

    # Check diagonals
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        return True

    if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        return True

    return False


# Function to verify if board is full
def board_filled(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True


# Main game function
def start_game():
    print("=== TIC TAC TOE ===\n")

    # Empty 3x3 board
    board = [[" " for _ in range(3)] for _ in range(3)]

    # Player details
    p1_name = input("Player 1 name: ")
    p1_symbol = input("Player 1 symbol: ")

    p2_name = input("Player 2 name: ")
    p2_symbol = input("Player 2 symbol: ")

    print("\nGame Started!\n")
    show_board(board)

    current_player = p1_name
    current_symbol = p1_symbol

    # Actual game loop
    while True:
        print(f"{current_player}'s turn ({current_symbol})")

        # Take user move
        move = input("Enter position (1–9): ")

        if not move.isdigit():
            print("Invalid input. Enter a number from 1 to 9.\n")
            continue

        move = int(move)

        if move < 1 or move > 9:
            print("Choose a number between 1 and 9.\n")
            continue

        row, col = (move - 1) // 3, (move - 1) % 3

        if board[row][col] != " ":
            print("Cell already used. Try again.\n")
            continue

        # Update board
        board[row][col] = current_symbol
        show_board(board)

        # Winner check
        if has_won(board, current_symbol):
            print(f"*** {current_player} wins the match! ***")
            break

        # Draw check
        if board_filled(board):
            print("Match Drawn. Board is full!")
            break

        # Switch player manually with if/else
        if current_player == p1_name:
            current_player = p2_name
            current_symbol = p2_symbol
        else:
            current_player = p1_name
            current_symbol = p1_symbol


# Start the game
start_game()

