grid = []
with open("../inputs/input7", "r") as file:
    for line in file:
        row = []
        line = line.strip()
        for i in range(len(line)):
            row.append(line[i])

        grid.append(row)


rows = len(grid)
cols = len(grid[0])
splits = 0
def p1():
    for row in range(rows):
        for col in range(cols):
            cell = grid[row][col]
            print(cell)
            # print (cell)
            if cell == "S":
                grid[row+1][col] = "|"
            if cell == "|":
                try:
                    if grid[row+1][col] == "^":
                        splits += 1
                        grid[row+1][col-1] = "|"
                        grid[row+1][col+1] = "|"
                    else:
                        grid[row + 1][col] = "|"
                except IndexError:
                    pass


    for row in grid:
        print(row)

for row in range(rows):
    for col in range(cols):
        #look at the cell
        cell = grid[row][col]
        #the start puts a line under it
        if cell == "S":
            grid[row+1][col] = "|"
        # if the cell is a line look under it
        if cell != "." and cell != "^":
            print("current cell: ", cell)
            try:
                print("below cell: ", grid[row+1][col])
                # if the underneither is an arrow make it split
                if grid[row+1][col] == "^":
                    splits += 1
                    #look at down left
                    # if its a . set it to 1
                    if grid[row+1][col-1] == ".":
                        grid[row+1][col-1] = "1"

                    # try change it to an int, add 1,  set back to a string
                    else:
                        try:
                            downleft = int(grid[row + 1][col - 1])
                            downleft += 1
                            grid[row + 1][col - 1] = str(downleft)
                        except:
                            pass


                    #looking at down right
                    downright = grid[row + 1][col + 1]

                    # if its a . set it to 1

                    if downright == ".":
                        grid[row+1][col+1] = "1"

                    # try change it to an int, add 1,  set back to a string
                    else:
                        try:
                            downright = int(downright)
                            downright += 1
                            grid[row + 1][col + 1] = str(downright)
                        except:
                            pass
                #if i dont split check if the cell bellow is an int if it is add 1 else make it a line
                else:
                    belowisint = False
                    #check if its a number
                    try:
                        below = int(grid[row + 1][col])
                        belowisint = True
                    except:
                        pass
                    #if it is add 1
                    if belowisint == True:
                        below += 1
                        grid[row+ 1][col] = str(below)
                    #if not just set to a line
                    else:
                        grid[row + 1][col] = "|"

            except IndexError:
                pass

for row in grid:
    print(row)

ans = 0
for row in range(rows):
    for col in range(cols):
        cell = grid[row][col]
        try:
            cell = int(cell)
            ans += cell
        except:
            pass


print(ans)
# print(splits)