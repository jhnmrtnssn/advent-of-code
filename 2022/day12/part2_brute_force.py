# First version of part2 that iterates all starting positions
# It works but it is highly inefficient..

from math import inf


def parse_input(file):
    data = []
    for line in open(file):
        data.append(list(line.strip()))
    return data


def get_lowest_fscore_node(f_score_map, nodes):
    fscore = []
    for node in nodes:
        fscore.append(f_score_map[node[0]][node[1]])
    return nodes[fscore.index(min(fscore))]


def convert_start_and_end_values(value):
    if value == "S":
        value = "a"
    if value == "E":
        value = "z"
    return value


class PathFinder:
    def __init__(self, data):
        self.map = data
        self.get_start_and_end_coords()
        self.map_values = list("abcdefghijklmnopqrstuvwxyz")

    def get_start_and_end_coords(self):
        self.start = []
        for x, row in enumerate(self.map):
            for y, value in enumerate(row):
                if value == "S":
                    self.start.append((x, y))
                if value == "a":
                    self.start.append((x, y))
                if value == "E":
                    self.end = (x, y)

    def get_neighbors(self, node_x, node_y):
        neighbors = []
        if node_x > 0:
            neighbors.append((node_x - 1, node_y))
        if node_x < len(self.map) - 1:
            neighbors.append((node_x + 1, node_y))
        if node_y > 0:
            neighbors.append((node_x, node_y - 1))
        if node_y < len(self.map[0]) - 1:
            neighbors.append((node_x, node_y + 1))
        return neighbors

    def move(self, current, new):
        pre_value = convert_start_and_end_values(self.map[current[0]][current[1]])
        new_value = convert_start_and_end_values(self.map[new[0]][new[1]])
        if self.map_values.index(new_value) - self.map_values.index(pre_value) <= 1:
            return 1
        return inf

    def init_score_map(self, start):
        score_map = [[inf] * len(self.map[0]) for _ in range(len(self.map))]
        score_map[start[0]][start[1]] = 0
        return score_map

    def a_star_algorithm(self, start_pos):
        discovered_nodes = [start_pos]
        came_from = {}
        g_score_map = self.init_score_map(start_pos)
        f_score_map = self.init_score_map(start_pos)

        while discovered_nodes:
            current = get_lowest_fscore_node(f_score_map, discovered_nodes)
            if self.map[current[0]][current[1]] == "E":
                return g_score_map[self.end[0]][self.end[1]]
            discovered_nodes.remove(current)

            for neighbor in self.get_neighbors(current[0], current[1]):
                tentative_gscore = g_score_map[current[0]][current[1]] + self.move(
                    current, neighbor
                )

                if tentative_gscore < g_score_map[neighbor[0]][neighbor[1]]:
                    came_from[neighbor] = current
                    g_score_map[neighbor[0]][neighbor[1]] = tentative_gscore
                    f_score_map[neighbor[0]][neighbor[1]] = tentative_gscore + 1
                    if neighbor not in discovered_nodes:
                        discovered_nodes.append(neighbor)
        return inf

    def iterate_best_path(self):
        shortest_path = inf
        for start in self.start:
            steps = self.a_star_algorithm(start)
            if steps < shortest_path:
                shortest_path = steps
        print(shortest_path)


def main():
    data = parse_input("input.txt")
    pf = PathFinder(data)
    pf.iterate_best_path()


if __name__ == "__main__":
    main()
