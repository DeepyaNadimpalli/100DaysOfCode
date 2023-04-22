# Black jack game
from art import logo11 as logo
# The deck is unlimited in size. 
# There are no jokers. 
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def print_cards():
	""" This function is used to calculate score and print the player's cards, player's score , computer's first card """
	current_score=sum(player_cards)
	dealer_score=sum(dealer_cards)
	print(f"Your cards: {player_cards},current_score: {current_score}")
	print(f"Computer's first card: {dealer_cards[0]}")
def print_final_cards():
	""" This function is used to calculate score and print the player's final cards, player's final score , computer's final cards and computer's final score """
	current_score=sum(player_cards)
	dealer_score=sum(dealer_cards)
	print(f"Your final hand: {player_cards}, final score : {current_score}")
	print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
def ace_value(_cards):
	"""This function checks for ace(value : 11) in the _cards and replaces it with 1 if sum(_cards)>21 """
	if sum(_cards)>21 and (11 in _cards):
		for i in range(len(_cards)):
			if sum(_cards)<=21:
				break
			elif _cards[i]==11:
				_cards[i]=1
def play():
	"""1.This function checks if either computer or player has Blackjack  
	   2.If the player wants to get more cards, it adds more cards into player_cards randomly
	   3.Otherwise it would print whether the player has won or lost"""
	if dealer_blackjack:
		print_final_cards()
		print("You lose. Opponent has Blackjack")
	elif sum(player_cards)==21 :
		print_final_cards()
		print("Black jack Win")
	else:
		print_cards()
		while True:		
			con=input("Type 'y' to get another card, type 'n' to pass:")
			if con.lower()=='y':
				player_cards.append(random.choice(cards))
				ace_value(player_cards)
				if sum(player_cards)>21:
					print_final_cards()
					print("You went over. You lose")
					break
			else :
				print_final_cards()
				if sum(player_cards)==21:
					print("You Won")
				elif sum(player_cards)<21 :
					if (((sum(player_cards)>sum(dealer_cards) ) or( sum(dealer_cards)>21 ) )):
						print("You won")
					elif (sum(player_cards)==sum(dealer_cards)):
						print("Draw")
					else:
						print("You lose")
				break
			print_cards()
while True:
	wanna_play=input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
	if wanna_play.lower()=='y':
		print(logo)
		dealer_blackjack=False
		player_cards=random.sample(cards,2)
		dealer_cards=random.sample(cards,2)
		if sum(dealer_cards)==21:
			dealer_blackjack=True
		while (sum(dealer_cards)<17 or (sum(dealer_cards)>21 and 11 in dealer_cards)):
			dealer_cards.append(random.choice(cards))
			ace_value(dealer_cards)
		play()
	else:
		print("Bye Bye")
		break



	




