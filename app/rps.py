#Ask User for an input
user_choice =  input("Please choose one: Rock, Paper, Scissors: ")
print("USER:", user_choice)


import random

#Validations
VALID_OPTIONS = ["Rock", "Paper", "Scissors"]

if user_choice not in VALID_OPTIONS:
    print("OOPS INVALID INPUT, PLEASE TRY AGAIN")
    quit()
#Generate random computer choice


computer_choice = random.choice(VALID_OPTIONS)

print("COMP:", computer_choice)
#Determine the winner

# DETERMINE THE WINNER

print("TODO:", "DETERMINE WINNER")