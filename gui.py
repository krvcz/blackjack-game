"""
       An application window builder

"""

from tkinter import Tk, Label, Button
from PIL import Image, ImageTk
from classes.game import Game




class App:
    """
         A class to represent app's window.
      """

    def __init__(self):
        """
        The __init__ function is called automatically every time the class
         is being used to create a new object.
        The self parameter refers to the newly created object; think of it as a copy of the class.


        Args:
            self: Access variables that belongs to a class

        Returns:
            None

        Doc Author:
            Trelent
        """
        self.window = Tk()
        self.window.title('BlackJack')
        self.window.geometry("600x400")
        self.img = None
        self.lbl = None
        self.label = None
        self.start_game = None
        self.quit = None
        self.player_score_label = None
        self.player_cards_label = None
        self.pass_button = None
        self.draw_button = None
        self.blackjack_button = None
        self.decision = None
        self.croupier_score_label = None
        self.croupier_cards_label = None
        self.img = None
        self.lbl = None
        self.images_players = None
        self.images_croupier = None

        self.play_again_button = None
        # self.card_position_x = 200
        # self.card_position_y = 220
        self.game = Game()
        self.game.start_game()
        self.refresh_background()
        self.init_menu_ui()
        self.window.mainloop()


    def init_menu_ui(self):
        """
        The init_menu_ui function creates the menu interface for the game.
        It creates two buttons, one to start a new game and another to quit.
        The function also places these buttons on screen.

        Args:
            self: Access variables that belongs to the class

        Returns:
            A tuple of the buttons that are created

        """
        self.start_game = Button(self.window, text="START GAME", width=20,
                                 command = self.init_game_ui)
        self.quit = Button(self.window, text="QUIT", width=20,
                           command = self.window.destroy)
        self.start_game.place(x=250, y=150, height=50,width=140)
        self.quit.place(x=250, y=210, height=50,width=140)
        # self.start_game.pack(ipady = 10)
        # self.quit.pack(ipady = 10)

    def init_game_ui(self):
        """
        The init_game_ui function is used to initialize the game UI.
        It is called when the user clicks on Play button in the main menu.
        The function destroys all widgets from previous game and creates new ones:
        labels, buttons, etc.

        Args:
            self: Access variables that belongs to the class

        Returns:
            The following:
        """
        self.start_game.destroy()
        self.quit.destroy()
        self.player_score_label = Label(self.window, text=f"YOUR SCORE: {self.game.player.score}",
                                        font=200, fg="black")
        #
        self.pass_button = Button(self.window, text="STAND", width=20,
                                  command=self.get_summary_labels)
        self.draw_button = Button(self.window, text="HIT", width=20,
                                  command=self.draw_card_action)
        self.blackjack_button = Button(self.window, text="BLACKJACK!", width=20,
                                       command=self.get_summary_labels)
        self.player_score_label.pack()
        self.player_score_label.place(relx=0.5, rely=0.5, anchor='center')
        # self.player_cards_label.pack()
        # self.player_cards_label.place(relx=0.5, rely=0.7, anchor='center')
        self.pass_button.pack()
        self.pass_button.place(relx=0.15, rely=0.9, anchor='center')
        self.draw_button.pack()
        self.draw_button.place(relx=0.85, rely=0.9, anchor='center')
        self.show_cards_player(130, 220)
        self.show_cards_croupier(130, 30, 1)

    @staticmethod
    def resize_cards(card):
        """
        The resize_cards function takes a card image and resizes it to fit the gameboard.
            Args:
                card (str): The path to the image of a playing card.

            Returns:
                Image: A resized version of the inputted image that fits on our gameboard.

        Args:

            card: Pass the card image to the resize_cards function

        Returns:
            A resized image of the card that is passed to it

        Doc Author:
            Trelent
        """

        our_card_img = Image.open(card)
        our_card_resize_image = our_card_img.resize((75, 100), Image.ANTIALIAS)
        our_card_image = ImageTk.PhotoImage(our_card_resize_image)
        return our_card_image

    def show_cards_player(self, x_variable, y_variable):
        """
        The show_cards_player function displays the cards of the player.
        It takes two arguments: x and y, which are coordinates for where to display them.
        The function displays each card in a list of cards called self.images_players,
        which is created by appending images from the deck folder to a list.

        Args:
            self: Access variables that belongs to the class
            x: Move the cards horizontally
            y: Move the cards down as more cards are added to the player's hand

        Returns:
            The list of the cards in the player's hand

        Doc Author:
            Trelent
        """
        print(self.game.player.cards)
        self.images_players = [self.resize_cards(f'deck/{card}.jpg')
                               for card in self.game.player.cards]
        for i, card in enumerate(self.images_players):
            # self.dealer_image = self.resize_cards(f'deck/{card}.jpg')

            move = i * 80
            Label(self.window, image=card).place(y=y_variable, x=x_variable + move, anchor = 'nw')



    def show_cards_croupier(self, x_variable, y_variable, hide = 0):
        """
        The show_cards_croupier function displays the cards of the croupier.
        It takes as input x and y coordinates, which are used to position
        the images on screen.
        The function also takes an optional parameter hide, which is set to 0 by default.
        If it is 1,
        the back side of all cards will be displayed instead

        Args:
            self: Represent the instance of the object itself
            x: Set the x-coordinate of each card
            y: Move the cards down
            hide=0: Show the cards of the croupier

        Returns:
            A list of the cards in the croupier's hand

        Doc Author:
            Trelent
        """
        print(self.game.croupier.cards)
        if hide == 1:
            self.images_croupier = [self.resize_cards('deck/back_cards-07.jpg') if i > 0
                                    else self.resize_cards(f'deck/{card}.jpg')
                                    for i, card in enumerate(self.game.croupier.cards)]
        elif hide == 0:
            self.images_croupier = [self.resize_cards(f'deck/{card}.jpg')
                                    for card in self.game.croupier.cards]

        for i, card in enumerate(self.images_croupier):
            # self.dealer_image = self.resize_cards(f'deck/{card}.jpg')

            move = i * 80
            Label(self.window, image=card).place(y=y_variable, x=x_variable + move, anchor = 'nw')



    def get_summary_labels(self):
        """
        The get_summary_labels function is used to display the summary of the game.
        It displays the decision, croupier score and cards.

        Args:
            self: Access variables that belongs to the class

        Returns:
            The labels that are shown after the game is over

        Doc Author:
            Trelent
        """
        self.pass_button.destroy()
        self.draw_button.destroy()
        self.blackjack_button.destroy()
        self.decision = Label(self.window, text=self.game.get_summary(),
                              font=200, fg="black")
        self.croupier_score_label = Label(self.window, text=f"CROUPIER_SCORE:"
                                                            f" {self.game.croupier.score}",
                                          font=200, fg="black")
        self.croupier_cards_label = Label(self.window, text=f"CROUPIER_CARDS:"
                                                            f" {self.game.croupier.cards}",
                                          font=200, fg="black")
        self.play_again_button = Button(self.window, text="PLAY AGAIN", width=20,
                                        command=self.play_again)
        self.decision.pack()
        self.croupier_score_label.place(y=140, x=210)
        # self.croupier_cards_label.pack()
        self.show_cards_croupier(130, 30)
        self.play_again_button.place(y=350, x=230)

    def play_again(self):
        """
        The play_again function is called when the player decides to play again after
        having won or lost a round. It destroys all of the labels and buttons from the
        previous game, then creates new ones for a new game.

        Args:
            self: Access variables that belongs to the class

        Returns:
            The game object

        Doc Author:
            Trelent
        """
        self.player_score_label.destroy()
        # self.player_cards_label.destroy()
        self.decision.destroy()
        self.croupier_score_label.destroy()
        self.croupier_cards_label.destroy()
        self.play_again_button.destroy()
        self.game = Game()
        self.refresh_background()
        self.game.start_game()
        self.init_game_ui()


    def draw_card_action(self):
        """
        The draw_card_action function draws a card for the player and updates the score label.
        It also shows the cards of both players.

        Args:
            self: Access variables that belongs to the class

        Returns:
            The player's score and the cards that he has

        Doc Author:
            Trelent
        """
        self.game.player.draw_card(self.game.deck)
        self.show_cards_player(130, 220)
        self.player_score_label.config(text=f"PLAYER_SCORE: {self.game.player.score}")
        # self.player_cards_label.config(text = f"PLAYER_CARDS: {self.game.player.cards}")
        self.game.croupier.decision(self.game.deck)
        self.show_cards_croupier(130, 30, 1)
        self.scan_score()

    def scan_score(self):
        """
        The scan_score function is used to check the score of the player and
        dealer. It will return a string that says whether or not the player won,
        lost, or tied.

        Args:
            self: Access the other methods in the class

        Returns:
            The value of the check_points function

        Doc Author:
            Trelent
        """
        if self.game.check_points() == 'BlackJack':
            self.blackjack_button.pack()
        elif self.game.check_points() == 'OutRange':
            self.get_summary_labels()

    def refresh_background(self):
        """
        The refresh_background function is used to refresh the background image.
        It takes no parameters and returns nothing.

        Args:
            self: Access the attributes and methods of the class in python

        Returns:
            The label object, self

        Doc Author:
            Trelent
        """
        self.img = ImageTk.PhotoImage(Image.open('img/desk.jpg').resize((600, 400),
                                                                        Image.ANTIALIAS))
        self.lbl = Label(self.window, image=self.img)
        self.lbl.img = self.img
        self.lbl.place(relx=0.5, rely=0.5, anchor='center')
