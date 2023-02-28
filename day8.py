# This project is all about decoding and encoding messages
from day8_art import logo
print(logo)
alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
def caesar(direction,text,shift):
	cipher_text=""
	for i in text:
		if i not in alphabets:
			cipher_text+=i
		elif direction=='encode':
		    cipher_text+=alphabets[alphabets.index(i)+shift]
		elif direction=='decode':
			cipher_text+=alphabets[alphabets.index(i)-shift]
	print(f"The {direction}d text is {cipher_text}")
	cipher_text=""
while True:
	direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
	text=input("Type your message:\n").lower()
	shift=int(input("Type the shift number:\n"))
	shift%=26
	caesar(direction,text,shift)
	game=input("Type 'yes' if you want to go again. Otherwise, type 'no'\n")
	if game.lower()=='no':
		print("Bye Bye")
		print("Have a good day")
		break


	




	