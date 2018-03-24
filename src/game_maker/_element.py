"""
"""
import abc
import enum


class _Element:

    __metaclass__ = abc.ABCMeta
    __nbInstances = 0

    def __new__(cls):
        cls.__nbInstances += 1
        return super(_Element, cls).__new__(cls)

    def __del__(self):
        self.__class__.__nbInstances -= 1
    
    def __init__(self, name=None, state=None, position=None, inGame=False):
        self._name = name or ("%s%i" % (self.__class__.__name__, self.__nbInstances))
        self._state = state
        self._position = position
        self._inGame = inGame
    
    @property
    def name(self):
        return self._name
    
    @property
    def state(self):
        return self._state
    
    @property
    def position(self):
        return self._position
    
    @property
    def inGame(self):
        return self._inGame


class Card(_Element):
    
    _states = enum.Enum('states', 'faceUp faceDown')
    _positions = enum.Enum('positions', 'inDeck inHands discarded')

    def __init__(self, name=None):
        super(Card, self).__init__(
            name,
            state=self._states.faceDown,
            position=self._positions.inDeck
        )

    @property
    def state(self):
        return str(self._state).split('.')[-1]
    
    @property
    def position(self):
        return str(self._position).split('.')[-1]


class Pawn(_Element):
    pass


# A tester, pas trop sur de comment ca va marcher ca
class Dice(_Element):

    def __init__(self, name=None, nbFace=6, positions=None):
        self._states = range(1, nbFace + 1)
        self._positions = positions or []

        super(Dice, self).__init__(
            name=name,
            state=self._states[0]
        )
