score_cards = []

with open("input.txt", "r") as file:
    data = file.read()
    lines = data.splitlines()
    for line in lines:
        a = line.split(":")
        lists = a[1].split("|")
        card = []
        for list in lists:
            list = list.strip()
            list = list.split()
            numbers = []
            for number in list:
                numbers.append(int(number))
            card.append(numbers)
        score_cards.append(card)

def get_amount_matching(winning, chosen):
    matching = 0
    for number in chosen:
        if number in winning:
            matching += 1
    return matching


p1_sum = 0
for card in score_cards:
    matches = get_amount_matching(card[0], card[1])
    if matches > 0:
        score = 1
        for _ in range(matches - 1):
            score = score * 2
        p1_sum += score

print(p1_sum)