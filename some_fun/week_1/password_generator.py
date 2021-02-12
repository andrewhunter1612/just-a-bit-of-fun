import random


def get_individual_letter(number):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    if number <25:
        return alphabet[number]
    elif number >=25 and number<52:
        return alphabet[number-26].upper()
    else:
        return str(number-52)
        
password_letter_index = 0
password = ""
letter = ""

password_length = int(input("Enter a password length: "))
while password_letter_index < password_length:
    letter = get_individual_letter(random.randrange(0,61))
    password += letter

    password_letter_index += 1
print(password)
