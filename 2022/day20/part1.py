# Advent of Code - Day 20
# Part 1


from copy import deepcopy


def parse_input(file):
    data = []
    with open(file, "r", encoding="utf-8") as f:
        for i, line in enumerate(f.readlines()):
            data.append((i + 1, int(line.strip())))
    return data


class Decrypter:
    def __init__(self, data):
        self.original_array = deepcopy(data)
        self.rearranged_array = deepcopy(data)
        self.length = len(data) - 1

    def move_digit(self, unit):
        value = unit[1]
        pos = self.rearranged_array.index(unit)
        new_pos = pos + value
        if not 0 <= new_pos < self.length:
            new_pos = new_pos % self.length
        if new_pos == 0:
            new_pos = self.length
        self.rearranged_array.pop(pos)
        self.rearranged_array.insert(new_pos, unit)

    def move_all_digits(self):
        for unit in self.original_array:
            self.move_digit(unit)

    def get_zero_value_pos(self):
        for pos, value in enumerate(self.rearranged_array):
            if value[1] == 0:
                return pos
        return "UNREACHABLE STATE"

    def get_coordinates(self):
        coords = []
        zero_pos = self.get_zero_value_pos()
        for pos in [zero_pos + 1000, zero_pos + 2000, zero_pos + 3000]:
            if pos > self.length:
                pos = pos % (self.length + 1)
            coords.append(self.rearranged_array[pos][1])
        print(sum(coords))


def main():
    data = parse_input("input.txt")
    d = Decrypter(data)
    d.move_all_digits()
    d.get_coordinates()


if __name__ == "__main__":
    main()
