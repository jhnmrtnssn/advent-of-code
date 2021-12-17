# Advent of Code - Day 16
# Part 2

import math

def parseInput(file):
    # Find dimensions of x and y
    for line in open(file):
        hex_string = line.strip()
    return hex_string


def parsePackage(bin_string):
    V_bin, T_bin = (bin_string[:3], bin_string[3:6])
    V, T = (int(V_bin, 2), int(T_bin, 2))
    literal_value = 0

    if T == 4:
        n_literal_groups = math.floor(len(bin_string[6:])/5)
        bin_value = ""
        for i in range(n_literal_groups):
            group = bin_string[6 + 5*i: 6 + 5*i + 5]
            bin_value += group[1:]
            if int(group[0]) == 0:
                break
        len_message = 6 + 5*(i+1)
        literal_value = int((bin_value), 2)

    else:
        I = bin_string[6]
        literal_values = []

        # Value of L is length of both packages
        if int(I) == 0:
            len_L = 15
            L = int(bin_string[7:7+len_L], 2)
            len_message = 7 + len_L + L
            new_bin_string = bin_string[7+len_L:len_message]
            while L > 0:
                new_V, new_literal_value, new_len_message = parsePackage(new_bin_string)
                V += new_V
                literal_values.append(new_literal_value)
                L -= new_len_message
                new_bin_string = new_bin_string[new_len_message:]

        # Value of L is number of groups
        else:
            len_L = 11
            L = int(bin_string[7:7+len_L], 2)
            new_bin_string = bin_string[7+len_L:]
            len_message = 7 + len_L
            for i in range(L):
                new_V, new_literal_value, new_len_message = parsePackage(new_bin_string)
                V += new_V
                literal_values.append(new_literal_value)
                new_bin_string = new_bin_string[new_len_message:]
                len_message += new_len_message

        # Part 2
        literal_value = calcLiteralValue(T, literal_values)

    return V, literal_value, len_message


def calcLiteralValue(T, values):
    if T == 0:
        return sum(values)

    if T == 1:
        if len(values) == 1:
            return values[0]
        product_sum = 1
        for x in values:
            product_sum = product_sum * x
        return product_sum

    if T == 2:
        return min(values)

    if T == 3:
        return max(values)

    if T == 5:
        return int(values[0] > values[1])

    if T == 6:
        return int(values[0] < values[1])

    if T == 7:
        return int(values[0] == values[1])


# ----- Part 2 ----- #

hex_string = parseInput("input.txt")

h_size = len(hex_string) * 4
package = (bin(int(hex_string, 16))[2:]).zfill(h_size)

V, literal_value, _ = parsePackage(package)

print("literal_value:", literal_value)
print("V:", V)
