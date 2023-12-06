import re

SPEED_PER_MS_CHARGE = 1
times = []
distances = []
p2_time = 0
p2_distance = 0

with open("dec6/input.txt", "r") as file:
    data = file.read()
    lines = data.splitlines()
    times = re.findall(r"\d+", lines[0])
    p2_time = int("".join(times))
    times = [int(i) for i in times]
    distances = re.findall(r"\d+", lines[1])
    p2_distance = int("".join(distances))
    distances = [int(i) for i in distances]


def get_win_with_charge_time(
    charge_time: int, race_time: int, record_distance: int
) -> bool:
    distance = (charge_time * SPEED_PER_MS_CHARGE) * (race_time - charge_time)
    return distance > record_distance


win_possibilitites = []
for count, time in enumerate(times):
    wins = 0
    for charge in range(time):
        if get_win_with_charge_time(charge, time, distances[count]):
            wins += 1

    win_possibilitites.append(wins)

p2_wins = 0
for charge in range(p2_time):
    if get_win_with_charge_time(charge, p2_time, p2_distance):
        p2_wins += 1


wins = 1
for win in win_possibilitites:
    wins *= win
print(wins)
print(p2_wins)
