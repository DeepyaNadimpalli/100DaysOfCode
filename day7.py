stages=[ '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       ''')
from day7_words import word_list
import random
chosen_word=random.choice(word_list)
l=len(chosen_word)*['_']
lives= 6 
flag=0
while (lives!=0 ):
    guess=input("Guess a letter ").lower()
    if guess in l:
        print("You have already guessed this letter")
        flag=1
    else:
        for i in range(len(chosen_word)):
            if chosen_word[i]==guess:
                l[i]=guess
                flag=1
    print("".join(l))
    if "".join(l)==chosen_word:
        print("You won")
        break
    elif flag==0:
        print(f'The letter you have guessed {guess} is not in the list. You loose a life')
        lives-=1
        print(stages[6-(lives+1)])
    flag=0
if lives==0:
    print("You lost")







