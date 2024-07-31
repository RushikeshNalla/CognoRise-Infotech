#Sudoku Solver

def find_empty_location(grid):

    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None


def is_valid_move(grid, row, col, num):

    if num in grid[row]:
        return False


    for i in range(9):
        if grid[i][col] == num:
            return False


    start_row, start_col = row // 3 * 3, col // 3 * 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(grid):

    empty_location = find_empty_location(grid)
    if not empty_location:
        return True

    row, col = empty_location
    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0

    return False


def print_grid(grid):

    for row in grid:
        print(" ".join(str(num) for num in row))


def main():

    grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    if solve_sudoku(grid):
        print("Sudoku solved successfully!")
        print_grid(grid)
    else:
        print("No solution exists for this Sudoku puzzle.")


if __name__ == "__main__":
    main()

