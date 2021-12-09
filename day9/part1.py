# Advent of Code - Day 9
# Part 1


def parseInput():
    fullMap = []
    for line in (open("input.txt")):
        lineMap = []
        for string in line.strip():
            for number in string:
                lineMap.append(int(number))
        fullMap.append(lineMap)
    return fullMap


def isLowPoint(map, row, col):
    n_cols = len(map[0])-1
    n_rows = len(map)-1
    if row != 0:
        if map[row][col] >= map[row-1][col]:
            return False
    if row != n_rows:
        if map[row][col] >= map[row+1][col]:
            return False
    if col != 0:
        if map[row][col] >= map[row][col-1]:
            return False
    if col != n_cols:
        if map[row][col] >= map[row][col+1]:
            return False
    return True


###### PART 1 ######

fullMap = parseInput()

sum_risk_level = 0
for row_id, row in enumerate(fullMap):
    for col_id, value in enumerate(row):
        if isLowPoint(fullMap, row_id, col_id):
            sum_risk_level += value + 1

print(sum_risk_level)
