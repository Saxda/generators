print("Welcome to RandomNumberGenerator!")
print("Please indicate in which area the number/numbers should be generated and how many numbers should be generated.")
print("Please note that you first enter the number range and then the number of numbers.")
print("Please note that you only use whole numbers.")

number_range_a = int(input("number range from:"))
number_range_b = int(input("number range to:"))
number_of_numbers = int(input("number of numbers:"))

import random

for num in range(number_of_numbers):
	num = random.randint(number_range_a, number_range_b)
	print(num)
