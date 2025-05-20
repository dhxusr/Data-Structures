"""
Implement a CardHand class that supports a person arranging a group of cards in his or her hand
The simulator should represent the sequence of cards using a single positional list ADT so that
cards of the same suit are kept together. Implement this strategy by means of four "fingers" into
the hand, one for each of the suits of hearts, clubs, spades, and diamonds, so that adding a new
can be done in constant time.

Methods
* add_card(r, s): Add a new card with rank r and suit s to the hand.
* play(s): Remove and return a card of suit s from the player's hand; if there is no card of suit
s, then remove and return an arbitrary card from the hand.
* __iter__():Iterate through all cards currently in the hand.
* all_of_suit(s): Iterate through all cards of suit s that are currently in the hand.
"""                          

from dataclasses import dataclass
from positional_list import Position, PositionalList

class CardHand:

    def __init__(self) -> None:

        self._cards = PositionalList()
        self._suits = ["heart", "club", "spade", "diamond"]
        #fingers
        self._hearts = None
        self._clubs = None
        self._spades = None
        self._diamonds = None


    def __len__(self) -> int:
        return len(self._cards)


    def __iter__(self):

        for card in self._cards:
            yield card

    def __str__(self) -> str:

        data = ''.join(
            str(card) for card in self
        )
        return data

    #--------------------- Utilities --------------------#
    def _add(self, card) -> None:
        """add the card into the list."""

        suit = card["suit"]
        next_suit = self._get_next_suit(suit)
        first_card = self._get_card(suit, strict=True)
        next_suit_card = self._get_card(next_suit, strict=True)
        new = None
                
        if first_card:
            self._cards.add_after(first_card, card)

        elif next_suit_card:
            new = self._cards.add_before(next_suit_card, card) 
            
        else:
            new = self._cards.add_last(card)

        if new:
            if suit == "heart":
                self._hearts = new
            elif suit == "club":
                self._clubs = new
            elif suit == "spade":
                self._spades = new
            else:
                self._diamonds = new

    def _get_next_suit(self, suit) -> str:
        """return the first previos available suit of the given suit."""

        if suit == "heart":
            next_suit = ("club" if self._clubs else
                         "spade" if self._spades else "diamond")

        elif suit == "club":
            next_suit = "spade" if self._spades else "diamond"

        elif suit == "spade":
            next_suit = "diamond"

        else:
            next_suit = "diamond"

        return next_suit

    
    def _remove(self, suit) -> dict:
        """Remove and return a card."""

        card_to_delete = self._get_card(suit)
        after = self._cards.after(card_to_delete)

        if suit == "heart":
            if after and after["suit"] == suit:
                self._hearts = after
            else:
                self._hearts = None

        elif suit == "club":
            if after and after["suit"] == suit:
                self._clubs = after
            else:
                self._clubs = None

        if suit == "spade":
            if after and after["suit"] == suit:
                self._spades = after
            else:
                self._spades = None

        else:
            if after:
                self._diamonds = after
            else:
                self._diamonds = None

        return self._cards.delete(card_to_delete)
                

    def _get_card(self, suit, strict=False) -> Position | None:    
        """Get a card of the given suit.
        return first next card if there is not card of given suit.
        with strict parameter been true, return None if there is no card in that suit."""

        card = None
        while not card:

            next_suit = None
            if suit == "heart":
                if self._hearts:
                    card = self._hearts
                elif not strict:
                    next_suit = "club"
                else:
                    return None
            elif suit == "club":
                if self._clubs:
                    card = self._clubs
                elif not strict:
                    next_suit = "spade"
                else:
                    return None

            elif suit == "spade":
                if self._spades:
                    card = self._spades
                elif not strict:
                    next_suit = "diamond"
                else:
                    return None
            else:
                if self._diamonds:
                    card = self._diamonds
                elif not strict:
                    next_suit = "heart"
                else:
                    return None

            suit = next_suit

        return card

    
    #-------------------- Public methods --------------------#
    def add_card(self, rank: int, suit: str) -> None:
        """Add a new card with rank and suit to the hand."""

        if not isinstance(suit, str):
            raise TypeError("suit of card must be of type string.")

        suit = suit.lower()
        if suit not in self._suits:
            raise ValueError(f"Invalid suit: {suit}")

        card = {
            "rank": int(rank),
            "suit": suit
        }

        self._add(card)


    def play(self, suit) -> dict | None:
        """Remove and return a card of suit s from the player's hand. 
        if not card of given suit, remove and return an arbitrary card from the hand."""

        if self._cards.is_empty():
            return None

        if suit not in self._suits:
            raise ValueError(f"Invalid suit: {suit}")

        return self._remove(suit)

    
    def all_of_suit(self, suit) -> list | None:
        """Iterate through all cards of suit that are currently in the hand."""

        if suit not in self._suits:
            raise ValueError(f"Invalid suit: {suit}")

        card = None
        if suit == "heart":
            if self._hearts is None:
                return None
            card = self._hearts

        elif suit == "club":
            if self._clubs is None:
                return None
            card = self._clubs
                
        elif suit == "spade":
            if self._spades is None:
                return None
            card = self._spades

        else:
            if self._diamonds is None:
                return None
            card = self._diamonds

        cards = []
        card_suit = card.element()["suit"]
        while card_suit == suit:
            cards.append(card.element())
            card = self._cards.after(card)

            if card:
                card_suit = card.element()["suit"]

            else:
                break

        return cards



import unittest
class TestCardHand(unittest.TestCase):

    def setUp(self):
        self.hand = CardHand()

    def test_add_card_and_len(self):
        self.assertEqual(len(self.hand), 0)
        self.hand.add_card(2, "heart")
        self.hand.add_card(10, "club")
        self.assertEqual(len(self.hand), 2)

    def test_add_card_invalid_type(self):
        with self.assertRaises(TypeError):
            self.hand.add_card(3, 123)  # Suit must be string

    def test_add_card_invalid_suit(self):
        with self.assertRaises(ValueError):
            self.hand.add_card(7, "stars")  # Invalid suit

    def test_iter(self):
        self.hand.add_card(4, "diamond")
        self.hand.add_card(9, "spade")
        result = list(self.hand)
        self.assertEqual(len(result), 2)
        self.assertTrue(all("rank" in card and "suit" in card for card in result))

    def test_play_exact_suit(self):
        self.hand.add_card(8, "club")
        card = self.hand.play("club")
        self.assertEqual(card["suit"], "club")
        self.assertEqual(len(self.hand), 0)

    def test_play_fallback(self):
        self.hand.add_card(5, "heart")
        card = self.hand.play("diamond")  # no diamond, should play any
        self.assertIsInstance(card, dict)
        self.assertEqual(len(self.hand), 0)

    def test_play_invalid_suit(self):
        self.hand.add_card(6, "spade")
        with self.assertRaises(ValueError):
            self.hand.play("banana")

    def test_play_empty_hand(self):
        self.assertIsNone(self.hand.play("club"))

    def test_all_of_suit(self):
        self.hand.add_card(1, "spade")
        self.hand.add_card(3, "spade")
        self.hand.add_card(6, "diamond")
        # redirect print to avoid clutter
        cards = self.hand.all_of_suit("spade")
        print(cards)

    def test_all_of_suit_invalid(self):
        with self.assertRaises(ValueError):
            self.hand.all_of_suit("moon")

if __name__ == "__main__":
    unittest.main()
    
