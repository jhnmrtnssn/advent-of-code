# Advent of Code - Day 21
# Part 1

def parseInput(file):
    start = []
    for line in open(file):
        start.append(int(line.strip()[-1]))
    return start


class Player:
    def __init__(self, start):
        self.position = start
        self.score = 0

    def move(self, amount):
        self.position = (self.position + amount) % 10
        if self.position == 0:
            self.position = 10
        self.score += self.position

    def get_score(self):
        return self.score


class Board:
    def __init__(self, p1_start, p2_start):
        self.p1 = Player(p1_start)
        self.p2 = Player(p2_start)
        self.dice = 1
        self.n_dice_rolls = 0
        self.player_turn = 1
        self.playing = True

    def roll(self):
        amount = 0
        for i in range(0, 3):
            amount += (self.dice + i) % 1000
        self.dice = (self.dice + 3) % 1000

        if self.player_turn == 1:
            self.p1.move(amount)
            self.player_turn = 2
            if self.p1.get_score() >= 1000:
                self.playing = False
        elif self.player_turn == 2:
            self.p2.move(amount)
            self.player_turn = 1
            if self.p2.get_score() >= 1000:
                self.playing = False

    def play(self):
        while self.playing:
            self.roll()
            self.n_dice_rolls += 3
        print("Answer part 1:", self.p2.get_score() * self.n_dice_rolls)

# ----- Part 1 ----- #

start_positions = parseInput("input.txt")
board = Board(start_positions[0], start_positions[1])
board.play()
