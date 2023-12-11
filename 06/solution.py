from pathlib import Path
from math import sqrt, ceil

INPUT_SHORT = """Time:      7  15   30
Distance:  9  40  200""".strip()


with open(Path(__file__).with_name("input.txt")) as f:
    INPUT_LONG = f.read().strip()


def solve(time, distance):
    # speed1 = (time + sqrt(time*time - 4*distance))/2
    speed2 = (time - sqrt(time * time - 4 * distance)) / 2
    return ceil(speed2 + 0.001)


def part1():
    """
    Time = Speed + Go
    Distance = Speed * Go
    Distance = Speed * (Time - Speed)
    Distance = Time * Speed - Speed^2
    Speed^2 - Time*Speed + Distance = 0
    Speed = (Time +/- sqrt(Time^2 - 4*Distance))/2
    """

    times = [int(i) for i in INPUT_LONG.split("\n")[0].split()[1:]]
    distances = [int(i) for i in INPUT_LONG.split("\n")[1].split()[1:]]

    p = 1
    for time, distance in zip(times, distances):
        print(f"{time}/{distance}: {solve(time, distance)}")
        speed = solve(time, distance)
        p *= time - 2 * speed + 1
        """
        4: 7, 2. 7-2=5. 5-2+1=4
        8: 15, 4. 15-4=11. 11-4+1=8
        9: 30, 11. 30-11=19. 19-11+1=9
        time - 2*speed + 1
        """
    print(p)


def part2():
    time = int("".join(INPUT_LONG.split("\n")[0].split()[1:]))
    distance = int("".join(INPUT_LONG.split("\n")[1].split()[1:]))

    print(f"{time}/{distance}: {solve(time, distance)}")
    speed = solve(time, distance)
    p = time - 2 * speed + 1
    print(p)


if __name__ == "__main__":
    part2()
