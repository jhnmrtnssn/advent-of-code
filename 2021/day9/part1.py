# Advent of Code - Day 9
# Part 1


def parseInput():
    full_map = []
    for line in open("input.txt"):
        line_map = []
        for string in line.strip():
            for number in string:
                line_map.append(int(number))
        full_map.append(line_map)
    return full_map


def isLowPoint(basin_map, row, col):
    n_cols = len(basin_map[0])-1
    n_rows = len(basin_map)-1
    if row != 0:
        if basin_map[row][col] >= basin_map[row-1][col]:
            return False
    if row != n_rows:
        if basin_map[row][col] >= basin_map[row+1][col]:
            return False
    if col != 0:
        if basin_map[row][col] >= basin_map[row][col-1]:
            return False
    if col != n_cols:
        if basin_map[row][col] >= basin_map[row][col+1]:
            return False
    return True


###### PART 1 ######

full_map = parseInput()

sum_risk_level = 0
for row_id, row in enumerate(full_map):
    for col_id, value in enumerate(row):
        if isLowPoint(full_map, row_id, col_id):
            sum_risk_level += value + 1

print(sum_risk_level)
