# Advent of Code - Day 8
# Part 2


def parse_input(file):
    data = []
    for line in open(file):
        data.append(list(map(int, line.strip())))
    return data


class ForestEvaluator:
    def __init__(self, data):
        self.value_grid = data
        self.width = len(self.value_grid[0]) - 1
        self.height = len(self.value_grid) - 1

    def scenic_score(self, x, y, value):
        lengths = [x, self.height - x, y, self.width - y]
        top = 0
        bottom = 0
        left = 0
        right = 0

        # Top
        trees = []
        for i in range(lengths[0]):
            trees.append(self.value_grid[i][y])
        for i, tree in enumerate(reversed(trees)):
            top = i + 1
            if value <= tree:
                break

        # Bottom
        trees = []
        for i in range(lengths[1]):
            trees.append(self.value_grid[self.height - i][y])
        for i, tree in enumerate(reversed(trees)):
            bottom = i + 1
            if value <= tree:
                break

        # Left
        trees = []
        for i in range(lengths[2]):
            trees.append(self.value_grid[x][i])
        for i, tree in enumerate(reversed(trees)):
            left = i + 1
            if value <= tree:
                break

        # Right
        trees = []
        for i in range(lengths[3]):
            trees.append(self.value_grid[x][self.width - i])
        for i, tree in enumerate(reversed(trees)):
            right = i + 1
            if value <= tree:
                break

        return top * bottom * left * right

    def check_all_trees(self):
        best_scenic_score = 0
        for x, row in enumerate(self.value_grid):
            for y, value in enumerate(row):
                score = self.scenic_score(x, y, value)
                if score > best_scenic_score:
                    best_scenic_score = score
        print(best_scenic_score)


def main():
    data = parse_input("input.txt")
    fe = ForestEvaluator(data)
    fe.check_all_trees()


if __name__ == "__main__":
    main()
