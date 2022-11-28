# Advent of Code - Day 17
# Part 1

import re

def parseInput(file):
    # Totally not rushed regex to find range of x and y
    for line in open(file):
        raw_input = line.strip()
        split_input = re.split(r"=+", raw_input)
        x_raw = re.split(r"\.\.", split_input[1])
        range_x = list(map(int, [x_raw[0], re.split(r"\,", x_raw[1])[0]]))
        range_y = list(map(int, re.split(r"\.\.", split_input[2])))
    return range_x, range_y


class Probe:
    def __init__(self, vel_x, vel_y):
        self.x = 0
        self.y = 0
        self.vel_x = int(vel_x)
        self.vel_y = int(vel_y)
        self.gravity = 1
        self.drag = 1

    def step(self):
        self.x += self.vel_x
        self.y += self.vel_y
        if self.vel_x > 0:
            self.vel_x -= self.drag
        elif self.vel_x < 0:
            self.vel_x += self.drag
        self.vel_y -= self.gravity

    def shoot(self, range_x, range_y):
        x_cords = [self.x]
        y_cords = [self.y]
        hit_target = False
        max_y = 0
        while self.x <= range_x[1] and self.y >= range_y[0]:
            self.step()
            x_cords.append(self.x)
            y_cords.append(self.y)
            # Här blir det lite galet, kolla på det imorgon johan!
            if self.x in range(range_x[0], range_x[1]+1) and self.y in range(range_y[0], range_y[1]+1):
                hit_target = True
                max_y = max(y_cords)
                print("In target!")
        return x_cords, y_cords, hit_target, max_y


# ----- Part 1 ----- #

range_x, range_y = parseInput("input.txt")
max_y = 0

for x in range(0, 100):
    for y in range(0, 100):
        probe = Probe(x, y)
        x_cords, y_cords, hit_target, init_max_y = probe.shoot(range_x, range_y)
        if hit_target and init_max_y > max_y:
            max_y = init_max_y

print(max_y)
