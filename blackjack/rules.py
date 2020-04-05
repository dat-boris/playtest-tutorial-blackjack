import blackjack.test_state as test_state
import blackjack.test_game as test_game
import blackjack.test_action as test_action
import blackjack.components.test_cards as test_cards

# This define the list of rules which we follow
RULE_TESTS = [
    """> `RULES.md`: do not modify this file - this is automatically generated
    by `mk_rules.py`
    """,
    test_state.test_setup,
    test_cards.test_deck,
    test_game.test_round,
    test_action.test_hit,
    test_action.test_skip,
    test_action.test_bet,
    test_game.test_victory,
]
