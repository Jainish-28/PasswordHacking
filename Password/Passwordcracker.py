
# importing random
from random import *

# taking input from user
user_pass = input("Enter your password")

# storing alphabet letter to use thm to crack password
password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 
            'w', 'x', 'y', 'z','1','2','3','4','5','6','7','8','9','0',
            '@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
            'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y','Z']

# initializing an empty string
guess = ""



while (guess != user_pass):
    guess = ""
    # generating random passwords using for loop
    for letter in range(len(user_pass)):
        #randint choose element from password randomly
        guess_letter = password[randint(0,75)]
        #Guess is a empty and its stote element from randint and concate them one by one
        guess = str(guess_letter) + str(guess)
    
    print(guess)
    
# printing the matched password 
print("Your password is",guess)
