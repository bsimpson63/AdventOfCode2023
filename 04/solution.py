from pathlib import Path
from collections import defaultdict
import math

INPUT_SHORT = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
""".strip()


with open(Path(__file__).with_name("input.txt")) as f:
    INPUT_LONG = f.read().strip()


def part1():
    s = 0
    for line in INPUT_LONG.split("\n"):
        _, _, line = line.partition(": ")
        winners_str, _, numbers_str = line.partition(" | ")
        winners = {int(s) for s in winners_str.split()}
        numbers = {int(s) for s in numbers_str.split()}
        overlap = winners.intersection(numbers)
        print(f"{winners}/{numbers}/{overlap}")
        if overlap:
            s += int(math.pow(2, len(overlap) - 1))
        print(s)


def part2():
    card_counts = defaultdict(int)
    for line in INPUT_LONG.split("\n"):
        card_str, _, line = line.partition(": ")
        card_number = int(card_str[len("Card ") :])
        winners_str, _, numbers_str = line.partition(" | ")
        winners = {int(s) for s in winners_str.split()}
        numbers = {int(s) for s in numbers_str.split()}
        overlap = winners.intersection(numbers)
        win_count = len(overlap)

        card_counts[card_number] += 1
        for next_card_number in range(card_number + 1, card_number + win_count + 1):
            card_counts[next_card_number] += card_counts[card_number]

    print(sum(card_count for card_number, card_count in card_counts.items()))


if __name__ == "__main__":
    part2()
