from pathlib import Path

INPUT_SHORT = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""


def part1():
    def get_num(line):
        first = next(c for c in line if c.isdigit())
        last = next(c for c in line[::-1] if c.isdigit())
        return int(first + last)

    with open(Path(__file__).with_name("input.txt")) as f:
        INPUT = f.read()

    s = sum(get_num(line) for line in INPUT.strip().split("\n"))
    print(s)


NUMBERS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0,
}

NUMBERS_REVERSED = {num_str[::-1]: num for num_str, num in NUMBERS.items()}


def part2():
    INPUT_SHORT = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

    def find_number(text, numbers):
        if text[0].isdigit():
            return int(text[0])
        for num_str, num in numbers.items():
            if text.startswith(num_str):
                return num
        return find_number(text[1:], numbers)

    def get_num(line):
        first = find_number(line, NUMBERS)
        last = find_number(line[::-1], NUMBERS_REVERSED)
        return int(f"{first}{last}")

    with open(Path(__file__).with_name("input.txt")) as f:
        INPUT = f.read()

    s = sum(get_num(line) for line in INPUT.strip().split("\n"))
    print(s)


if __name__ == "__main__":
    part2()
