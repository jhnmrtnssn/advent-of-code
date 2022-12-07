# Advent of Code - Day 7
# Part 1


def parse_input(file):
    data = []
    new_dir = []
    for line in open(file):
        if line.startswith("$ cd"):
            if new_dir:
                data.append(new_dir)
            new_dir = [line.strip()]
        else:
            new_dir.append(line.strip())
    return data


class FileSystem:
    def __init__(self, data):
        self.folders = {}
        self.current_dir = []

        for command in data:
            if command[0] == "$ cd ..":
                self.step_back()
            else:
                self.add_folder(command)

    def add_folder(self, command):
        name, size = create_folder(command)
        self.current_dir.append(name)
        self.folders[str(self.current_dir)] = 0

        for i, _ in enumerate(self.current_dir):
            self.folders[str(self.current_dir[0 : i + 1])] += size

    def step_back(self):
        self.current_dir.pop()

    def get_total_sum(self):
        total_sum = 0
        for value in self.folders.values():
            if value <= 100000:
                total_sum += value
        return total_sum


def create_folder(ls_command: list):
    name = ls_command[0].split("cd")[1].strip()
    size = 0
    if len(ls_command) > 2:
        for f in ls_command[2:]:
            if not f.startswith("dir"):
                size += int(f.split(" ")[0])
    return name, size


def main():
    data = parse_input("input.txt")
    file_system = FileSystem(data)
    print(file_system.get_total_sum())


if __name__ == "__main__":
    main()
