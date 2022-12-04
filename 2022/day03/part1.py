# Advent of Code - Day 1
# Part 1


def parse_input(file):
    data = []
    for line in open(file):
        split_content_index = (len(line.strip()) - 1) / 2
        b1 = []
        b2 = []
        for i, char in enumerate(line.strip()):
            if i <= split_content_index:
                b1.append(char)
            else:
                b2.append(char)
        data.append((b1, b2))
    return data


def get_priority_value(c):
    lower_case = [*"abcdefghijklmnopqrstuvwxyz"]
    upper_case = [*"ABCDEFGHIJKLMNOPQRSTUVWXYZ"]

    if c in lower_case:
        return lower_case.index(c) + 1
    return len(lower_case) + upper_case.index(c) + 1


def find_common_char(b1, b2):
    for char in b1:
        if char in b2:
            return char
    return "UNREACHABLE STATE"


def calculate_rucksack_sum(data):
    total_sum = 0
    for rucksack in data:
        c = find_common_char(rucksack[0], rucksack[1])
        total_sum += get_priority_value(c)
    return total_sum


def main():
    data = parse_input("input.txt")
    print(calculate_rucksack_sum(data))


if __name__ == "__main__":
    main()
