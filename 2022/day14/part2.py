# Advent of Code - Day 14
# Part 2

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
        self.added_left = 0
        self.number_of_sand = 0
        self.initialize_range_and_empty_map(walls)
        self.source = self.norm_coord((500, 0))
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
            ["."] * (self.y_range[1] - self.y_range[0] + 3)
            for _ in range(self.x_range[0], self.x_range[1] + 3)
        ]

    def norm_coord(self, edge):
        x = edge[1] - self.x_range[0]
        y = edge[0] - self.y_range[0] + self.added_left
        return (x, y)

    def build_map(self):
        self.map[self.source[0]][self.source[1]] = "+"
        self.map[-1] = ["#"] * len(self.map[-1])
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

    def add_column(self, side):
        position = 0 if side == "left" else -1
        if side == "left":
            self.added_left += 1
            self.source = (self.source[0], self.source[1] + 1)
        for row in self.map:
            row.insert(position, ".")
        if position == -1:
            position -= 1
        self.map[-1][position] = "#"

    def spawn_sand(self):
        sand = Sand(self.source, self.map)
        while not sand.ended:
            sand.move()
        if sand.add_side:
            self.add_column(sand.add_side)
            sand.update_map(self.map)
        if sand.landed:
            self.map[sand.pos[0]][sand.pos[1]] = "o"
            self.number_of_sand += 1
        return sand.overflown

    def produce_all_sand(self):
        overflown = False
        while not overflown:
            overflown = self.spawn_sand()
        print(self.number_of_sand)


class Sand:
    def __init__(self, start, sand_map):
        self.start = start
        self.pos = [start[0], start[1]]
        self.map = sand_map
        self.depth = len(sand_map)
        self.landed = False
        self.ended = False
        self.overflown = ""
        self.add_side = ""

    def update_map(self, new_map):
        self.map = new_map

    def move(self):
        # Priority 1: Move down one step
        if self.map[self.pos[0] + 1][self.pos[1]] == ".":
            self.pos[0] += 1
        # Priority 2: Move diagonally down left one step
        elif self.map[self.pos[0] + 1][self.pos[1] - 1] == ".":
            if self.will_overflow("down-left"):
                self.add_side = "left"
                self.ended = True
            else:
                self.pos[0] += 1
                self.pos[1] -= 1
        # Priority 3: Move diagonally down left one step
        elif self.map[self.pos[0] + 1][self.pos[1] + 1] == ".":
            if self.will_overflow("down-right"):
                self.add_side = "right"
                self.ended = True
            else:
                self.pos[0] += 1
                self.pos[1] += 1
        # Priority 4: No available moves
        else:
            self.ended = True
            self.landed = True
        # End if we've overflown the start
        if (self.pos[0], self.pos[1]) == self.start:
            self.overflown = True

    def will_overflow(self, direction):
        if direction == "down-left":
            return self.pos[1] == 0
        return self.pos[1] == len(self.map[0]) - 2


def main():
    data = parse_input("input.txt")
    sp = SandProducer(data)
    sp.produce_all_sand()


if __name__ == "__main__":
    main()
