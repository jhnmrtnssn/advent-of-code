# Advent of Code - Day 9
# Part 2

import time
import pygame

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


def updateBasin(basin_map, row, col, unique_positions):
    n_cols = len(basin_map[0])-1
    n_rows = len(basin_map)-1
    if row != 0:
        if basin_map[row-1][col] != 9 and [row-1, col] not in unique_positions:
            unique_positions.append([row-1, col])
    if row != n_rows:
        if basin_map[row+1][col] != 9 and [row+1, col] not in unique_positions:
            unique_positions.append([row+1, col])
    if col != 0:
        if basin_map[row][col-1] != 9 and [row, col-1] not in unique_positions:
            unique_positions.append([row, col-1])
    if col != n_cols:
        if basin_map[row][col+1] != 9 and [row, col+1] not in unique_positions:
            unique_positions.append([row, col+1])

    return unique_positions


def calcBasinSize(basin_map, row, col):
    unique_positions = [[row, col]]

    for pos in unique_positions:
        unique_positions = updateBasin(basin_map, pos[0], pos[1], unique_positions)
        value = basin_map[pos[0]][pos[1]]
        pygame.draw.rect(win, (value*20, value*20, 255), (pos[0]*8, pos[1]*8, 8, 8))
        pygame.time.delay(2)
        pygame.display.update()
        pygame.event.get()


    return len(unique_positions)


#### Visualize day9 with pygame ####
full_map = parseInput()

# Initiate pygame window
win = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Advent of Code day 9")
win.fill((255, 255, 255))
pygame.display.update()
pygame.event.get()

# Show all borders
for row_id, row in enumerate(full_map):
    for col_id, value in enumerate(row):
        if value == 9:
            pygame.draw.rect(win, (0, 0, 0), (row_id*8, col_id*8, 8, 8))

pygame.display.update()
pygame.event.get()

# Calculate basins and show them in window
basin_size_list = []
for row_id, row in enumerate(full_map):
    for col_id, value in enumerate(row):
        if isLowPoint(full_map, row_id, col_id):
            basin_size = calcBasinSize(full_map, row_id, col_id)
            basin_size_list.append(basin_size)
            pygame.draw.rect(win, (150, 0, 150), (row_id*8, col_id*8, 8, 8))

# Wait 10s before closing
time.sleep(10)
