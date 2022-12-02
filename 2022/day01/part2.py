# Advent of Code - Day 1
# Part 2


def parse_input(file):
    data = []
    for line in open(file):
        data.append((line.strip()))
    return data


def find_three_max_calories(data):
    max_calories = [0, 0, 0]
    calories = 0
    for line in data:
        if line != "":
            calories += int(line)
        else:
            if calories > min(max_calories):
                max_calories.append(calories)
                max_calories.remove(min(max_calories))
            calories = 0
    return max_calories


def main():
    data = parse_input("input.txt")
    max_calories = find_three_max_calories(data)
    print(sum(max_calories))


if __name__ == "__main__":
    main()
