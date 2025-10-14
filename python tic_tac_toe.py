# -------------------------
# Tic Tac Toe - Clean Version
# -------------------------

def print_grid(grid):
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(grid[i][j], "|", end="")
        print()


def check_winner(grid, player_symbol):
    # Rows and Columns
    for i in range(3):
        if all(grid[i][j] == player_symbol for j in range(3)):  # Row check
            return True
        if all(grid[j][i] == player_symbol for j in range(3)):  # Column check
            return True

    # Diagonals
    if all(grid[i][i] == player_symbol for i in range(3)):
        return True
    if all(grid[i][2 - i] == player_symbol for i in range(3)):
        return True

    return False


def is_full(grid):
    return all(grid[i][j] != " " for i in range(3) for j in range(3))


def play_game():
    print("Welcome to Tic-Tac-Toe!\n")

    # Initialize grid
    grid = [[" " for _ in range(3)] for _ in range(3)]

    # Player setup
    player1 = input("Enter name of Player 1: ")
    player1_symbol = input("Enter symbol for Player 1: ")
    player2 = input("Enter name of Player 2: ")
    player2_symbol = input("Enter symbol for Player 2: ")

    print("\nStarting Game!\n")
    print_grid(grid)

    turn_player1 = True

    while True:
        current_player = player1 if turn_player1 else player2
        current_symbol = player1_symbol if turn_player1 else player2_symbol

        print(f"\nIt's {current_player}'s turn ({current_symbol})")

        # Take input
        try:
            cell = int(input("Choose a cell (1–9): "))
            if not (1 <= cell <= 9):
                print("❌ Invalid cell number! Choose between 1–9.")
                continue
        except ValueError:
            print("❌ Please enter a valid number!")
            continue

        # Convert to grid index
        i, j = divmod(cell - 1, 3)

        if grid[i][j] != " ":
            print("❌ That cell is already taken! Try again.")
            continue

        # Make move
        grid[i][j] = current_symbol
        print_grid(grid)

        # Check winner
        if check_winner(grid, current_symbol):
            print(f"\n🏆 {current_player} wins the game!")
            break

        # Check draw
        if is_full(grid):
            print("\nIt's a draw! No more moves left.")
            break

        # Switch turn
        turn_player1 = not turn_player1


# Run the game
if __name__ == "__main__":
    play_game()
