def overlap(x, y):
    x_0 = int(x[0])
    x_1 = int(x[1])
    y_0 = int(y[0])
    y_1 = int(y[1])

    x_in_y_left = y_0 <= x_0 <= y_1
    x_in_y_right = y_0 <= x_1 <= y_1

    y_in_x_left = x_0 <= y_0 <= x_1
    y_in_x_right = x_0 <= y_1 <= x_1

    overlap = (x_in_y_left or x_in_y_right or y_in_x_left or y_in_x_right)

    return overlap

with open('day4/input4.txt', 'r') as f:
    lines = f.readlines()
    total = 0

    for line in lines:
        line = line.strip()
        ranges = line.split(',')

        assignment_one = ranges[0].split('-')
        assignment_two = ranges[1].split('-')

        if overlap(assignment_one, assignment_two):
            total += 1

print(total)