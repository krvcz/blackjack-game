from classes.cards import Deck
import os

def test_check_all_marks():
    deck = Deck()
    for card in deck.cards:
        assert card.mark in ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3','2']

def test_check_length_deck():
    deck = Deck()
    assert len(deck.cards) == 52

def test_number_marks():
    deck = Deck()
    marks = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
    for mark in marks:
        assert deck.cards.count(f'{mark}') == 4

def test_number_figures():
    deck = Deck()
    figures = ['C', 'D', 'H', 'S']
    deck_figures = [card.figure for card in  deck.cards]
    for figure in figures:
        assert deck_figures.count(f'{figure}') == 13

def test_check_existing_card_img():
    deck = Deck()
    deck_figures_img = [f'{card.mark}{card.figure}.jpg' for card in deck.cards]
    deck_figures_img.append('back_cards-07.jpg')
    path_of_the_directory = './deck'
    for img in deck_figures_img:
        assert img in os.listdir(path_of_the_directory)