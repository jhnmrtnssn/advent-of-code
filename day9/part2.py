# Advent of Code - Day 9
# Part 2


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


def updateBasin(map, row, col, unique_positions):
    n_cols = len(map[0])-1
    n_rows = len(map)-1
    if row != 0:
        if map[row-1][col] != 9 and [row-1, col] not in unique_positions:
            unique_positions.append([row-1, col])
    if row != n_rows:
        if map[row+1][col] != 9 and [row+1, col] not in unique_positions:
            unique_positions.append([row+1, col])
    if col != 0:
        if map[row][col-1] != 9 and [row, col-1] not in unique_positions:
            unique_positions.append([row, col-1])
    if col != n_cols:
        if map[row][col+1] != 9 and [row, col+1] not in unique_positions:
            unique_positions.append([row, col+1])

    return unique_positions


def calcBasinSize(map, row, col):
    unique_positions = [[row, col]]

    for pos in unique_positions:
        unique_positions = updateBasin(map, pos[0], pos[1], unique_positions)

    return len(unique_positions)


###### PART 2 ######

fullMap = parseInput()

basin_size_list = []
for row_id, row in enumerate(fullMap):
    for col_id, value in enumerate(row):
        if isLowPoint(fullMap, row_id, col_id):
            basin_size = calcBasinSize(fullMap, row_id, col_id)
            basin_size_list.append(basin_size)

# Multiplicate the three highest basins
basin_size_list.sort(reverse=True)
print(basin_size_list[0]*basin_size_list[1]*basin_size_list[2])
