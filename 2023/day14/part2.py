# Advent of Code - Day 14
# Part 2


def parse_input(file):
    platform = []
    with open(file, "r", encoding="utf-8") as f:
        for line in f.readlines():
            platform.append(list(line.strip()))

    return platform


def rotate_platform(platform, degrees):
    if degrees == 90:
        return list(map(list, reversed(list(zip(*platform)))))
    if degrees == 270:
        return list(map(list, zip(*platform[::-1])))


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
    return total_load


def rotate_one_cycle(platform):
    for _ in range(0, 4):
        platform = move_all_rocks_left(platform)
        platform = rotate_platform(platform, 270)
    return platform


def rotate_n_cycles(platform, n):
    load_values = []
    for _ in range(0, n):
        platform = rotate_one_cycle(platform)
        load_values.append(calc_total_load(platform))
    start, pattern = get_pattern_and_start(load_values)
    print(pattern[(1000000000 - start) % len(pattern) - 1])


def get_pattern_and_start(load_values):
    pattern = []
    found_pattern = False
    for i, value in enumerate(load_values):
        if found_pattern:
            pattern.append(value)

        if value == 100305:  # Scanned load_values for value in pattern
            if found_pattern:
                break
            found_pattern = True
            start = i
    return start + 1, pattern


def main():
    platform = parse_input("input.txt")
    platform = rotate_platform(platform, 90)
    rotate_n_cycles(platform, 140)  # Manually run until pattern shows


if __name__ == "__main__":
    main()
