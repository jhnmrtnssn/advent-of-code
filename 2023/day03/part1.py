# Advent of Code - Day 3
# Part 1


def connected_position(pos1, pos2):
    return pos1[0] == pos2[0] and pos1[1] == pos2[1] - 1


class SchematicHandler:
    def __init__(self, schematic):
        self.schematic = schematic
        self.symbol_positions = self.get_symbol_positions()
        self.connected_digits = self.get_all_connected_digits()
        self.connected_values = self.get_all_connected_values()

    def inside_schematic(self, x, y) -> bool:
        if x >= 0 and x < len(self.schematic):
            if y >= 0 and y < len(self.schematic[0]):
                return True
        return False

    def get_symbol_positions(self):
        symbol_positions = []
        for x, row in enumerate(self.schematic):
            for y, value in enumerate(row):
                if not value.isdigit() and value != ".":
                    symbol_positions.append([x, y])
        return symbol_positions

    def get_surrounding_values(self, pos):
        x_vals = [pos[0] - 1, pos[0], pos[0] + 1]
        y_vals = [pos[1] - 1, pos[1], pos[1] + 1]

        surrounding_digits = []
        for x in x_vals:
            for y in y_vals:
                if x == pos[0] and y == pos[1]:
                    continue
                if self.inside_schematic(x, y):
                    if self.schematic[x][y].isdigit():
                        surrounding_digits.append([x, y])
        return surrounding_digits

    def get_all_connected_digits(self):
        connected_digit_positions = []
        scanned_positions = []
        for symbol in self.symbol_positions:
            surrounded_digits = self.get_surrounding_values(symbol)
            for digit in surrounded_digits:
                if digit not in connected_digit_positions:
                    connected_digit_positions.append(digit)

        i = 0
        while len(scanned_positions) != len(connected_digit_positions):
            scanned_positions.append(connected_digit_positions[i])
            connected_digits = self.get_surrounding_values(scanned_positions[i])
            for digit in connected_digits:
                if digit not in connected_digit_positions:
                    connected_digit_positions.append(digit)
            i += 1

        connected_digit_positions.sort()
        return connected_digit_positions

    def get_all_connected_values(self):
        connected_values_pos = []
        value = []
        for i, digit_pos in enumerate(self.connected_digits):
            if not value:
                value.append(digit_pos)
                continue
            prev_digit_pos = self.connected_digits[i - 1]
            if connected_position(prev_digit_pos, digit_pos):
                value.append(digit_pos)
            else:
                connected_values_pos.append(value)
                value = [digit_pos]

        # Last value gets appended
        connected_values_pos.append(value)

        return connected_values_pos

    def calc_sum_of_part_numbers(self):
        # Convert values pos to values
        connected_values = []
        for value_positions in self.connected_values:
            value = ""
            for x, y in value_positions:
                value += self.schematic[x][y]
            connected_values.append(int(value))
        print(sum(connected_values))


def parse_input(file):
    schematic = []
    with open(file, "r", encoding="utf-8") as f:
        for line in f.readlines():
            row = []
            for char in line.strip():
                row.append(char)
            schematic.append(row)
    return schematic


def main():
    schematic = parse_input("input.txt")
    sh = SchematicHandler(schematic)
    sh.calc_sum_of_part_numbers()


if __name__ == "__main__":
    main()
