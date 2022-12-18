# Advent of Code - Day 18
# Part 2


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


def outside_range(c):
    return (c[0] < 0 or c[0] > 20) or (c[1] < 0 or c[1] > 20) or (c[2] < 0 or c[2] > 20)


class AreaEvaluator:
    def __init__(self, data: Dict):
        self.cubes = data
        self.checked = []
        self.neighbor_air = []
        self.visited = []
        self.air_bubble = []
        self.all_air_bubbles = []
        self.area = 0

    def check_neighbors(self, cube):
        neighbors = get_neighbors(cube)
        for c in neighbors:
            if c in self.cubes and c not in self.checked:
                self.cubes[cube] -= 1
                self.cubes[c] -= 1

    def calculate_area(self):
        cubes = self.cubes.keys()
        for c in cubes:
            self.check_neighbors(c)
            self.checked.append(c)
            self.area += self.cubes[c]

    def find_all_air_neighbors(self):
        for cube in self.cubes:
            neighbors = get_neighbors(cube)
            for c in neighbors:
                if c not in self.cubes and c not in self.neighbor_air:
                    self.neighbor_air.append(c)

    def found_air_bubble(self, cube, max_volume):
        checked_bubbles = []
        new_bubbles = [cube]
        for _ in range(max_volume):
            if new_bubbles:
                air_cube = new_bubbles.pop(0)
            else:
                return True
            checked_bubbles.append(air_cube)
            neighbors = get_neighbors(air_cube)
            for c in neighbors:
                if outside_range(c):
                    return False
                if len(self.air_bubble) > max_volume - 1:
                    return False
                if (
                    c not in self.cubes
                    and c not in self.air_bubble
                    and c not in self.all_air_bubbles
                    and c not in checked_bubbles
                ):
                    new_bubbles.append(c)
                    self.air_bubble.append(c)
        return True

    def find_all_air_bubbles(self):
        for air_cube in self.neighbor_air:
            if air_cube not in self.all_air_bubbles:
                self.air_bubble = []
                self.air_bubble.append(air_cube)
                if self.found_air_bubble(air_cube, max_volume=8000):
                    for c in self.air_bubble:
                        self.all_air_bubbles.append(c)

    def calculate_exterior_surface_area(self):
        self.find_all_air_neighbors()
        self.find_all_air_bubbles()
        for air_cube in self.all_air_bubbles:
            neighbors = get_neighbors(air_cube)
            for c in neighbors:
                if c in self.cubes:
                    self.area -= 1
        print(self.area)


def main():
    data = parse_input("input.txt")
    ae = AreaEvaluator(data)
    ae.calculate_area()
    ae.calculate_exterior_surface_area()


if __name__ == "__main__":
    main()
