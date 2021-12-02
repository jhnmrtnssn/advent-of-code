# Advent of Code - Day 2
# Part 2

def move(curr_d, curr_h, curr_aim, direction, length):
    if direction == "forward":
        return (curr_d + aim * length, curr_h + length, curr_aim)
    if direction == "down":
        return (curr_d, curr_h, curr_aim + length)
    if direction == "up":
        return (curr_d, curr_h, curr_aim - length)

d = 0
h = 0
aim = 0

for index, line in enumerate(open("input.txt")):
    direction, length = str.split(line)
    (d, h, aim) = move(d, h, aim, direction, int(length))

print(d * h)