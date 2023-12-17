# Advent of Code - Day 16
# Part 1

from copy import deepcopy


LEFT = 0
UP = 1
RIGHT = 2
DOWN = 3


class BeamNavigator:
    def __init__(self, layout):
        self.layout = layout
        self.next_beam_id = 0
        self.beams = {self.next_beam_id: (0, 0)}
        self.beam_direction = {self.next_beam_id: DOWN}
        self.splitted_beams = []

    def inside_layout(self, position):
        x, y = position
        if 0 <= x < len(self.layout):
            if 0 <= y < len(self.layout[0]):
                return True
        return False

    def spawn_new_beam(self, position, direction):
        self.next_beam_id += 1
        self.beams[self.next_beam_id] = position
        self.beam_direction[self.next_beam_id] = direction

    def next_beam_position(self, beam_id):
        x, y = self.beams[beam_id]
        if self.beam_direction[beam_id] == LEFT:
            y -= 1
        if self.beam_direction[beam_id] == UP:
            x -= 1
        if self.beam_direction[beam_id] == RIGHT:
            y += 1
        if self.beam_direction[beam_id] == DOWN:
            x += 1
        return (x, y)

    def move_beam_one_step(self, beam_id):
        next_position = self.next_beam_position(beam_id)

        # Remove beam from set of beams if outside layout
        if not self.inside_layout(next_position):
            self.beams.pop(beam_id)
            self.beam_direction.pop(beam_id)
            return

        # Move beam one step
        self.beams[beam_id] = next_position
        tile_value = self.layout[next_position[0]][next_position[1]]

        # Mirror: Set new direction of beam
        if tile_value == "/":
            # Change direction clockwise for up/down
            if self.beam_direction[beam_id] in [UP, DOWN]:
                self.beam_direction[beam_id] = (self.beam_direction[beam_id] + 1) % 4
            else:
                self.beam_direction[beam_id] = (self.beam_direction[beam_id] - 1) % 4
        if tile_value == "\\":
            # Change direction counter clockwise for up/down
            if self.beam_direction[beam_id] in [UP, DOWN]:
                self.beam_direction[beam_id] = (self.beam_direction[beam_id] - 1) % 4
            else:
                self.beam_direction[beam_id] = (self.beam_direction[beam_id] + 1) % 4

        # Splitter: Change direction of beam and spawn new beam
        if tile_value == "-":
            if self.beam_direction[beam_id] in [UP, DOWN]:
                self.beam_direction[beam_id] = LEFT
                # Avoid spawning already spawned beam
                if ((next_position, RIGHT)) not in self.splitted_beams:
                    self.spawn_new_beam(next_position, RIGHT)
                    self.splitted_beams.append((next_position, RIGHT))
        if tile_value == "|":
            if self.beam_direction[beam_id] in [LEFT, RIGHT]:
                self.beam_direction[beam_id] = UP
                if ((next_position, DOWN)) not in self.splitted_beams:
                    self.spawn_new_beam(next_position, DOWN)
                    self.splitted_beams.append((next_position, DOWN))

        return next_position

    def fill_layout_with_energized_tiles(self, energized_tiles):
        for x, y in energized_tiles:
            self.layout[x][y] = "#"
        for row in self.layout:
            print("".join(row))

    def run(self):
        energized_tiles = [(0, 0)]
        while self.beams:
            current_beams = deepcopy(self.beams)
            for beam_id in current_beams:
                next_position = self.move_beam_one_step(beam_id)
                if next_position and next_position not in energized_tiles:
                    energized_tiles.append(next_position)

        print(len(energized_tiles))


def parse_input(file):
    layout = []
    with open(file, "r", encoding="utf-8") as f:
        for line in f.readlines():
            layout.append(list(line.strip()))

    return layout


def main():
    layout = parse_input("input.txt")
    navigator = BeamNavigator(layout)
    navigator.run()


if __name__ == "__main__":
    main()
