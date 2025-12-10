from pyparsing import empty
from sqlalchemy import column

grid = []
ans = 0
def p1():
    with open('../inputs/input6', 'r') as file:
        for line in file:
            line = line.strip()
            oned_linelist = line.split()
            grid.append(oned_linelist)
    rows = len(grid)
    cols = len(grid[0])

    for col in range(cols):
        multiplier = grid[rows - 1][col]
        numlist = []

        for row in range(rows-1):
            numlist.append(grid[row][col])

        if multiplier == "*":
            coltot = 1
            for num in numlist:
                coltot *= int(num)
            ans += coltot

        else:
            coltot = 0
            for num in numlist:
                coltot += int(num)
            ans += coltot

    print(ans)

grid = []
with open('../inputs/input6', 'r') as file:
    for line in file:
        line = line.rstrip("\n")
        grid.append(list(line))

max_len = max(len(row) for row in grid)
for row in grid:
    while len(row) < max_len:
        row.append(" ")

rows = len(grid)
cols = max_len

columns_to_keep = []
for col in range(cols):
    empty = True
    for row in range(rows):
        if grid[row][col] != " ":
            empty = False
            break
    if not empty:
        columns_to_keep.append(col)


new_grid = []
for row in range(rows):
    new_row = [grid[row][col] for col in columns_to_keep]
    new_grid.append(new_row)

grid = new_grid


for row in grid:
    print(row)

