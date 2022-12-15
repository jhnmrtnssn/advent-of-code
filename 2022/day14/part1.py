# Advent of Code - Day 14
# Part 1

from copy import deepcopy


def parse_input(file):
    walls = []
    for line in open(file):
        edges = line.strip().split(" -> ")
        wall = []
        for edge in edges:
            edge = (int(edge.split(",")[0]), int(edge.split(",")[1]))
            wall.append(edge)
            if len(wall) == 2:
                walls.append(deepcopy(wall))
                wall.pop(0)
    return walls


class SandProducer:
    def __init__(self, walls):
        self.walls = walls
        self.initialize_range_and_empty_map(walls)
        self.source = self.norm_coord((500, 0))
        self.number_of_sand = 0
        self.build_map()

    def initialize_range_and_empty_map(self, walls):
        self.x_range = [0, walls[0][0][1]]
        self.y_range = [walls[0][0][0], walls[0][0][0]]
        for wall_pair in walls:
            for edge in wall_pair:
                if edge[1] < self.x_range[0]:
                    self.x_range[0] = edge[1]
                if edge[1] > self.x_range[1]:
                    self.x_range[1] = edge[1]
                if edge[0] < self.y_range[0]:
                    self.y_range[0] = edge[0]
                if edge[0] > self.y_range[1]:
                    self.y_range[1] = edge[0]
        self.map = [
            ["."] * (self.y_range[1] - self.y_range[0] + 2)
            for _ in range(self.x_range[0], self.x_range[1] + 2)
        ]

    def norm_coord(self, edge):
        x = edge[1] - self.x_range[0]
        y = edge[0] - self.y_range[0]
        return (x, y)

    def build_map(self):
        self.map[self.source[0]][self.source[1]] = "+"
        for wall_pair in self.walls:
            start = self.norm_coord(wall_pair[0])
            end = self.norm_coord(wall_pair[1])
            if start[0] == end[0]:
                if start[1] < end[1]:
                    x_range = range(start[1], end[1] + 1)
                else:
                    x_range = range(end[1], start[1] + 1)
                for x in x_range:
                    self.map[start[0]][x] = "#"
            if start[1] == end[1]:
                if start[0] < end[0]:
                    y_range = range(start[0], end[0] + 1)
                else:
                    y_range = range(end[0], start[0] + 1)
                for y in y_range:
                    self.map[y][start[1]] = "#"

    def spawn_sand(self):
        sand = Sand(self.source, self.map)
        while not sand.landed:
            if sand.overflown:
                break
            sand.move()
        if sand.landed:
            self.map[sand.pos[0]][sand.pos[1]] = "o"
            self.number_of_sand += 1
        return sand.overflown

    def produce_all_sand(self):
        overflown = False
        while not overflown:
            overflown = self.spawn_sand()
        print(self.number_of_sand)
        for row in self.map:
            print("".join(map(str, row)))


class Sand:
    def __init__(self, start, sand_map):
        self.pos = [start[0], start[1]]
        self.map = sand_map
        self.depth = len(sand_map)
        self.landed = False
        self.moved = False
        self.overflown = False

    def move(self):
        # Priority 1: Move down one step
        if self.map[self.pos[0] + 1][self.pos[1]] == ".":
            if self.will_overflow("down"):
                self.overflown = True
            else:
                self.pos[0] += 1
        # Priority 2: Move diagonally down left one step
        elif self.map[self.pos[0] + 1][self.pos[1] - 1] == ".":
            if self.will_overflow("down-left"):
                self.overflown = True
            else:
                self.pos[0] += 1
                self.pos[1] -= 1
        # Priority 3: Move diagonally down left one step
        elif self.map[self.pos[0] + 1][self.pos[1] + 1] == ".":
            if self.will_overflow("down-right"):
                self.overflown = True
            else:
                self.pos[0] += 1
                self.pos[1] += 1
        # Priority 4: No available moves
        else:
            self.landed = True

    def will_overflow(self, direction):
        overflow_x = self.pos[0] + 1 == self.depth - 1
        if direction == "down":
            return overflow_x
        if direction == "down-left":
            return overflow_x and self.pos[0] - 1 == 0
        return overflow_x and self.pos[0] + 1 == len(self.map[0])


def main():
    data = parse_input("input.txt")
    sp = SandProducer(data)
    sp.produce_all_sand()


if __name__ == "__main__":
    main()
