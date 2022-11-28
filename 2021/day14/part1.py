# Advent of Code - Day 14
# Part 1

def parseInput(file):
    transformations = []
    for i, line in enumerate(open(file)):
        if i == 0:
            polymer_template = line.strip()
        elif i > 1:
            line = line.strip().split()
            transformations.append([line[0], line[2]])

    return polymer_template, transformations


def returnTransformation(pair, transformations):
    for transform in transformations:
        if pair == transform[0]:
            return transform[1]
    return False


def findUniqueElements(polymer):
    elements = []
    for element in polymer:
        if element not in elements:
            elements.append(element)
    return elements


def returnOccurances(polymer, elements):
    n_occurances = []
    for element in elements:
        n_occurances.append(polymer.count(element))
    return n_occurances


def step(polymer, transformations):
    new_polymer = polymer[0]
    for i in range(1, len(polymer)):
        char = returnTransformation(polymer[i-1:i+1], transformations)
        new_polymer = new_polymer + char + polymer[i]
    return new_polymer


polymer, transformations = parseInput("test_input.txt")
steps = 10
for i in range(0, steps):
    polymer = step(polymer, transformations)

elements = findUniqueElements(polymer)
n_occurances = returnOccurances(polymer, elements)
print(max(n_occurances)-min(n_occurances))
