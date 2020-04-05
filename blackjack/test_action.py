import pytest

from .state import State
from .action import ActionHit

# importing fixture
from .test_state import state


def test_hit(state: State):
    """### Action: hit

    When player call a hit action, a card is dealt into their hand.
    """
    ps1 = state.get_player_state(0)

    assert len(ps1.hand) == 0

    action = ActionHit()
    action.resolve(state, player_id=0)

    assert len(ps1.hand) == 1


@pytest.mark.xfail
def test_bet(state: State):
    """### Action: Bet

    When player takes a bet, the amount that they bet are taken out
    of the bank, into the betting pool
    """
    raise NotImplementedError()


@pytest.mark.xfail
def test_skip(state: State):
    """### Action: Skip

    When player decide to skip, the it goes to the next player's turn.
    """
    raise NotImplementedError()
