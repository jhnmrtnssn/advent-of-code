# Advent of Code - Day 19
# Part 1

from copy import deepcopy

ORE = 0
CLAY = 1
OBSIDIAN = 2
GEODE = 3
PASS = 4


def parse_input(file):
    blueprints = {}
    for line in open(file):
        line = line.strip().split(":")
        id_number = int(line[0].split(" ")[1])
        ore_robot_cost = int(line[1].split("costs ")[1].split(" ore")[0])
        clay_robot_cost = int(line[1].split("costs ")[2].split(" ore")[0])
        ores = int(line[1].split("costs ")[3].split(" ore")[0])
        clay = int(line[1].split("costs ")[3].split("and ")[1].split(" clay")[0])
        obsidian_robot_cost = (ores, clay)
        geode_ores = int(line[1].split("costs ")[4].split(" ore")[0])
        obs = int(line[1].split("costs ")[4].split("and ")[1].split(" obsidian")[0])
        geode_robot_cost = (geode_ores, obs)
        blueprints[id_number] = {
            "id": id_number,
            "ore_robot_cost": ore_robot_cost,
            "clay_robot_cost": clay_robot_cost,
            "obsidian_robot_cost": obsidian_robot_cost,
            "geode_robot_cost": geode_robot_cost,
        }
    return blueprints


def get_tactics(n_robots):
    """
    if n_robots == 1:
        return [ORE, CLAY]
    if n_robots == 2:
        return [ORE, CLAY]
    if n_robots == 3:
        return [ORE, CLAY]
    if n_robots == 4:
        return [OBSIDIAN]
    if n_robots == 5:
        return [CLAY]
    if n_robots == 6:
        return [ORE, CLAY, OBSIDIAN]
    if n_robots == 7:
        return [GEODE]
    if n_robots == 8:
        return [GEODE]
    return [GEODE]
    """

    # return [ORE, CLAY, OBSIDIAN, GEODE]

    # Filter 6 - Optimize build order
    if n_robots <= 2:
        return [ORE, CLAY]
    elif n_robots <= 10:
        return [ORE, CLAY, OBSIDIAN, GEODE]
    elif n_robots <= 15:
        return [ORE, CLAY, OBSIDIAN, GEODE]
    elif n_robots <= 18:
        return [CLAY, OBSIDIAN, GEODE]
    else:
        return [OBSIDIAN, GEODE]


class OreCollector:
    def __init__(self, blueprint):
        self.initiate_robot_costs(blueprint)
        self.states = {"": ""}
        self.minutes_left = 24
        self.resources = [0, 0, 0, 0]
        self.income = [1, 0, 0, 0]
        self.new_income = [0, 0, 0, 0]
        self.best_score = 0

    def initiate_robot_costs(self, blueprint):
        ores = blueprint["ore_robot_cost"]
        self.ore_robot_cost = [ores, 0, 0, 0]

        ores = blueprint["clay_robot_cost"]
        self.clay_robot_cost = [ores, 0, 0, 0]

        ores = blueprint["obsidian_robot_cost"][0]
        clay = blueprint["obsidian_robot_cost"][1]
        self.obsidian_robot_cost = [ores, clay, 0, 0]

        ores = blueprint["geode_robot_cost"][0]
        obsidian = blueprint["geode_robot_cost"][1]
        self.geode_robot_cost = [ores, 0, obsidian, 0]

    def max_cost(self, robot):
        o1 = self.ore_robot_cost[robot]
        o2 = self.clay_robot_cost[robot]
        o3 = self.obsidian_robot_cost[robot]
        o4 = self.geode_robot_cost[robot]
        return max((o1, o2, o3, o4))

    def can_build(self, robot, resources):
        if robot == ORE:
            return resources[ORE] >= self.ore_robot_cost[ORE]
        if robot == CLAY:
            return resources[ORE] >= self.clay_robot_cost[ORE]
        if robot == OBSIDIAN:
            return (
                resources[ORE] >= self.obsidian_robot_cost[ORE]
                and resources[CLAY] >= self.obsidian_robot_cost[CLAY]
            )
        if robot == GEODE:
            return (
                resources[ORE] >= self.geode_robot_cost[ORE]
                and resources[OBSIDIAN] >= self.geode_robot_cost[OBSIDIAN]
            )
        if robot == PASS:
            return True

    def can_build_in_five_turns(self, robot):
        future_resources = [0, 0, 0, 0]
        for i in range(4):
            future_resources[i] = self.resources[i] + 5 * self.income[i]
        return self.can_build(robot, future_resources)

    def build_robot(self, robot):
        if robot == ORE:
            cost = self.ore_robot_cost
        elif robot == CLAY:
            cost = self.clay_robot_cost
        elif robot == OBSIDIAN:
            cost = self.obsidian_robot_cost
        elif robot == GEODE:
            cost = self.geode_robot_cost
        else:
            return

        self.new_income[robot] += 1
        for i in range(4):
            self.resources[i] -= cost[i]

    def increase_resources(self):
        for i in range(4):
            self.resources[i] += self.income[i]

    def increase_income(self):
        for i in range(4):
            self.income[i] += self.new_income[i]
        self.new_income = [0, 0, 0, 0]

    def recursive_robot_buyer(self, minutes_left):
        state = (
            tuple(self.income),
            tuple(self.resources),
            tuple(self.new_income),
            minutes_left,
        )
        if state in self.states:
            return
        self.states[state] = 1

        curr_minutes_left = minutes_left
        curr_income = deepcopy(self.income)
        curr_new_income = deepcopy(self.new_income)
        curr_resources = deepcopy(self.resources)
        for robot in get_tactics(sum(curr_income) + sum(curr_new_income)):
            # Filter 1 - Don't build more robots than max material cost
            if (
                robot in [ORE, CLAY, OBSIDIAN]
                and self.max_cost(robot) == curr_income[robot]
            ):
                continue
            # Filter 2 - Build a geode if it can be built
            if robot is not GEODE and self.can_build(GEODE, curr_resources):
                continue
            # Filter 3 - Build an Obsidian robot if it can be built
            # if robot in [ORE, CLAY] and self.can_build(OBSIDIAN, curr_resources):
            #    continue
            # Filter 4 - Skip deep states which will yield too few geodes
            # if minutes_left < 3 and self.income[GEODE] == 0:
            #    break
            # Filter 5 - Try next robot if it can not be built in five turns
            # if not self.can_build_in_five_turns(robot):
            #    continue

            for i in range(1, curr_minutes_left + 1):
                self.increase_income()

                built_robot = False
                if self.can_build(robot, self.resources):
                    self.build_robot(robot)
                    built_robot = True
                self.increase_resources()

                if built_robot:
                    prev_minutes_left = curr_minutes_left - i
                    prev_income = deepcopy(self.income)
                    prev_new_income = deepcopy(self.new_income)
                    prev_resources = deepcopy(self.resources)

                    self.recursive_robot_buyer(prev_minutes_left)

                    self.income = deepcopy(prev_income)
                    self.new_income = deepcopy(prev_new_income)
                    self.resources = deepcopy(prev_resources)

                if self.resources[GEODE] > self.best_score:
                    self.best_score = self.resources[GEODE]

            self.income = deepcopy(curr_income)
            self.new_income = deepcopy(curr_new_income)
            self.resources = deepcopy(curr_resources)


def calc_quality_level(data):
    quality_level = 0
    for key in data.keys():
        id_number = key
        ore_collector = OreCollector(data[id_number])
        ore_collector.recursive_robot_buyer(minutes_left=24)
        geodes = ore_collector.best_score
        print(id_number)
        print(id_number * geodes)
        print("-----------")
        quality_level += id_number * geodes
    print(quality_level)


def main():
    data = parse_input("input.txt")
    calc_quality_level(data)


if __name__ == "__main__":
    main()
