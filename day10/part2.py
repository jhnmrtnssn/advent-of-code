# Advent of Code - Day 10
# Part 1


def parseInput():
    lines = []
    for line in (open("input.txt")):
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


def valueModel(char):
    if char == ")":
        return 1
    if char == "]":
        return 2
    if char == "}":
        return 3
    if char == ">":
        return 4


def calcScore(remaining_chars):
    score = 0
    for char in remaining_chars:
        score = score*5 + valueModel(char)
    return score


###### PART 2 ######

lines = parseInput()

score_list = []
for line in lines:
    left_side_list = []
    corrupted = False
    for char in line:
        if isLeftSide(char):
            left_side_list.append(char)
        else:
            if char == expectedRightSide(left_side_list[-1]):
                left_side_list.pop()
            else:
                corrupted = True
                break

    if not corrupted:
        remaining_chars = []
        for char in reversed(left_side_list):
            remaining_chars.append(expectedRightSide(char))
        score_list.append(calcScore(remaining_chars))

score_list.sort()
print(score_list[int(len(score_list)/2 - 0.5)])
