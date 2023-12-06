with open("input.txt", "r") as file:
    data = file.read()
    lines = data.splitlines()

number_map = []
gear_coords = []

for line_count, line in enumerate(lines):
    n_coord = None
    for char_count, char in enumerate(line):
        if char == "*":
            gear_coords.append({"x": char_count, "y": line_count})

        if char.isdigit():
            if n_coord:
                n_coord["value"] += char
                n_coord["coords"].append({"x": char_count, "y": line_count})
            else:
                n_coord = {
                    "value": char,
                    "coords": [{"x": char_count, "y": line_count}],
                }
        else:
            if n_coord:
                n_coord["value"] = int(n_coord["value"])
                number_map.append(n_coord)
                n_coord = None

    if n_coord:
        if n_coord:
            n_coord["value"] = int(n_coord["value"])
            number_map.append(n_coord)
            n_coord = None

special_characters = "!@#$%^&*()-+?_=,<>/"


def get_surrounding_coords(x: int, y: int):
    surrounding = []
    if y - 1 >= 0:
        if x - 1 >= 0:
            surrounding.append({"x": x - 1, "y": y - 1})
        surrounding.append({"x": x, "y": y - 1})
        if x + 1 <= len(lines[y - 1]) - 1:
            surrounding.append({"x": x + 1, "y": y - 1})

    if x - 1 >= 0:
        surrounding.append({"x": x - 1, "y": y})
    if x + 1 <= len(lines[y]) - 1:
        surrounding.append({"x": x + 1, "y": y})

    if y + 1 <= len(lines) - 1:
        if x - 1 >= 0:
            surrounding.append({"x": x - 1, "y": y + 1})
        surrounding.append({"x": x, "y": y + 1})
        if x + 1 <= len(lines[y + 1]) - 1:
            surrounding.append({"x": x + 1, "y": y + 1})
    return surrounding


def get_surrounding_characters(x: int, y: int):
    characters = []
    for coord in get_surrounding_coords(x, y):
        characters.append(lines[coord["y"]][coord["x"]])

    return characters


p1_sum = 0
for map in number_map:
    for coord in map["coords"]:
        characters = get_surrounding_characters(coord["x"], coord["y"])
        if any(c in special_characters for c in characters):
            p1_sum += map["value"]
            break

p2_sum = 0
for gear in gear_coords:
    surrounding_numbers = set()
    for coord in get_surrounding_coords(gear["x"], gear["y"]):
        for nm in number_map:
            if coord in nm["coords"]:
                surrounding_numbers.add(nm["value"])

    if len(surrounding_numbers) == 2:
        prod = 1
        for num in surrounding_numbers:
            prod *= num
        p2_sum += prod


print(p1_sum)
print(p2_sum)
