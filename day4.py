#Rock paper Scissors game
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
print("Welcome to Rock paper Scissors game")
user=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if (user==0):
	print(rock)
elif(user ==1):
	print(paper)
else:
	print(scissors)
import random
comp=random.choice([0,1,2])
print("Computer chose\n")
if (comp==0):
	print(rock)
elif(comp ==1):
	print(paper)
else:
	print(scissors)
if(comp==user):
	print("Draw")
elif((user==0 and comp==2) or(user==1 and comp ==0) or (user==2 and comp==1) ):
	print("You won")
else:
	print("You lose")
