# Advent of Code - Day 13
# Part 1


def cluster_rows_to_int(cluster):
    row_values = []
    for line in cluster:
        value = 0
        for i, char in enumerate(reversed(line)):
            if char == "#":
                value += 2**i
        row_values.append(value)
    return row_values


def cluster_cols_to_int(cluster):
    column_values = []
    for i in range(0, len(cluster[0])):
        column = [row[i] for row in cluster]
        value = 0
        for j, char in enumerate(reversed(column)):
            if char == "#":
                value += 2**j
        column_values.append(value)
    return column_values


def is_perfect_reflection_line(l, i):
    j = 0
    while True:
        j += 1
        if i - j < 0 or i + j + 2 > len(l):
            return True
        if l[i - j] == l[i + 1 + j]:
            continue
        return False


def get_reflection_lines(l):
    for i in range(len(l) - 1):
        if l[i] == l[i + 1]:
            if is_perfect_reflection_line(l, i):
                return i + 1
    return 0


def get_reflection_value(clusters):
    value = 0
    for cluster in clusters:
        row, col = cluster
        n_rows = get_reflection_lines(row)
        n_cols = get_reflection_lines(col)

        if n_rows >= n_cols:
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
        row = cluster_rows_to_int(c)
        col = cluster_cols_to_int(c)
        cluster_values.append((row, col))

    return cluster_values


def main():
    clusters = parse_input("input.txt")
    get_reflection_value(clusters)


if __name__ == "__main__":
    main()
