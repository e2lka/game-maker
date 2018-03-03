""" A Strategy is like a decorator of a Rule.
"""
import abc

class _Strategy:

    __metaclass__ = abc.ABCMeta

    def __init__(self, rule=None):
        self._rule = rule

    @property
    def element(self):
        return self._rule.element

    @abc.abstractmethod
    def _setup(self):
        return None
    
    @abc.abstractmethod
    def _tearDown(self):
        return None
    
    def apply(self):
        self._setup()
        self._rule.apply()
        self._tearDown()

