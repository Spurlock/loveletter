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


def mprint(stuff=None, lvl=5):
    if lvl <= PRINT_LEVEL:
        if stuff is None:
            stuff = ""
        print stuff

GUARD = 1
PRIEST = 2
BARON = 3
HANDMAID = 4
PRINCE = 5
KING = 6
COUNTESS = 7
PRINCESS = 8
SUICIDE = 9

AFFECTION_GOAL = 4

"""
0	silence
1	print match outcome
2	game outcomes
3	round outcomes
4	major occurrences in round
5	minor occurrences in round
6	debugging minutiae
"""
PRINT_LEVEL = 2


def full_deck():
    return [
        1, 1, 1, 1, 1,
        2, 2,
        3, 3,
        4, 4,
        5, 5,
        6, 7, 8
    ]