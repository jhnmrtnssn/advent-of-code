# Advent of Code - Day 21
# Part 1


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
    return "UNREACHABLE STATE"


class MonkeyInterpreter:
    def __init__(self, number_apes, operation_apes):
        self.num_apes = number_apes
        self.op_apes = operation_apes

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
        print(int(self.num_apes["root"]))


def main():
    number_apes, operation_apes = parse_input("input.txt")
    mi = MonkeyInterpreter(number_apes, operation_apes)
    mi.run_until_all_have_yelled()


if __name__ == "__main__":
    main()
