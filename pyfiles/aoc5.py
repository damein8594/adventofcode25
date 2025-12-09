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

for num in numbers:
    for low, high in ranges:
        if low <= num <= high:
            ans += 1
            break

print(ans)


