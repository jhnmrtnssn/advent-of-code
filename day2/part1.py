# Advent of Code - Day 2
# Part 1

def move(curr_h, curr_d, direction, length):
    if direction == "forward":
        return (curr_h + length, curr_d)
    if direction == "down":
        return (curr_h, curr_d + length)
    if direction == "up":
        return (curr_h, curr_d - length)

d = 0
h = 0

for index, line in enumerate(open("input.txt")):
    direction, length = str.split(line)
    (d, h) = move(d, h, direction, int(length))

print(d*h)