# Advent of Code - Day 18
# Part 1

import json
import math
from copy import deepcopy

def parseInput(file):
    list_numbers = []
    for line in open(file):
        list_numbers.append(json.loads(line.strip()))
    return list_numbers


def calc_magnitude(total_sum):
    mag = 0
    for i, ele in enumerate(total_sum):
        factor = 3 if i == 0 else 2
        if isinstance(ele, list):
            mag += calc_magnitude(ele) * factor
        else:
            mag += ele * factor
    return mag


class SnailfishAdder:
    def __init__(self, numbers):
        self.sum = numbers.pop(0)
        self.numbers = numbers
        self.ele_ids = []

        self.update_list = True
        self.is_action_explode = False
        self.explode_id = []
        self.is_action_split = False
        self.split_id = []
        self.split_value = 0

    def get_sum_by_index(self, i):
        if len(i) == 1:
            return self.sum[i[0]]
        if len(i) == 2:
            return self.sum[i[0]][i[1]]
        if len(i) == 3:
            return self.sum[i[0]][i[1]][i[2]]
        if len(i) == 4:
            return self.sum[i[0]][i[1]][i[2]][i[3]]
        if len(i) == 5:
            return self.sum[i[0]][i[1]][i[2]][i[3]][i[4]]
        return []

    def increase_sum_by_index(self, i, value):
        if len(i) == 1:
            self.sum[i[0]] += value
        if len(i) == 2:
            self.sum[i[0]][i[1]] += value
        if len(i) == 3:
            self.sum[i[0]][i[1]][i[2]] += value
        if len(i) == 4:
            self.sum[i[0]][i[1]][i[2]][i[3]] += value
        if len(i) == 5:
            self.sum[i[0]][i[1]][i[2]][i[3]][i[4]] += value

    def set_value_by_index(self, i, value):
        if len(i) == 1:
            self.sum[i[0]] = value
        if len(i) == 2:
            self.sum[i[0]][i[1]] = value
        if len(i) == 3:
            self.sum[i[0]][i[1]][i[2]] = value
        if len(i) == 4:
            self.sum[i[0]][i[1]][i[2]][i[3]] = value
        if len(i) == 5:
            self.sum[i[0]][i[1]][i[2]][i[3]][i[4]] = value

    def get_nearest_index(self, i):
        expl_id = deepcopy(i)
        expl_id.append(0)
        left_index = []
        right_index = []
        left_ele_index = self.ele_ids.index(expl_id)
        right_ele_index = self.ele_ids.index(expl_id)+1
        if left_ele_index > 0:
            left_index = self.ele_ids[left_ele_index-1]
        if right_ele_index < len(self.ele_ids)-1:
            right_index = self.ele_ids[right_ele_index+1]
        return left_index, right_index

    def explode(self, i):
        pair = self.get_sum_by_index(i)
        left_index, right_index = self.get_nearest_index(i)
        self.increase_sum_by_index(left_index, pair[0])
        self.increase_sum_by_index(right_index, pair[1])
        self.sum[i[0]][i[1]][i[2]][i[3]] = 0

        self.update_list = True
        self.is_action_explode = False
        self.explode_id = []

    def split(self, i, value):
        x = math.floor(value/2)
        y = value - x
        self.set_value_by_index(i, [x, y])

        self.update_list = True
        self.is_action_split = False
        self.split_value = 0
        self.split_id = []

    def update_ele_list(self, ele_expr, ele_id):
        for i, ele in enumerate(ele_expr):
            ele_id.append(i)
            if not isinstance(ele, list):
                self.ele_ids.append(deepcopy(ele_id))
            else:
                self.update_ele_list(ele, ele_id)

            ele_id.pop()

    def reduce(self, expr, ele_id):
        # Update list of elements if action has happened
        if self.update_list:
            self.ele_ids = []
            self.update_ele_list(self.sum, [])
            self.update_list = False
            self.reduce(self.sum, [])
        else:
            # Check for explode
            for i, ele in enumerate(expr):
                ele_id.append(i)
                if isinstance(ele, list) and not self.is_action_explode:
                    if len(ele_id) == 4:
                        self.is_action_explode = True
                        self.explode_id = deepcopy(ele_id)
                    else:
                        self.reduce(ele, ele_id)
                ele_id.pop()

            # Check for split
            if not self.is_action_explode:
                for single_ele_id in self.ele_ids:
                    val = self.get_sum_by_index(single_ele_id)
                    if val > 9:
                        self.is_action_split = True
                        self.split_id = deepcopy(single_ele_id)
                        self.split_value = deepcopy(val)
                        break

        self.update_list = False

    def add_next_value(self):
        self.sum = [self.sum, self.numbers.pop(0)]
        self.update_list = True
        while self.update_list:
            self.reduce(self.sum, [])
            if self.is_action_explode:
                self.explode(self.explode_id)
            if self.is_action_split and not self.update_list:
                self.split(self.split_id, self.split_value)

    def add_all_values(self):
        while len(self.numbers) > 0:
            self.add_next_value()

    def get_sum(self):
        return self.sum


# ----- Part 1 ----- #

numbers = parseInput("input.txt")
sf_adder = SnailfishAdder(numbers)

sf_adder.add_all_values()
total_sum = sf_adder.get_sum()

print("Part 1:", calc_magnitude(total_sum))
