# Advent of Code - Day 3
# Part 1

import numpy as np

v = np.zeros(12)
np_gamma = np.zeros(12)
np_eps = np.zeros(12)

for line in open("input.txt"):
    for i, char in enumerate(line.strip()):
        if char == "1":
            v[i] = int(v[i]) + 1
        else:
            v[i] = int(v[i]) - 1

for i, byte in enumerate(v):
    if byte > 0:
        np_gamma[i] = 1
        np_eps[i] = 0
    else:
        np_gamma[i] = 0
        np_eps[i] = 1

print(np_gamma)

gamma = np_gamma.dot(2**np.arange(np_gamma.size)[::-1])
eps = np_eps.dot(2**np.arange(np_eps.size)[::-1])
print(gamma)
print(eps)

print(int(gamma)*int(eps))
