# Advent of Code - Day 11
# Part 2

from typing import List


def calc_manhattan_distance(pair):
    return abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])


class GalaxyNavigator:
    def __init__(self, image: List[List]):
        self.image = image
        self.empty_rows, self.empty_columns = self.get_empty_rows_and_columns()
        self.galaxies = self.get_galaxies()
        self.galaxy_pairs = self.get_galaxy_pairs()

    def get_galaxies(self):
        galaxies = []
        for x, row in enumerate(self.image):
            for y, value in enumerate(row):
                if value == "#":
                    galaxies.append((x, y))
        return galaxies

    def get_empty_rows_and_columns(self):
        empty_rows = []
        for x, row in enumerate(self.image):
            if len(list(set(row))) == 1:
                empty_rows.append(x)

        empty_columns = []
        for y in range(0, len(self.image[0])):
            column = []
            for x, _ in enumerate(self.image):
                column.append(self.image[x][y])
            if len(list(set(column))) == 1:
                empty_columns.append(y)

        return empty_rows, empty_columns

    def get_galaxy_pairs(self):
        galaxy_pairs = []
        for i, _ in enumerate(self.galaxies[:-1]):
            for j, _ in enumerate(self.galaxies[i + 1 :], i + 1):
                galaxy_pairs.append((self.galaxies[i], self.galaxies[j]))
        return galaxy_pairs

    def get_sum_of_galaxy_pair_distances(self):
        distance_sum = 0
        for pair in self.galaxy_pairs:
            distance_sum += calc_manhattan_distance(pair)
            n_empty_rows = self.get_n_empty_space_between_pairs(pair)
            distance_sum += (1000000 - 1) * n_empty_rows
        print(distance_sum)

    def get_n_empty_space_between_pairs(self, pair):
        n = 0
        x = (pair[0][0], pair[1][0])
        for row in self.empty_rows:
            if min(x) < row < max(x):
                n += 1

        y = (pair[0][1], pair[1][1])
        for col in self.empty_columns:
            if min(y) < col < max(y):
                n += 1
        return n


def parse_input(file):
    image = []
    with open(file, "r", encoding="utf-8") as f:
        for line in f.readlines():
            image.append(list(line.strip()))

    return image


def main():
    image = parse_input("input.txt")
    navigator = GalaxyNavigator(image)
    navigator.get_sum_of_galaxy_pair_distances()


if __name__ == "__main__":
    main()
