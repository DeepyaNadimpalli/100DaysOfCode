# Building a silent auction program where the person who bids for more money wins
print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')
print("Welcome to the secret auction program.")
bids={}
import replit
while True:
	name=input("What is your name:\n")
	bid=int(input("What's your bid? \n $"))
	bids[name]=bid
	val=input("Are there any other bidders? Type 'yes' or 'no'\n")
	replit.clear()
	if val.lower()=="no":
		break
highest_bid=max(bids.values())
for i in bids:
	if bids[i]==highest_bid:
		print(f"{i} is the winner with a bid of {highest_bid}")

