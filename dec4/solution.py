import re

score_cards = []

with open("input.txt", "r") as file:
    data = file.read()
    lines = data.splitlines()
    for line in lines:
        a = line.split(":")
        lists = a[1].split("|")
        card = {"solution": [], "ticket": [], "amount": 1}
        for count, list in enumerate(lists):
            list = list.strip()
            list = list.split()
            for number in list:
                if count == 0:
                    card["solution"].append(int(number))
                else:
                    card["ticket"].append(int(number))


        score_cards.append(card)

def get_amount_matching(winning, chosen):
    matching = 0
    for number in chosen:
        if number in winning:
            matching += 1
    return matching


p1_sum = 0
for card_count, card in enumerate(score_cards):
    matches = get_amount_matching(card["solution"], card["ticket"])
    #p1
    if matches > 0:
        score = 1
        for _ in range(matches - 1):
            score = score * 2
        p1_sum += score
    #p2
    for _ in range(card["amount"]):
        for i in range(matches):
            score_cards[card_count + i + 1]["amount"] += 1
            
            

print(p1_sum)
print(sum([card["amount"] for card in score_cards]))
