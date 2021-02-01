class Player:
    def __init__(self, name, moves):
        self.name = name
        self.moves = moves

    def add_player_move(self, move):
        self.moves.append(move)