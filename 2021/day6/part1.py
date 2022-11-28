# Advent of Code - Day 6
# Part 1
import time
import numpy as np

def parseInput():
    for line in open("input.txt"):
        return list(map(np.uint8, (line.strip().split(","))))


fish_list = parseInput()
#fish_list = [3, 4, 3, 0, 2]

start_time = time.time()
for day in range(0, 80):
    n_new_fish = 0
    new_fish_list = []
    for index, days in enumerate(fish_list):
        if days == 0:
            fish_list[index] = 6
            n_new_fish += 1
        else:
            fish_list[index] -= 1

    new_fish_list = [8] * n_new_fish
    fish_list += new_fish_list
    print(day)

print(time.time() - start_time)
print(len(fish_list))
