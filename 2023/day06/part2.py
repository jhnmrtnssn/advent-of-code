# Advent of Code - Day 6
# Part 1


import math


class Race:
    def __init__(self, time, distance):
        self.time = time
        self.record_distance = distance


def parse_input(file):
    with open(file, "r", encoding="utf-8") as f:
        for line in f.readlines():
            if "Time:" in line:
                time_list = list(map(int, line.strip().split(":")[1].split()))
            if "Distance:" in line:
                distance_list = list(map(int, line.strip().split(":")[1].split()))

        time = int("".join(map(str, time_list)))
        distance = int("".join(map(str, distance_list)))

    return Race(time, distance)


def calc_distance_from_charge_time(race, charge_time):
    velocity = charge_time
    distance = (race.time - charge_time) * velocity
    return distance


def calc_all_distances_for_race(race):
    distances = []
    for charge_time in range(1, race.time):
        distances.append(calc_distance_from_charge_time(race, charge_time))
    return distances


def find_lower_boundary(race):
    # Initialize charge time at reasonable value (lower values impossible to win)
    charge_time = math.floor(race.record_distance / race.time)

    while calc_distance_from_charge_time(race, charge_time) < race.record_distance:
        charge_time += 1

    return charge_time


def find_upper_boundary(race):
    # Initialize charge time at reasonable value (higher values impossible to win)
    charge_time = race.time - math.floor(race.record_distance / race.time)

    while calc_distance_from_charge_time(race, charge_time) < race.record_distance:
        charge_time -= 1

    return charge_time


def get_winning_times(race):
    lb = find_lower_boundary(race)
    ub = find_upper_boundary(race)

    return ub - lb + 1


def main():
    race = parse_input("input.txt")
    print(get_winning_times(race))


if __name__ == "__main__":
    main()
