import collections
import copy
import random


class HexagonalGrid(object):
    """Data structure to store info for an hexagonal grid."""

    Hexagone = collections.namedtuple('Hexagone', ['x', 'y', 'z'])
    neighborDirection = [
        Hexagone(1, -1, 0), Hexagone(1, 0, -1), Hexagone(0, 1, -1),
        Hexagone(-1, 1, 0), Hexagone(-1, 0, 1), Hexagone(0, -1, 1)
    ]

    def __init__(self):
        self.data = {}
        self.radius = 0
        self.redShip = None
        self.greenShip = None

    def __setitem__(self, key, value):
        self.data[self.hexaKey(key)] = value

    def __getitem__(self, key):
        return self.data[self.hexaKey(key)]

    def hexaKey(self, key):
        try:
            hexaKey = self.__validateKey(key)
        except KeyError as err:
            raise KeyError('The given key is not valid: %s', err)

        return hexaKey

    def generate(self, radius, defaultValue='empty'):
        self.radius = radius

        ran = range(-radius, radius + 1)
        for x in ran:
            for y in ran:
                for z in ran:
                    if x + y + z == 0:
                        self.data[self.hexaKey((x, y, z))] = (defaultValue, random.randint(1, 3))

    def populate(self, green=4, red=4):
        keys = self.data.keys()

        irand = random.randint(0, green - 1)
        for i in range(green):
            key = random.choice(keys)
            keys.remove(key)
            if i == irand:
                self.data[key] = ('green', self.data[key][1], True)
                self.greenShip = key
            else:
                self.data[key] = ('green', self.data[key][1], False)

        irand = random.randint(0, red - 1)
        for i in range(red):
            key = random.choice(keys)
            keys.remove(key)
            if i == irand:
                self.data[key] = ('red', self.data[key][1], True)
                self.redShip = key
            else:
                self.data[key] = ('red', self.data[key][1], False)

    def listPossibleMove(self, color):
        result = []
        start = self.greenShip if color == 'green' else self.redShip

        for direction in self.neighborDirection:
            for r in range(1, self.radius * 2 + 1):
                newPos = self.Hexagone(r * direction.x + start.x,
                                       r * direction.y + start.y,
                                       r * direction.z + start.z)
                if newPos not in self.data:
                    break

                if self.data[newPos][0] == 'empty':
                    result.append(newPos)
                elif self.data[newPos][0] == color:
                    continue
                else:
                    break
        return result

    def isValidMove(self, newPos):
        if self.data[newPos] == 'empty':
            return True
        else:
            return False

    def scoreMove(self, end, color):
        score = self.data[end][1]  # tile score

        tempGrid = copy.deepcopy(self)
        tempGrid[end] = (color, self.data[end][0])

        opponentColor = 'red' if color == 'green' else 'green'
        result1 = self.listPossibleMove(opponentColor)
        opponentPossibleScore1 = sum(self.data[r][1] for r in result1)

        result2 = tempGrid.listPossibleMove(opponentColor)
        opponentPossibleScore2 = sum(tempGrid[r][1] for r in result2)

        score += opponentPossibleScore1 - opponentPossibleScore2

    def getNeighbour(self, key):
        hexaKey = self.hexaKey(key)

    def __validateKey(self, key):
        """Validate a given key and return the Hexagone version of it if valid.
        """
        if not isinstance(key, str) and not isinstance(key, tuple):
            raise KeyError('Key must be a string or a tuple')

        if isinstance(key, str):
            key = key.replace(' ', '')
            x, y, z = (int(k) for k in key.split(','))
        else:
            x, y, z = key

        if (x + y + z) != 0:
            raise KeyError('The sum of coordinates should be 0, not %s' % (x + y + z))

        return self.Hexagone(x, y, z)

hexaGrid = HexagonalGrid()
# hexaGrid.generate(2)
# hexaGrid.populate()
hexaGrid.data = {HexagonalGrid.Hexagone(x=-2, y=0, z=2): ('green', 1, False),
 HexagonalGrid.Hexagone(x=-2, y=1, z=1): ('empty', 1),
 HexagonalGrid.Hexagone(x=-2, y=2, z=0): ('empty', 2),
 HexagonalGrid.Hexagone(x=-1, y=-1, z=2): ('empty', 1),
 HexagonalGrid.Hexagone(x=-1, y=0, z=1): ('red', 1, True),
 HexagonalGrid.Hexagone(x=-1, y=1, z=0): ('red', 1, False),
 HexagonalGrid.Hexagone(x=-1, y=2, z=-1): ('red', 3, False),
 HexagonalGrid.Hexagone(x=0, y=-2, z=2): ('red', 3, False),
 HexagonalGrid.Hexagone(x=0, y=-1, z=1): ('empty', 1),
 HexagonalGrid.Hexagone(x=0, y=0, z=0): ('green', 1, False),
 HexagonalGrid.Hexagone(x=0, y=1, z=-1): ('empty', 2),
 HexagonalGrid.Hexagone(x=0, y=2, z=-2): ('empty', 2),
 HexagonalGrid.Hexagone(x=1, y=-2, z=1): ('empty', 2),
 HexagonalGrid.Hexagone(x=1, y=-1, z=0): ('empty', 3),
 HexagonalGrid.Hexagone(x=1, y=0, z=-1): ('empty', 1),
 HexagonalGrid.Hexagone(x=1, y=1, z=-2): ('green', 3, False),
 HexagonalGrid.Hexagone(x=2, y=-2, z=0): ('green', 1, True),
 HexagonalGrid.Hexagone(x=2, y=-1, z=-1): ('empty', 1),
 HexagonalGrid.Hexagone(x=2, y=0, z=-2): ('empty', 1)}
hexaGrid.redShip = HexagonalGrid.Hexagone(x=-1, y=0, z=1)
hexaGrid.greenShip = HexagonalGrid.Hexagone(x=2, y=-2, z=0)
hexaGrid.radius = 2

result = hexaGrid.listPossibleMove('red')
scores = []
for move in result:
    scores.append(hexaGrid.scoreMove(move, 'red'))

maxScore = max(scores)
bestMove = result[scores.index(maxScore)]
print "Score/Move: ", maxScore, bestMove

# result = hexaGrid.listPossibleMove((0,0,0), 'red')
# print result

import pprint
pprint.pprint(hexaGrid.data)
