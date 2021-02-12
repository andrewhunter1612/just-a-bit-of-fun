class Player:
    def __init__(self, name, id=None):
        self.name = name
        self.guessing = False
        self.id = id
        self.current_word = ""
        self.number_of_wins = 0
        self.number_of_games = 0
        self.words_used = []

    def set_new_word_used(self, new_word):
        self.words_used.append(new_word)

    def game_won(self):
        self.number_of_wins += 1
        self.number_of_games += 1
    
    def game_lost(self):
        self.number_of_games += 1

    def set_player_guessing_turn(self, guessing):
        self.guessing = guessing