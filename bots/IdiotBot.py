from common import Player, GUARD, PRIEST, BARON, HANDMAID, PRINCE, KING, COUNTESS, PRINCESS
from random import randint

class IdiotBot(Player):
    def __init__(self, my_idx):
        Player.__init__(self, my_idx)
        self.my_idx = my_idx

    def play_turn(self, player_hand, public_game_state):
        card = min(player_hand)
        target = None
        guess = None

        if card in [PRIEST, BARON, PRINCE, KING, GUARD]:
            for p_idx, player_state in enumerate(public_game_state.player_states):
                if p_idx != self.my_idx and player_state.is_alive and not player_state.handmaided:
                    target = p_idx
                    break
            
        if card == GUARD:
            guess = randint(2, 8)

        return {
            'card': card,
            'target_player': target,
            'guess': guess
        }


    def learn(self, player_idx, hand, turn_idx):
        pass