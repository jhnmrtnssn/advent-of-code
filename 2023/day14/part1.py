# Advent of Code - Day 14
# Part 1


def parse_input(file):
    platform = []
    with open(file, "r", encoding="utf-8") as f:
        for line in f.readlines():
            platform.append(list(line.strip()))

    return platform


def rotate_platform(platform):
    return list(map(list, reversed(list(zip(*platform)))))


def move_rocks_in_row(row):
    tilted_row = row
    start_counting = False
    empty_space_start = 0
    n_moveable_rocks = 0
    for i, item in enumerate(row):
        # Start count the moveable rocks from first empty space
        if not start_counting:
            if item == ".":
                start_counting = True
                empty_space_start = i
            continue

        # Increment moveable rock
        if item == "O":
            n_moveable_rocks += 1

        # Rearrange rocks if we hit (#) or end of row
        if item == "#" or i == len(row) - 1:
            start_counting = False
            for space in range(empty_space_start, i):
                if n_moveable_rocks > 0:
                    tilted_row[space] = "O"
                    n_moveable_rocks -= 1
                else:
                    tilted_row[space] = "."

            # Edge case: Remove last item if its a rock
            if i == len(row) - 1 and row[-1] == "O":
                tilted_row[-1] = "."

    return tilted_row


def move_all_rocks_left(platform):
    tilted_platform = []
    for row in platform:
        tilted_platform.append(move_rocks_in_row(row))
    return tilted_platform


def calc_total_load(platform):
    total_load = 0
    for row in platform:
        for i, item in enumerate(row):
            if item == "O":
                total_load += len(row) - i
    print(total_load)


def main():
    platform = parse_input("input.txt")
    rotated_platform = rotate_platform(platform)
    tilted_platform = move_all_rocks_left(rotated_platform)
    calc_total_load(tilted_platform)


if __name__ == "__main__":
    main()
