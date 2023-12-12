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

crossing_loop_west = ["|", "L", "J"]


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

    def clear_map(self):
        empty_map = []
        for _ in self.network:
            empty_map.append(["."] * len(self.network[0]))

        for x, y in self.pipe_loop:
            empty_map[x][y] = self.network[x][y]

        self.network = empty_map

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

    def amount_of_crossing_loop(self, node):
        n_crossed_loop = 0
        value = "O"
        i = 0
        while value != ".":
            i += 1
            next_node = (node[0], node[1] - i)
            if not self.valid_position(next_node):
                break
            node = next_node
            value = self.network[node[0]][node[1]]
            if value in crossing_loop_west:
                n_crossed_loop += 1
        return n_crossed_loop

    def get_all_enclosed_ground(self):
        n_enclosed_ground = 0
        for node in self.semi_enclosed_ground:
            n_crossed_loop = self.amount_of_crossing_loop(node)
            if n_crossed_loop % 2 == 1:
                n_enclosed_ground += 1
        print(n_enclosed_ground)


def parse_input(file):
    pipe_network = []
    with open(file, "r", encoding="utf-8") as f:
        for line in f.readlines():
            pipe_network.append(list(line.strip()))

    return pipe_network


def main():
    pipe_network = parse_input("input.txt")
    navigator = PipeNavigator(pipe_network)
    navigator.get_all_enclosed_ground()


if __name__ == "__main__":
    main()
