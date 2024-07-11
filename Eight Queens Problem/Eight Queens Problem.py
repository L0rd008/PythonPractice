import itertools

class Chessboard:
    def __init__(self, size):
        self.size = size
        self.board = [[0] * size for _ in range(size)]

    //check if a position (row, col) is safe for placing a queen
    def is_safe(self, row, col):
        //check this row on left side
        for i in range(col):
            if self.board[row][i] == 1:
                return False
        //check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False
        //check lower diagonal on left side
        for i, j in zip(range(row, self.size, 1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False
        return True

    //place a queen at position (row, col)
    def place_queen(self, row, col):
        self.board[row][col] = 1

    //remove a queen from position (row, col)
    def remove_queen(self, row, col):
        self.board[row][col] = 0

    //print the current state of the board
    def print_board(self):
        for row in self.board:
            print(' '.join('Q' if cell == 1 else '.' for cell in row))
        print()

//recursive function to solve the n-queens problem
def solve_n_queens(board, col, solutions):
    if col >= board.size:
        solutions.append([row.index(1) for row in board.board])
        return
    for i in range(board.size):
        if board.is_safe(i, col):
            board.place_queen(i, col)
            solve_n_queens(board, col + 1, solutions)
            board.remove_queen(i, col)

//find and print all possible solutions for the n-queens puzzle
def find_queen_placements(size):
    board = Chessboard(size)
    solutions = []
    solve_n_queens(board, 0, solutions)
    for idx, solution in enumerate(solutions, 1):
        print(f"Solution {idx}")
        board.board = [[0] * size for _ in range(size)]
        for col, row in enumerate(solution):
            board.place_queen(row, col)
        board.print_board()

if __name__ == "__main__":
    board_size = 8
    find_queen_placements(board_size)
