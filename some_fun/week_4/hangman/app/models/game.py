class Game:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.current_word = ""
        self.number_of_guesses_left = 10

    def game_won(self, player):
        player.game_won()

    def reduce_guesses_left(self):
        self.number_of_guesses_left -=1
    
    def play_game(self):

        pass

