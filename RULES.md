> `RULES.md`: do not modify this file - this is automatically generated
by `mk_rules.py`

## Setting up blackjack

A game of blackjack will contain the following:

* Each player will have a set of hands
* Each player will have back and the amount they want to bet.

## Deck

The deck consists of 52 cards.  Just standard deck of cards.

# Game round

At each round of game:

1. Player are initially dealt with two cards.
2. Then player will be asked for how much they want to bet
3. After that, they are given 2 options: hit or miss
4. The player closest to 21 win the round, they get all the
  money that was bet.
5. The player that lost will lose their money.
6. In case of draw, all money is returned to player.

### Action: hit

When player call a hit action, a card is dealt into their hand.

### Action: Skip

When player decide to skip, the it goes to the next player's turn.

### Action: Bet

When player takes a bet, the amount that they bet are taken out
of the bank, into the betting pool

# Victory condition

When one of the player gone bankrupt, the other player win.
