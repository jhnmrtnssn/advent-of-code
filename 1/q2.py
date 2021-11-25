n_increased = 0
val1 = 0
val2 = 0
val3 = 0
sum = 0

for line, value in enumerate(open('input.txt')):
    val1 = val2
    val2 = val3
    val3 = int(value)
    sum = val1 + val2 + val3
    if line > 2:
        if sum > prev_sum:
            n_increased += 1
    prev_sum = sum

print(n_increased)