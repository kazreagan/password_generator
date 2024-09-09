print("Welcome!")
char = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', 'a', 'B', 'c', 'D', 'e', 'F', 'g', 'H', 'i', 'J', 'K', 'Z', 'x']

import random
password = ''
num_digits = int(input("how many characters do you want for your password?:\n"))

for i in range(num_digits):
    num_digits = random.choice(char)
    password += num_digits

print(f"Your Password is: {password}")