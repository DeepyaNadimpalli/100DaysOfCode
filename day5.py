# Password Generator
alphabets=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']
print("Welcome to the Password Generator")
no_of_letters=int(input("Howmany no of letters do you want in your password?\n"))
no_of_symbols=int(input("Howmany no of symbols do you want in your password?\n"))
no_of_numbers=int(input("Howmany no of numbers do you want in your password?\n"))
l=[]
import random
for i in range(no_of_letters):
	l.append(random.choice(alphabets))
for i in range(no_of_symbols):
	l.append(random.choice(symbols))
for i in range(no_of_numbers):
	l.append(random.choice(numbers))
random.shuffle(l)
print(f"Here is your password : {''.join(l)}")
