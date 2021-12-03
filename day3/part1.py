# Advent of Code - Day 3
# Part 1

import numpy as np

v = np.zeros(12)
np_gamma = np.zeros(12)
np_eps = np.zeros(12)

for index, line in enumerate(open("input.txt")):
    for id, char in enumerate(line.strip()):
        if char == "1":
            v[id] = int(v[id]) + 1
        else:
            v[id] = int(v[id]) - 1

for id, byte in enumerate(v):
    if byte > 0:
        np_gamma[id] = 1
        np_eps[id] = 0
    else:
        np_gamma[id] = 0
        np_eps[id] = 1

print(np_gamma)

gamma = np_gamma.dot(2**np.arange(np_gamma.size)[::-1])
eps = np_eps.dot(2**np.arange(np_eps.size)[::-1])
print(gamma)
print(eps)

print(int(gamma)*int(eps))