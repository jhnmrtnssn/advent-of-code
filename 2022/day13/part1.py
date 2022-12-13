# Advent of Code - Day 13
# Part 1

import json

CONTINUE = 0
RIGHT_ORDER = 1
WRONG_ORDER = 2


def parse_input(file):
    data = []
    pair = []
    for line in open(file):
        if line.strip():
            pair.append(json.loads(line.strip()))
            if len(pair) == 2:
                data.append((pair[0], pair[1]))
                pair = []
    return data


def get_first_element(packet):
    if isinstance(packet) == list:
        get_first_element(packet[0])
    return packet


def compare_integers(left, right):
    if left < right:
        return RIGHT_ORDER
    if left > right:
        return WRONG_ORDER
    return CONTINUE


def empty_result(left, right):
    if left and not right:
        return WRONG_ORDER
    if right and not left:
        return RIGHT_ORDER
    return CONTINUE


class PairEvaluator:
    def __init__(self, data):
        self.pairs = data
        self.indices_sum = 0

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
        return WRONG_ORDER

    def compare_all(self):
        for i, pair in enumerate(self.pairs):
            result = self.compare(pair)
            if result == RIGHT_ORDER:
                self.indices_sum += i + 1
        print(self.indices_sum)


def main():
    data = parse_input("input.txt")
    pe = PairEvaluator(data)
    pe.compare_all()


if __name__ == "__main__":
    main()
