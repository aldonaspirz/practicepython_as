# Create a program that will play the “cows and bulls” game with the user. The game works like this:

# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.
# ” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. 
# Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

# Say the number generated by the computer is 1038. An example interaction could look like this:

#   Welcome to the Cows and Bulls Game! 
#   Enter a number: 
#   >>> 1234
#   2 cows, 0 bulls
#   >>> 1256
#   1 cow, 1 bull
#   ...
# Until the user guesses the number.
import random
print("Welcome to the Cows and Bulls Game!\n ")
x=['0','1','2','3','4','5','6','7','8','9']
a=random.sample(x,4)
player_number=int(input('Enter a number:'))
print(a, player_number)

# while a!=player_number:
#     for i in a:
#         for j in player_number:
            
