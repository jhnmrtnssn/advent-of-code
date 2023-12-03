# Advent of Code - Day 3
# Part 2


def connected_position(pos1, pos2):
    return pos1[0] == pos2[0] and pos1[1] == pos2[1] - 1


class SchematicHandler:
    def __init__(self, schematic):
        self.schematic = schematic
        self.gear_positions = self.get_gear_positions()
        self.connected_digits = self.get_all_connected_digits()
        self.connected_values = self.get_all_connected_values()
        self.gear_values = self.get_connected_values_to_gear()

    def inside_schematic(self, x, y) -> bool:
        if x >= 0 and x < len(self.schematic):
            if y >= 0 and y < len(self.schematic[0]):
                return True
        return False

    def get_gear_positions(self):
        gear_positions = []
        for x, row in enumerate(self.schematic):
            for y, value in enumerate(row):
                if value == "*":
                    gear_positions.append([x, y])
        return gear_positions

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
        for gear in self.gear_positions:
            surrounded_digits = self.get_surrounding_values(gear)
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

    def get_connected_values_to_gear(self):
        gear_values = []
        for gear in self.gear_positions:
            gear_value = []
            connected_gear_values_pos = self.get_surrounding_values(gear)
            for x, y in connected_gear_values_pos:
                for connected_value in self.connected_values:
                    if [x, y] in connected_value:
                        if connected_value not in gear_value:
                            gear_value.append(connected_value)

            gear_values.append(gear_value)

        return gear_values

    def calc_gear_ratio(self):
        gear_ratio = 0
        for connected_values in self.gear_values:
            if len(connected_values) == 2:
                values = []
                for value_positions in connected_values:
                    value = ""
                    for x, y in value_positions:
                        value += self.schematic[x][y]
                    values.append(int(value))
                gear_ratio += values[0] * values[1]
        print(gear_ratio)


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
    sh.calc_gear_ratio()


if __name__ == "__main__":
    main()
