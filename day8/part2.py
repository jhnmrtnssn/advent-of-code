# Advent of Code - Day 8
# Part 2


def parseInput():
    entry_list = list([])
    output_list = list([])

    for line in open("input.txt"):
        line = line.split("|")
        entry_line = line[0].split()
        output_line = line[1].split()
        entry_list.append(entry_line)
        output_list.append(output_line)

    return entry_list, output_list


def mapSignals(input):

    mapping = [None] * 10

    # Divide signals by their lengths
    signal_235 = []
    for val in input:
        if len(val) == 5:
            signal_235.append(val)

    signal_069 = []
    for val in input:
        if len(val) == 6:
            signal_069.append(val)

    # Find signals for 1, 4, 7, 8
    for val in input:
        if len(val) == 2:
            mapping[1] = val
        if len(val) == 3:
            mapping[7] = val
        if len(val) == 4:
            mapping[4] = val
        if len(val) == 7:
            mapping[8] = val

    # Find mapping for 9 (4, (069))
    for val in signal_069:
        match = True
        for letter in mapping[4]:
            if not letter in val:
                match = False
        if match:
            mapping[9] = val

    # Find mapping for 3 (1, (235))
    for val in signal_235:
        match = True
        for letter in mapping[1]:
            if not letter in val:
                match = False
        if match:
            mapping[3] = val

    # Find mapping for 0 and 6 (7, (069))
    for val in signal_069:
        match = True
        if val == mapping[9]:
            continue
        for letter in mapping[7]:
            if not letter in val:
                mapping[6] = val
                match = False
        if match:
            mapping[0] = val

    # Find mapping for 2 and 5 (9, (235))
    for val in signal_235:
        match = True
        if val == mapping[3]:
            continue
        for letter in val:
            if not letter in mapping[9]:
                mapping[2] = val
                match = False
        if match:
            mapping[5] = val

    return(mapping)


def mapDigit(mapping, digit):
    for val in mapping:
        match = True
        if len(digit) == len(val):
            for letter in digit:
                if not letter in val:
                    match = False
            if match:
                return(mapping.index(val))


###### PART 2 ######

#test_input = ["acedgfb", "cdfbe", "gcdfa", "fbcad", "dab", "cefabd", "cdfgeb", "eafb", "cagedb", "ab"]
#test_output = ["cdfeb", "fcadb", "cdfeb", "cdbaf"]


entry_list, output_list = parseInput()
val = 0

for line, entry in enumerate(entry_list):
    mapping = mapSignals(entry)

    for id, digit in enumerate(output_list[line]):
        if id == 0:
            val += 1000 * mapDigit(mapping, digit)
        if id == 1:
            val += 100 * mapDigit(mapping, digit)
        if id == 2:
            val += 10 * mapDigit(mapping, digit)
        if id == 3:
            val += mapDigit(mapping, digit)

print(val)
