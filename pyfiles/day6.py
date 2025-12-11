def p1():
    grid = []
    ans = 0
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

def p2():
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

    rows = len(grid) - 1
    cols = len(grid[0])

    for row in grid:
        print(row)

    operators = []
    for c in range(cols - 1, -1, -1):
        if grid[rows][c] != " ":
            operators.append([grid[rows][c], c])

    op_num = 0
    nums = []

    for col in range(cols - 1, -1, -1):

        colnum = ""
        op = operators[op_num][0]
        op_pos = operators[op_num][1]

        for row in range(0,rows):
            cell = grid[row][col]
            if cell != " ":
                colnum += cell

        nums.append(int(colnum))

        if col == op_pos:
            if op == "*":
                subans = 1
                for num in nums:
                    subans *= num
            else:
                subans = 0
                for num in nums:
                    subans += num
            ans += subans
            op_num += 1
            nums = []

    print(ans)

