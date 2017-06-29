from common import Player, GUARD, PRIEST, BARON, HANDMAID, PRINCE, KING, COUNTESS, PRINCESS
from random import randint, choice


class IdiotBot(Player):
    def __init__(self, my_idx):
        Player.__init__(self, my_idx)
        self.my_idx = my_idx
        self.name = "Idiot"

    def get_available_targets(self, player_states):
        available_targets = []
        for idx, p_state in enumerate(player_states):
            if idx != self.my_idx and p_state.is_alive and not p_state.handmaided:
                available_targets.append(idx)
        return available_targets

    def play_turn(self, player_hand, public_game_state):
        card = min(player_hand)
        target = None
        guess = None

        available_targets = self.get_available_targets(public_game_state.player_states)

        if COUNTESS in player_hand:
            card = COUNTESS

        if card == PRINCE:
            if len(available_targets) > 0:
                target = choice(available_targets)
            else:
                target = self.my_idx

        if card in [PRIEST, BARON, KING, GUARD]:
            target = choice(available_targets) if len(available_targets) > 0 else None
            
        if card == GUARD:
            guess = randint(2, 8)

        return {
            'card': card,
            'target_player': target,
            'guess': guess
        }

    def learn(self, player_idx, hand, turn_idx):
        pass