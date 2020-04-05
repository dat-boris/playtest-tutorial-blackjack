import pytest

from playtest import Visibility
from playtest.components import Counter

from .constants import Param
from .state import State, PlayerState
from .components.cards import Deck

NUMBER_OF_PLAYERS = 2


@pytest.fixture
def state() -> State:
    param = Param(number_of_players=NUMBER_OF_PLAYERS)
    return State(param=param)


def test_setup(state: State):
    """## Setting up blackjack

    A game of blackjack will contain the following:

    * Each player will have a set of hands
    * Each player will have back and the amount they want to bet.
    """
    assert isinstance(state.deck, Deck)
    assert len(state.deck) == 52

    for player_state in state.players:
        assert isinstance(player_state, PlayerState)
        assert isinstance(player_state.hand, Deck)
        assert len(player_state.hand) == 0
