# Advent of Code - Day 13
# Part 2


def cluster_rows_to_int(cluster):
    row_values = []
    for line in cluster:
        value = 0
        n_smudges = line.count("#")
        for i, char in enumerate(reversed(line)):
            if char == "#":
                value += 2**i
        row_values.append((value, n_smudges))
    return row_values


def cluster_cols_to_int(cluster):
    column_values = []
    for i in range(0, len(cluster[0])):
        column = [row[i] for row in cluster]
        value = 0
        n_smudges = column.count("#")
        for j, char in enumerate(reversed(column)):
            if char == "#":
                value += 2**j
        column_values.append((value, n_smudges))
    return column_values


def is_perfect_reflection_line(row, i, fixed_smudge):
    j = 0
    while True:
        j += 1
        if i - j < 0 or i + j + 2 > len(row):
            if not fixed_smudge:
                return False
            return True
        if row[i - j][0] == row[i + 1 + j][0]:
            continue
        if not fixed_smudge:
            if equal_if_one_smudge(row, i - j, i + 1 + j):
                fixed_smudge = True
                continue

        return False


def equal_if_one_smudge(row, x1, x2):
    diff = abs(row[x1][0] - row[x2][0])
    if diff in [2**j for j in range(0, 20)]:
        if abs(row[x1][1] - row[x2][1]) == 1:
            return True
    return False


def get_reflection_lines(row):
    for i in range(len(row) - 1):
        if equal_if_one_smudge(row, i, i + 1):
            if is_perfect_reflection_line(row, i, fixed_smudge=True):
                return i + 1
        if row[i][0] == row[i + 1][0]:
            if is_perfect_reflection_line(row, i, fixed_smudge=False):
                return i + 1
    return 0


def get_reflection_value(clusters):
    value = 0
    for cluster in clusters:
        row, col = cluster
        n_rows = get_reflection_lines(row)
        n_cols = get_reflection_lines(col)
        if n_rows > 0:
            value += 100 * n_rows
        else:
            value += n_cols
    print(value)


def parse_input(file):
    all_clusters = []
    cluster = []
    with open(file, "r", encoding="utf-8") as f:
        for line in f.readlines():
            if len(line.strip()) == 0:
                all_clusters.append(cluster)
                cluster = []
            else:
                cluster.append(line.strip())
        all_clusters.append(cluster)

    cluster_values = []
    for c in all_clusters:
        row = cluster_rows_to_int(c)  # (value, n_smudges)
        col = cluster_cols_to_int(c)  # (value, n_smudges)
        cluster_values.append((row, col))

    return cluster_values


def main():
    clusters = parse_input("input.txt")
    get_reflection_value(clusters)


if __name__ == "__main__":
    main()
