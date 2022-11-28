# Advent of Code - Day 21
# Part 2

from copy import deepcopy

def parseInput(file):
    start = []
    for line in open(file):
        start.append(int(line.strip()[-1]))
    return start

class QuantumBoard:
    def __init__(self, p1_start, p2_start):
        s1 = 0
        s2 = 0
        self.all_states = {}
        self.all_states[(p1_start, p2_start, s1, s2)] = 1
        self.temp_states = deepcopy(self.all_states)
        self.new_states = {}
        self.variants = [1, 3, 6, 7, 6, 3, 1]
        self.wins = [0, 0]
        self.player_turn = 1
        self.playing = True

    def roll(self, state):
        p1 = state[0]
        p2 = state[1]
        s1 = state[2]
        s2 = state[3]
        for i, variant in enumerate(self.variants):
            if self.player_turn == 1:
                new_p1 = (p1 + i + 3) % 10
                if new_p1 == 0:
                    new_p1 = 10
                new_state = (new_p1, p2, s1 + new_p1, s2)
            else:
                new_p2 = (p2 + i + 3) % 10
                if new_p2 == 0:
                    new_p2 = 10
                new_state = (p1, new_p2, s1, s2 + new_p2)

            if new_state in self.new_states:
                self.new_states[new_state] += self.temp_states[state] * variant
            else:
                self.new_states[new_state] = self.temp_states[state] * variant

    def play(self):
        while self.playing:
            # Roll and get new states
            self.new_states = {}
            for state in self.temp_states:
                self.roll(state)

            self.temp_states = {}
            for state in self.new_states:
                # Save all states that does not lead to a win
                if state[2] < 21 and state[3] < 21:
                    self.temp_states[state] = self.new_states[state]
                # Add new states to all states and multiply if state exists
                if state in self.all_states:
                    self.all_states[state] += self.new_states[state]
                else:
                    self.all_states[state] = self.new_states[state]

            # Stop if there are no new states without wins
            if not self.temp_states:
                self.playing = False
                for state in self.all_states:
                    if state[2] >= 21:
                        self.wins[0] += self.all_states[state]
                    elif state[3] >= 21:
                        self.wins[1] += self.all_states[state]
                print("Answer part 2:", self.wins[0])

            if self.player_turn == 1:
                self.player_turn = 2
            else:
                self.player_turn = 1


# ----- Part 2 ----- #

start_positions = parseInput("input.txt")
qboard = QuantumBoard(start_positions[0], start_positions[1])
qboard.play()
