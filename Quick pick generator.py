import random

NUMBERS_IN_ROW = 6
LOWER = 1
MAX = 45
number_generator = []
quick_picks = int(input("How many quick picks would you like to generate?"))
for quick_picks in range(quick_picks):
    for num in range(NUMBERS_IN_ROW):
        random_number = random.randint(LOWER,MAX)
        while random_number in number_generator:
            random_number = random.randint(LOWER, MAX)
        number_generator.append(random_number)
    number_generator.sort()
    print(number_generator)
    number_generator.clear()

