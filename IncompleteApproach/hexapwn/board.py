# -*- coding: utf-8 -*-
"""
Game board definition and position checking

@author: seanxiong
"""

import enum
from gameplay import Point

__all__ = [
    'Board',
    'Player',
]

class Player(enum.Enum):
    black = 1
    white = 2

    @property
    def other(self):
        return Player.black if self == Player.white else Player.white

class Board:
    def __init__(self, size):
        assert(size > 2 and size < 27)
        self.size = size
        self._grid = {}
        for c in tuple(range(1, size + 1)):
            self._grid[Point(1, c)] = Player(Player.black)
            self._grid[Point(size, c)] = Player(Player.white)

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
    
