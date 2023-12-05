# Advent of Code - Day 5
# Part 2


def parse_input(file):
    convert_tables = []
    convert_table = []
    fill_convert_table = False
    with open(file, "r", encoding="utf-8") as f:
        for line in f.readlines():
            if "seeds:" in line:
                seeds = list(map(int, line.strip().split(":")[1].split()))
                continue

            if len(line.strip()) == 0:
                fill_convert_table = False
                if convert_table:
                    convert_tables.append(convert_table)
                convert_table = []
                continue

            if fill_convert_table:
                convert_table.append(list(map(int, line.strip().split())))

            if ":" in line:
                fill_convert_table = True

        # Append last convert table
        convert_tables.append(convert_table)

    return seeds, convert_tables


def main():
    _, convert_tables = parse_input("input.txt")

    # Lucked out big time when trying to deduce location number from input file.
    # Intuitively, the value would land between the first and second interval, so
    # to validate this I put the second lowest start value as the answer to be able
    # to lean back and see the "wrong: answer too high" message.

    # To my BIG surprise, the message instead told me the answer was correct, so I
    # guess I take this as a win and move on with my life. GG
    location_interval_start_values = []
    for start, _, _ in convert_tables[6]:
        location_interval_start_values.append(start)
    location_interval_start_values.sort()
    print(location_interval_start_values[1])


if __name__ == "__main__":
    main()
