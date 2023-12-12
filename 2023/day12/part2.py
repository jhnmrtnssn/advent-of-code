# Advent of Code - Day 12
# Part 2

from functools import lru_cache
from typing import List

placeable_items = ["?", "#"]


def subgroup_can_be_placed(row, spring_length, i):
    # If any operational (.) in subgroup placement, can't be placed
    for value in row[i : i + spring_length]:
        if value not in placeable_items:
            return False
    # If any previous space after subgroup is broken (#), cant be placed
    for j in range(0, i):
        if row[j] == "#":
            return False
    # If there is no last element, it can be placed
    if len(row) == i + spring_length:
        return True
    # If next space after subgroup is broken (#), cant be placed
    if row[i + spring_length] == "#":
        return False

    return True


@lru_cache(maxsize=None)
def get_arrangements(state):
    n_arrangements = 0
    row, group = state
    spring_length = group[0]
    for i, _ in enumerate(row):
        if len(row) < i + spring_length:
            break
        if subgroup_can_be_placed(row, spring_length, i):
            if len(group) == 1:
                if "#" not in row[i + spring_length + 1 :]:
                    n_arrangements += 1
                continue
            new_row = row[i + spring_length + 1 :]
            new_group = group[1:]
            n_arrangements += get_arrangements((new_row, new_group))
    return n_arrangements


def sum_all_arrangements(spring_rows: List):
    n_arrangements = 0
    for spring_row in spring_rows:
        n_arrangements += get_arrangements(spring_row)
    print(n_arrangements)


def parse_input(file):
    spring_rows = []
    with open(file, "r", encoding="utf-8") as f:
        for line in f.readlines():
            row, group = line.strip().split()
            group = list(map(int, group.split(",")))

            unfolded_group = []
            unfolded_row = []
            for i in range(0, 5):
                for group_item in group:
                    unfolded_group.append(group_item)
                for row_item in list(row):
                    unfolded_row.append(row_item)
                if i < 4:
                    unfolded_row.append("?")

            spring_rows.append((tuple(unfolded_row), tuple(unfolded_group)))

    return spring_rows


def main():
    spring_rows = parse_input("input.txt")
    sum_all_arrangements(spring_rows)


if __name__ == "__main__":
    main()
