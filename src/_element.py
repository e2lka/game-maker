"""
"""
import abc
import enum


class _Element:

    __metaclass__ = abc.ABCMeta

    _states = None
    _positions = None
    
    def __init__(self, name=None, state=None, position=None, inGame=False):
        self._name = name or ''
        self._state = state
        self._position = position
        self._inGame = inGame


class Card(_Element):
    
    _states = enum.Enum('states', 'faceUp faceDown')
    _positions = enum.Enum('positions', 'inDeck inHands discarded')

    def __init__(self):
        super(Card, self).__init__(
            state=self._states.faceDown,
            position=self._positions.inDeck
        )


class Pawn(_Element):
    pass


# A tester, pas trop sur de comment ca va marcher ca
class Dice(_Element):

    def __new__(cls, nbFace, positions):
        cls._states = range(1, nbFace + 1)
        cls._positions = positions

    def __init__(self):
        super(Dice, self).__init__(state=1)
