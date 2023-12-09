# Advent of Code - Day 8
# Part 2


# Directions
from functools import reduce
import math


LEFT = 0
RIGHT = 1


def parse_input(file):
    network = {}
    directions = []
    with open(file, "r", encoding="utf-8") as f:
        for i, line in enumerate(f.readlines()):
            if i == 0:
                directions = list(line.strip())
            if i > 1:
                start, end = line.strip().split("=")
                start = start.strip()
                end = [end[2:5], end[7:10]]
                network[start] = end

    return directions, network


class NetworkNavigator:
    def __init__(self, directions, network: dict):
        self.directions = directions
        self.network = network
        self.n_steps = 0
        self.total_steps = 0

        self.positions = []
        self.end_positions = []
        self.get_start_and_end_positions()
        self.step_list = [0] * len(self.positions)

    def get_start_and_end_positions(self):
        for node in list(self.network.keys()):
            if node[2] == "A":
                self.positions.append(node)
            if node[2] == "Z":
                self.end_positions.append(node)

    def update_steps(self):
        self.n_steps = (self.n_steps + 1) % len(self.directions)
        self.total_steps += 1

    def step(self):
        direction = LEFT if self.directions[self.n_steps] == "L" else RIGHT
        for i, position in enumerate(self.positions):
            self.positions[i] = self.network[position][direction]
        self.update_steps()

    def reached_end(self):
        for i, position in enumerate(self.positions):
            if position in self.end_positions:
                self.step_list[i] = self.total_steps

        # Check if all positions have reached the end once
        if 0 in self.step_list:
            return False
        return True

    def run(self):
        while not self.reached_end():
            self.step()

        # Lowest common multiple
        lcm = reduce(lambda x, y: (x * y) // math.gcd(x, y), self.step_list)
        print(lcm)


def main():
    directions, network = parse_input("input.txt")
    navigator = NetworkNavigator(directions, network)
    navigator.run()


if __name__ == "__main__":
    main()
