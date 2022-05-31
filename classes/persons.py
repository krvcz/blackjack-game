"""
       A module consist of two classes.
       The first one create player object and the second one croupier object

"""

import random
from classes.cards import SCORE_CARD



class Player:
    """
               A class to represent a player.

               Attributes
               ----------
               cards : list
            """

    def __init__(self, cards = None):
        """
        The __init__ function is the constructor for a class. It is called whenever an
        object of that class is instantiated. The __init__ function can take arguments, but
        the first argument must always be 'self'. This refers to the object itself (e.g.,
        my_object). The self parameter allows you to access variables and methods in the
        class from outside of the class.

        Args:
            self: Reference the object itself
            cards=None: Create a deck of cards

        Returns:
            Nothing
        """
        if cards is None:
            self.cards = []


    def draw_card(self, deck):
        """
        The draw_card function takes a deck as an argument and returns the card
        at the top of that deck.
        It also removes that card from the deck.

        Args:
            self: Access variables that belongs to the class
            deck: Specify the deck that is being drawn from

        Returns:
            The card that was drawn from the deck
        """
        self.cards.append(deck.cards.pop(1))

    @property
    def score(self):
        """
        The score function takes a list of cards and returns the score.
        If there are two Aces, then the function will return 21.
        If there is one Ace and any other card that is a King, Queen or Jack,
        then it will return 21.
        Otherwise it returns the sum of all scores.

        Args:
            self: Access variables that belongs to the class

        Returns:
            The sum of the cards in the hand

        Doc Author:
            Trelent
        """

        if self.cards.count('A') == 2 and \
                sum([SCORE_CARD[card.mark] for card in self.cards]) <= 21:
            return 21

        if 'A' in self.cards and any((card in ['K', 'Q', 'J'] for card in self.cards)) \
                                    and \
                sum([SCORE_CARD[card.mark] for card in self.cards]) <= 21:
            return 21


        return sum([SCORE_CARD[card.mark] for card in self.cards])



class Croupier(Player):
    """
                  A class to represent a croupier.

                  Attributes
                  ----------
                  cards : list
               """
    def __init__(self, cards=None):
        """
        The __init__ function is called automatically every time the class is instantiated.
        The parameters of the __init__ function are those that we wish to provide as arguments
        when instantiating our class. In this case, cards is a parameter that takes an
        optional argument;
        if no argument is provided when the class CardDeck is instantiated,
        then cards will be equal to 52.
        However, if a list of integers between 0 and 51 (inclusive) are provided
        as arguments when CardDeck
        is instantiated, then these integers will be stored in self._cards.

        Args:
            self: Refer to the instance of the object itself
            cards=None: Initialize the cards list

        Returns:
            A reference to the newly created object
        """
        super().__init__(cards)

    @staticmethod
    def shuffle_cards(deck):
        """
        The shuffle_cards function accepts a deck of cards (a list of 2-element lists)
        and then shuffles the deck
        using the shuffle function from Python's random module. The result returned
        is a single list containing all 52
        cards, which represents a full, shuffled deck.

        Args:
            self: Access the attributes and methods of the class in python
            deck: Pass the deck to be shuffled

        Returns:
            A list of shuffled cards

        """
        random.shuffle(deck.cards)

    def decision(self, deck):
        """
        The decision function is the heart of the Blackjack game. It is called
        whenever a player's hand is worth less than 17, and it allows the player to
        either hit or stand. The function takes in a deck as an argument, which it uses
        to draw cards for both itself and its opponent (the dealer).

        Args:
            self: Access variables that belongs to the class
            deck: Draw a card

        Returns:
            The value of the decision function for a given state
        """
        if self.score <= 16:
            self.cards.append(deck.cards.pop(1))
