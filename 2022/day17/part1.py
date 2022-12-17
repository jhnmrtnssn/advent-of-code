# Advent of Code - Day 17
# Part 1


def parse_input(file):
    for line in open(file):
        moves = line.strip()
    return moves


class Rock:
    def __init__(self, rtype):
        self.type = rtype
        self.left_alignment = 2
        self.empty_height = 3
        self.width = 7
        self.block = []
        self.add_empty_rows(3)
        self.spawn()

    def spawn(self):
        match self.type:
            # Shape: ----
            case 0:
                self.add_empty_rows(1)
                for i in range(4):
                    self.block[0][self.left_alignment + i] = "@"
            # Shape: +
            case 1:
                self.add_empty_rows(3)
                self.block[0][self.left_alignment + 1] = "@"
                for i in range(3):
                    self.block[1][self.left_alignment + i] = "@"
                self.block[2][self.left_alignment + 1] = "@"
            # Shape _|
            case 2:
                self.add_empty_rows(3)
                self.block[0][self.left_alignment + 2] = "@"
                self.block[1][self.left_alignment + 2] = "@"
                for i in range(3):
                    self.block[2][self.left_alignment + i] = "@"
            # Shape |
            case 3:
                self.add_empty_rows(4)
                for i in range(4):
                    self.block[i][self.left_alignment] = "@"
            # Shape []
            case 4:
                self.add_empty_rows(2)
                for i in range(2):
                    for j in range(2):
                        self.block[i][self.left_alignment + j] = "@"

    def add_empty_rows(self, n_rows):
        for _ in range(n_rows):
            self.block.append(self.width * ["."])


class Tetris:
    def __init__(self, data):
        self.moves = list(data)
        self.turn = 0
        self.block_type = 0
        self.width = 7
        self.landed = False
        self.map = [["#"] * self.width]

    def move_block(self, moving_down):
        if moving_down:
            direction = "v"
        else:
            direction = self.moves[self.turn]
            self.turn += 1
            if self.turn == len(self.moves):
                self.turn = 0

        block = self.get_block()

        moving = True
        for part in block:
            if not self.can_move(part, direction):
                moving = False
                if moving_down:
                    self.landed = True
        if moving:
            new_block = []
            for part in block:
                new_block.append(self.get_new_part(part, direction))
                self.map[part[0]][part[1]] = "."
            for part in new_block:
                self.map[part[0]][part[1]] = "@"

    def get_new_part(self, part, direction):
        if direction == "<":
            return [part[0], part[1] - 1]
        if direction == ">":
            return [part[0], part[1] + 1]
        return [part[0] + 1, part[1]]

    def can_move(self, part, direction):
        if direction == "<":
            if part[1] == 0:
                return False
            if self.map[part[0]][part[1] - 1] == "#":
                return False
        if direction == ">":
            if part[1] == 6:
                return False
            if self.map[part[0]][part[1] + 1] == "#":
                return False
        if direction == "v":
            if self.map[part[0] + 1][part[1]] == "#":
                return False
        return True

    def spawn_block(self):
        new_block = Rock(self.block_type).block
        for row in reversed(new_block):
            self.map.insert(0, row)
        self.block_type += 1
        if self.block_type == 5:
            self.block_type = 0

    def get_block(self):
        block = []
        for x, row in enumerate(self.map):
            for y, value in enumerate(row):
                if value == "@":
                    block.append([x, y])
        return block

    def clean_up_map(self):
        # Set all moving blocks to solid ground
        block = self.get_block()
        for part in block:
            self.map[part[0]][part[1]] = "#"
        # Remove empty rows from top
        n_rows_to_remove = 0
        for row in self.map:
            if "#" not in row:
                n_rows_to_remove += 1
            else:
                break
        for _ in range(n_rows_to_remove):
            self.map.pop(0)

    def play_number_of_rounds(self, n_rounds):
        played_rounds = 0
        while played_rounds < n_rounds:
            self.spawn_block()
            self.landed = False
            while not self.landed:
                self.move_block(moving_down=False)
                self.move_block(moving_down=True)
            self.clean_up_map()
            played_rounds += 1

    def get_tower_height(self):
        return len(self.map) - 1


def main():
    data = parse_input("input.txt")
    tetris = Tetris(data)
    tetris.play_number_of_rounds(2022)
    print(tetris.get_tower_height())


if __name__ == "__main__":
    main()
