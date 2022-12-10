# Advent of Code - Day 7
# Part 1


def parse_input(file):
    data = []
    for line in open(file):
        direction, length = line.strip().split(" ")
        data.append((direction, int(length)))
    return data


class RopeSimulator:
    def __init__(self, data):
        self.movements = data
        self.head = [0, 0]
        self.tail = [[0, 0] for i in range(9)]
        self.unique_position = [(0, 0)]

    def move_head_one_step(self, direction):
        if direction == "U":
            self.head[1] += 1
        if direction == "D":
            self.head[1] -= 1
        if direction == "L":
            self.head[0] -= 1
        if direction == "R":
            self.head[0] += 1

    def move_part_horizontal(self, diff, index):
        if diff > 0:
            self.tail[index][0] += 1
        else:
            self.tail[index][0] -= 1

    def move_part_vertical(self, diff, index):
        if diff > 0:
            self.tail[index][1] += 1
        else:
            self.tail[index][1] -= 1

    def move_part_one_step(self, p1, index):
        diff_x = p1[0] - self.tail[index][0]
        diff_y = p1[1] - self.tail[index][1]
        if diff_x != 0 and diff_y != 0:
            self.move_part_horizontal(diff_x, index)
            self.move_part_vertical(diff_y, index)
        elif diff_x != 0:
            self.move_part_horizontal(diff_x, index)
        elif diff_y != 0:
            self.move_part_vertical(diff_y, index)

    def add_unique_position(self):
        if (self.tail[-1][0], self.tail[-1][1]) not in self.unique_position:
            self.unique_position.append((self.tail[-1][0], self.tail[-1][1]))

    def move_rope(self):
        for direction, length in self.movements:
            for _ in range(length):
                self.move_head_one_step(direction)
                for i, part in enumerate(self.tail):
                    if i == 0:
                        p1 = self.head
                    else:
                        p1 = self.tail[i - 1]
                    if not tail_in_vicinity(p1, part):
                        self.move_part_one_step(p1, i)
                self.add_unique_position()
        print(len(self.unique_position))


def tail_in_vicinity(p1, p2):
    for x in [p1[0] - 1, p1[0], p1[0] + 1]:
        for y in [p1[1] - 1, p1[1], p1[1] + 1]:
            if p2 == [x, y]:
                return True
    return False


def main():
    data = parse_input("input.txt")
    rs = RopeSimulator(data)
    rs.move_rope()


if __name__ == "__main__":
    main()
