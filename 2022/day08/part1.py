# Advent of Code - Day 8
# Part 1


def parse_input(file):
    data = []
    for line in open(file):
        data.append(list(map(int, line.strip())))
    return data


class ForestEvaluator:
    def __init__(self, data):
        self.value_grid = data
        self.visible_grid = self.create_visible_grid()
        self.width = len(self.value_grid[0]) - 1
        self.height = len(self.value_grid) - 1

    def is_visible(self, x, y, value):
        lengths = [x, self.height - x, y, self.width - y]
        # Top
        trees = []
        for i in range(lengths[0]):
            trees.append(self.value_grid[i][y])
        if all(tree < value for tree in trees):
            return True
        # Bottom
        trees = []
        for i in range(lengths[1]):
            trees.append(self.value_grid[self.height - i][y])
        if all(tree < value for tree in trees):
            return True
        # Left
        trees = []
        for i in range(lengths[2]):
            trees.append(self.value_grid[x][i])
        if all(tree < value for tree in trees):
            return True
        # Right
        trees = []
        for i in range(lengths[3]):
            trees.append(self.value_grid[x][self.width - i])
        if all(tree < value for tree in trees):
            return True
        return False

    def check_all_trees(self):
        for x, row in enumerate(self.value_grid):
            for y, value in enumerate(row):
                if self.is_visible(x, y, value):
                    self.visible_grid[x][y] = 1

    def get_all_visible_trees(self):
        n = 0
        for _, row in enumerate(self.visible_grid):
            n += sum(row)
        print(n)

    def create_visible_grid(self):
        grid = [[0] * len(self.value_grid[0]) for _ in range(len(self.value_grid))]
        grid[0] = [1] * len(self.value_grid[0])
        grid[-1] = [1] * len(self.value_grid[0])
        for i, _ in enumerate(grid):
            grid[i][0] = 1
            grid[i][-1] = 1
        return grid


def main():
    data = parse_input("input.txt")
    fe = ForestEvaluator(data)
    fe.check_all_trees()
    fe.get_all_visible_trees()


if __name__ == "__main__":
    main()
