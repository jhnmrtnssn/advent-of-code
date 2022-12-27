# Advent of Code - Day 25
# Part 1


from math import floor


def parse_input(file):
    snafu_numbers = []
    with open(file, "r", encoding="utf-8") as f:
        for line in f.readlines():
            snafu_numbers.append(line.strip())
    return snafu_numbers


class SNAFUAdder:
    def __init__(self, snafu_numbers):
        self.snafu_numbers = snafu_numbers

    def sum_all_snafu_to_decimal(self):
        decimal_sum = 0
        for snafu_num in self.snafu_numbers:
            decimal_sum += self.convert_snafu_to_decimal(snafu_num)
        return decimal_sum

    def convert_snafu_to_decimal(self, snafu_number):
        decimal_number = 0
        for pos, digit in enumerate(reversed(list(snafu_number))):
            if digit.isnumeric():
                decimal_number += int(digit) * (5**pos)
            elif digit == "-":
                decimal_number -= 5**pos
            elif digit == "=":
                decimal_number -= 2 * (5**pos)
        return decimal_number

    def convert_decimal_to_snafu(self, decimal_number):
        digit_pos = 0
        snafu_exponents = []
        while True:
            snafu_digit_value = 5**digit_pos
            value_bigger = decimal_number >= snafu_digit_value
            if not value_bigger:
                break
            snafu_exponents.append(snafu_digit_value)
            digit_pos += 1

        n_times_exponents = []
        for exponent in reversed(snafu_exponents):
            n_times_in_decimal = floor(decimal_number / exponent)
            n_times_exponents.append(n_times_in_decimal)
            decimal_number -= n_times_in_decimal * exponent

        snafu_number = []
        for snafu_pos, value in enumerate(reversed(n_times_exponents)):
            if len(snafu_number) == snafu_pos:
                snafu_number.append(value)
            else:
                snafu_number[snafu_pos] += value
            if snafu_number[snafu_pos] == 3:
                snafu_number.append(1)
                snafu_number[snafu_pos] = "="
            if snafu_number[snafu_pos] == 4:
                snafu_number.append(1)
                snafu_number[snafu_pos] = "-"
            if snafu_number[snafu_pos] == 5:
                snafu_number.append(1)
                snafu_number[snafu_pos] = 0
        snafu_number.reverse()
        for i, char in enumerate(snafu_number):
            snafu_number[i] = str(char)

        print("".join(snafu_number))


def main():
    snafu_numbers = parse_input("input.txt")
    sa = SNAFUAdder(snafu_numbers)
    decimal_number = sa.sum_all_snafu_to_decimal()
    sa.convert_decimal_to_snafu(decimal_number)


if __name__ == "__main__":
    main()
