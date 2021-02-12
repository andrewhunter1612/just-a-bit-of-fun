import random

class Password:
    def __init__(self):
        self.password = ""
        self.password_length = 0

    def get_individual_character(self, number):
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

        # if the number entered by the user is between 0 and 25 inclusive return the item in the alphabet list
        #else if the number entered by the user is between 25 and 51 return the letter at position -26, and capitlise the letter
        #else display an error to the user, saying that the number given is out of range
    
        if number <25:
            return alphabet[number]
        elif number >=25 and number<52:
            return alphabet[number-26].upper()
        else:
            return str(number-52)
            

    def generate_password(self, length):
        while len(self.password)< length:
            letter = self.get_individual_character(random.randrange(0,61))
            self.password += letter
        
