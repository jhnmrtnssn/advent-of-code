# Advent of Code - Day 12
# Part 1

from typing import List

placeable_items = ["?", "#"]


class SpringRow:
    def __init__(self, row, group):
        self.n_arrangements = 0
        self.get_arrangements(row, group)

    def subgroup_can_be_placed(self, row, spring_length, i):
        # If any operational (.) in subgroup placement, can't be placed
        if "." in row[i : i + spring_length]:
            return False
        # If any previous space after subgroup is broken (#), cant be placed
        if "#" in row[0:i]:
            return False
        # If there is no last element, it can be placed
        if len(row) == i + spring_length:
            return True
        # If next space after subgroup is broken (#), cant be placed
        if row[i + spring_length] == "#":
            return False

        return True

    def get_arrangements(self, row, group):
        spring_length = group[0]
        for i, _ in enumerate(row):
            if len(row) < i + spring_length:
                break
            if self.subgroup_can_be_placed(row, spring_length, i):
                if len(group) == 1:
                    if "#" not in row[i + spring_length + 1 :]:
                        self.n_arrangements += 1
                    continue
                new_row = row[i + spring_length + 1 :]
                new_group = group[1:]
                self.get_arrangements(new_row, new_group)


def sum_all_arrangements(spring_rows: List[SpringRow]):
    n_arrangements = 0
    for spring_row in spring_rows:
        n_arrangements += spring_row.n_arrangements
    print(n_arrangements)


def parse_input(file):
    spring_rows = []
    with open(file, "r", encoding="utf-8") as f:
        for line in f.readlines():
            row, group = line.strip().split()
            group = list(map(int, group.split(",")))
            spring_rows.append(SpringRow(list(row), group))
    return spring_rows


def main():
    spring_rows = parse_input("input.txt")
    sum_all_arrangements(spring_rows)


if __name__ == "__main__":
    main()
