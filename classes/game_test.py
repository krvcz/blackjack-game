from classes.game import Game
from classes.cards import Card
import pytest



dataset = [(['A', 'K'], 'BlackJack'), (['2', '3'], None), (['K', 'K','K'], 'OutRange'), (['A', '6', 'K'], 'BlackJack')]

@pytest.mark.parametrize("marks, response", dataset)
def test_decision(marks, response):
    game = Game()
    # game.croupier.cards = [Card('S', mark) for mark in marks]
    game.player.cards = [Card('S', mark) for mark in marks]
    assert game.check_points() == response