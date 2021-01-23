import random

def return_random_decision(random_number):
    choice = ["rock", "paper", "scissors"]
    return choice[random_number] 


def start_game():
    number_of_players = int(input("Enter the number of players: "))
    while number_of_players < 0 or number_of_players > 2:
        number_of_players = int(input("Enter a number of players between 0 and 2: "))

    number_of_games = 1
    player_one_wins = 0
    player_two_wins = 0
    draws = 0

    outcomes = [
        {"name": "rock", "beats": "scissors", "loses": "paper"}, 
        {"name": "paper", "beats": "rock", "loses": "scissors"},
        {"name": "scissors", "beats": "paper", "loses": "rock"}
    ]

    number_of_games = int(input("Enter number of games: "))

    for _ in range(number_of_games):
        if number_of_players == 0:
            player_one = return_random_decision(random.randrange(0,2))
            player_two = return_random_decision(random.randrange(0,2))
        elif number_of_players ==1:
            player_one = input("Player 1: enter rock, paper or scissors: ")
            player_two = return_random_decision(random.randrange(0,2))
        elif number_of_players ==2:
            player_one = input("Player 1: enter rock, paper or scissors: ")
            player_two = input("Player 2: enter rock, paper or scissors: ")
        else:
            number_of_players = input("Enter the number of players: ")

        for outcome in outcomes:
            if outcome["name"] == player_one:
                if player_two == outcome["beats"]:
                    player_one_wins += 1
                    print("player one wins")
                elif player_two == outcome["loses"]:
                    player_two_wins += 1
                    print("player two wins")
                elif player_two == outcome["name"]:
                    draws += 1
        print("Player one wins: "+str(player_one_wins))
        print("Player two wins: "+str(player_two_wins))
        print("Draws: " + str(draws))

    play_again()

def play_again():
    again = input("Would you like to play again?: ")
    if again.lower() == "yes":
        start_game()

start_game()