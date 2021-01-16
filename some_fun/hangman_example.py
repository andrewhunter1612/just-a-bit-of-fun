

user_word_list = list(input("Enter a word: "))

correct_word = []

for letter in user_word_list:
    correct_word.append("")

while correct_word != user_word_list:
    second_user_guess = input("Enter a letter: ")
    for index, letter in enumerate(user_word_list):
        if second_user_guess == letter:
            correct_word[index] = letter
            
    print(correct_word)
    if correct_word == user_word_list:
        break

print("You are correct!")

