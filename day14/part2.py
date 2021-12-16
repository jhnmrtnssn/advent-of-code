# Advent of Code - Day 14
# Part 2

def parseInput(file):
    transform_input = []
    transform_output = []
    for i, line in enumerate(open(file)):
        if i == 0:
            polymer_template = bytes(line.strip(), 'utf-8')
        elif i > 1:
            line = line.strip().split()
            transform_input.append(bytes(line[0], 'utf-8'))
            transform_output.append(bytes(line[2], 'utf-8'))

    return polymer_template, transform_input, transform_output


def findUniqueElements(polymer):
    elements = []
    for element in polymer:
        if element not in elements:
            elements.append(element)
    return elements


def returnOccurances(element_pairs, transform_input, transform_output):
    unique_elements = findUniqueElements(transform_output)
    element_occurances = [0] * len(unique_elements)
    for i, n in enumerate(element_pairs):
        if i == 0:
            first_char = transform_input[i][0:1]
            element_occurances[unique_elements.index(first_char)] += 1
        second_char = transform_input[i][1:2]
        element_occurances[unique_elements.index(second_char)] += n
    return element_occurances


def step(element_pairs, transform_input, transform_output):
    new_element_pairs = [0] * len(transform_input)
    for i, n in enumerate(element_pairs):
        if n > 0:
            left = transform_input[i][0:1] + transform_output[i]
            right = transform_output[i] + transform_input[i][1:2]
            index_left = transform_input.index(left)
            index_right = transform_input.index(right)
            new_element_pairs[index_left] += n
            new_element_pairs[index_right] += n

    return new_element_pairs


polymer, transform_input, transform_output = parseInput("input.txt")
element_pairs = [0] * len(transform_input)

# Initial set of element pairs
for i, pair in enumerate(transform_input):
    element_pairs[i] += polymer.count(pair)

# Iterate and extend element_pairs list
for _ in range(0, 40):
    element_pairs = step(element_pairs, transform_input, transform_output)

n_element_list = returnOccurances(element_pairs, transform_input, transform_output)
print(max(n_element_list)-min(n_element_list))
