from pathlib import Path

INPUT_SHORT = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4""".strip()


with open(Path(__file__).with_name("input.txt")) as f:
    INPUT_LONG = f.read().strip()


def part1():
    parts = INPUT_LONG.split("\n\n")
    seeds = None

    for part in parts:
        lines = part.split("\n")
        if len(lines) == 1 and lines[0].startswith("seeds: "):
            seeds = [int(s) for s in lines[0][len("seeds: ") :].split(" ")]
            print(seeds)
        else:
            which, mappings = lines[0], lines[1:]
            next_seeds = [s for s in seeds]
            for mapping in mappings:
                dst_start, src_start, length = [int(p) for p in mapping.split(" ")]
                for i, seed in enumerate(seeds):
                    if src_start <= seed < src_start + length:
                        next_seed = dst_start + seed - src_start
                        next_seeds[i] = next_seed
            seeds = next_seeds
            print(seeds)
    print(sorted(seeds))


def part2():
    parts = INPUT_LONG.split("\n\n")
    seed_ranges = []

    for part in parts:
        lines = part.split("\n")
        if len(lines) == 1 and lines[0].startswith("seeds: "):
            seed_pairs = [int(s) for s in lines[0][len("seeds: ") :].split(" ")]
            for start, length in zip(seed_pairs[0::2], seed_pairs[1::2]):
                seed_ranges.append((start, length))
        else:
            which, mappings = lines[0], lines[1:]
            next_seed_ranges = []
            for mapping in mappings:
                dst_start, src_start, length = [int(p) for p in mapping.split(" ")]
                i = 0
                while i < len(seed_ranges):
                    seed_start, seed_length = seed_ranges.pop(i)
                    if src_start <= seed_start < src_start + length:
                        if seed_start + seed_length <= src_start + length:
                            """
                            seed:     S---E
                            src:    S-------E
                            """
                            next_seed_range = (
                                dst_start + seed_start - src_start,
                                seed_length,
                            )
                            next_seed_ranges.append(next_seed_range)
                        else:
                            """
                            seed:     S-----|---E
                            src:    S-------E
                            """
                            # seed range exceeds dst remapping, split into remapped + trailing
                            next_seed_range = (
                                dst_start + seed_start - src_start,
                                src_start + length - seed_start,
                            )
                            next_seed_ranges.append(next_seed_range)
                            trailing_range = (
                                src_start + length,
                                seed_start + seed_length - src_start - length,
                            )
                            seed_ranges.append(trailing_range)
                    elif seed_start <= src_start < seed_start + seed_length:
                        if seed_start + seed_length > src_start + length:
                            """
                            seed:   S-|-----|-E
                            src:      S-----E
                            """
                            next_seed_range = (seed_start, src_start - seed_start)
                            seed_ranges.append(next_seed_range)
                            next_seed_range = (dst_start, length)
                            next_seed_ranges.append(next_seed_range)
                            next_seed_range = (
                                src_start + length,
                                seed_start + seed_length - src_start - length,
                            )
                            seed_ranges.append(next_seed_range)
                        else:
                            """
                            seed:   S-|-------E
                            src:      S-----------E
                            """
                            next_seed_range = (seed_start, src_start - seed_start)
                            seed_ranges.append(next_seed_range)
                            next_seed_range = (
                                dst_start,
                                seed_start + seed_length - src_start,
                            )
                            next_seed_ranges.append(next_seed_range)
                    else:
                        seed_ranges.insert(i, (seed_start, seed_length))
                        i += 1
            seed_ranges.extend(next_seed_ranges)
    print(sorted(seed_ranges)[0])


if __name__ == "__main__":
    part2()
