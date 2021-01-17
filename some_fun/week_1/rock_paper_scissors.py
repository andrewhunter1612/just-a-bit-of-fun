
player_one = input("Player 1: enter rock, paper or scissors: ")
player_two = input("Player 2: enter rock, paper or scissors: ")

outcomes = [
    {"name": "rock", "beats": "scissors", "loses": "paper"}, 
    {"name": "paper", "beats": "rock", "loses": "scissors"},
    {"name": "scissors", "beats": "paper", "loses": "rock"}
]

for outcome in outcomes:
    if outcome["name"] == player_one:
        if player_two == outcome["beats"]:
            print("player one wins")
        elif player_two == outcome["loses"]:
            print("player two wins")
    
