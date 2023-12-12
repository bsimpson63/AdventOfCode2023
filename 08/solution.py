from pathlib import Path
from itertools import cycle

INPUT_SHORT = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)""".strip()


with open(Path(__file__).with_name("input.txt")) as f:
    INPUT_LONG = f.read().strip()


def part1():
    nodes = {}
    steps, node_strs = INPUT_LONG.split("\n\n")
    for line in node_strs.split("\n"):
        source, _, rest = line.partition(" = ")
        left, _, right = rest[1:-1].partition(", ")
        nodes[source] = {"L": left, "R": right}

    node = "AAA"
    for i, step in enumerate(cycle(steps)):
        node = nodes[node][step]
        if node == "ZZZ":
            print(i + 1)
            break


def part2():
    INPUT_SHORT = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)""".strip()

    mapping = {}
    steps, node_strs = INPUT_LONG.split("\n\n")
    for line in node_strs.split("\n"):
        source, _, rest = line.partition(" = ")
        left, _, right = rest[1:-1].partition(", ")
        mapping[source] = {"L": left, "R": right}

    answer = 1
    nodes = [node for node in mapping.keys() if node.endswith("A")]
    for start_node in nodes:
        node = start_node
        seen = {}
        for i, step in enumerate(cycle(steps)):
            node = mapping[node][step]
            if node.endswith("Z"):
                if node in seen:
                    print(f"{start_node}: {node} loop {seen[node]},{i+1}")
                    answer *= seen[node]
                    break
                else:
                    seen[node] = i + 1
    print(answer)
    """
    We need to take the prime factors of each and see there is a common 271 in each
    Then multiply the unique factors to get the answer.
    79 x 271
    53 x 271
    59 x 271
    61 x 271
    71 x 271
    73 x 271
    """


if __name__ == "__main__":
    part2()
