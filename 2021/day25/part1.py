# Advent of Code - Day 25
# Part 1


def parseInput(file):
    full_map = []
    for line in open(file):
        map_line = []
        for char in line.strip():
            map_line.append(char)
        full_map.append(map_line)
    return full_map


def next_pos(full_map, direction, pos):
    max_x = len(full_map)-1
    max_y = len(full_map[0])-1
    x = pos[0]
    y = pos[1]
    if direction == ">":
        if y == max_y:
            new_pos = (x, 0)
        else:
            new_pos = (x, y+1)
    elif direction == "v":
        if x == max_x:
            new_pos = (0, y)
        else:
            new_pos = (x+1, y)
    else:
        return False
    return new_pos


def can_move(full_map, direction, pos):
    new_pos = next_pos(full_map, direction, pos)
    if full_map[new_pos[0]][new_pos[1]] == ".":
        return True
    return False


def get_all_cucumbers(full_map):
    east_cucumbers = []
    south_cucumbers = []
    for row, line in enumerate(full_map):
        for col, value in enumerate(line):
            if value == ">":
                east_cucumbers.append((row, col))
            if value == "v":
                south_cucumbers.append((row, col))
    return east_cucumbers, south_cucumbers


def get_all_moving_cucumbers(full_map):
    east_cucumbers, south_cucumbers = get_all_cucumbers(full_map)
    east_moving = []
    south_moving = []

    # Check all east cucumbers
    for cuc in east_cucumbers:
        if can_move(full_map, ">", cuc):
            east_moving.append(cuc)

    # Check all south cucumbers
    for cuc in south_cucumbers:
        if can_move(full_map, "v", cuc):
            south_moving.append(cuc)

    return east_moving, south_moving


def step(full_map):
    east_moving, _ = get_all_moving_cucumbers(full_map)

    # Check all east cucumbers
    for cuc in east_moving:
        next_cuc = next_pos(full_map, ">", cuc)
        full_map[cuc[0]][cuc[1]] = "."
        full_map[next_cuc[0]][next_cuc[1]] = ">"

    _, south_moving = get_all_moving_cucumbers(full_map)

    # Check all east cucumbers
    for cuc in south_moving:
        next_cuc = next_pos(full_map, "v", cuc)
        full_map[cuc[0]][cuc[1]] = "."
        full_map[next_cuc[0]][next_cuc[1]] = "v"

    return full_map


# ----- Part 1 ----- #

full_map = parseInput("input.txt")
steps = 0

while True:
    steps += 1
    east_cucs, south_cucs = get_all_moving_cucumbers(full_map)
    if not east_cucs and not south_cucs:
        print(steps+1)
        break
    full_map = step(full_map)
