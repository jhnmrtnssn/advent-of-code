# Advent of Code - Day 16
# Part 1

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

        # Value of L is length of both packages
        if int(I) == 0:
            len_L = 15
            L = int(bin_string[7:7+len_L], 2)
            len_message = 7 + len_L + L
            new_bin_string = bin_string[7+len_L:len_message]
            while L > 0:
                new_V, new_literal_value, new_len_message = parsePackage(new_bin_string)
                V += new_V
                literal_value += new_literal_value
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
                literal_value += new_literal_value
                new_bin_string = new_bin_string[new_len_message:]
                len_message += new_len_message

    return V, literal_value, len_message


# ----- Part 1 ----- #

hex_string = parseInput("input.txt")

h_size = len(hex_string) * 4
package = (bin(int(hex_string, 16))[2:]).zfill(h_size)

V, literal_value, _ = parsePackage(package)

print("literal_value:", literal_value)
print("V:", V)
