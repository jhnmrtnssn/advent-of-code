# Advent of Code - Day 7
# Part 2

def parseInput():
    for line in open("input.txt"):
        return list(map(int, (line.strip().split(","))))


def calcFuelRate(value):
    i = 0
    fuel = 0
    while i < value:
        i += 1
        fuel += i
    return fuel


crabs = parseInput()

min_fuel = 10000000000000000
for i in range(400, 700):
    print(i)
    fuel_list = [calcFuelRate(abs(i-x)) for x in crabs]
    fuel = sum(fuel_list)
    if fuel < min_fuel:
        min_fuel = fuel

print(min_fuel)
