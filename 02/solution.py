from pathlib import Path
from operator import mul
from functools import reduce


INPUT_SHORT = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
""".strip()

with open(Path(__file__).with_name("input.txt")) as f:
    INPUT_LONG = f.read().strip()

MAXIMUMS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def parse(line):
    game_str, _, group_strs = line.partition(": ")
    game = int(game_str[len("Game ") :])
    groups = []
    for group_str in group_strs.split("; "):
        counts = {}
        for color_str in group_str.split(", "):
            count_str, _, color = color_str.partition(" ")
            count = int(count_str)
            counts[color] = count
        groups.append(counts)
    return game, groups


def part1():
    def is_valid(group):
        return all(count <= MAXIMUMS[color] for color, count in group.items())

    count = 0
    for line in INPUT_LONG.split("\n"):
        game, groups = parse(line)
        if all(is_valid(group) for group in groups):
            count += game
    print(count)


def part2():
    def find_minimums(groups):
        def find_max(color):
            return max(group.get(color, 0) for group in groups)

        return {color: find_max(color) for color in ("red", "green", "blue")}

    count = 0
    for line in INPUT_LONG.split("\n"):
        _, groups = parse(line)
        minimums = find_minimums(groups)
        power = reduce(mul, minimums.values(), 1)
        count += power

    print(count)


if __name__ == "__main__":
    part2()
