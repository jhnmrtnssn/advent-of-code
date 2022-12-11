# Advent of Code - Day 7
# Part 1


from math import floor


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
        self.crt = CRT()

    def add_signal_strength(self):
        if self.cycle in [20, 60, 100, 140, 180, 220]:
            self.signal_strength.append(self.value * self.cycle)

    def run_instruction(self, instruction):
        self.cycle += 1
        self.crt.set_pixel(self.cycle, self.value)
        self.add_signal_strength()
        if instruction[0] == "addx":
            self.cycle += 1
            self.add_signal_strength()
            self.value += instruction[1]
            self.crt.set_pixel(self.cycle, self.value)

    def run_all_instructions(self):
        self.crt.set_pixel(self.cycle, self.value)
        for instruction in self.instructions:
            self.run_instruction(instruction)
        print(self.crt.draw())


class CRT:
    def __init__(self):
        self.display = [[" "] * 40 for _ in range(6)]

    def set_pixel(self, pixel, cpu_value):
        cpu_value = cpu_value % 40
        sprite = [cpu_value - 1, cpu_value, cpu_value + 1]
        if sprite[2] == 40:
            sprite[2] = 0
        x = floor(pixel / 40)
        y = pixel % 40
        if y in sprite:
            self.display[x][y] = "\u2588"

    def draw(self):
        for row in self.display:
            print("".join(row))


def main():
    data = parse_input("input.txt")
    cpu = CPU(data)
    cpu.run_all_instructions()


if __name__ == "__main__":
    main()
