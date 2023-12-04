# Advent of Code - Day 4
# Part 2


from typing import List


class Ticket:
    def __init__(self, winning_numbers, numbers):
        self.winning_numbers = winning_numbers
        self.numbers = numbers


def get_amount_of_winning_scratchcards(ticket: Ticket) -> int:
    n_winning_numbers = 0
    for winning_number in ticket.winning_numbers:
        if winning_number in ticket.numbers:
            n_winning_numbers += 1
    return n_winning_numbers


def get_total_amount_of_scratchcards(tickets: List[Ticket]) -> int:
    n_tickets_list = [1] * len(tickets)
    for i, ticket in enumerate(tickets):
        n_new_tickets = get_amount_of_winning_scratchcards(ticket)
        for new_ticket in range(i + 1, i + 1 + n_new_tickets):
            n_tickets_list[new_ticket] += n_tickets_list[i]
    print(sum(n_tickets_list))


def parse_input(file):
    tickets = []
    with open(file, "r", encoding="utf-8") as f:
        for line in f.readlines():
            winning_numbers, numbers = line.split(":")[1].split("|")
            winning_numbers = list(map(int, winning_numbers.strip().split()))
            numbers = list(map(int, numbers.strip().split()))
            tickets.append(Ticket(winning_numbers, numbers))
    return tickets


def main():
    tickets = parse_input("input.txt")
    get_total_amount_of_scratchcards(tickets)


if __name__ == "__main__":
    main()
