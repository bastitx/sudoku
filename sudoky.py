import numpy as np


class SudokuSolver():
    def __init__(self, grid):
        self.grid = np.array(grid)
        self.solutions = []

    def possible(self, x, y, n):
        if not ((self.grid[x] == n).any() or (self.grid[:, y] == n).any()):
            x_ = (x//3)*3
            y_ = (y//3)*3
            if not (self.grid[x_:x_+3, y_:y_+3] == n).any():
                return True
        return False

    def solve(self):
        for x in range(9):
            for y in range(9):
                if self.grid[x, y] == 0:
                    for n in range(1, 10):
                        if self.possible(x, y, n):
                            self.grid[x, y] = n
                            self.solve()
                            self.grid[x, y] = 0
                    return
        self.solutions += [np.array(self.grid)]
        return


def main():
    agrid = np.array([[0, 0, 8, 4, 3, 0, 0, 0, 0],
                      [0, 0, 1, 0, 5, 2, 0, 0, 0],
                      [7, 2, 3, 8, 0, 0, 0, 0, 0],
                      [2, 0, 4, 0, 0, 0, 0, 0, 0],
                      [6, 0, 0, 9, 0, 1, 0, 0, 5],
                      [0, 0, 0, 0, 0, 0, 9, 0, 6],
                      [0, 0, 0, 0, 0, 5, 3, 4, 2],
                      [0, 0, 0, 2, 8, 0, 7, 0, 0],
                      [0, 0, 0, 0, 7, 4, 5, 0, 0]])
    '''agrid = np.array([[0, 0, 0, 0, 0, 5, 3, 9, 0],
                      [0, 9, 4, 3, 0, 7, 5, 8, 1],
                      [0, 5, 0, 0, 0, 0, 0, 4, 2],
                      [6, 0, 0, 0, 0, 4, 0, 7, 0],
                      [5, 0, 0, 6, 0, 9, 0, 0, 3],
                      [0, 4, 0, 1, 0, 0, 0, 0, 8],
                      [1, 3, 0, 0, 0, 0, 0, 2, 0],
                      [4, 8, 9, 7, 0, 2, 1, 6, 0],
                      [0, 6, 2, 8, 0, 0, 0, 0, 0]])'''
    solver = SudokuSolver(agrid)
    solver.solve()
    for s in solver.solutions:
        print(s)


if __name__ == "__main__":
    main()
