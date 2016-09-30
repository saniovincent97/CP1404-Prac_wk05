import random

NUMBERS_IN_ROW = 6
LOWER = 1
MAX = 45
quick_picks = int(input("How many quick picks would you like to generate?"))
for number in range(quick_picks):
    numbers = []
    for num in range(NUMBERS_IN_ROW):
        random_number = random.randint(LOWER,MAX)
        while random_number in numbers:
            random_number = random.randint(LOWER, MAX)
        numbers.append(random_number)
    numbers.sort()


