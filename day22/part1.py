# Advent of Code - Day 21
# Part 1

import numpy as np

def parseInput(file):
    instructions = []
    for line in open(file):
        inst_line = []
        raw_input = line.strip().split(" ")
        x_dim = raw_input[1].split("=")[1].split("..")
        x_dim[1] = x_dim[1].split(",")[0]
        y_dim = raw_input[1].split("=")[2].split("..")
        y_dim[1] = y_dim[1].split(",")[0]
        z_dim = raw_input[1].split("=")[3].split("..")

        inst_line.append(raw_input[0])
        inst_line.append([int(x_dim[0]), int(x_dim[1])])
        inst_line.append([int(y_dim[0]), int(y_dim[1])])
        inst_line.append([int(z_dim[0]), int(z_dim[1])])
        instructions.append(inst_line)

    # [on/off, xdim, ydim, zdim]
    return instructions


# ----- Part 1 ----- #

instructions = parseInput("input.txt")
offset = 50
cuboid = np.zeros((101, 101, 101), dtype=int)
for i, instruction in enumerate(instructions):
    if i < 20:
        if instruction[0] == "on":
            set_value = 1
        else:
            set_value = 0
        x_dim = (instruction[1][0] + offset, instruction[1][1] + offset)
        y_dim = (instruction[2][0] + offset, instruction[2][1] + offset)
        z_dim = (instruction[3][0] + offset, instruction[3][1] + offset)
        cuboid[x_dim[0]:x_dim[1]+1, y_dim[0]:y_dim[1]+1, z_dim[0]:z_dim[1]+1] = set_value

n_lights = np.sum(cuboid)
print(n_lights)
