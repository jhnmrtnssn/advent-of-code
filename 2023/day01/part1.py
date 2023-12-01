# Advent of Code - Day 1
# Part 1


def parse_input(file):
    calibration_lines = []
    with open(file, "r", encoding="utf-8") as f:
        for line in f.readlines():
            calibration_line = []
            for char in line:
                calibration_line.append(char)
            calibration_lines.append(calibration_line)
    return calibration_lines

def get_first_digit(line):
    for char in line:
        if char.isdigit():
            return int(char)

def get_calibration_value(line):
    return 10 * get_first_digit(line) + get_first_digit(reversed(line))

def calc_total_calibration_value(lines):
    calibration_value = 0
    for line in lines:
        calibration_value += get_calibration_value(line)
    print(calibration_value)

def main():
    lines = parse_input("input.txt")
    calc_total_calibration_value(lines)

if __name__ == "__main__":
    main()
