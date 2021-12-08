# Advent of Code - Day 8
# Part 1


def parseInput():
    entry_list = list([])
    output_list = list([])

    for line in (open("input.txt")):
        line = line.split("|")
        entry_line = line[0].split()
        output_line = line[1].split()
        entry_list.append(entry_line)
        output_list.append(output_line)

    return entry_list, output_list


###### PART 1 ######

n_digits = 0
entry_list, output_list = parseInput()

for output in output_list:
    for val in output:
        if len(val) in [2, 3, 4, 7]:
            n_digits += 1


# 292 too low
print(n_digits)
