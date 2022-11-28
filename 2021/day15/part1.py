# Advent of Code - Day 15
# Part 1

import numpy as np


def parseInput(file):
    # Find dimensions of x and y
    x_dim = 0
    y_dim = 0
    for line in open(file):
        x_dim += 1
        for _ in line.strip():
            if x_dim == 1:
                y_dim += 1

    # Allocate and fill np array
    risk_map = np.zeros([x_dim, y_dim]).astype(int)
    for x, line in enumerate(open(file)):
        for y, value in enumerate(line.strip()):
            risk_map[x][y] = value

    return risk_map


def find_lowest_prev_val(acc_risk_map, x, y, rescan):
    x_dim, y_dim = risk_map.shape
    vals = []
    # Value from Left
    if x > 0:
        vals.append(acc_risk_map[x-1][y])
    # Value from Top
    if y > 0:
        vals.append(acc_risk_map[x][y-1])
    if rescan:
        # Value from Right
        if x < x_dim-1:
            if acc_risk_map[x+1][y] != np.inf:
                vals.append(acc_risk_map[x+1][y])
        # Value from Bottom
        if y < y_dim-1:
            if acc_risk_map[x][y+1] != np.inf:
                vals.append(acc_risk_map[x][y+1])

    # Return min value
    if len(vals) > 0:
        return min(vals)
    return 0


def find_new_nodes(risk_map, x, y):
    x_dim, y_dim = risk_map.shape
    new_nodes = []
    # Move Right
    if x < x_dim-1:
        new_nodes.append([x+1, y])
    # Move Down
    if y < y_dim-1:
        new_nodes.append([x, y+1])

    return new_nodes


def add_rescan_neighbors(risk_map, x, y):
    new_rescan_nodes = []
    x_dim, y_dim = risk_map.shape
    # Left
    if x > 0:
        new_rescan_nodes.append([x-1, y])
    # Top
    if y > 0:
        new_rescan_nodes.append([x, y-1])
    # Right
    if x < x_dim-1:
        new_rescan_nodes.append([x+1, y])
    # Down
    if y < y_dim-1:
        new_rescan_nodes.append([x, y+1])
    return new_rescan_nodes


def calc_node_risk(acc_risk_map, prev_val, x, y):
    new_val = risk_map[x][y] + prev_val
    if acc_risk_map[x][y] > new_val:
        acc_risk_map[x][y] = new_val
    return acc_risk_map


# ----- Part 1 ----- #

risk_map = parseInput("input.txt")
acc_risk_map = np.ones(risk_map.shape) * np.inf
risk_map[0][0] = 0
start_node = [[0, 0]]

visited_nodes = start_node
rescan_list = []
current_nodes = start_node

while len(current_nodes) > 0 or len(rescan_list) > 0:
    new_nodes_list = []
    for node in current_nodes:
        rescan = False
        x = node[0]
        y = node[1]
        node_val = risk_map[x][y]
        prev_val = find_lowest_prev_val(acc_risk_map, x, y, rescan)
        acc_risk_map = calc_node_risk(acc_risk_map, prev_val, x, y)

        new_nodes = find_new_nodes(risk_map, x, y)
        for new_node in new_nodes:
            if new_node not in new_nodes_list:
                new_nodes_list.append(new_node)

    for rescan_node in rescan_list:
        rescan = True
        x = rescan_node[0]
        y = rescan_node[1]
        node_val = acc_risk_map[x][y]
        prev_val = find_lowest_prev_val(acc_risk_map, x, y, rescan)
        if prev_val + risk_map[x][y] < node_val:
            acc_risk_map[x][y] = prev_val + risk_map[x][y]
            current_nodes.extend(add_rescan_neighbors(risk_map, x, y))

    rescan_list = current_nodes
    current_nodes = new_nodes_list
    new_nodes_list = []


print(acc_risk_map)
