def handle():
    ans = 0
    ranges = []
    numbers = []
    with open("../inputs/input5", "r") as file:
        for line in file:
            if line == "\n":
                continue
            if "-" in line:
                parts = line.split("-")
                low = int(parts[0])
                high = int(parts[1])
                ranges.append((low, high))
            else:
                numbers.append(int(line))

    return ans, numbers, ranges

def p1():
    ans,ranges,numbers = handle()
    for num in numbers:
        for low, high in ranges:
            if low <= num <= high:
                ans += 1
                break

    print(ans)


def p2():
    ans, numbers, ranges = handle()
    availableingrediants = []
    ranges.sort(key=lambda r: r[0])
    merged = []
    c_start, c_end = ranges[0][0], ranges[0][1]

    for i in range(1, len(ranges)):
        start, end = ranges[i][0], ranges[i][1]

        if start <= c_end:
            if end > c_end:
                c_end = end
        else:

            merged.append((c_start, c_end))
            c_start, c_end = start, end


    merged.append((c_start, c_end))

    for ranges in merged:
        diff = ranges[1] + 1 - ranges[0]
        ans+=diff
    print(ans)
