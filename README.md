# PyPlaytest tutorial: Blackjack

This is a basic repository for learning [PyPlaytest](https://github.com/dat-boris/py-playtest).


Documentation draft:[Google docs](https://docs.google.com/document/d/1RsXewXl0SH-vwHwH6N4I3viaqTZObvFS_-9lfbgY9as/edit#heading=h.ik94pw9fmrrd)


# Getting started

Run the test:

```
pipenv install --dev
pytest
```

This should says:

```
$ pytest
============================================================================= test session starts =============================================================================
platform darwin -- Python 3.7.5, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
plugins: cov-2.8.1
collected 7 items

blackjack/test_action.py .xx                                                                                                                                            [ 42%]
blackjack/test_game.py .x                                                                                                                                               [ 71%]
blackjack/test_state.py .                                                                                                                                               [ 85%]
blackjack/components/test_cards.py .                                                                                                                                    [100%]

======================================================================== 4 passed, 3 xfailed in 0.20s =========================================================================
```