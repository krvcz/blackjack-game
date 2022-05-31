"""
       A module consist of one class representing
       mechanism of blackjack game.

"""


from classes.cards import Deck
from classes.persons import Player, Croupier




class Game:
    """
           A class to represent a game.

           Attributes
           ----------
           player : Player class
           croupier : Croupier class
           deck : Deck class
        """

    def __init__(self):
        """
        The __init__ function is called automatically
         every time the class is being used to create a new object.
        The self parameter is a reference to the current instance of the class,
        and is used to access variables
        that belongs to the class.
        It does not have be named self , you can call it whatever you like,
        but it has to be the first parameter of any function in the class:

        Args:
            self: Refer to the object itself

        Returns:
            The object of the class
        """
        self.player = Player()
        self.croupier = Croupier()
        self.deck = Deck()


    def start_game(self):
        """
        The start_game function shuffles the deck, deals
        two cards to the player and
        two cards to the croupier. The function returns nothing.

        Args:
            self: Access variables that belongs to the class

        Returns:
            The player score
        """
        self.croupier.shuffle_cards(self.deck)
        self.player.draw_card(self.deck)
        self.player.draw_card(self.deck)
        self.croupier.draw_card(self.deck)
        self.croupier.draw_card(self.deck)
        # print(self.player_score)
        # print(self.player.cards)
        # self.make_decision()


    def check_points(self):
        """
        The check_points function checks the player's score to see if
        it is equal to 21.
        If so, it returns 'BlackJack'.
        If  the player's score is more than 21 or the croupier's score is
         more or equal to 21,
        it return 'OutRange'
        If otherwise, it returns None.

        Args:
            self: Access variables that belongs to the class

        Returns:
            The string 'blackjack' if the player's score is 21 or
            The string 'OutRange'  if the croupier's score
            is more or equal to 21

        """
        if self.player.score == 21:
            return 'BlackJack'

        if self.player.score > 21 or self.croupier.score >= 21:
            return 'OutRange'

        return None



    def get_summary(self):
        """
        The get_summary function returns a string that summarizes the game.

        The summary is of the form:

            'Wygrałeś!' if player won,
            'Przegrałeś!' if player lost or
            'Remis' if it's a tie.

        Args:
            self: Give the object calling the method access to the attributes
            and methods of the object

        Returns:
            A string, which is a message that indicates the result of the game
        """

        if self.player.score > 21:
            return 'Przegrałeś!'

        if self.player.score > self.croupier.score or self.croupier.score > 21:
            return 'Wygrałeś!'

        if self.player.score < self.croupier.score:
            return 'Przegrałeś!'

        if self.player.score == self.croupier.score:
            return 'Remis!'

        return None
