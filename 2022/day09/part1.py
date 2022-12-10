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
        self.tail = [0, 0]
        self.unique_position = [self.tail]

    def move_head_one_step(self, direction):
        if direction == "U":
            self.head[1] += 1
        if direction == "D":
            self.head[1] -= 1
        if direction == "L":
            self.head[0] -= 1
        if direction == "R":
            self.head[0] += 1

    def tail_in_vicinity(self):
        for x in [self.head[0] - 1, self.head[0], self.head[0] + 1]:
            for y in [self.head[1] - 1, self.head[1], self.head[1] + 1]:
                if self.tail == [x, y]:
                    return True
        return False

    def move_tail_horizontal(self, diff):
        if diff > 0:
            self.tail[0] += 1
        else:
            self.tail[0] -= 1

    def move_tail_vertical(self, diff):
        if diff > 0:
            self.tail[1] += 1
        else:
            self.tail[1] -= 1

    def move_tail_one_step(self):
        diff_x = self.head[0] - self.tail[0]
        diff_y = self.head[1] - self.tail[1]
        if diff_x != 0 and diff_y != 0:
            self.move_tail_horizontal(diff_x)
            self.move_tail_vertical(diff_y)
        elif diff_x != 0:
            self.move_tail_horizontal(diff_x)
        elif diff_y != 0:
            self.move_tail_vertical(diff_y)

    def add_unique_position(self):
        if (self.tail[0], self.tail[1]) not in self.unique_position:
            self.unique_position.append((self.tail[0], self.tail[1]))

    def move_rope(self):
        for direction, length in self.movements:
            for _ in range(length):
                self.move_head_one_step(direction)
                if not self.tail_in_vicinity():
                    self.move_tail_one_step()
                    self.add_unique_position()
        print(len(self.unique_position))


def main():
    data = parse_input("input.txt")
    rs = RopeSimulator(data)
    rs.move_rope()


if __name__ == "__main__":
    main()
