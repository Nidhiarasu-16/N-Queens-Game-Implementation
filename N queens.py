def is_valid(board, row, col, n):
    """
    Checks if placing a queen at (row, col) is valid.
    Ensures no other queen is in the same column, diagonal left, or diagonal right.
    """
    for i in range(row):
        if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
            return False
    return True


def check_n_queens(board, n):
    """
    Validates the entire board to check if all placed queens satisfy the N-Queens constraints.
    """
    for i in range(n):
        if not is_valid(board, i, board[i], n):
            return False
    return True


def print_board(board, n):
    """
    Prints the current board with 'Q' for queens and '-' for empty spaces.
    """
    print("\nCurrent Board:")
    for i in range(n):
        row = ["Q" if board[i] == j else "-" for j in range(n)]
        print(" ".join(row))


def visualize_board(board, n):
    """
    Visualizes the board in a grid format using 'Q' for queens and '_' for empty spaces.
    """
    print("\nBoard Layout:")
    for i in range(n):
        row = ["Q" if board[i] == j else "_" for j in range(n)]
        print("|" + " | ".join(row) + "|")


def main():
    """
    Main function to execute the N-Queens game.
    - Takes input for board size N
    - Allows player to place queens one by one
    - Visualizes the board after each move
    - Checks if the final placement is correct
    """
    print("Rule : The game environment will be an NxN matrix.")
    print(
        "       Player must place N number of 'Q's , that is, Queens in such a way "
        "   \n       that none of the Queens are present horizontally/vertically/diagonally to one another.")
    n = int(input("Enter the value of N: "))
    board = [-1] * n
    visualize_board(board, n)  # Show initial empty board
    print(f"Place {n} queens on an {n}x{n} board.")

    for i in range(n):
        while True:
            try:
                # Asking user for the position of queen
                row, col = map(int, input(f"Enter row and column for Queen {i + 1} (1 to {n}): ").split())
                if 1 <= row <= n and 1 <= col <= n and board[row - 1] == -1:
                    board[row - 1] = col - 1  # Place queen
                    visualize_board(board, n)  # Show updated board
                    break
                else:
                    print("Invalid position! Try again.")
            except ValueError:
                print("Invalid input! Enter two numbers separated by space.")

    print_board(board, n)  # Final board display
    if check_n_queens(board, n):
        print("Congratulations! You placed the queens correctly.")
    else:
        print("Incorrect placement! Try again.")


if __name__ == "__main__":
    main()
