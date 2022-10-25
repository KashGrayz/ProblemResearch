# Declare a variable called favorite_number and store your favorite or lucky number within it. 
# Use the random module to generate a random number between a range that includes your favorite number.
# Determine how many numbers away the random number was from your favorite number
# Create a while loop that generates a random number and checks if it matches your favorite number.
# Keep track of how many times the computer has guessed.
# Once the computer guesses the correct number, display a message explaining how many attempts it took the computer to guess your favorite number.

import random


# def difference_cal(rand_num, fav_num):
#     cal = int(rand_num) - int(fav_num)
#     return cal

# favorite_num = 93
# random_number = random.randrange(93)

# fav_diff = difference_cal(random_number, favorite_num)
# print(f' The difference is {abs(fav_diff)} ')





fav_num = 93

tries = 0

random_number = int()

while random_number != fav_num:
    random_number = random.randint(1,93)
    tries += 1 
    print("re-rolling..")
    if random_number == fav_num:
        print(f' It took {tries} rolls to find your {fav_num}')