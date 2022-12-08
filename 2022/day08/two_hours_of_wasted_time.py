# Misinterpreted a detail in the description and created this monstrosity.
# Keeping this file just as a reminder to read the description better next time :)


def parse_input(file):
    data = []
    for line in open(file):
        data.append(list(line.strip()))
    return data


class ForestEvaluator:
    def __init__(self, data):
        self.value_grid = data
        self.visible_grid = self.create_visible_grid()
        self.width = len(self.value_grid[0])
        self.height = len(self.value_grid)
        self.depth = 0

    def create_visible_grid(self):
        grid = [[0] * len(self.value_grid[0]) for _ in range(len(self.value_grid))]
        grid[0] = [1] * len(self.value_grid[0])
        grid[-1] = [1] * len(self.value_grid[0])
        for i, _ in enumerate(grid):
            grid[i][0] = 1
            grid[i][-1] = 1
        return grid

    def get_border(self):
        """
        Corners are only included in top and bottom rows
        """
        d = self.depth
        w = len(self.value_grid[0])
        top = self.value_grid[d][d : w - d]
        bottom = self.value_grid[-1 - d][d : w - d]
        left = []
        right = []
        for i, row in enumerate(self.value_grid):
            if d <= i < w - d:
                left.append(row[d])
                right.append(row[w - d - 1])
        return [top, bottom, left, right]

    def update_visible_grid(self, border):
        d = self.depth
        w = self.width
        self.visible_grid[d][d : w - d] = border[0]
        self.visible_grid[-1 - d][d : w - d] = border[1]
        for i in range(1, len(border[2]) + 1):
            self.visible_grid[d + i][d] = border[2][i - 1]
            self.visible_grid[d + i][-1 - d] = border[3][i - 1]
        return self.visible_grid

    def calculate_visible_border(self, border):
        d = self.depth
        # Top
        for i, value in enumerate(border[0]):
            if self.visible_grid[d - 1][d + i] == 1:
                if value > self.value_grid[d - 1][d + i]:
                    self.visible_grid[d][d + i] = 1
        # Bottom
        for i, value in enumerate(border[1]):
            if self.visible_grid[-d + 1][d + i] == 1:
                if value > self.value_grid[-d + 1][d + i]:
                    self.visible_grid[-d][d + i] = 1
        # Left
        for i, value in enumerate(border[2]):
            if self.visible_grid[d + i][d] == 1:
                if value > self.value_grid[d + i][d]:
                    self.visible_grid[d + i][d + 1] = 1
        # Right
        for i, value in enumerate(border[3]):
            if self.visible_grid[d + i][-d] == 1:
                if value > self.value_grid[d + i][-d]:
                    self.visible_grid[d + i][-d - 1] = 1

    def calculate_visible_grid(self):
        self.depth += 1
        data_border = self.get_border()
        while not empty_border(data_border):
            self.calculate_visible_border(data_border)
            # self.update_visible_grid(visible_border)
            self.depth += 1
            data_border = self.get_border()
        print(self.visible_grid)


def empty_border(border):
    for layer in border:
        if layer:
            return False
    return True


def main():
    data = parse_input("test_input.txt")
    fe = ForestEvaluator(data)
    fe.calculate_visible_grid()


if __name__ == "__main__":
    main()
