# Advent of Code - Day 22
# Part 2


def parse_input(file):
    board_map = []
    instructions = []
    width = 0
    with open(file, "r", encoding="utf-8") as f:
        for line in f.readlines():
            if len(list(line)) > width:
                if not line[0].isdigit():
                    width = len(list(line)) - 1

    with open(file, "r", encoding="utf-8") as f:
        board_map.append(["X"] * (width + 2))
        for line in f.readlines():
            line = list(line)[:-1]
            if len(line) > 0 and line[0].isdigit():
                new_digit = []
                for char in line:
                    if char.isdigit():
                        new_digit.append(char)
                    else:
                        instructions.append(int("".join(new_digit)))
                        new_digit = []
                        instructions.append(char)
                if new_digit:
                    instructions.append(int("".join(new_digit)))
                break

            line_width = len(line)
            for y in range(width):
                if y >= line_width:
                    line.append("X")
                elif line[y] == " ":
                    line[y] = "X"
            line.insert(0, "X")
            line.append("X")
            board_map.append(line)

    return board_map, instructions


RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3


class MapTraveller:
    def __init__(self, board_map, instructions):
        self.map = board_map
        self.instructions = instructions
        self.pos = self.get_initial_position()
        self.direction = RIGHT
        self.cube_paths = self.define_cube_movement()
        self.rx = [1, 51, 101, 151, 201]
        self.ry = [1, 51, 101, 151]

    def get_initial_position(self):
        for x, row in enumerate(self.map):
            for y, value in enumerate(row):
                if value == ".":
                    return [x, y]
        return "UNREACHABLE STATE"

    def define_cube_movement(self):
        paths = {}
        paths[1] = {RIGHT: (3, UP), DOWN: (6, DOWN), LEFT: (5, DOWN)}
        paths[2] = {LEFT: (5, RIGHT), UP: (4, RIGHT)}
        paths[3] = {RIGHT: (6, LEFT), DOWN: (1, LEFT)}
        paths[4] = {RIGHT: (6, UP), LEFT: (2, DOWN)}
        paths[5] = {LEFT: (2, RIGHT), UP: (1, RIGHT)}
        paths[6] = {RIGHT: (3, LEFT), DOWN: (4, LEFT), UP: (1, UP)}
        return paths

    def turn(self, turn_direction):
        if turn_direction == "R":
            self.direction += 1
        else:
            self.direction -= 1
        self.direction = self.direction % 4

    # NOT TESTED
    def get_region_from_position(self):
        x = self.pos[0]
        y = self.pos[1]
        rx = self.rx
        ry = self.ry

        if ry[0] <= y < ry[1]:
            if rx[3] <= x < rx[4]:
                return 1
            if rx[2] <= x < rx[3]:
                return 2
        elif ry[1] <= y < ry[2]:
            if rx[2] <= x < rx[3]:
                return 3
            if rx[1] <= x < rx[2]:
                return 4
            if rx[0] <= x < rx[1]:
                return 5
        elif ry[2] <= y < ry[3]:
            if rx[0] <= x < rx[1]:
                return 6
        return "UNREACHABLE STATE"

    def get_position_from_region(self, region):
        rx = self.rx
        ry = self.ry

        if region == 1:
            return rx[3], ry[0]
        if region == 2:
            return rx[2], ry[0]
        if region == 3:
            return rx[2], ry[1]
        if region == 4:
            return rx[1], ry[1]
        if region == 5:
            return rx[0], ry[1]
        if region == 6:
            return rx[0], ry[2]
        return "UNREACHABLE STATE"

    def correct_alignment(self, new_direction):
        alignment_x = (self.pos[0] - 1) % 50
        alignment_y = (self.pos[1] - 1) % 50

        if abs(new_direction - self.direction) == 2:
            alignment_x = 49 - alignment_x
            alignment_y = 49 - alignment_y

        if self.direction in [RIGHT, LEFT]:
            return alignment_x
        if self.direction in [UP, DOWN]:
            return alignment_y
        return "UNREACHABLE STATE"

    def find_next_cube_space(self, x, y):
        region = self.get_region_from_position()
        new_region, new_direction = self.cube_paths[region][self.direction]
        x, y = self.get_position_from_region(new_region)
        alignment = self.correct_alignment(new_direction)

        if new_direction == RIGHT:
            for next_y, _ in enumerate(self.map[x + alignment]):
                if self.map[x + alignment][next_y] != "X":
                    return new_direction, [x + alignment, next_y]
        if new_direction == DOWN:
            for next_x, _ in enumerate(self.map):
                if self.map[next_x][y + alignment] != "X":
                    return new_direction, [next_x, y + alignment]
        if new_direction == LEFT:
            for next_y in reversed(range(len(self.map[x + alignment]))):
                if self.map[x + alignment][next_y] != "X":
                    return new_direction, [x + alignment, next_y]
        if new_direction == UP:
            for next_x in reversed(range(len(self.map))):
                if self.map[next_x][y + alignment] != "X":
                    return new_direction, [next_x, y + alignment]
        return "UNREACHABLE STATE"

    def get_next_pos(self):
        x = self.pos[0]
        y = self.pos[1]
        if self.direction == RIGHT:
            y += 1
        if self.direction == DOWN:
            x += 1
        if self.direction == LEFT:
            y -= 1
        if self.direction == UP:
            x -= 1
        return x, y

    def step(self):
        x, y = self.get_next_pos()
        if self.map[x][y] == ".":
            self.pos = [x, y]
        elif self.map[x][y] == "#":
            return False
        elif self.map[x][y] == "X":
            new_direction, tile = self.find_next_cube_space(x, y)
            if self.map[tile[0]][tile[1]] == ".":
                self.pos = [tile[0], tile[1]]
                self.direction = new_direction
            else:
                return False
        return True

    def move(self, n_units):
        for _ in range(n_units):
            can_step = self.step()
            if not can_step:
                break

    def move_with_all_instructions(self):
        for instruction in self.instructions:
            if isinstance(instruction, int):
                self.move(instruction)
            else:
                self.turn(instruction)
        print(1000 * self.pos[0] + 4 * self.pos[1] + self.direction)


def main():
    board_map, instructions = parse_input("input.txt")
    map_traveller = MapTraveller(board_map, instructions)
    map_traveller.move_with_all_instructions()


if __name__ == "__main__":
    main()
