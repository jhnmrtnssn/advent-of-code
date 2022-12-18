# Advent of Code - Day 18
# Part 1


from typing import Dict


def parse_input(file):
    data = {}
    for line in open(file):
        x, y, z = line.strip().split(",")
        coord = (int(x), int(y), int(z))
        data[coord] = 6
    return data


def get_neighbors(coord):
    neighbors = []
    for x in [-1, 1]:
        neighbors.append((coord[0] + x, coord[1], coord[2]))
    for y in [-1, 1]:
        neighbors.append((coord[0], coord[1] + y, coord[2]))
    for z in [-1, 1]:
        neighbors.append((coord[0], coord[1], coord[2] + z))
    return neighbors


class AreaEvaluator:
    def __init__(self, data: Dict):
        self.cubes = data
        self.checked = []

    def check_neighbors(self, cube):
        neighbors = get_neighbors(cube)
        for c in neighbors:
            if c in self.cubes and c not in self.checked:
                self.cubes[cube] -= 1
                self.cubes[c] -= 1

    def calculate_area(self):
        cubes = self.cubes.keys()
        area = 0
        for c in cubes:
            self.check_neighbors(c)
            self.checked.append(c)
            area += self.cubes[c]
        print(area)


def main():
    data = parse_input("input.txt")
    ae = AreaEvaluator(data)
    ae.calculate_area()


if __name__ == "__main__":
    main()
