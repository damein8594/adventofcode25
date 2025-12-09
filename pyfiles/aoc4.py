def p1():
    grid = []
    with open("../inputs/input4", "r") as file:
        for line in file:
            line = line.strip()
            line = list(line)
            grid.append(line)

    rows = len(grid)
    cols = len(grid[0])
    checknums = [-1, 0, 1]
    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "@":
                count = 0
                for row in checknums:
                    for column in checknums:

                        if row==0 and column==0:
                            continue

                        nrow = i + row
                        ncolumn = j + column

                        if 0 <= nrow < rows and 0 <= ncolumn < cols:
                            value = grid[nrow][ncolumn]
                            if value == "@":
                                count += 1

                if count < 4:
                    ans += 1

    print(ans)

def p2():
    grid = []
    with open("../inputs/input4", "r") as file:
        for line in file:
            line = line.strip()
            line = list(line)
            grid.append(line)

    rows = len(grid)
    cols = len(grid[0])
    checknums = [-1, 0, 1]
    ans = 0
    change = True
    while change:
        change = False
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "@":
                    count = 0
                    for row in checknums:
                        for column in checknums:

                            if row==0 and column==0:
                                continue

                            nrow = i + row
                            ncolumn = j + column

                            if 0 <= nrow < rows and 0 <= ncolumn < cols:
                                value = grid[nrow][ncolumn]
                                if value == "@":
                                    count += 1

                    if count < 4:
                        ans += 1
                        grid[i][j] = "."
                        change = True


    print(ans)
