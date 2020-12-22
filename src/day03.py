from typing import List


def read_input(fn: str):
    with open(fn, "r") as f:
        return f.read().split()


def count_trees(grid: List[str]) -> int:
    nrows = len(grid)
    ncols = len(grid[0])

    row, col = 0, 0
    trees = 0
    while True:
        row, col = row + 1, (col + 3) % ncols
        if row >= nrows:
            break
        trees += grid[row][col] == "#"

    return trees


def count_trees_all_slopes(grid: List[str]) -> int:
    nrows = len(grid)
    ncols = len(grid[0])

    ans = 1
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for dc, dr in slopes:
        row, col = 0, 0
        trees = 0
        while True:
            row, col = row + dr, (col + dc) % ncols
            if row >= nrows:
                break
            trees += grid[row][col] == "#"

        ans *= trees

    return ans


assert count_trees(read_input("sample/day03.txt")) == 7
assert count_trees_all_slopes(read_input("sample/day03.txt")) == 336

print(count_trees(read_input("input/day03.txt")))
print(count_trees_all_slopes(read_input("input/day03.txt")))
