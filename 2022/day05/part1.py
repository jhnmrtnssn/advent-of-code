# Advent of Code - Day 5
# Part 1


from math import ceil


def parse_input(file):
    stacks = {}
    movements = []
    for i, line in enumerate(open(file)):
        if i < 8:
            for pos, char in enumerate(line):
                if pos % 4 == 1 and char != " ":
                    n_stack = ceil(pos / 4)
                    if n_stack not in stacks:
                        stacks.update({n_stack: [char]})
                    else:
                        stacks[n_stack].append(char)
        if i > 9:
            line = line.strip().split("move")[1].split("from")
            num = int(line[0].strip())
            p1 = int(line[1].split("to")[0].strip())
            p2 = int(line[1].split("to")[1].strip())
            movements.append([num, p1, p2])

    return stacks, movements


def move(stacks, num, p1, p2):
    moving_box = ""
    for _ in range(num):
        moving_box = stacks[p1].pop(0)
        stacks[p2].insert(0, moving_box)
    return stacks


def rearrange_all(stacks, movements):
    for num, p1, p2 in movements:
        stacks = move(stacks, num, p1, p2)
    return stacks


def get_first_box_in_stacks(stacks):
    for i in range(1, len(stacks) + 1):
        print(stacks[i][0])


def main():
    stacks, movements = parse_input("input.txt")
    stacks = rearrange_all(stacks, movements)
    get_first_box_in_stacks(stacks)


if __name__ == "__main__":
    main()
