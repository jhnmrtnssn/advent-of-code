# Advent of Code - Day 2
# Part 1


from typing import List


RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14


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


def valid_cube_game(game: List[Cubes]) -> bool:
    for cubes in game:
        if cubes.red > RED_MAX or cubes.blue > BLUE_MAX or cubes.green > GREEN_MAX:
            return False
    return True


def check_all_games(games):
    sum_of_valid_ids = 0
    for i, game in enumerate(games, 1):
        if valid_cube_game(game):
            sum_of_valid_ids += i
    print(sum_of_valid_ids)


def main():
    games = parse_input("input.txt")
    check_all_games(games)


if __name__ == "__main__":
    main()
