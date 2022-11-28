# Advent of Code - Day 13
# Part 1

import re
import numpy as np

def parseInput(file):
    x = []
    y = []
    folds = []
    for line in open(file):
        if re.search(r"^\d*\,\d", line):
            point = line.strip().split(",")
            x.append(int(point[0]))
            y.append(int(point[1]))
        elif re.search(r".*\s.*\s.*", line):
            line = line.strip().split()
            fold = line[2].split("=")
            folds.append(fold)
    return x, y, folds


def fillPaper(paper, xv, yv):
    max_x = np.shape(paper)[0]
    max_y = np.shape(paper)[1]
    for i, _ in enumerate(xv):
        if xv[i] > max_x:
            xv[i] = xv[i] - 2*(xv[i]-max_x)
        if yv[i] > max_y:
            yv[i] = yv[i] - 2*(yv[i]-max_y)
        paper[xv[i], yv[i]] = 1
    return paper, xv, yv


def foldPaper(paper, fold):
    axis = fold[0]
    fold_line = int(fold[1])
    if axis == "x":
        paper_dim = [fold_line, np.shape(paper)[1]]
    else:
        paper_dim = [np.shape(paper)[0], fold_line]
    return np.zeros(paper_dim)


# ----- Part 1 && Part 2 ----- #

xv, yv, folds = parseInput('input.txt')
paper = np.zeros([max(xv)+1, max(yv)+1])

for i, fold in enumerate(folds):
    paper = foldPaper(paper, fold)
    paper, xv, yv = fillPaper(paper, xv, yv)

    # Part 1
    if i == 0:
        print(int(sum(sum(paper))))

# Part 2
paper = np.transpose(paper)
for line in paper:
    print_line = []
    for num in line:
        if int(num) == 0:
            print_line.append("\u2B1B")
        else:
            print_line.append("\u2B1C")
    print(*print_line)
