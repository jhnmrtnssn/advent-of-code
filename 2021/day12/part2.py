# Advent of Code - Day 12
# Part 2

from copy import deepcopy

def parseInput(file):
    all_connections = []
    for line in open(file):
        all_connections.append(line.strip().split("-"))
    return all_connections


def buildMap(all_connections):
    unique_spots = []
    connections = []
    for line in all_connections:
        if [line[0]] not in unique_spots:
            unique_spots.append([line[0]])
            connections.append([line[1]])
        else:
            pos = unique_spots.index([line[0]])
            connections[pos].append(line[1])

        if [line[1]] not in unique_spots:
            unique_spots.append([line[1]])
            connections.append([line[0]])
        else:
            pos = unique_spots.index([line[1]])
            connections[pos].append(line[0])

    # Create map in form [[start, [a, b, c]], [a, [b, c]], ..]
    cavern_map = deepcopy(unique_spots[:])
    for i, _ in enumerate(cavern_map):
        cavern_map[i].append(connections[i])

    return cavern_map, unique_spots


def returnConnections(cavern_map, unique_spots, node):
    index = unique_spots.index([node])
    return cavern_map[index][1]


all_connections = (parseInput("input.txt"))
cavern_map, unique_spots = buildMap(all_connections)

all_paths = [['start']]
valid_paths = []
for path in all_paths:
    # Set flag for visiting a small cave twice
    visited_small_cave_twice = False
    for node in path:
        if path.count(node) > 1 and node.islower():
            visited_small_cave_twice = True

    for node in returnConnections(cavern_map, unique_spots, path[-1]):
        if node == 'start' or path.count('end') == 1:
            continue
        if path.count(node) > 0 and node.islower() and visited_small_cave_twice:
            continue
        all_paths.append(path + [node])
        if node == 'end':
            valid_paths.append(all_paths)

print(len(valid_paths))
