from art import logo12 as logo
import random
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty_level=input("Choose a difficulty. Type 'easy' or 'hard':")
if difficulty_level.lower()=='easy':
	attempts=10
else:
	attempts=5
num=random.randint(1,100)
win=False
while attempts>0:
	print(f"You have {attempts} attempts remaining to guess the number.")
	guess=int(input("Make a guess: "))
	if (guess>num):
		print("Too high.")
		print("Guess again")
	elif (guess<num):
		print("Too low")
		print("Guess again")
	else:
		print(f"You got it! The answer was {num}")
		win=True
		break
	attempts-=1
if not win:
	print("You ran out of guesses, you lose")
