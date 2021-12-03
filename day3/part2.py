# Advent of Code - Day 3
# Part 2

import numpy as np

v = np.zeros(12)
np_gamma = np.zeros(12)
np_eps = np.zeros(12)

# Store all bytes as np array
all_bytes = np.zeros([1000, 12])
for index, line in enumerate(open("input.txt")):
    for id, char in enumerate(line.strip()):
        all_bytes[index, id] = char

############ Find oxygen generator rating ############

# First run, use all bytes and reset new bytes
OGR_list = all_bytes

# Loop for all positions
for bit in range(12):
    # Find the most common bit
    v = np.zeros(12)
    for index, line in enumerate(OGR_list):
        for id, char in enumerate(line):
            if int(char) == 1:
                v[id] = int(v[id]) + 1
            else:
                v[id] = int(v[id]) - 1

    # Normalize the common bit
    for id, value in enumerate(v):
        if value >= 0:
            np_gamma[id] = 1
        else:
            np_gamma[id] = 0

    print(np_gamma)

    # Find index for all rows that contain the bit
    save_rows = np.zeros(1000)
    for index, byte in enumerate(OGR_list):
        if int(byte[bit]) == int(np_gamma[bit]):
            save_rows[index] = 1

    copy_row_index = []
    for index, save in enumerate(save_rows):
        if int(save) == 1:
            copy_row_index.append(index)

    new_OGR_list = np.copy(OGR_list[copy_row_index, ])

    # Use new list as input for algorithm
    OGR_list = new_OGR_list

    # Store and save final value
    if new_OGR_list.size == 12:
        OGR = new_OGR_list

############ Find CO2 scrubber rating ############

# First run, use all bytes and reset new bytes
OXY_list = all_bytes

# Loop for all positions
for bit in range(12):
    # Find the most common bit
    v = np.zeros(12)
    for index, line in enumerate(OXY_list):
        for id, char in enumerate(line):
            if int(char) == 1:
                v[id] = int(v[id]) - 1
            else:
                v[id] = int(v[id]) + 1

    # Normalize the non-common bit
    for id, byte in enumerate(v):
        if byte > 0:
            np_eps[id] = 1
        else:
            np_eps[id] = 0

    # Find index for all rows that contain the bit
    save_rows = np.zeros(1000)
    for index, byte in enumerate(OXY_list):
        if int(byte[bit]) == int(np_eps[bit]):
            save_rows[index] = 1

    copy_row_index = []
    for index, save in enumerate(save_rows):
        if int(save) == 1:
            copy_row_index.append(index)

    new_OXY_list = np.copy(OXY_list[copy_row_index, ])

    # Use new list as input for algorithm
    OXY_list = new_OXY_list

    # Store and save final value
    if new_OXY_list.size == 12:
        OXY = new_OXY_list
        break

ogr = OGR.dot(2**np.arange(OGR.size)[::-1])
oxy = OXY.dot(2**np.arange(OXY.size)[::-1])

print(ogr*oxy)
