# Advent of Code - Day 10
# Part 1

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

pipe_directions = {
    "|": (NORTH, SOUTH),
    "-": (EAST, WEST),
    "L": (NORTH, EAST),
    "J": (NORTH, WEST),
    "7": (SOUTH, WEST),
    "F": (SOUTH, EAST),
}


class PipeNavigator:
    def __init__(self, pipe_network):
        self.network = pipe_network
        self.start = self.get_start_position()
        self.network[self.start[0]][self.start[1]] = "|"
        self.visited_nodes = {}

    def get_start_position(self):
        for x, row in enumerate(self.network):
            for y, value in enumerate(row):
                if value == "S":
                    return (x, y)

    def next_pos(self, position, direction):
        if direction == NORTH:
            return (position[0] - 1, position[1])
        if direction == EAST:
            return (position[0], position[1] + 1)
        if direction == SOUTH:
            return (position[0] + 1, position[1])
        if direction == WEST:
            return (position[0], position[1] - 1)

    def visit_all_nodes(self):
        nodes_to_visit = [(self.start, 0)]
        while nodes_to_visit:
            node, steps = nodes_to_visit.pop(0)
            self.visited_nodes[node] = steps
            pipe_part = self.network[node[0]][node[1]]

            for direction in pipe_directions[pipe_part]:
                new_position = self.next_pos(node, direction)
                if new_position not in self.visited_nodes:
                    nodes_to_visit.append((new_position, steps + 1))

        max_steps = 0
        for node in self.visited_nodes.items():
            if node[1] > max_steps:
                max_steps = node[1]
        print(max_steps)


def parse_input(file):
    pipe_network = []
    with open(file, "r", encoding="utf-8") as f:
        for line in f.readlines():
            pipe_network.append(list(line.strip()))

    return pipe_network


def main():
    pipe_network = parse_input("input.txt")
    navigator = PipeNavigator(pipe_network)
    navigator.visit_all_nodes()


if __name__ == "__main__":
    main()
