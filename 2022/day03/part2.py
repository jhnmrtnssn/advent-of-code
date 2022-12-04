# Advent of Code - Day 1
# Part 1


def parse_input(file):
    data = []
    group = []
    for index, line in enumerate(open(file)):
        b = []
        for char in line.strip():
            b.append(char)
        group.append(b)
        if index % 3 == 2:
            data.append(group)
            group = []

    return data


def get_priority_value(c):
    lower_case = [*"abcdefghijklmnopqrstuvwxyz"]
    upper_case = [*"ABCDEFGHIJKLMNOPQRSTUVWXYZ"]

    if c in lower_case:
        return lower_case.index(c) + 1
    return len(lower_case) + upper_case.index(c) + 1


def find_common_char(b1, b2, b3):
    common_items = []
    for char in b1:
        if char in b2:
            common_items.append(char)
    for char in common_items:
        if char in b3:
            return char
    return "UNREACHABLE STATE"


def calculate_rucksack_sum(data):
    total_sum = 0
    for group in data:
        c = find_common_char(group[0], group[1], group[2])
        total_sum += get_priority_value(c)
    return total_sum


def main():
    data = parse_input("input.txt")
    print(calculate_rucksack_sum(data))


if __name__ == "__main__":
    main()
