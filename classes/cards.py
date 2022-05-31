"""
       A module consist of two classes.
       The first one create card object and the second one deck of cards
"""



SCORE_CARD = {'2': 2, '3': 3, '4': 4,
              '5': 5, '6': 6, '7': 7,
              '8': 8, '9': 9, '10': 10,
              'K': 10, 'Q': 10, 'J': 10,
              'A': 1}


class Card:
    """
       A class to represent a card.

       Attributes
       ----------
       figure : str
           figure of the card
       mark : str
           mark of the card
    """

    def __init__(self, figure, mark):
        """
        The __init__ function is called automatically when a
        new instance of the class is created.
        The first argument to __init__ must always be 'self'
        (though it isn't explicitly passed, Python adds it for you)
        any other arguments required can be listed after self.
        In this case, we require one additional argument: the figure
        that will contain our mark.

        Args:
            self: Refer to the object itself
            figure: Store the figure object
            mark: Determine the color of the figure

        Returns:
            The object that was created

        """
        self.figure = figure
        self.mark = mark

    def __repr__(self):
        """
        The __repr__ function is the default representation of a class instance.
        It is called by the repr() function and by string conversions (reverse quotes)
        The __repr__ method defined here will be tailored to suit our needs.

        Args:
            self: Refer to the instance of the class

        Returns:
            A string that can be used to recreate the object

        """
        return f"{self.mark}{self.figure}"

    def __eq__(self, other):
        """
        The __eq__ function is called when two
        objects are compared with the == operator.
        It should return True if the objects are
        equal and False otherwise.
        This function is automatically defined
        for all new-style classes (those derived from object)


        Args:
            self: Refer to the instance of the class
            other: Compare the two objects

        Returns:
            A boolean

        """
        return self.mark == other

    def __str__(self):
        """
        The __str__ function is called when the object is printed.
        It returns a string representation of the object,
        which can be used for debugging and logging


        Args:
            self: Refer to the object itself

        Returns:
            A string that represents the object

        """
        return f"{self.mark}{self.figure}"


class Deck:
    """
          A class to represent a Deck.

          Attributes
          ----------
          cards : list
              list of card's classes
       """
    def __init__(self):
        """
        The __init__ function is called automatically every time the class is
        instantiated.  It sets up all of the attributes that will be used by the
        class's methods.

        Args:
            self: Refer to the object that is being created

        Returns:
            The object that is created
        """
        self.cards = Deck.generate_cards()

    @staticmethod
    def generate_cards():
        """
        The generate_cards function generates a list of card's class
        representing all 52 cards in the deck
        The first element of each card's class is the mark and
         the second element is the figure.

        Args:

        Returns:
            A list of tuples with the cards
        """
        marks = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
        figures = ['C', 'D', 'H', 'S']
        return [Card(figure, mark) for mark in marks for figure in figures]
