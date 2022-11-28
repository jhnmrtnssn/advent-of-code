# Advent of Code - Day 24
# Part 1

import re

def parseInput(file):
    instructions = []
    for line in open(file):
        raw_input = line.strip()
        split_input = re.split(" ", raw_input)
        instructions.append(split_input)

    return instructions


class ALU:
    def __init__(self, model_number, instructions):
        self.model_number = str(model_number)
        self.instructions = instructions
        self.values = [0, 0, 0, 0] # [w, x, y, z]
        self.input_counter = 0
        self.running = True

    def execute_input(self, instruction):
        task = instruction[0]
        if task == "inp":
            self.inp(instruction[1])
        elif task == "add":
            self.add(instruction[1], instruction[2])
        elif task == "mul":
            self.mul(instruction[1], instruction[2])
        elif task == "div":
            self.div(instruction[1], instruction[2])
        elif task == "mod":
            self.mod(instruction[1], instruction[2])
        elif task == "eql":
            self.eql(instruction[1], instruction[2])
        else:
            print("Invalid instruction:", task)

    def char_to_number(self, char):
        if char == "w":
            return 0
        elif char == "x":
            return 1
        elif char == "y":
            return 2
        elif char == "z":
            return 3
        else:
            print("Invalid character:", char)
            return False

    def instruction_to_value(self, b):
        if b.startswith("-") or b.isdigit():
            value = int(b)
        else:
            position = self.char_to_number(b)
            value = self.values[position]
        return value

    def inp(self, a):
        value = int(self.model_number[self.input_counter])
        position = self.char_to_number(a)
        self.input_counter += 1
        self.values[position] = value

    def add(self, a, b):
        value = self.instruction_to_value(b)
        position = self.char_to_number(a)
        self.values[position] = self.values[position] + value

    def mul(self, a, b):
        value = self.instruction_to_value(b)
        position = self.char_to_number(a)
        self.values[position] = self.values[position] * value

    def div(self, a, b):
        value = self.instruction_to_value(b)
        if value == 0:
            print("Abort: Trying to divide by zero.")
            self.running = False
            return
        position = self.char_to_number(a)
        self.values[position] = int(self.values[position] / value)

    def mod(self, a, b):
        value = self.instruction_to_value(b)
        position = self.char_to_number(a)
        if value <= 0 or self.values[position] < 0:
            print("Trying to do modulus with invalid values")
            self.running = False
            return
        self.values[position] = self.values[position] % value

    def eql(self, a, b):
        value = self.instruction_to_value(b)
        position = self.char_to_number(a)
        self.values[position] = int(self.values[position] == value)

    def MONAD(self):
        for instruction in self.instructions:
            self.execute_input(instruction)
            if not self.running:
                return False
        if self.values[3] == 0:
            return True
        return False

    def get_z_value(self):
        return self.values[3]


def array_to_int(arr):
    return int(''.join(map(str, arr)))

instructions = parseInput("input.txt")

model_number_arr = [9] * 14
lowest_z_value = 999999999999999
running = True

for loop in range(0, 1000):

    for i in range(0, 14):
        for digit in reversed(range(1, 10)):
            model_number_arr[i] = digit
            alu = ALU(array_to_int(model_number_arr), instructions)
            if alu.MONAD():
                running = False
                print("FOUND Z = 0")
            if alu.get_z_value() < lowest_z_value:
                lowest_z_value = alu.get_z_value()
                print(lowest_z_value)
                temp_model_number = model_number_arr
                print(loop)
                break
        model_number_arr = temp_model_number

    for i in range(0, 14):
        for digit in reversed(range(1, 10)):
            model_number_arr[i] = digit
            alu = ALU(array_to_int(model_number_arr), instructions)
            if alu.MONAD():
                running = False
                print("FOUND Z = 0")
            if alu.get_z_value() < lowest_z_value:
                lowest_z_value = alu.get_z_value()
                print(lowest_z_value)
                print(loop)
                temp_model_number = model_number_arr
        model_number_arr = temp_model_number
