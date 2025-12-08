######################################################day 1############################################################

######################################################part 1############################################################

def p1():
    ans = 0
    with open("inputs/input3", "r") as file:
        for line in file:
            line = line.strip()
            n = len(line)

            best = -1

            for i in range(n):
                for j in range(i + 1, n):
                    pair = int(line[i] + line[j])
                    if pair > best:
                        best = pair

            ans += best

    print(ans)

########################################################################################################################
######################################################part 2############################################################
def p2():
    ans = 0
    with open("inputs/input3", "r") as file:
        for line in file:
            line = line.strip()
            count = 0
            best = ""
            length = 0
            while length < 12:

                highnum = 0
                highpos = 0
                front = line[:len(line)-(11-length)]
                for j in range(len(front)):
                    if front[j] > str(highnum):
                        highnum = front[j]
                        highpos = j

                best = best + str(front[highpos])
                line = line[highpos+1:]
                length = len(best)
            print(best)
            ans += int(best)
        print(ans)