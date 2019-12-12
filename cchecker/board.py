# -*- coding: utf-8 -*-

"""
Game board definition and position checking

@author: seanxiong
"""

import enum, math
from gameplay import Point

__all__ = [
    'Board',
    'Player',
]

class Player(enum.Enum):
    black = 2
    white = 3

    @property
    def other(self):
        return Player.black if self == Player.white else Player.white
    
class Board:
    def __init__(self, size):
        assert(size > 4 and size < 22) # Max 5 line of pawns
        assert(size%2 == 1) # cannot be even number
        self.size = size
        self._grid = {}
        ''' Grid is rotated 45 degree to square, for simplicity.
            Padding at top left to avoid 0 index. e.g.(size=5):
            _ _ _ _ _ _
            _ _ _ _ _ 1
            _ _ _ _ _ _
            _ _ _ _ _ _
            _ _ _ _ _ _
            _ 2 _ _ _ _
        '''
        lines = math.floor(size / 2)
        for c in range(lines):
            for r in range(lines):
                if c < r or c== r:
                    self._grid[Point(r+size+1-lines, c+1)] = Player(Player.black)
                if c > r or c== r:
                    self._grid[Point(r+1, c+size+1-lines)] = Player(Player.white)
            
    def place(self, player, point):
        assert self.is_on_grid(point)
        self._grid[point] = player
        
    def remove(self, player, point):
        assert self.is_on_grid(point)
        self._grid[point] = None

    def is_on_grid(self, point):
        return 1 <= point.row <= self.size and \
            1 <= point.col <= self.size

    def get(self, point):
        """Return the content of a point on the board.

        Returns None if the point is empty, or a Player if there is a
        stone on that point.
        """
        return self._grid.get(point)