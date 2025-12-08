total = 0

with open('inputs/input3', 'r') as file:
    for line in file:
        # best = line.strip()
        #
        # total = 0
        # count = -1
        # difference = 0
        # while len(best) > 12:
        #     count += 1
        #     highnum = -1
        #     highpos = -1
        #     for i in range(count,len(best)-1):
        #         if count == 12:
        #             best = best[:12]
        #             break
        #         elif not i < count:
        #             num = best[i]
        #             if num > str(highnum):
        #                 highpos = i
        #                 highnum = num
        #
        #             if i == len(best)-(12+count):
        #                 best = best[len(best)-(12+count):]
        #                 best = best[highpos:]
        #                 break
        #             if highpos > len(best)-12:
        #                 best = best[:highpos]
        #                 lowestnum = 0
        #                 while len(best) > 12:
        #                     for k in range(len(best)-11):
        #                         if best[k] == lowestnum:
        #                             temp = best
        #                             best = temp[:k] + temp[k+1:]
        #                             break
        #                     lowestnum += 1
        # print(best)
        #


        line = line.strip()
        count = 0
        while count <12:
            highnum = 0
            highpos = 0
            best = ""
            print(line)
            front =line[count:len(line)-(12-count)]
            end = line[len(line)-(12-count):]
            print(front)
            print(end)
            for j in range(len(front)):
                if front[j] >= str(highnum):
                    highnum = line[j]
                    highpos = j
            line = line[highpos+1:]
            count += 1
        print(best)