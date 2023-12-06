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
                times = list(map(int, line.strip().split(":")[1].split()))
            if "Distance:" in line:
                distances = list(map(int, line.strip().split(":")[1].split()))

        races = []
        for i, time in enumerate(times):
            races.append(Race(time, distances[i]))

    return races


def calc_distance_from_charge_time(race, charge_time):
    velocity = charge_time
    distance = (race.time - charge_time) * velocity
    return distance


def calc_all_distances_for_race(race):
    distances = []
    for charge_time in range(1, race.time):
        distances.append(calc_distance_from_charge_time(race, charge_time))
    return distances


def get_all_winning_combinations_from_race(race):
    distances = calc_all_distances_for_race(race)
    winning_distances = [x for x in distances if x > race.record_distance]
    return len(winning_distances)


def calc_winning_combination_from_all_races(races):
    combinations = []
    for race in races:
        combinations.append(get_all_winning_combinations_from_race(race))
    return math.prod(combinations)


def main():
    races = parse_input("input.txt")
    print(calc_winning_combination_from_all_races(races))


if __name__ == "__main__":
    main()
