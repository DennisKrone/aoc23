BLUE_RULE = 14
RED_RULE = 13
GREEN_RULE = 12

games = []
with open("input.txt", "r") as file:
    lines = file.read().splitlines()

    for line in lines:
        s = line.split(":")
        sets = s[1].split(";")
        game = []
        for set in sets:
            formatted_set = {}
            r = set.split(",")
            for result in r:
                result = result.strip()
                x = result.split(" ")
                formatted_set[x[1]] = int(x[0])
            game.append(formatted_set)

        games.append(game)
sum = 0
p2_sum = 0
count = 0
for game in games:
    valid = True
    count += 1

    blue_max = 0
    red_max = 0
    green_max = 0
    for set in game:
        blue_max = max(set.get("blue", 0), blue_max)
        red_max = max(set.get("red", 0), red_max)
        green_max = max(set.get("green", 0), green_max)

        if (
            set.get("blue", 0) > BLUE_RULE
            or set.get("red", 0) > RED_RULE
            or set.get("green", 0) > GREEN_RULE
        ):
            valid = False
    p2_sum += red_max * green_max * blue_max
    if valid:
        sum += count


print(sum)
print(p2_sum)
