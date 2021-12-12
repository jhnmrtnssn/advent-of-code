# Advent of Code - Day 1
# Part 1


n_increased = 0
prev_sum = 0
val = [0, 0, 0]

for line, value in enumerate(open('input.txt')):
    val = [val[1], val[2], int(value)]
    if line > 2:
        if sum(val) > prev_sum:
            n_increased += 1
    prev_sum = sum(val)

print(n_increased)
