from classes.persons import Player, Croupier
from classes.cards import Card, Deck
import pytest

dataset = [(['A', 'A'], 21), (['A', 'A', 'king'], 21), (['A', 'king'], 21), (['3', '2'], 5)]


@pytest.mark.parametrize("marks, score", dataset)
def test_score(marks, score):
    player = Player()
    player.cards = [Card('S', mark) for mark in marks]
    assert player.score == score



dataset = [(['A', '10'], 3), (['A', 'A'], 2), (['A', 'king'], 2), (['3', '2'], 3)]

@pytest.mark.parametrize("marks, length", dataset)
def test_decision(marks, length):
    croupier = Croupier()
    deck = Deck()
    croupier.cards = [Card('S', mark) for mark in marks]
    croupier.decision(deck)
    assert len(croupier.cards) == length
