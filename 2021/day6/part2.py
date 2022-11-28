# Advent of Code - Day 6
# Part 1
import time
import numpy as np

def parseInput():
    for line in open("input.txt"):
        return list(map(np.uint8, (line.strip().split(","))))


input_fish_list = parseInput()
fish_list = []
for i in range(0, 9):
    fish_list.append(input_fish_list.count(i))

start_time = time.time()
for day in range(0, 256):
    born_fish = fish_list[0]
    for i, _ in enumerate(fish_list):
        if i > 0:
            fish_list[i-1] = fish_list[i]
    fish_list[8] = born_fish
    fish_list[6] += born_fish


print(sum(fish_list))
