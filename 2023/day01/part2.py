# Advent of Code - Day 1
# Part 2

from typing import List

string_digits = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def parse_input(file):
    calibration_lines = []
    with open(file, "r", encoding="utf-8") as f:
        for line in f.readlines():
            calibration_line = []
            for char in line:
                calibration_line.append(char)
            calibration_lines.append(calibration_line)
    return calibration_lines


def get_first_digit(line: List[str], reverse_order=False) -> int:
    if reverse_order:
        line.reverse()

    # First real digit
    digit_index = 10000  # Arbitrarily high number
    for i, char in enumerate(line):
        if char.isdigit():
            digit = int(char)
            digit_index = i
            break

    # First string digit
    string_digit_index = 10000  # Arbitrarily high number
    for value, string_digit in enumerate(string_digits):
        if reverse_order:
            string_digit = string_digit[::-1]

        string_line = "".join(line)
        if string_digit in string_line:
            index = string_line.find(string_digit)
            if index < string_digit_index:
                string_digit_index = index
                string_digit_value = value

    if digit_index > string_digit_index:
        return string_digit_value

    return digit


def get_calibration_value(line: List[str]) -> int:
    return 10 * get_first_digit(line) + get_first_digit(line, reverse_order=True)


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
