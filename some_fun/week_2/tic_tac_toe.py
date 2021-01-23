player_history = [
    {"name": "player_1", "turn_history": []},
    {"name": "player_2", "turn_history": []}
]

player_one_turn = True
game_won = False
turn_count = [0, 0]

def take_a_turn(remaining_positions, player_move):
    while player_move not in possible_inputs:
        player_move = int(input("Enter a position: "))
    print(player_one_turn)
    possible_inputs.remove(player_move)
    if player_one_turn:
        player_history[0]["turn_history"].append(player_move)
    else:
        player_history[1]["turn_history"].append(player_move)

    return remaining_positions

def check_if_game_won(player_history, player_one_turn):
    winning_positions = [
        [1,3,5],
        [1,2,3],
        [3,6,9],
        [1,5,9],
        [7,8,9],
        [3,5,7],
        [2,5,8],
        [4,5,6]
    ]

    if player_one_turn:
        pass






first_question = input("Would you like to play a game? ")
number_of_players = int(input("How many players: "))



possible_inputs = [*range(1,10)]


while game_won == False:
    if player_one_turn:
        player_one_move = int(input("Enter a position: "))
        possible_inputs = take_a_turn(possible_inputs, player_one_move)
        
    else:
        player_two_move = int(input("Enter a position: "))
        take_a_turn(possible_inputs, player_two_move)
    print(player_history)
    if turn_count[0] >= 3 or turn_count[1] >= 3:
        check_if_game_won(player_history, player_one_turn)

    player_one_turn = not player_one_turn







