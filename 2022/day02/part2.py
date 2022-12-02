# Advent of Code - Day 2
# Part 2


def parse_input(file):
    data = []
    for line in open(file):
        data.append((line.strip().split(" ")))
    return data


def get_total_score(rounds):
    score = 0
    for rnd in rounds:
        score += get_round_score(rnd[0], rnd[1])
    return score


def get_round_score(p1, p2):
    r = 1
    p = 2
    s = 3
    win_score = 6
    draw_score = 3
    if p1 == "A":  # Rock
        if p2 == "X":  # Lose
            score = s
        if p2 == "Y":  # Draw
            score = r + draw_score
        if p2 == "Z":  # Win
            score = p + win_score
    elif p1 == "B":  # Paper
        if p2 == "X":
            score = r
        if p2 == "Y":
            score = p + draw_score
        if p2 == "Z":
            score = s + win_score
    else:  # Scissor
        if p2 == "X":
            score = p
        if p2 == "Y":
            score = s + draw_score
        if p2 == "Z":
            score = r + win_score
    return score


def main():
    data = parse_input("input.txt")
    print(get_total_score(data))


if __name__ == "__main__":
    main()
