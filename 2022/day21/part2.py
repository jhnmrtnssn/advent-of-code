# Advent of Code - Day 21
# Part 2


from copy import deepcopy


def parse_input(file):
    number_apes = {}
    operation_apes = {}
    with open(file, "r", encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip().split(": ")
            name = line[0]
            if " " not in line[1]:
                number_apes[name] = int(line[1])
            else:
                p1, op, p2 = line[1].split(" ")
                if name == "root":
                    op = "="
                operation_apes[name] = {"name": name, "p1": p1, "op": op, "p2": p2}
    return number_apes, operation_apes


def calculate_value(x1, x2, op):
    if op == "+":
        return x1 + x2
    if op == "-":
        return x1 - x2
    if op == "/":
        return x1 / x2
    if op == "*":
        return x1 * x2
    if op == "=":
        print(x1)
        print(x2)
        return x1 == x2
    return "UNREACHABLE STATE"


class MonkeyInterpreter:
    def __init__(self, number_apes, operation_apes):
        self.original_num_apes = number_apes
        self.original_op_apes = operation_apes
        self.num_apes = deepcopy(self.original_num_apes)
        self.op_apes = deepcopy(self.original_op_apes)
        self.root_p1 = self.op_apes["root"]["p1"]

    def update_ape_lists(self, op_ape):
        p1 = op_ape["p1"]
        p2 = op_ape["p2"]
        op = op_ape["op"]
        name = op_ape["name"]
        if all(key in self.num_apes.keys() for key in (p1, p2)):
            value = calculate_value(self.num_apes[p1], self.num_apes[p2], op)
            self.num_apes[name] = value
            self.op_apes.pop(name)
            return True
        return False

    def run_until_all_have_yelled(self):
        while len(self.op_apes) > 0:
            for op_ape in self.op_apes.values():
                if self.update_ape_lists(op_ape):
                    break

    def update_humn_value(self, value):
        self.num_apes["humn"] = value

    def reset_dicts(self):
        self.num_apes = deepcopy(self.original_num_apes)
        self.op_apes = deepcopy(self.original_op_apes)

    def iterate_and_increase_humn_value(self): # Gradient descent
        self.update_humn_value(0)
        self.run_until_all_have_yelled()
        init_p1_value = self.num_apes[self.root_p1]
        self.reset_dicts()

        self.update_humn_value(10)
        self.run_until_all_have_yelled()
        second_p1_value = self.num_apes[self.root_p1]
        self.reset_dicts()

        value_increasing = True
        if init_p1_value > second_p1_value:
            value_increasing = False
        print(value_increasing)


def main():
    number_apes, operation_apes = parse_input("input.txt")
    mi = MonkeyInterpreter(number_apes, operation_apes)
    mi.iterate_and_increase_humn_value()  # 3712643961892


if __name__ == "__main__":
    main()
