"""
"""
import abc
import enum

constraints = enum.Enum('constraints', 'must musnt can')

class _Rule:

    __metaclass__ = abc.ABCMeta
    
    def __init__(self, element=None, action=None, constraint=None):
        self._element = element
        self._action = action or (lambda elem: None)
        self._constraint = constraint or constraints.can
    
    @property
    def element(self):
        return self._element

    def apply(self):
        return self._action(self._element)


class Move(_Rule):

    def __init__(self, element, action=None, constraint=None):
        super(Move, self).__init__(
            element=element,
            action=action,
            constraint=constraint
        )
    
    # Est ce que j'lui donne une action par defaut ?
