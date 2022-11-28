# Advent of Code - Day 10
# Part 1


def parseInput():
    lines = []
    for line in open("input.txt"):
        lines.append(line.strip())
    return lines


def isLeftSide(char):
    return(char in ["(", "[", "<", "{"])


def expectedRightSide(char):
    if char == "(":
        return ")"
    if char == "[":
        return "]"
    if char == "<":
        return ">"
    if char == "{":
        return "}"

    return False


def calcCorruptedChars(chars):
    score_sum = 0
    for char in chars:
        if char == ")":
            score_sum += 3
        if char == "]":
            score_sum += 57
        if char == "}":
            score_sum += 1197
        if char == ">":
            score_sum += 25137
    return score_sum


###### PART 1 ######

lines = parseInput()

left_side_list = []
corrupted_chars = []

for line in lines:
    for char in line:
        if isLeftSide(char):
            left_side_list.append(char)
        else:
            if char == expectedRightSide(left_side_list[-1]):
                left_side_list.pop()
            else:
                corrupted_chars.append(char)
                break

print(calcCorruptedChars(corrupted_chars))
