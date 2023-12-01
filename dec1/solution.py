with open("input.txt", "r") as file:
    data = file.readlines()

digits = []
for line in data:
    all_digits = ''.join(filter(str.isdigit, line))
    digits.append(int(all_digits[0] + all_digits[-1]))


print(sum(digits))