# Advent of Code - Day 5
# Part 1


from typing import List


class AlmanacHandler:
    def __init__(self, seeds, convert_tables):
        self.seeds = seeds
        self.convert_tables = convert_tables

    def get_new_value_from_convert_table(self, value, table_id: int):
        convert_table = self.convert_tables[table_id]
        for line in convert_table:
            source_range = [line[1], line[1] + line[2] - 1]
            if min(source_range) <= value <= max(source_range):
                delta = value - min(source_range)
                destination_start_value = line[0]
                return destination_start_value + delta

        # Return same destination if no match
        return value

    def get_location_from_seed(self, value):
        for table_id in range(0, len(self.convert_tables)):
            value = self.get_new_value_from_convert_table(value, table_id)
        return value

    def get_lowest_location_number_from_seed(self):
        location_values = []
        for seed in self.seeds:
            location_values.append(self.get_location_from_seed(seed))
        print(min(location_values))


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
    seeds, convert_tables = parse_input("input.txt")
    almenac_handler = AlmanacHandler(seeds, convert_tables)
    almenac_handler.get_lowest_location_number_from_seed()


if __name__ == "__main__":
    main()
