# Advent of Code - Day 23
# Part 1


def parse_input(file):
    elves = []
    with open(file, "r", encoding="utf-8") as f:
        for x, row in enumerate(f.readlines()):
            row = row.strip()
            for y, value in enumerate(row):
                if value == "#":
                    elves.append(Elf(x, y))
    return elves


NORTH = 0
SOUTH = 1
WEST = 2
EAST = 3


class Elf:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.proposed_pos = (x, y)
        self.can_walk = False

    def get_proposed_pos(self, direction, elves_position):
        x = self.x
        y = self.y

        # Check complete surrounding
        complete_surrounding = [
            (x - 1, y - 1),
            (x - 1, y),
            (x - 1, y + 1),
            (x + 1, y),
            (x + 1, y + 1),
            (x + 1, y - 1),
            (x, y - 1),
            (x, y + 1),
        ]
        elf_in_surrounding = False
        for pos in complete_surrounding:
            if pos in elves_position:
                elf_in_surrounding = True
        if not elf_in_surrounding:
            self.proposed_pos = (x, y)
            return False

        if direction == NORTH:
            surrounding = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1)]
        if direction == SOUTH:
            surrounding = [(x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]
        if direction == WEST:
            surrounding = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1)]
        if direction == EAST:
            surrounding = [(x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]

        occupied = False
        for pos in surrounding:
            if pos in elves_position:
                occupied = True
        if not occupied:
            self.proposed_pos = surrounding[1]
            return True
        return False

    def reset_proposed_pos(self):
        self.proposed_pos = (self.x, self.y)

    def prepare(self):
        self.can_walk = True

    def move(self):
        if self.can_walk:
            self.x, self.y = self.proposed_pos
            self.can_walk = False


class ElfMovement:
    def __init__(self, elves):
        self.elves = elves
        self.elves_position = self.get_elves_position()
        self.prio_directions = [NORTH, SOUTH, WEST, EAST]

    def update_prio_direction(self):
        prev_prio = self.prio_directions.pop(0)
        self.prio_directions.append(prev_prio)

    def get_elves_position(self):
        elves_positions = []
        for elf in self.elves:
            elves_positions.append((elf.x, elf.y))
        return elves_positions

    def get_all_proposed_position(self):
        proposed_positions = []
        elves_position = self.get_elves_position()
        for elf in self.elves:
            for direction in self.prio_directions:
                can_move = elf.get_proposed_pos(direction, elves_position)
                if can_move:
                    break

            proposed_positions.append(elf.proposed_pos)
        return proposed_positions

    def two_elves_one_spot(self, proposed_positions, proposed_pos):
        occurance = 0
        for pos in proposed_positions:
            if pos == proposed_pos:
                occurance += 1
        return occurance > 1

    def move_all_elves(self):
        for elf in self.elves:
            elf.move()

    def prepare_all_elves_to_move(self, proposed_positions):
        for elf in self.elves:
            proposed_pos = elf.proposed_pos
            if not self.two_elves_one_spot(proposed_positions, proposed_pos):
                elf.prepare()

    def reset_proposed_positions(self):
        for elf in self.elves:
            elf.reset_proposed_pos()

    def round(self):
        proposed_positions = self.get_all_proposed_position()
        self.prepare_all_elves_to_move(proposed_positions)
        self.move_all_elves()
        self.update_prio_direction()
        self.reset_proposed_positions()

    def walk_amount_of_round(self, n_rounds):
        for _ in range(n_rounds):
            self.round()

    def get_elf_area(self):
        x_range = [0, 0]
        y_range = [0, 0]
        for elf in self.elves:
            if elf.x < x_range[0]:
                x_range[0] = elf.x
            if elf.x > x_range[1]:
                x_range[1] = elf.x
            if elf.y < y_range[0]:
                y_range[0] = elf.y
            if elf.y > y_range[1]:
                y_range[1] = elf.y
        x_width = x_range[1] - x_range[0] + 1
        y_width = y_range[1] - y_range[0] + 1
        area = x_width * y_width
        return area - len(self.elves)

    def debug_print_map(self):
        x_range = [0, 0]
        y_range = [0, 0]
        for elf in self.elves:
            if elf.x < x_range[0]:
                x_range[0] = elf.x
            if elf.x > x_range[1]:
                x_range[1] = elf.x
            if elf.y < y_range[0]:
                y_range[0] = elf.y
            if elf.y > y_range[1]:
                y_range[1] = elf.y
        x_width = x_range[1] - x_range[0]
        y_width = y_range[1] - y_range[0]

        elfmap = []
        for x in range(x_width + 12):
            map_row = []
            for y in range(y_width + 12):
                map_row.append(".")
            elfmap.append(map_row)

        for elf in self.elves:
            elfmap[elf.x + x_range[1]][elf.y + y_range[1]] = "#"

        for row in elfmap:
            print("".join(row))
        print(" -----------------  ")


def main():
    elves = parse_input("input.txt")
    em = ElfMovement(elves)
    em.walk_amount_of_round(n_rounds=10)
    print(em.get_elf_area())


if __name__ == "__main__":
    main()
