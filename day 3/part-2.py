from pathlib import Path


fn = Path(".")/"day 3"/"in"
with open(fn, "r") as f:
    grid = f.read().split()

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
        trees += (grid[row][col] == "#")
    
    ans *= trees

print(ans)
