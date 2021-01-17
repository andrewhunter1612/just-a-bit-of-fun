import random

number_of_possibilities = 10000

number_to_guess = random.randrange(0,number_of_possibilities)
guessed_number = None

for guess in range(number_of_possibilities+1):
    if guess == number_to_guess:
        print(guess)
        break



