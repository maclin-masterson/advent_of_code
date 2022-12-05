import string


def has_line(file):
    cur_pos = file.tell()
    does_it = bool(file.readline())
    file.seek(cur_pos)
    return does_it

# Initialize point dict
letters = dict.fromkeys(string.ascii_letters)

pv = 1 # point value
for letter in letters:
    letters[letter] = pv
    pv += 1


# read file
with open('day3/input3.txt', 'r') as f:

    more_lines = has_line(f)
    total = 0
    while more_lines:
        lines = []
        for i in range(0,3):
            new_line = f.readline().strip()
            lines.append(new_line)
        
        matches = set(lines[0]) & set(lines[1]) & set(lines[2])
        for match in matches:
            total += letters[match]
        
        more_lines = has_line(f)

print(total)
