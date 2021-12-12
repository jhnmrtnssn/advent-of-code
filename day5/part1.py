# Advent of Code - Day 5
# Part 1
import numpy as np


def parseInput():
    x1 = list([])
    y1 = list([])
    x2 = list([])
    y2 = list([])

    for line in open("input.txt"):
        line = line.strip().split()
        p1 = line[0].split(",")
        p2 = line[2].split(",")
        x1.append(int(p1[0]))
        y1.append(int(p1[1]))
        x2.append(int(p2[0]))
        y2.append(int(p2[1]))

    return x1, y1, x2, y2


def markMap(line_map, x1, y1, x2, y2):
    if x1 == x2:
        if y1 < y2:
            start_y = y1
            stop_y = y2
        else:
            start_y = y2
            stop_y = y1
        for y in range(start_y, stop_y+1):
            line_map[x1, y] += 1

    elif y1 == y2:
        if x1 < x2:
            start_x = x1
            stop_x = x2
        else:
            start_x = x2
            stop_x = x1
        for x in range(start_x, stop_x+1):
            line_map[x, y1] += 1


    return line_map


#######  PART 1  #######

x1, y1, x2, y2 = parseInput()
line_map = np.zeros([1000, 1000])
for i, _ in enumerate(x1):
    line_map = markMap(line_map, x1[i], y1[i], x2[i], y2[i])

n_intersections = 0
for row in line_map:
    for elem in row:
        if elem > 1:
            n_intersections += 1

print(n_intersections)
