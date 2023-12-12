from pathlib import Path

INPUT_SHORT = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45""".strip()


with open(Path(__file__).with_name("input.txt")) as f:
    INPUT_LONG = f.read().strip()


def solve(sequence):
    levels = [sequence]
    while True:
        level = [b - a for a, b in zip(levels[-1][:-1], levels[-1][1:])]
        levels.append(level)
        if all(i == 0 for i in level):
            break

    last = 0
    for level in levels[::-1]:
        last = level[-1] + last

    return last


def part1():
    answer = 0
    for line in INPUT_LONG.split("\n"):
        history = [int(i) for i in line.split()]
        answer += solve(history)
    print(answer)


def solve_backwards(sequence):
    levels = [sequence]
    while True:
        level = [b - a for a, b in zip(levels[-1][:-1], levels[-1][1:])]
        levels.append(level)
        if all(i == 0 for i in level):
            break

    last = 0
    for level in levels[::-1]:
        last = level[0] - last

    return last


def part2():
    answer = 0
    for line in INPUT_LONG.split("\n"):
        history = [int(i) for i in line.split()]
        answer += solve_backwards(history)
    print(answer)


if __name__ == "__main__":
    part2()
