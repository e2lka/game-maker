import collections



class HexagonalGrid(object):
    """Data structure to store info for an hexagonal grid."""

    Hexagone = collections.namedtuple('Hexagone', ['x', 'y', 'z'])

    def __init__(self):
        self.data = {}

    def __setitem__(self, key, value):
        try:
            hexaKey = self.__validateKey(key)
        except KeyError as err:
            raise KeyError('The given key is not valid: %s', err)

        self.data[hexaKey] = value

    def __getitem__(self, key):
        try:
            hexaKey = self.__validateKey(key)
        except KeyError as err:
            raise KeyError('The given key is not valid: %s', err)

        return self.data[hexaKey]

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

        print x, y, z, x + y + z

        if (x + y + z) != 0:
            raise KeyError('The sum of coordinates should be 0, not %s' % (x + y + z))

        return self.Hexagone(x, y, z)

hexaGrid = HexagonalGrid()

hexaGrid['0, 1, -1'] = 'nothing'
hexaGrid[(1,2,-3)] = 'something'
print hexaGrid['0,1,-1']
print hexaGrid[(1,2,-3)]
