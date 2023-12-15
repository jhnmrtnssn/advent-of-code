# Advent of Code - Day 15
# Part 1


def parse_input(file):
    with open(file, "r", encoding="utf-8") as f:
        for line in f.readlines():
            sequence = line.strip().split(",")

    return sequence


def calc_hash_value(ascii_string):
    value = 0
    for char in ascii_string:
        value += ord(char)
        value *= 17
        value = value % 256
    return value


def calc_sequence_hash_value(sequence):
    values = []
    for ascii_string in sequence:
        values.append(calc_hash_value(ascii_string))
    print(sum(values))


def main():
    sequence = parse_input("input.txt")
    calc_sequence_hash_value(sequence)


if __name__ == "__main__":
    main()
