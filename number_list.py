import math
numbers = []
for i in range(5):
    input_number = int(input("Number:"))
    numbers.append(input_number)
print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
average = sum(numbers)/len(numbers)
print("The average number is {}".format(average))