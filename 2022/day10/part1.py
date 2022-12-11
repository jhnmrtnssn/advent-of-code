# Advent of Code - Day 7
# Part 1


def parse_input(file):
    data = []
    for line in open(file):
        if line.strip() == "noop":
            operation = line.strip()
            value = 0
        else:
            operation, value = line.strip().split(" ")
        data.append((operation, int(value)))
    return data


class CPU:
    def __init__(self, data):
        self.instructions = data
        self.cycle = 0
        self.value = 1
        self.executing = False
        self.signal_strength = []

    def add_signal_strength(self):
        if self.cycle in [20, 60, 100, 140, 180, 220]:
            self.signal_strength.append(self.value * self.cycle)

    def run_instruction(self, instruction):
        self.cycle += 1
        self.add_signal_strength()
        if instruction[0] == "addx":
            self.cycle += 1
            self.add_signal_strength()
            self.value += instruction[1]

    def run_all_instructions(self):
        for instruction in self.instructions:
            self.run_instruction(instruction)
        print(sum(self.signal_strength))


def main():
    data = parse_input("input.txt")
    cpu = CPU(data)
    cpu.run_all_instructions()


if __name__ == "__main__":
    main()
