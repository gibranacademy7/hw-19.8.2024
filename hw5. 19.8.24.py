import random

numbers: int = [random.randint(100, 500) for _ in range(50)];
# random.randint(100, 500) generates a random integer between 100 and 500, inclusive.
unique_numbers = set(numbers);
unique_count = len(unique_numbers);

print("The numbers:", numbers);
print("Unique numbers:", unique_numbers);
print("Count of Unique numbers:", unique_count);
