from typing import Dict, Type


from playtest import Param, SubState, FullState, Visibility
from playtest.components import Component
from playtest.components import Token


from .components.cards import Deck


class PlayerState(SubState):
    visibility = {
        "hand": Visibility.ALL,
    }

    hand: Deck
    # bank: Token

    def __init__(self, param=None):
        self.hand = Deck([])
        # self.bank = Token(10)


class State(FullState[PlayerState]):
    player_state_class = PlayerState

    visibility = {
        # Deck is face down and nobody can see it
        "deck": Visibility.NONE,
    }

    deck: Deck
    # betting_pool: Token

    def __init__(self, param=None):
        self.deck = Deck(all_cards=True)
        # self.betting_pool = Token(0)
        super().__init__(param=param)
