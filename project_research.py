#PROBLEM SOLVING I

# Declare a variable called favorite_number and store your favorite or lucky number within it. 
# Use the random module to generate a random number between a range that includes your favorite number.
# Determine how many numbers away the random number was from your favorite number
# Create a while loop that generates a random number and checks if it matches your favorite number.
# Keep track of how many times the computer has guessed.
# Once the computer guesses the correct number, display a message explaining how many attempts it took the computer to guess your favorite number.

from operator import index
import random
import string
#Favorite number
#favorite_num = 93 // 


# Difference between favorite and random number
# def difference_cal(rand_num, fav_num):  
#     cal = int(rand_num) - int(fav_num)
#     return cal

# favorite_num = 93
# random_number = random.randint(1,93)

# fav_diff = difference_cal(random_number, favorite_num)
# print(f' The difference is {abs(fav_diff)} ')

#Python loop number guessing loop
# fav_num = 93

# tries = 0

# random_number = int()

# while random_number != fav_num:
#     random_number = random.randint(1,93)
#     tries += 1 
#     print("re-rolling..")
#     if random_number == fav_num:
#         print(f' It took {tries} rolls to find your {fav_num}')

#PROBLEM SOLVING II

# Write code that takes a string as input and returns the string reversed
#i.e. “Hello” will be returned as “olleH”

#Word reverserizor
# words = input("What's the word?\n")
# drow_ver = ''

# for drow in range(len(words) -1, -1, -1):
#     drow_ver += words[drow]
# print(drow_ver)

# Write code that takes a string as input and 
# capitalize the first letter of each word. Words will be separated by only one space. 
# i.e. “hello world” should be outputted as “Hello World”

# Cap my words
# cap_my_word = input("Cap what?\n")
# result = string.capwords(cap_my_word)
# print(result)

# cap_my_word2 = input("Cap what?\n") #second try at it, unsucessful.
# first_l = cap_my_word2[0]
# rest_l = cap_my_word2[1:]
# result = first_l.upper() + rest_l
# print(result)

# A “palindrome” is a word, phrase, or sequence that reads the same backward as forward i.e. madam	
# Write code that takes a user input and checks to see if it is a Palindrome and reports the result

# Palindrome checker

# palindrome = input("Is it a palindrome?\n")

# answer = ''

# for drome in range(len(palindrome) -1, -1, -1): #checks the word in the reverse
#     answer += palindrome[drome]

# if answer == palindrome:
#      print("Succes")
# else:
#     print("Fail!")

#Compress a string of characters
# For example, an input of "aaabbbbbccccaacccbbbaaabbbaaa" would compress to "3a5b4c2a3c3b3a3b3a"

# condense_this = input("What would you like to condense?\n")

# answer = ""

# number = 1
# for this in range(len(condense_this)-1):
#     if answer[this] = answer[this+1]:
#         number = number + 1

# Happy Numbers

# A happy number is a number defined by the following process: starting with any positive integer, 
# replace the number by the sum of the squares of its digits, 
# and repeat the process until the number equals 1. 
# An example of a happy number is 19

#  def happy_number(HN): #funtion to calculate input number
#     #number = add = 0
#     while (number > 0):
#         number = HN % 10
#         add = add + (number * number)
#         HN = HN / 10
#     return add

# sad_number = int(input)

# A prime number is a number that is only divisible by one and itself.
# Write a method that prints out all prime numbers between 1 and 100 

prime_numbers = int(input("Enter a number to list the primes:\n"))

print("The prime numbers are:\n")

for num in range(0, prime_numbers +1):
    if num > 1:
        for p in range(2,num):
            if (num % p)==0:
             break
        else:
            print(num)

    