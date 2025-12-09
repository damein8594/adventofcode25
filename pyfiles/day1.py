######################################################day 1############################################################

#####################################################part 1############################################################
def p1():
    with open('../inputs/input1', 'r') as file:
        num = 50
        ans = 0
        for line in file:
            line = line.strip()
            if line[0] == "L":
                num -= int(line[1:])
            else:
                num += int(line[1:])


            while num > 99 or num < 0:
                if num >= 100:
                    num -= 100
                elif num < 0:
                    num += 100

            if num == 0:
                ans += 1


    print(ans)
########################################################################################################################
######################################################part 2############################################################
def p2():
    with open('../inputs/input1', 'r') as file:
        num = 50
        ans = 0
        for line in file:
            line = line.strip()
            direction = line[0]
            distance = int(line[1:])

            old = num
            laps = distance // 100
            distance = distance % 100
            ans += laps



            if direction == "L":
                num -= distance
            else:
                num += distance


            if num >= 100:
                num -= 100
                ans += 1
            elif num < 0:
                num += 100
                ans += 1


            print(f"line:{line}")
            print(f"laps:{laps}")
            print(f"distance:{distance}")
            print(f"num:{num}")
            print(f"ans:{ans}")


            num = 50
            ans = 0
            for line in file:
                line = line.strip()
                direction = line[0]
                distance = int(line[1:])

                old = num

                if direction == "L":
                    num -= distance
                else:
                    num += distance

                # count zero crossings
                # each time we go below 0 or >= 100, it counts as crossing
                while num >= 100:
                    num -= 100
                    ans += 1
                while num < 0:
                    num += 100
                    ans += 1

            print(ans)

    print(ans)