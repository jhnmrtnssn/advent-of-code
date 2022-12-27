# Advent of Code - Day 22
# Part 1


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

    def get_initial_position(self):
        for x, row in enumerate(self.map):
            for y, value in enumerate(row):
                if value == ".":
                    return [x, y]
        return "UNREACHABLE STATE"

    def turn(self, turn_direction):
        if turn_direction == "R":
            self.direction += 1
        else:
            self.direction -= 1
        self.direction = self.direction % 4

    def find_next_nonvoid_space(self, x, y):
        if self.direction == RIGHT:
            for next_y, _ in enumerate(self.map[x]):
                if self.map[x][next_y] != "X":
                    return [x, next_y]
        if self.direction == DOWN:
            for next_x, _ in enumerate(self.map):
                if self.map[next_x][y] != "X":
                    return [next_x, y]
        if self.direction == LEFT:
            for next_y in reversed(range(len(self.map[x]))):
                if self.map[x][next_y] != "X":
                    return [x, next_y]
        if self.direction == UP:
            for next_x in reversed(range(len(self.map))):
                if self.map[next_x][y] != "X":
                    return [next_x, y]
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
            tile = self.find_next_nonvoid_space(x, y)
            if self.map[tile[0]][tile[1]] == ".":
                self.pos = [tile[0], tile[1]]
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
