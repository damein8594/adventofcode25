######################################################day 1############################################################
ans = 0
filelist = []


######################################################part 1############################################################# with open('inputs/input2', 'r') as file:
with open('inputs/input2', 'r') as file:
    for line in file:
        oned_filelist = line.split(",")
    print(oned_filelist)
    for item in oned_filelist:
        start,end = item.split("-")
        filelist.append([int(start), int(end)])
    print(filelist)
    for _range in filelist:
        rangelist = []
        for i in range(_range[0],_range[1]+1,1):
            rangelist.append(i)
        for num in rangelist:
            num = str(num)
            mid = len(num) // 2
            left = num[:mid]
            right = num[mid:]
            if left == right:
                print(num)
                ans += int(num)

    print(ans)

########################################################################################################################
######################################################part 2############################################################
with open('inputs/input2', 'r') as file:
    for line in file:
        oned_filelist = line.split(",")
    print(oned_filelist)
    for item in oned_filelist:
        start,end = item.split("-")
        filelist.append([int(start), int(end)])
    print(filelist)
    for _range in filelist:
        rangelist = []
        for i in range(_range[0],_range[1]+1,1):
            rangelist.append(i)
        for num in rangelist:
            num = str(num)
            length = len(num)
            for i in range(1,length):
                if length % i == 0:
                    block = num[:i]
                    repeated = block * (length//i)
                    if repeated == num and (length//i) >= 2:
                        ans+=int(num)
                        break

    print(ans)