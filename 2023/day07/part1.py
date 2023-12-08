# Advent of Code - Day 7
# Part 1

# Poker hand scores
FIVE_OF_A_KIND = 7
FOUR_OF_A_KIND = 6
FULL_HOUSE = 5
THREE_OF_A_KIND = 4
TWO_PAIR = 3
ONE_PAIR = 2
HIGH_CARD = 1

dressed_cards = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}


def card_to_value(card):
    if card.isdigit():
        return int(card)
    return dressed_cards[card]


def secondary_hand_score(cards):
    c = [card_to_value(x) for x in cards]
    return c[0] * 14**4 + c[1] * 14**3 + c[2] * 14**2 + c[3] * 14 + c[4]


def parse_input(file):
    poker_hands = []
    with open(file, "r", encoding="utf-8") as f:
        for line in f.readlines():
            cards, bid = line.strip().split()
            poker_hands.append(PokerHand(list(cards), int(bid)))

    return poker_hands


class PokerHand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.card_value_list = self.get_card_value_list()
        self.poker_score = self.get_hand_score()
        self.effective_score = self.get_effective_poker_score()

    def get_card_value_list(self):
        card_value_list = [0] * 15
        for card in self.cards:
            card_value_list[card_to_value(card)] += 1
        return card_value_list

    def get_hand_score(self):
        if max(self.card_value_list) == 5:
            return FIVE_OF_A_KIND
        if max(self.card_value_list) == 4:
            return FOUR_OF_A_KIND
        if max(self.card_value_list) == 3:
            if 2 in self.card_value_list:
                return FULL_HOUSE
            return THREE_OF_A_KIND
        if max(self.card_value_list) == 2:
            if self.card_value_list.count(2) == 2:
                return TWO_PAIR
            return ONE_PAIR
        return HIGH_CARD

    def get_effective_poker_score(self):
        return self.poker_score * 14**5 + secondary_hand_score(self.cards)


def sort_by_effective_poker_score(hands):
    all_hands = {}
    for hand in hands:
        all_hands[hand.effective_score] = hand
    return list(sorted(all_hands.items()))


def get_total_winnings(hands):
    sorted_hands = sort_by_effective_poker_score(hands)
    total_winnings = 0
    for rank, (_, hand) in enumerate(sorted_hands, 1):
        total_winnings += hand.bid * rank
    print(total_winnings)


def main():
    hands = parse_input("input.txt")
    get_total_winnings(hands)


if __name__ == "__main__":
    main()
