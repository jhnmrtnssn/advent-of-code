# Advent of Code - Day 2
# Part 1


from typing import List


class Cubes:
    def __init__(self, red=0, blue=0, green=0):
        self.red = red
        self.blue = blue
        self.green = green


def parse_input(file):
    games = []
    with open(file, "r", encoding="utf-8") as f:
        for line in f.readlines():
            game_rounds = line.strip().split(":")[1].split(";")
            rounds_data = []
            for game_round in game_rounds:
                cubes = Cubes()
                raw_cubes = game_round.strip().split(",")
                for item in raw_cubes:
                    amount, color = item.strip().split(" ")
                    if color == "red":
                        cubes.red = int(amount)
                    if color == "blue":
                        cubes.blue = int(amount)
                    if color == "green":
                        cubes.green = int(amount)
                rounds_data.append(cubes)
            games.append(rounds_data)

    return games


def get_minimum_power_of_cubes_per_game(game: List[Cubes]) -> int:
    max_known_cubes = Cubes()
    for cubes in game:
        if cubes.red > max_known_cubes.red:
            max_known_cubes.red = cubes.red
        if cubes.green > max_known_cubes.green:
            max_known_cubes.green = cubes.green
        if cubes.blue > max_known_cubes.blue:
            max_known_cubes.blue = cubes.blue

    return max_known_cubes.red * max_known_cubes.blue * max_known_cubes.green


def check_all_games(games):
    minimum_power = 0
    for game in games:
        minimum_power += get_minimum_power_of_cubes_per_game(game)
    print(minimum_power)


def main():
    games = parse_input("input.txt")
    check_all_games(games)


if __name__ == "__main__":
    main()
