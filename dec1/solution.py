import re

number_replacements = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}

with open("input.txt", "r") as file:
    data = file.readlines()


def replace_written_numbers(text):
    regex = re.compile("(%s)" % "|".join(map(re.escape, number_replacements.keys())))
    translated = regex.subn(lambda mo: number_replacements[mo.group()], text)

    while translated[1] > 0:
        translated = regex.subn(
            lambda mo: number_replacements[mo.group()], translated[0]
        )

    return translated[0]


digits = []
for line in data:
    translated_line = replace_written_numbers(line)
    all_digits = "".join(filter(str.isdigit, translated_line))
    final_digits = int(all_digits[0] + all_digits[-1])
    digits.append(int(all_digits[0] + all_digits[-1]))


print(sum(digits))
