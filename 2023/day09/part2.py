# Advent of Code - Day 9
# Part 2


from typing import List


def parse_input(file):
    all_sequences = []
    with open(file, "r", encoding="utf-8") as f:
        for line in f.readlines():
            all_sequences.append(Sequence(list(map(int, line.strip().split()))))

    return all_sequences


def get_diff_sequence(sequence) -> List[int]:
    diff_sequence = []
    for i in range(0, len(sequence) - 1):
        diff_sequence.append(sequence[i + 1] - sequence[i])
    return diff_sequence


def contains_same_values(sequence) -> bool:
    return len(list(set(sequence))) == 1


class Sequence:
    def __init__(self, sequence):
        self.sequence = sequence
        self.extrapolated_value = self.recursive_calc_ep(sequence)

    def recursive_calc_ep(self, sequence):
        diff_sequence = get_diff_sequence(sequence)
        if contains_same_values(diff_sequence):
            return sequence[0] - diff_sequence[0]

        return sequence[0] - self.recursive_calc_ep(diff_sequence)


def sum_all_extrapolated_values(sequences: List[Sequence]):
    ep_sum = 0
    for sequence in sequences:
        ep_sum += sequence.extrapolated_value
    print(ep_sum)


def main():
    sequences = parse_input("input.txt")
    sum_all_extrapolated_values(sequences)


if __name__ == "__main__":
    main()
