import pytest

from .game import Game
from .constants import Param

NUMBER_OF_PLAYERS = 2


@pytest.fixture
def game() -> Game:
    param = Param(number_of_players=NUMBER_OF_PLAYERS)
    g = Game(param=param)
    return g


def test_round(game: Game):
    """# Game round

    At each round of game:

    1. Player are initially dealt with two cards.
    2. Then player will be asked for how much they want to bet
    3. After that, they are given 2 options: hit or miss
    4. The player closest to 21 win the round, they get all the
      money that was bet.
    5. The player that lost will lose their money.
    6. In case of draw, all money is returned to player.
    """
    game_gen = game.play_round()

    next_player_id, possible_actions, _ = next(game_gen)
    assert next_player_id == 0
    assert list(map(str, possible_actions)) == [
        "hit",
        "skip",
    ], "Player 1 have 2 choice of actions."


@pytest.mark.xfail
def test_victory(game: Game):
    """# Victory condition

    When one of the player gone bankrupt, the other player win.
    """
    raise NotImplementedError()
