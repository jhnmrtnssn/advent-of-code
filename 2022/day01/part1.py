# Advent of Code - Day 1
# Part 2


def parse_input(file):
    full_map = []
    for line in open(file):
        map_line = []
        for char in line.strip():
            map_line.append(char)
        full_map.append(map_line)
    return full_map
