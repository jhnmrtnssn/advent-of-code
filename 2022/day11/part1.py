# Advent of Code - Day 11
# Part 1

from math import floor
from typing import List


def parse_input(file):
    monkeys = []
    div_value = 0
    true_value = 0
    false_value = 0
    for line in open(file):
        line = line.strip()
        if line.startswith("Starting items"):
            line = line.split(":")[1].split(",")
            items = []
            for item in line:
                items.append(int(item.strip()))
        elif line.startswith("Operation"):
            operation = add_operation(line)
        elif line.startswith("Test:"):
            div_value = int(line.split("by ")[1])
        elif line.startswith("If true:"):
            true_value = int(line.split("monkey ")[1])
        elif line.startswith("If false:"):
            false_value = int(line.split("monkey ")[1])
            test = add_test(div_value, true_value, false_value)
            monkeys.append(Monkey(items, operation, test))
    return monkeys


def add_test(div_val, true_val, false_val):
    return lambda x: true_val if x % div_val == 0 else false_val


def add_operation(op_line):
    op = op_line.split("= ")[1].split(" ")
    if op[1] == "+":
        if op[2].isnumeric():
            operation = lambda x: x + int(op[2])
        else:
            operation = lambda x: x + x
    else:
        if op[2].isnumeric():
            operation = lambda x: x * int(op[2])
        else:
            operation = lambda x: x * x
    return operation


class Monkey:
    def __init__(self, items, operation, test):
        self.items = items
        self.operation = operation
        self.test = test
        self.inspected = 0

    def inspect(self):
        for i, item in enumerate(self.items):
            item = self.operation(item)
            self.items[i] = floor(item / 3)
            self.inspected += 1

    def throw(self):
        thrown_items = []
        for item in self.items:
            monkey_id = self.test(item)
            thrown_items.append((item, monkey_id))
        self.items = []
        return thrown_items

    def receive(self, item):
        self.items.append(item)

    def get_items(self):
        return self.items

    def get_inspected_value(self):
        return self.inspected


class MonkeyGame:
    def __init__(self, monkeys: List[Monkey]):
        self.monkeys = monkeys

    def round(self):
        for monkey in self.monkeys:
            monkey.inspect()
            items = monkey.throw()
            for item, monkey_id in items:
                self.monkeys[monkey_id].receive(item)

    def check_items(self):
        for monkey in self.monkeys:
            print(monkey.get_items())

    def score(self):
        inspected = []
        for monkey in self.monkeys:
            inspected.append(monkey.get_inspected_value())
        inspected.sort(reverse=True)
        return inspected[0] * inspected[1]

    def play(self, rounds):
        for _ in range(rounds):
            self.round()
        print(self.score())


def main():
    data = parse_input("test_input.txt")
    game = MonkeyGame(data)
    game.play(rounds=20)


if __name__ == "__main__":
    main()
