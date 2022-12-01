elves = []
with open('input1.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

    cals = 0
    for line in lines:
        if line.strip():
            cals += int(line)
        else:
            elves.append(cals)
            cals = 0


sorted_elves = sorted(elves, reverse=True)

print(sum(sorted_elves[0:3]))
