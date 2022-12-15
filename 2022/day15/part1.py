# Advent of Code - Day 15
# Part 1


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


class BeaconFinder:
    def __init__(self, data):
        self.sensor_pairs = data
        self.eval_y = 2000000
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
        return final_span

    def get_beacons_in_row(self, final_span):
        n_beacons = 0
        found_beacons = []
        for pair in self.sensor_pairs:
            if pair[1][1] == self.eval_y:
                if value_in_range(pair[1][0], final_span):
                    if pair[1] not in found_beacons:
                        n_beacons += 1
                    found_beacons.append(pair[1])
        return n_beacons

    def get_empty_in_row(self):
        final_span = self.get_final_span()
        occupied_beacons = self.get_beacons_in_row(final_span)
        return final_span[1] - final_span[0] + 1 - occupied_beacons

    def scan_all_sensors(self):
        for pair in self.sensor_pairs:
            self.create_empty_range(pair)
        print(self.get_empty_in_row())


def main():
    data = parse_input("input.txt")
    bf = BeaconFinder(data)
    bf.scan_all_sensors()


if __name__ == "__main__":
    main()
