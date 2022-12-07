# Advent of Code - Day 4
# Part 1


class ElfRange:
    def __init__(self, lower_bound, upper_bound):
        self.lb = int(lower_bound)
        self.ub = int(upper_bound)


def parse_input(file):
    data = []
    for line in open(file):
        pair = line.strip().split(",")
        elf_pair = []
        for e in pair:
            lb, ub = e.split("-")
            elf_pair.append(ElfRange(lb, ub))
        data.append(elf_pair)
    return data


def is_fully_contained(e1: ElfRange, e2: ElfRange):
    return (e1.lb <= e2.lb and e1.ub >= e2.ub) or (e2.lb <= e1.lb and e2.ub >= e1.ub)


def get_contained_range_number(data):
    n_contained_range = 0
    for pair in data:
        if is_fully_contained(pair[0], pair[1]):
            n_contained_range += 1
    return n_contained_range


def main():
    data = parse_input("input.txt")
    print(get_contained_range_number(data))


if __name__ == "__main__":
    main()
