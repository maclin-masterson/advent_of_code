def contained(x, y):
    x_0 = int(x[0])
    x_1 = int(x[1])
    y_0 = int(y[0])
    y_1 = int(y[1])
    x_in_y = x_0 >= y_0 and x_1 <= y_1
    y_in_x = y_0 >= x_0 and y_1 <= x_1

    contained = x_in_y or y_in_x
    return contained

with open('day4/input4.txt', 'r') as f:
    lines = f.readlines()
    total = 0

    for line in lines:
        line = line.strip()
        ranges = line.split(',')

        assignment_one = ranges[0].split('-')
        assignment_two = ranges[1].split('-')

        if contained(assignment_one, assignment_two):
            total += 1

print(total)