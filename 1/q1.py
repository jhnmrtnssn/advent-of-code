# Advent of Code - Day 1
# Part 2

n_increased = 0

for line, value in enumerate(open('input.txt')):
    if(int(line) > 0):
        if(int(value) > prev_value):
            n_increased += 1
    prev_value = int(value)

print(n_increased)