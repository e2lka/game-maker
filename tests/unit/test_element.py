"""
"""
from game_maker import _element
from game_maker import Card, Dice

def test_element_name():
    elem = _element._Element()
    assert elem.name == '_Element1'
    del elem

def test_card_initValues():
    card = Card()
    try:
        assert card.name == 'Card1'
        assert card.state == 'faceDown'
        assert card.position == 'inDeck'
        assert not card.inGame
    finally:
        del card

def test_dice_initValues():
    dice = Dice()
    try:
        assert dice.name == 'Dice1'
        assert dice.state == 1
        assert dice.positon is None
        assert not dice.inGame
    finally:
        del dice