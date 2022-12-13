# Advent of Code - Day 13
# Part 2

import json
from copy import deepcopy

CONTINUE = 0
LEFT = 1
RIGHT = 2


def parse_input(file):
    data = []
    for line in open(file):
        if line.strip():
            data.append(json.loads(line.strip()))
    return data


def get_first_element(packet):
    if isinstance(packet) == list:
        get_first_element(packet[0])
    return packet


def compare_integers(left, right):
    if left < right:
        return LEFT
    if left > right:
        return RIGHT
    return CONTINUE


def empty_result(left, right):
    if left and not right:
        return RIGHT
    if right and not left:
        return LEFT
    return CONTINUE


class PackageSorter:
    def __init__(self, data):
        self.packages = data
        self.packages.append([[2]])  # Divider package 1
        self.packages.append([[6]])  # Divider package 2
        self.sorted_packages = [0] * len(self.packages)

    def compare(self, pair):
        left = pair[0]
        right = pair[1]
        result = CONTINUE

        while result == CONTINUE:
            if not left or not right:
                return empty_result(left, right)

            left_element = left.pop(0) if isinstance(left, list) else left
            right_element = right.pop(0) if isinstance(left, list) else right

            if isinstance(left_element, int) and isinstance(right_element, int):
                result = compare_integers(left_element, right_element)
                if result is not CONTINUE:
                    return result

            elif isinstance(left_element, list) and isinstance(right_element, list):
                result = self.compare((left_element, right_element))
                if result is not CONTINUE:
                    return result

            else:
                if isinstance(left_element, int):
                    left_element = [left_element]
                if isinstance(right_element, int):
                    right_element = [right_element]
                result = self.compare((left_element, right_element))
                if result is not CONTINUE:
                    return result
        return RIGHT

    def sort_packages(self):
        for i, left in enumerate(self.packages):
            index = 0
            for j, right in enumerate(self.packages):
                if i is not j:
                    result = self.compare((deepcopy(left), deepcopy(right)))
                    if result == RIGHT:
                        index += 1
            self.sorted_packages[index] = left

    def calc_distress_signal(self):
        divider_package1 = self.sorted_packages.index([[2]]) + 1
        divider_package2 = self.sorted_packages.index([[6]]) + 1
        print(divider_package1 * divider_package2)


def main():
    data = parse_input("input.txt")
    pe = PackageSorter(data)
    pe.sort_packages()
    pe.calc_distress_signal()


if __name__ == "__main__":
    main()
