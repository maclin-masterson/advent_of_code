import string

# Initialize point dict
letters = dict.fromkeys(string.ascii_letters)

pv = 1 # point value
for letter in letters:
    letters[letter] = pv
    pv += 1


# read file
with open('day3/input3.txt', 'r') as f:
    lines = f.readlines()
    total = 0
    for line in lines:
        middle = int(len(line)/2)

        first_compartment = line[0:middle]
        second_compartment = line[middle:]

        matches = set(first_compartment) & set(second_compartment)

        for match in matches:
            total += letters[match]

print(total)


#TODO: Find middle of line and split into two compartments
#TODO: find any matching character between two compartments

