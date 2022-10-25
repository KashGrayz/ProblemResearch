# Declare a variable called favorite_number and store your favorite or lucky number within it. 
# Use the random module to generate a random number between a range that includes your favorite number.
# Determine how many numbers away the random number was from your favorite number
# Create a while loop that generates a random number and checks if it matches your favorite number.
# Keep track of how many times the computer has guessed.
# Once the computer guesses the correct number, display a message explaining how many attempts it took the computer to guess your favorite number.

import random


def difference_cal(rand_num, fav_num):
    cal = int(rand_num) - int(fav_num)
    return cal

favorite_num = 93
random_number = random.randrange(93)

fav_diff = difference_cal(random_number, favorite_num)
print(f' The difference is {fav_diff} ')
