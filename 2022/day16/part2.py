# Advent of Code - Day 16
# Part 2


# Run time of ~3h and coded with incredibly stupid functions.
# Might fix someday, probably not.


from typing import Dict, List


def parse_input(file):
    data = {}
    for line in open(file):
        line = line.strip().split(" has flow rate=")
        name = line[0].split(" ")[1]
        flow = int(line[1].split(";")[0])
        valves = line[1].split("valve")[1].split(", ")
        if valves[0].startswith("s"):
            valves[0] = valves[0].split("s ")[1]
        if valves[0].startswith(" "):
            valves[0] = valves[0].strip()
        data[name] = {"name": name, "flow": flow, "connecting": valves}
    return data


class PressureOptimizer:
    def __init__(self, data: Dict):
        self.valves = data
        self.flow_valves = self.get_flow_valves()
        self.me_start = self.valves["AA"]
        self.elephant_start = self.valves["AA"]
        self.traveled: List[Dict] = []
        self.my_time_left = 26
        self.elephant_time_left = 26
        self.best_score = 0
        self.is_elephant = True
        print(
            self.simulate_elephant_and_me_score(
                self.me_start,
                self.elephant_start,
                0,
                [],
                self.elephant_time_left,
                self.my_time_left,
            )
        )

    def get_flow_valves(self):
        flow_valves = {}
        for name in self.valves:
            if self.valves[name]["flow"] > 0:
                flow_valves[name] = self.valves[name]
        return flow_valves

    def travel_and_open_valve(
        self,
        me_start_valve,
        elephant_start_valve,
        goal_valve,
        my_time_left,
        elephant_time_left,
    ):
        if self.is_elephant:
            dist = self.get_shortest_distance(elephant_start_valve, goal_valve) + 1
            if elephant_time_left - dist < 0 or (dist > 4 and elephant_time_left < 20):
                return my_time_left, elephant_time_left, 0
            elephant_time_left -= dist
            time_left = elephant_time_left
        else:
            dist = self.get_shortest_distance(me_start_valve, goal_valve) + 1
            if my_time_left - dist < 0 or (dist > 4 and my_time_left < 20):
                return my_time_left, elephant_time_left, 0
            my_time_left -= dist
            time_left = my_time_left

        return my_time_left, elephant_time_left, time_left * goal_valve["flow"]

    def get_shortest_distance(self, start_valve, goal_valve):
        distance = 0
        valves_to_visit = start_valve["connecting"]
        visited_valves = [start_valve["name"]]
        new_valves = []
        found_valve = False
        while not found_valve:
            distance += 1
            new_valves = []
            for valve_name in valves_to_visit:
                if valve_name in visited_valves:
                    continue
                visited_valves.append(valve_name)
                if valve_name == goal_valve["name"]:
                    found_valve = True
                    break
                for connecting_valve in self.valves[valve_name]["connecting"]:
                    if connecting_valve not in visited_valves:
                        new_valves.append(connecting_valve)
            valves_to_visit = new_valves

        return distance

    def simulate_elephant_and_me_score(
        self,
        me_start_valve,
        elephant_start_valve,
        score,
        traveled,
        elephant_time_left,
        my_time_left,
    ):
        best_score = 0
        prev_score = score
        self.is_elephant = not self.is_elephant
        for valve_name in self.flow_valves:
            new_score = score
            if valve_name in traveled:
                continue
            (
                new_my_time_left,
                new_elephant_time_left,
                travel_score,
            ) = self.travel_and_open_valve(
                me_start_valve,
                elephant_start_valve,
                self.valves[valve_name],
                my_time_left,
                elephant_time_left,
            )
            if travel_score == 0:
                self.is_elephant = not self.is_elephant
                (
                    new_my_time_left,
                    new_elephant_time_left,
                    travel_score,
                ) = self.travel_and_open_valve(
                    me_start_valve,
                    elephant_start_valve,
                    self.valves[valve_name],
                    my_time_left,
                    elephant_time_left,
                )
            if travel_score > 0:
                traveled.append(valve_name)
                if self.is_elephant:
                    new_score += self.simulate_elephant_and_me_score(
                        me_start_valve,
                        self.valves[valve_name],
                        travel_score,
                        traveled,
                        new_elephant_time_left,
                        new_my_time_left,
                    )
                else:
                    new_score += self.simulate_elephant_and_me_score(
                        self.valves[valve_name],
                        elephant_start_valve,
                        travel_score,
                        traveled,
                        new_elephant_time_left,
                        new_my_time_left,
                    )

                if new_score == prev_score:
                    new_score += travel_score
                if new_score > best_score:
                    best_score = new_score
                if new_score > self.best_score:
                    print(self.best_score)
                    print(traveled)
                    self.best_score = new_score

                traveled.pop(traveled.index(valve_name))
        return best_score


def main():
    data = parse_input("input.txt")
    po = PressureOptimizer(data)


if __name__ == "__main__":
    main()
