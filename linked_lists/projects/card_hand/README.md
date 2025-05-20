# Card Hand class
Implement a CardHand class that supports a person arranging a group of cards in his or her hand
The simulator should represent the sequence of cards using a single positional list ADT so that
cards of the same suit are kept together. Implement this strategy by means of four "fingers" into
the hand, one for each of the suits of hearts, clubs, spades, and diamonds, so that adding a new
can be done in constant time.

## Methods
* add_card(r, s): Add a new card with rank r and suit s to the hand.
* play(s): Remove and return a card of suit s from the player's hand; if there is no card of suit
s, then remove and return an arbitrary card from the hand.
* __iter__():Iterate through all cards currently in the hand.
* all_of_suit(s): Iterate through all cards of suit s that are currently in the hand.
                          
