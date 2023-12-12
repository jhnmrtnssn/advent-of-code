# Advent of Code - Day 10
# Part 1

from copy import deepcopy


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

zoomed_in_parts = {
    "|": [[" ", "|", " "], [" ", "|", " "], [" ", "|", " "]],
    "-": [[" ", " ", " "], ["-", "-", "-"], [" ", " ", " "]],
    "L": [[" ", "|", " "], [" ", "|", "-"], [" ", " ", " "]],
    "J": [[" ", "|", " "], ["-", "|", " "], [" ", " ", " "]],
    "7": [[" ", " ", " "], ["-", "|", " "], [" ", "|", " "]],
    "F": [[" ", " ", " "], [" ", "|", "-"], [" ", "|", " "]],
    ".": [[".", ".", "."], [".", ".", "."], [".", ".", "."]],
    "O": [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]],
}

crossing_loop_west = ["|", "L", "J", "7", "F"]


class PipeNavigator:
    def __init__(self, pipe_network):
        self.network = pipe_network
        self.start = self.get_start_position()
        self.network[self.start[0]][self.start[1]] = "|"
        self.visited_nodes = {}
        self.visit_all_nodes()
        self.pipe_loop = sorted(self.visited_nodes.keys())
        self.clear_map()
        self.connected_ground = self.get_all_connected_ground()
        self.semi_enclosed_ground = self.get_all_semi_enclosed_tiles()
        print(len(self.semi_enclosed_ground))
        self.zoomed_network = self.enhance_network()
        self.get_all_fully_enclosed_tiles()

    def get_start_position(self):
        for x, row in enumerate(self.network):
            for y, value in enumerate(row):
                if value == "S":
                    return (x, y)

    def valid_position(self, position):
        if 0 <= position[0] < len(self.network):
            if 0 <= position[1] < len(self.network[0]):
                return True
        return False

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

    def get_neighbor_ground_nodes(self, node):
        directions = [NORTH, EAST, SOUTH, WEST]
        ground_nodes = []
        for direction in directions:
            if not self.valid_position(self.next_pos(node, direction)):
                continue
            x, y = self.next_pos(node, direction)
            neighbor_node = self.network[x][y]
            if neighbor_node == ".":
                ground_nodes.append((x, y))
        return ground_nodes

    def get_neighbor_subpixel_ground_nodes(self, node):
        directions = [NORTH, EAST, SOUTH, WEST]
        ground_nodes = []
        for direction in directions:
            x, y = self.next_pos(node, direction)
            neighbor_node = self.zoomed_network[x][y]
            if neighbor_node == " " or neighbor_node == "." or neighbor_node == "O":
                ground_nodes.append((x, y))
        return ground_nodes

    def clear_map(self):
        empty_map = []
        for _ in self.network:
            empty_map.append(["."] * len(self.network[0]))

        for x, y in self.pipe_loop:
            empty_map[x][y] = self.network[x][y]

        self.network = empty_map

    def invalid_move(self, node):
        directions = [NORTH, EAST, SOUTH, WEST]
        for direction in directions:
            if not self.valid_position(self.next_pos(node, direction)):
                return True
        return False

    def get_all_connected_ground(self):
        connected_ground = []
        for node in self.pipe_loop:
            neighbor_nodes = self.get_neighbor_ground_nodes(node)
            for neighbor_node in neighbor_nodes:
                if neighbor_node not in connected_ground:
                    connected_ground.append(neighbor_node)
        return connected_ground

    def get_all_semi_enclosed_tiles(self):
        visited_not_enclosed_tiles = []
        visited_enclosed_tiles = []
        nodes_to_visit = deepcopy(self.connected_ground)
        while nodes_to_visit:
            connected_ground_to_visit = [nodes_to_visit.pop(0)]
            ground_segment = deepcopy(connected_ground_to_visit)
            while connected_ground_to_visit:
                node = connected_ground_to_visit.pop(0)

                # All ground in ground segment is not enclosed
                if node in visited_not_enclosed_tiles or self.invalid_move(node):
                    for ground in ground_segment:
                        if ground not in visited_enclosed_tiles:
                            visited_not_enclosed_tiles.append(ground)
                    connected_ground_to_visit = []
                    ground_segment = []
                    continue

                # All ground in ground segment is enclosed
                if node in visited_enclosed_tiles:
                    for ground in ground_segment:
                        if ground not in visited_enclosed_tiles:
                            visited_enclosed_tiles.append(ground)
                    connected_ground_to_visit = []
                    ground_segment = []
                    continue

                # Get neighbor ground nodes
                neighbor_ground = self.get_neighbor_ground_nodes(node)
                for new_ground in neighbor_ground:
                    if new_ground not in ground_segment:
                        connected_ground_to_visit.append(new_ground)
                        ground_segment.append(new_ground)

            # If we couldnt move out, the ground is enclosed
            if ground_segment:
                for ground in ground_segment:
                    visited_enclosed_tiles.append(ground)

        for g in visited_enclosed_tiles:
            self.network[g[0]][g[1]] = "O"

        return visited_enclosed_tiles

    def enhance_network(self):
        enhanced_network = []
        for _ in range(0, 3 * len(self.network)):
            enhanced_network.append(["."] * 3 * len(self.network[0]))

        for x, row in enumerate(self.network):
            for y, value in enumerate(row):
                symbol = zoomed_in_parts[value]
                for i, symbol_row in enumerate(symbol):
                    for j, symbol_value in enumerate(symbol_row):
                        enhanced_network[3 * x + i][3 * y + j] = symbol_value

        return enhanced_network

    def get_all_fully_enclosed_tiles(self):
        nodes_to_visit = []
        visited_enclosed_ground = []
        for node in self.semi_enclosed_ground:
            nodes_to_visit.append((3 * node[0] + 1, 3 * node[1] + 1))

        while nodes_to_visit:
            semi_enclosed_ground_to_visit = [nodes_to_visit.pop(0)]
            ground_segment = []
            enclosed_ground = deepcopy(semi_enclosed_ground_to_visit)

            while semi_enclosed_ground_to_visit:
                node = semi_enclosed_ground_to_visit.pop(0)
                neighbors = self.get_neighbor_subpixel_ground_nodes(node)

                for neighbor in neighbors:
                    if neighbor in visited_enclosed_ground:
                        semi_enclosed_ground_to_visit = []
                        break
                    if neighbor in ground_segment:
                        continue
                    if self.zoomed_network[neighbor[0]][neighbor[1]] == ".":
                        for ground in ground_segment:
                            self.zoomed_network[ground[0]][ground[1]] = "."
                        semi_enclosed_ground_to_visit = []
                        ground_segment = []

                        for ground in enclosed_ground:
                            if ground in nodes_to_visit:
                                nodes_to_visit.remove(ground)
                        enclosed_ground = []
                    elif self.zoomed_network[neighbor[0]][neighbor[1]] == "O":
                        enclosed_ground.append(neighbor)
                    else:
                        semi_enclosed_ground_to_visit.append(neighbor)
                        ground_segment.append(neighbor)

            # If we couldnt move out, the ground is enclosed
            for ground in enclosed_ground:
                visited_enclosed_ground.append(ground)

        print(len(list(set(visited_enclosed_ground))))

        for g in visited_enclosed_ground:
            self.zoomed_network[g[0]][g[1]] = "I"

        return visited_enclosed_ground

    # DEBUG PURPOSE
    def print_pipe_loop(self):
        for row in self.zoomed_network:
            print("".join(row))


def parse_input(file):
    pipe_network = []
    with open(file, "r", encoding="utf-8") as f:
        for line in f.readlines():
            pipe_network.append(list(line.strip()))

    return pipe_network


def main():
    pipe_network = parse_input("input.txt")
    navigator = PipeNavigator(pipe_network)
    # navigator.print_pipe_loop()


if __name__ == "__main__":
    main()
