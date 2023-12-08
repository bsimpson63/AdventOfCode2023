from pathlib import Path
from collections import defaultdict

INPUT_SHORT = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".strip()


with open(Path(__file__).with_name("input.txt")) as f:
    INPUT_LONG = f.read().strip()


DELTAS = [
    (1, 1),
    (1, 0),
    (1, -1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
    (0, 1),
    (0, -1),
]


def parse_grid(text):
    grid = {}
    for y, line in enumerate(text.split("\n")):
        for x, c in enumerate(line):
            grid[(x, y)] = c
    return grid


def part1():
    grid = parse_grid(INPUT_LONG)
    xmax = max(x for x, _ in grid.keys())
    ymax = max(y for _, y in grid.keys())

    s = 0
    for y in range(ymax + 1):
        x = 0
        while x <= xmax:
            if not grid[(x, y)].isdigit():
                x += 1
                continue

            is_valid = False
            num = ""
            while x <= xmax:
                if not grid[(x, y)].isdigit():
                    break

                if not is_valid:
                    for dx, dy in DELTAS:
                        is_valid |= (
                            (x + dx, y + dy) in grid
                            and grid[(x + dx, y + dy)] != "."
                            and not grid[(x + dx, y + dy)].isdigit()
                        )

                num += grid[(x, y)]
                x += 1

            if is_valid:
                s += int(num)
    print(s)


def part2():
    grid = parse_grid(INPUT_LONG)
    xmax = max(x for x, _ in grid.keys())
    ymax = max(y for _, y in grid.keys())

    gears = defaultdict(list)
    for y in range(ymax + 1):
        x = 0
        while x <= xmax:
            if not grid[(x, y)].isdigit():
                x += 1
                continue

            gear_location = None
            num = ""
            while x <= xmax:
                if not grid[(x, y)].isdigit():
                    break

                if not gear_location:
                    for dx, dy in DELTAS:
                        if (x + dx, y + dy) in grid and grid[(x + dx, y + dy)] == "*":
                            gear_location = (x + dx, y + dy)

                num += grid[(x, y)]
                x += 1

            if gear_location:
                gears[gear_location].append(int(num))
    s = 0
    for numbers in gears.values():
        if len(numbers) == 2:
            s += numbers[0] * numbers[1]
    print(s)


if __name__ == "__main__":
    part2()
