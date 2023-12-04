# Advent of Code - Day 4
# Part 1


from typing import List


class Ticket:
    def __init__(self, winning_numbers, numbers):
        self.winning_numbers = winning_numbers
        self.numbers = numbers


def get_amount_of_winning_numbers(ticket: Ticket) -> int:
    n_winning_numbers = 0
    for winning_number in ticket.winning_numbers:
        if winning_number in ticket.numbers:
            n_winning_numbers += 1
    return n_winning_numbers


def get_ticket_score(ticket: Ticket) -> int:
    n_winning_numbers = get_amount_of_winning_numbers(ticket)
    if n_winning_numbers == 0:
        return 0
    return 2 ** (n_winning_numbers - 1)


def get_all_tickets_score(tickets: List[Ticket]) -> int:
    sum_ticket_score = 0
    for ticket in tickets:
        sum_ticket_score += get_ticket_score(ticket)
    print(sum_ticket_score)


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
    get_all_tickets_score(tickets)


if __name__ == "__main__":
    main()
