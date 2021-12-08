# Advent of Code - Day 7
# Part 1

def parseInput():
    for line in (open("input.txt")):
        return list(map(int, (line.strip().split(","))))

crabs = parseInput()

min_fuel = 10000000
for i in range(0, max(crabs)):
    fuel_list = [abs(i-x) for x in crabs]
    fuel = sum(fuel_list)
    if fuel < min_fuel:
        min_fuel = fuel
        print(min_fuel)
