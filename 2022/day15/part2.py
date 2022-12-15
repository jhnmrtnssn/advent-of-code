# Advent of Code - Day 15
# Part 2


import time


def parse_input(file):
    data = []
    for line in open(file):
        line = line.strip().split(": closest beacon")
        sensor_line = line[0].split("x=")[1].split(", y=")
        sensor = (int(sensor_line[0]), int(sensor_line[1]))
        beacon_line = line[1].split("x=")[1].split(", y=")
        beacon = (int(beacon_line[0]), int(beacon_line[1]))
        data.append((sensor, beacon))
    return data


def get_manhattan_distance(sensor_pair):
    s1, s2 = sensor_pair
    return abs(s1[0] - s2[0]) + abs(s1[1] - s2[1])


def value_in_range(value, r):
    return r[0] <= value <= r[1]


def is_overlapping(r1, r2):
    return (r1[0] - 1 <= r2[0] and r2[0] - 1 <= r1[1]) or (
        r2[0] - 1 <= r1[0] and r1[0] - 1 <= r2[1]
    )


def is_contained(r1, r2):
    return r1[0] >= r2[0] and r1[1] <= r2[1]


def merge(r1, r2):
    return [min(r1[0], r2[0]), max(r1[1], r2[1])]


def calc_distress_position(x, y):
    return 4000000 * x + y


class BeaconFinder:
    def __init__(self, data):
        self.sensor_pairs = data
        self.eval_y = 0
        self.valid_range = [0, 4000000]
        self.merged_range = []
        self.empty_range = []

    def create_empty_range(self, sensor_pair):
        mdist = get_manhattan_distance(sensor_pair)
        s1 = sensor_pair[0]
        if s1[1] <= self.eval_y:
            diff = s1[1] + mdist - self.eval_y
        else:
            diff = self.eval_y - (s1[1] - mdist)

        if diff >= 0:
            new_empty_range = [s1[0] - diff, s1[0] + diff]
            self.update_range(new_empty_range)

    def update_range(self, new_range):
        updated_range = False
        for i, r in enumerate(self.empty_range):
            if is_overlapping(new_range, r):
                self.empty_range[i] = merge(new_range, r)
                updated_range = True

        if not updated_range:
            self.empty_range.append(new_range)

    def get_final_span(self):
        merged = []
        for i, _ in enumerate(self.empty_range):
            if i == 0:
                final_span = self.empty_range[0]
            for j, r in enumerate(self.empty_range):
                if j not in merged:
                    if is_overlapping(final_span, r):
                        final_span = merge(final_span, r)
                        merged.append(j)
                        break

        return [final_span]

    def scan_all_sensors(self):
        for pair in self.sensor_pairs:
            self.create_empty_range(pair)
        return self.get_final_span()

    def scan_all_rows(self):
        for _ in range(0, 4000000):
            new_span = self.scan_all_sensors()
            if not is_contained(self.valid_range, new_span[0]):
                print(calc_distress_position(new_span[0][1] + 1, self.eval_y))
                break
            self.eval_y += 1
            self.empty_range = []


def main():
    start_time = time.time()
    data = parse_input("input.txt")
    bf = BeaconFinder(data)
    bf.scan_all_rows()
    print(time.time() - start_time)


if __name__ == "__main__":
    main()
