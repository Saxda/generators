print("Welcome to Password-Generator")
print("Special characters are: !, \", §, %, &, /, (, ), =, ?, # and *")


number_of_characters = int(input("Enter the length of the password: "))

import random

for num in range(number_of_characters):
	num = random.randint(0, 50)
	print(num)