class Player(object):
    def __init__(self, my_idx):
        pass

    def play_turn(self, player_hand, public_game_state):
        pass

    def learn(self, player_idx, hand, turn_idx):
        pass


def get_card_name(card_rank):
    if not isinstance(card_rank, int) or card_rank < 1 or card_rank > 8:
        return "Invalid"
    names = ["Guard", "Priest", "Baron", "Handmaid", "Prince", "King", "Countess", "Princess", "Suicide"]
    return names[card_rank - 1]

GUARD = 1
PRIEST = 2
BARON = 3
HANDMAID = 4
PRINCE = 5
KING = 6
COUNTESS = 7
PRINCESS = 8
SUICIDE = 9
