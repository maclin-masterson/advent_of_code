
#TODO: create file object


elves = []
with open('day1/input1.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

    cals = 0
    for line in lines:
        if line.strip():
            cals += int(line)
        else:
            elves.append(cals)
            cals = 0


print(max(elves))