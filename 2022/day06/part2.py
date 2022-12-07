# Advent of Code - Day 1
# Part 1


def parse_input(file):
    with open(file) as f:
        data = f.read().strip()
    return data


def find_first_marker(data):
    message = list(data[0:13])
    for index, char in enumerate(data[13:]):
        message.append(char)
        if len(set(message)) == 14:
            return index + 14
        message.pop(0)
    return "UNREACHABLE STATE"


def main():
    data = parse_input("input.txt")
    print(find_first_marker(data))


if __name__ == "__main__":
    main()
