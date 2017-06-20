class Player(object):
    def __init__(self, my_idx):
        pass

    def play_turn(self, player_hand, public_game_state, game_history):
        pass

    def learn(self, player_idx, hand, turn_idx):
        pass

GUARD = 1
PRIEST = 2
BARON = 3
HANDMAID = 4
PRINCE = 5
KING = 6
COUNTESS = 7
PRINCESS = 8
SUICIDE = 9
