# Advent of Code - Day 8
# Part 1

# Directions
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
    def __init__(self, directions, network):
        self.position = "AAA"
        self.end_position = "ZZZ"
        self.directions = directions
        self.network = network
        self.n_steps = 0
        self.total_steps = 0

    def update_steps(self):
        self.n_steps = (self.n_steps + 1) % len(self.directions)
        self.total_steps += 1

    def step(self):
        direction = LEFT if self.directions[self.n_steps] == "L" else RIGHT
        self.position = self.network[self.position][direction]
        self.update_steps()

    def run(self):
        while self.position != self.end_position:
            self.step()
        print(self.total_steps)


def main():
    directions, network = parse_input("input.txt")
    navigator = NetworkNavigator(directions, network)
    navigator.run()


if __name__ == "__main__":
    main()
