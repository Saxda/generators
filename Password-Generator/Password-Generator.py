print("Welcome to Password-Generator")

number_of_characters = int(input("Enter the length of the password"))



import random

for num in range(number_of_characters):
	num = random.randint(character_range_a, character_range_b)
	print(num)
