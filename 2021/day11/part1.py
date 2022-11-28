# Advent of Code - Day 11
# Part 1


def parseInput():
    full_map = []
    for line in open("input.txt"):
        line_map = []
        for number in line.strip():
            line_map.append(int(number))
        full_map.append(line_map)
    return full_map


def increaseNumber(num, is_boomed):
    if num == 0:
        if is_boomed:
            return 0
        return num+1

    elif num == 9:
        return 0
    return num+1


def increaseAll(octopus_map):
    is_boomed = False
    for x, line in enumerate(octopus_map):
        for y, _ in enumerate(line):
            octopus_map[x][y] = increaseNumber(octopus_map[x][y], is_boomed)
    return octopus_map


def getflashRange(x, y, max_x, max_y):
    if x == 0:
        range_x = [x, x+1]
    elif x == max_x:
        range_x = [x-1, x]
    else:
        range_x = [x-1, x, x+1]

    if y == 0:
        range_y = [y, y+1]
    elif y == max_y:
        range_y = [y-1, y]
    else:
        range_y = [y-1, y, y+1]

    return range_x, range_y


def findAllFlashed(octopus_map):
    boom_list = []
    for x, line in enumerate(octopus_map):
        for y, _ in enumerate(line):
            if octopus_map[x][y] == 0:
                boom_list.append([x, y])
    return boom_list


def boom(octupus_map, posx, posy):
    is_boomed = True
    max_x = len(octupus_map[0])-1
    max_y = len(octupus_map)-1

    range_x, range_y = getflashRange(posx, posy, max_x, max_y)
    for x in range_x:
        for y in range_y:
            octupus_map[x][y] = increaseNumber(octupus_map[x][y], is_boomed)
    return octupus_map


def step(octopus_map):
    prev_boom_list = []
    octopus_map = increaseAll(octopus_map)
    boom_list = findAllFlashed(octopus_map)
    while len(boom_list) > len(prev_boom_list):
        newly_boomed_list = [item for item in boom_list if item not in prev_boom_list]
        prev_boom_list = boom_list
        for flash in newly_boomed_list:
            octopus_map = boom(octopus_map, flash[0], flash[1])
        boom_list = findAllFlashed(octopus_map)
    return octopus_map, len(boom_list)


octopus_map = parseInput()
n_boomed = 0
for _ in range(0, 100):
    octopus_map, n_new_boomed = step(octopus_map)
    n_boomed += n_new_boomed

print(n_boomed)
