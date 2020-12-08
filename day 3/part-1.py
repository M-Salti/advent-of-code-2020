from pathlib import Path


fn = Path(".")/"day 3"/"in"
with open(fn, "r") as f:
    grid = f.read().split()

nrows = len(grid)
ncols = len(grid[0])

row, col = 0, 0
trees = 0
while True:
    row, col = row + 1, (col + 3) % ncols
    if row >= nrows:
        break
    trees += (grid[row][col] == "#")

print(trees)
