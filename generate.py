import random

numbers = []

for i in range(10):
    new_numbers = random.randint(1, 10)
    numbers.append(new_numbers)
print(numbers)

numbers = set(numbers)
print(numbers)