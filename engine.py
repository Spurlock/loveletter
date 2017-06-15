"""
NOTES AND DEFINITIONS

deck = [CARD_RANK, CARD_RANK, ..., CARD_RANK] # burner is not separate, is just the last card

move = {
    card: CARD_RANK, 
    ?target_player: player_idx, 
    ?target_card: CARD_RANK
}

game_history = [
  {
    player: INT,
    move,
    ?eliminated_player: INT
  }
]



create deck
shuffle
deal //random starter for first round?

loop until game winner:
  loop until round winner:
    update current_player
    move = current_player.play(player_hand, public_game_state)
    compute move results, update game_state and game_history
"""

from random import shuffle
from copy import copy

GUARD = 1
PRIEST = 2
BARON = 3
HANDMAID = 4
PRINCE = 5
KING = 6
COUNTESS = 7
PRINCESS = 8

class Player(object):
    def __init__(self):
        pass

    def play_turn(self, player_hand, public_game_state, game_history):
        pass

    def learn(player_idx, hand, turn_idx):
        pass


class GameState(object):
    def __init__(self, players):
        player_states = []
        for _ in players:
            player_states.append(PlayerState())

        game_deck = [card for card in FULL_DECK]
        shuffle(game_deck)
        self.deck = game_deck

        self.player_states = player_states
        self.history = []
        self.turn_record = None

    def deal_card(self, player_idx):
        card = self.deck.pop(0)
        self.player_states[player_idx]['hand'].append(card)

    def eliminate_player(self, player_idx, reason=None):
        print "Eliminating player %d" % player_idx
        if reason:
            print "Reason: %s" % reason
        self.turn_record['eliminated_player'] = player_idx

        player_state = self.player_states[player_idx]
        player_state.is_alive = False
        player_state.graveyard.extend(player_state.hand)
        player_state.hand = []


class PublicGameState(object):
    def __init__(self, game_state):
        self.player_states = [PublicPlayerState(p) for p in game_state.player_states]
        self.cards_remaining = len(game_state.deck)
        self.history = [copy(record) for record in game_state.history]


class PlayerState(object):
    def __init__(self):
        self.graveyard = []
        self.is_alive = True,
        self.affection_tokens = 0
        self.hand = []
        self.handmaided = False


class PublicPlayerState(object):
    def __init__(self, player_state):
        self.graveyard = player_state.graveyard
        self.is_alive = player_state.is_alive
        self.affection_tokens = player_state.affection_tokens
        self.handmaided = player_state.handmaided


FULL_DECK = [
    1, 1, 1, 1, 1,
    2, 2,
    3, 3,
    4, 4,
    5, 5,
    6, 7, 8
]

PLAYERS = [Player() for _ in xrange(4)]

def play_game():

    game_state = GameState(PLAYERS)
    for player_idx, _ in enumerate(PLAYERS):
        game_state.deal_card(player_idx)

    winner = None
    current_player_idx = 0  # TO DO: respect last winner

    # play a round
    while winner is None and len(game_state.deck) > 0:

        # whose turn is it?
        current_player_idx = (current_player_idx + 1) % len(PLAYERS)
        while not game_state.player_states[current_player_idx].is_alive:
            current_player_idx = (current_player_idx + 1) % len(PLAYERS)
        current_player = PLAYERS[current_player_idx]
        current_player_state = game_state.player_states[current_player_idx]

        # every turn housekeeping
        current_player_state.handmaided = False

        game_state.deal_card(current_player_idx)
        public_game_state = PublicGameState(game_state)

        player_action = current_player.play_turn(current_player_state.hand, public_game_state)

        played_card = player_action['card']
        target = player_action.get('target_player')
        guess = player_action.get('target_card')

        game_state.turn_record = {
            'player_idx': current_player_idx,
            'action': player_action,
            'eliminated_player': None
        }

        try:
            current_player_state.hand.remove(played_card)
        except ValueError as err:
            game_state.eliminate_player(current_player_idx, "played unavailable card")
            # TO DO : check for winner?
            continue

        current_player_state.graveyard.append(played_card)

        if played_card == GUARD:
            # TO DO: validate that target and guess are provided and valid
            if guess in game_state.player_states[target].hand:
                # hit
                game_state.eliminate_player(target, "guessed by guard")

        elif played_card == PRIEST:
            PLAYERS[current_player_idx].learn(target, game_state.player_states[target].hand, len(game_state.history))

        elif played_card == BARON:
            my_card = current_player_state.hand[0]
            their_card = game_state.player_states[target].hand[0]

            if my_card == their_card:
                pass
            else:
                loser = target if my_card > their_card else current_player_idx
                game_state.eliminate_player(loser, "outranked in baron-off")

        elif played_card == HANDMAID:
            current_player_state.handmaided = True

        elif played_card == PRINCE:
            discarded = game_state.player_states[target].hand[0]
            if discarded == PRINCESS:
                game_state.eliminate_player(target, "discarded princess")
            else:
                game_state.deal_card(target)

        elif played_card == KING:
            my_card = current_player_state.hand.pop()
            current_player_state.hand.append(game_state.player_states[target].hand.pop())
            game_state.player_states[target].hand.append(my_card)

        elif played_card == COUNTESS:
            pass

        elif played_card == PRINCESS:
            game_state.eliminate_player(current_player_idx, "played princess")

            


play_game()

