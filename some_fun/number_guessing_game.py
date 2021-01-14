import random


user_input = input("Please enter a number: ")
target_number = random.randrange(0,10)


while int(user_input) != int(target_number):
    print("Sorry, try again")
    user_input = input("Please enter a number: ")

print("Correct") 

    


