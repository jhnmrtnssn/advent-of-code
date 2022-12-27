# Advent of Code - Day 24
# Part 1


from copy import deepcopy


def parse_input(file):
    blizzard_map = []
    with open(file, "r", encoding="utf-8") as f:
        for line in f.readlines():
            blizzard_map.append(list(line.strip()))
    return blizzard_map


class BlizzardPathFinder:
    def __init__(self, blizzard_init_map, init_minute, start_to_end):
        self.init_minute = init_minute
        self.map_over_time = {0: blizzard_init_map}
        self.empty_map = self.clear_map(blizzard_init_map)
        self.init_blizzards = self.get_blizzards()
        self.open_height = len(blizzard_init_map) - 2
        self.open_width = len(blizzard_init_map[0]) - 2
        self.initiate_start_and_goal(init_minute, start_to_end)

    def initiate_start_and_goal(self, init_minute, start_to_end):
        if start_to_end:
            self.start = ((0, 1), init_minute)
            self.goal = (self.open_height + 1, self.open_width)
        else:
            self.start = ((self.open_height + 1, self.open_width), init_minute)
            self.goal = (0, 1)

    def clear_map(self, blizzard_map):
        empty_map = deepcopy(blizzard_map)
        for x, row in enumerate(empty_map):
            for y, value in enumerate(row):
                if value not in [".", "#"]:
                    empty_map[x][y] = "."
        return empty_map

    def get_blizzards(self):
        blizzards = []
        for x, row in enumerate(self.map_over_time[0]):
            for y, value in enumerate(row):
                if value not in ["#", "."]:
                    blizzards.append((value, (x, y)))
        return blizzards

    def update_map(self, time):
        updated_map = deepcopy(self.empty_map)
        for blizzard in self.init_blizzards:
            value = blizzard[0]
            x = blizzard[1][0] - 1
            y = blizzard[1][1] - 1
            if value == "^":
                new_x = ((x - time) % self.open_height) + 1
                new_y = y + 1
            if value == "v":
                new_x = ((x + time) % self.open_height) + 1
                new_y = y + 1
            if value == ">":
                new_x = x + 1
                new_y = ((y + time) % self.open_width) + 1
            if value == "<":
                new_x = x + 1
                new_y = ((y - time) % self.open_width) + 1

            if updated_map[new_x][new_y] in ["^", "v", ">", "<"]:
                updated_map[new_x][new_y] = "X"
            if updated_map[new_x][new_y] == ".":
                updated_map[new_x][new_y] = value

        self.map_over_time[time] = updated_map

    def manhattan_distance_from_goal(self, node):
        x = node[0][0]
        y = node[0][1]
        return abs(self.goal[0] - x) + abs(self.goal[1] - y)

    def get_lowest_fscore_state(self, nodes):
        fscore = []
        for node in nodes:
            mdist = self.manhattan_distance_from_goal(node)
            fscore.append(mdist + 10 * node[1])
        lowest_index = fscore.index(min(fscore))
        return nodes[lowest_index]

    def get_new_nodes(self, node):
        time = node[1] + 1
        if time not in self.map_over_time.keys():
            self.update_map(time)
        current_map = self.map_over_time[time]

        x = node[0][0]
        y = node[0][1]
        new_nodes = []
        possible_nodes = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x, y)]
        for new_node in possible_nodes:
            if new_node[0] >= self.open_height + 2:
                continue
            if current_map[new_node[0]][new_node[1]] == ".":
                new_nodes.append((new_node, time))
        return new_nodes

    def path_algorithm(self):
        discovered_nodes = [self.start]

        while discovered_nodes:
            current = self.get_lowest_fscore_state(discovered_nodes)
            if current[0] == self.goal:
                return current[1] - self.init_minute
            discovered_nodes.remove(current)

            for new_node in self.get_new_nodes(current):
                if new_node not in discovered_nodes:
                    discovered_nodes.append(new_node)


def main():
    blizzard_map = parse_input("input.txt")
    bpf = BlizzardPathFinder(blizzard_map, init_minute=0, start_to_end=True)
    time_spent = bpf.path_algorithm()
    print(time_spent)
    bpf = BlizzardPathFinder(blizzard_map, init_minute=time_spent, start_to_end=False)
    time_spent += bpf.path_algorithm()
    print(time_spent)
    bpf = BlizzardPathFinder(blizzard_map, init_minute=time_spent, start_to_end=True)
    time_spent += bpf.path_algorithm()
    print(time_spent)


if __name__ == "__main__":
    main()
