#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    """
    Check if it is safe to place a queen at a specific position on the board.

    Args:
        board (list): A list representing the current state of the chessboard.
        row (int): The row index where the queen is to be placed.
        col (int): The column index where the queen is to be placed.

    Returns:
        bool: True if it is safe to place a queen at the given position, False
    otherwise.
    """
    for i in range(col):
        if board[i] == row or board[i] == row - (col - i) or\
           board[i] == row + (col - i):
            return False
    return True


def solve_util(board, col, n, solutions):
    """
    Recursive utility function to solve the N-queens problem.

    Args:
        board (list): A list representing the current state of the chessboard.
        col (int): The current column being considered for queen placement.
        n (int): The size of the board and the number of queens to place.
        solutions (list): A list to store the valid solutions.

    Returns:
        None
    """
    if col >= n:
        solutions.append(board[:])
        return
    for row in range(n):
        if is_safe(board, row, col):
            board[col] = row
            solve_util(board, col + 1, n, solutions)


def solve_nqueens(n):
    """
    Solve the N-queens problem for a given board size.

    Args:
        n (int): The size of the board and the number of queens to place.

    Returns:
        None

    Prints:
        Every possible solution to the N-queens problem, one solution
        per line. The format of each solution is a representation of the
        board configuration.

    Raises:
        ValueError: If `n` is not an integer.
        SystemExit: If `n` is less than 4 or the wrong number of arguments
    is provided.
    """
    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if n < 4:
        print('N must be at least 4')
        sys.exit(1)

    board = [-1] * n
    solutions = []
    solve_util(board, 0, n, solutions)
    for solution in solutions:
        list_t = []
        for i in range(n):
            lists = []
            lists.append(i)
            lists.append(solution[i])
            list_t.append(lists)
        print(list_t)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    solve_nqueens(sys.argv[1])
