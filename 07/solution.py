from pathlib import Path
from collections import defaultdict

INPUT_SHORT = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
""".strip()


"""Every hand is exactly one type. From strongest to weakest, they are:

Five of a kind, where all five cards have the same label: AAAAA
Four of a kind, where four cards have the same label and one card has a different label: AA8AA
Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
High card, where all cards' labels are distinct: 23456
"""


ORDER = "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2"
CARD_RANKS = {card: rank for rank, card in enumerate(reversed(ORDER.split(", ")))}


def sort_key(cards):
    counts = defaultdict(int)
    for card in cards:
        counts[card] += 1

    card_counts = sorted(counts.values(), reverse=True)
    rank = 0
    if card_counts[0] == 5:
        rank = 6
    elif card_counts[0] == 4:
        rank = 5
    elif card_counts[0] == 3 and card_counts[1] == 2:
        rank = 4
    elif card_counts[0] == 3:
        rank = 3
    elif card_counts[0] == 2 and card_counts[1] == 2:
        rank = 2
    elif card_counts[0] == 2:
        rank = 1

    return (rank,) + tuple(CARD_RANKS[card] for card in cards)


with open(Path(__file__).with_name("input.txt")) as f:
    INPUT_LONG = f.read().strip()


def part1():
    hands = {}
    for line in INPUT_LONG.split("\n"):
        hand, bid_str = line.split()
        hands[hand] = int(bid_str)

    winnings = 0
    for i, hand in enumerate(sorted(hands.keys(), key=sort_key)):
        print(f"{i+1}: {hand} ({hands[hand]})")
        winnings += (i + 1) * hands[hand]
    print(winnings)


ORDER_JOKER = "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J"
CARD_RANKS_JOKER = {
    card: rank for rank, card in enumerate(reversed(ORDER_JOKER.split(", ")))
}


def sort_key_joker(cards):
    counts = defaultdict(int)
    for card in cards:
        counts[card] += 1

    joker_count = counts.pop("J", 0)
    card_counts = sorted(counts.values(), reverse=True)
    if joker_count == 5:
        card_counts = [5]
    else:
        card_counts[0] += joker_count

    rank = 0
    if card_counts[0] == 5:
        rank = 6
    elif card_counts[0] == 4:
        rank = 5
    elif card_counts[0] == 3 and card_counts[1] == 2:
        rank = 4
    elif card_counts[0] == 3:
        rank = 3
    elif card_counts[0] == 2 and card_counts[1] == 2:
        rank = 2
    elif card_counts[0] == 2:
        rank = 1

    return (rank,) + tuple(CARD_RANKS_JOKER[card] for card in cards)


def part2():
    hands = {}
    for line in INPUT_LONG.split("\n"):
        hand, bid_str = line.split()
        hands[hand] = int(bid_str)

    winnings = 0
    for i, hand in enumerate(sorted(hands.keys(), key=sort_key_joker)):
        print(f"{i+1}: {hand} ({hands[hand]})")
        winnings += (i + 1) * hands[hand]
    print(winnings)


if __name__ == "__main__":
    part2()
