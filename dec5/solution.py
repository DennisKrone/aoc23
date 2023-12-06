import re

p1_seeds = []
p2_seed_ranges = []
maps = []
with open("input.txt", "r") as file:
    data = file.read()
    lines = data.splitlines()
    seedline = lines.pop(0)
    p1_seeds = re.findall(r"\d+", seedline)
    p1_seeds = [int(i) for i in p1_seeds]
    lines = list(filter(None, lines))

    for seed in [i for i in p1_seeds if p1_seeds.index(i) % 2 == 0]:
        p2_seed_ranges.append([seed, seed + p1_seeds[p1_seeds.index(seed) + 1] - 1])

    map_count = 0
    maps.append([])
    for line in lines:
        numbers = re.findall(r"\d+", line)
        numbers = [int(i) for i in numbers]
        if numbers:
            maps[map_count].append(numbers)
        else:
            maps.append([])
            map_count += 1
    maps = [m for m in maps if m]


def get_output_from_map(input: int, map_list: list[list[int]]) -> int:
    for l in map_list:
        if l[1] <= input <= l[1] + l[2]:
            return l[0] + (input - l[1])

    return input


p1_soil_numbers = []
for seed in p1_seeds:
    value = seed
    for map in maps:
        value = get_output_from_map(value, map)

    p1_soil_numbers.append(value)


def split_at_number(start: int, end: int, split: int) -> list[list[int]]:
    ranges = []
    if start <= split < end:
        ranges.append([start, split])
        ranges.append([split + 1, end])
    return ranges


def split_range(range: list[int], map: list[int]) -> dict:
    range_start = range[0]
    range_end = range[1]
    map_start = map[1]
    map_end = map[1] + map[2] - 1
    ranges_inside = []
    ranges_outside = []

    if map_start <= range_start:
        # Range start to the right of map start
        if map_end < range_start:
            # Completely outside (to the right)
            ranges_outside.append([range_start, range_end])
        elif range_end <= map_end:
            # Completely inside
            ranges_inside.append([range_start, range_end])
        else:
            # Range end outside map (to the right). Need to split rangess
            ranges = split_at_number(range_start, range_end, map_end)
            ranges_inside.append(ranges[0])
            ranges_outside.append(ranges[1])
    else:
        # Range start to the left of map start
        if range_end < map_start:
            # Completely outside to the left
            ranges_outside.append([range_start, range_end])
        elif range_end <= map_end:
            # Partly inside
            ranges = split_at_number(range_start, range_end, map_start - 1)
            ranges_outside.append(ranges[0])
            ranges_inside.append(ranges[1])
        else:
            # cover map completely
            left_split = split_at_number(range_start, range_end, map_start - 1)
            ranges_outside.append(left_split[0])

            right_split = split_at_number(left_split[1][0], range_end, map_end)
            ranges_inside.append(right_split[0])
            ranges_outside.append(right_split[1])

    return {"inside": ranges_inside, "outside": ranges_outside}


p2_locations = []


def locations_for_range(start: int, end: int) -> list[int]:
    ranges = [[start, end]]
    for map in maps:
        new_ranges = []
        for submap in map:
            checked = []
            for r in ranges:
                split = split_range(r, submap)
                for inside in split["inside"]:
                    inside[0] = submap[0] + (inside[0] - submap[1])
                    inside[1] = submap[0] + (inside[1] - submap[1])
                    new_ranges.append(inside)
                checked.extend(split["outside"])
            ranges = checked

        ranges.extend(new_ranges)

    p2_locations.extend(ranges)


for r in p2_seed_ranges:
    locations_for_range(r[0], r[1])


locations = []
for r in p2_locations:
    locations.append(r[0])

print(min(p1_soil_numbers))
print(min(locations))
