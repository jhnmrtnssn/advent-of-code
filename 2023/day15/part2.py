# Advent of Code - Day 15
# Part 2


def parse_input(file):
    with open(file, "r", encoding="utf-8") as f:
        for line in f.readlines():
            sequence = line.strip().split(",")

    return sequence


def parse_instructions(sequence):
    instructions = []
    for ascii_string in sequence:
        if "-" in ascii_string:
            instructions.append(("-", ascii_string[:-1]))
        else:
            lens, focal_length = ascii_string.split("=")
            instructions.append(("=", lens, focal_length))
    return instructions


def calc_hash_value(ascii_string):
    value = 0
    for char in ascii_string:
        value += ord(char)
        value *= 17
        value = value % 256
    return value


def organize_boxes(instructions):
    boxes = {key: {} for key in list(range(0, 256))}
    current_box = 0
    for instruction in instructions:
        op = instruction[0]
        if op == "=":
            lens, focal_length = instruction[1:]
            current_box = calc_hash_value(lens)
            boxes[current_box][lens] = focal_length

        if op == "-":
            lens = instruction[1]
            current_box = calc_hash_value(lens)
            if lens in boxes[current_box]:
                boxes[current_box].pop(lens)
    return boxes


def calc_focusing_power(boxes: dict):
    focusing_power = 0
    for box_id, box in enumerate(boxes.values(), 1):
        for slot_id, focal_length in enumerate(box.values(), 1):
            focusing_power += int(box_id) * int(slot_id) * int(focal_length)
    print(focusing_power)


def main():
    sequence = parse_input("input.txt")
    instructions = parse_instructions(sequence)
    boxes = organize_boxes(instructions)
    calc_focusing_power(boxes)


if __name__ == "__main__":
    main()
