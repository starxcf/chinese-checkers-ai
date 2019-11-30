# -*- coding: utf-8 -*-
"""
Game board definition and position checking

@author: seanxiong
"""

import enum
from collections import namedtuple

__all__ = [
    'Board',
    'Move',
    'Player',
]

COL_NAMES = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Player(enum.Enum):
    black = 1
    white = 2

    @property
    def other(self):
        return Player.black if self == Player.white else Player.white


class Point(namedtuple('Point', 'row col')):
    def __deepcopy__(self, memodict={}):
        # These are very immutable.
        return self

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
    
    def print_out(self):
        col_or_rows = tuple(range(1, self.size + 1))
        print('  ', end = '')
        for c in col_or_rows:
            print(' ', COL_NAMES[c-1], end='')
        print('\n--', end='')
        for c in col_or_rows:
            print('---', end='')
        print('')
        for row in col_or_rows:
            pieces = []
            for col in col_or_rows:
                piece = self.get(Point(row, col))
                if piece == Player.white:
                    pieces.append('W')
                elif piece == Player.black:
                    pieces.append('B')
                else:
                    pieces.append(' ')
            print('%d|  %s' % (row, '  '.join(pieces)))

class MoveType(enum.Enum):
    MOVE = 0
    CAPTURE = 1

class Move:
    invalid_point = Point(0, 0)
    
    def __init__(self, mfrom, op, mto):
        self.movefrom = mfrom
        self.operation = op
        self.moveto = mto
        
    @staticmethod
    def init_from_code(code):
        assert(len(code) == 5)
        movefrom = Move.point_from_coords(code[0]+code[1])
        moveto = Move.point_from_coords(code[3]+code[4])
        if code[2] == '-':
            operation = MoveType.MOVE
        else:
            operation = MoveType.CAPTURE
        return Move(movefrom, operation, moveto)
    
    @staticmethod
    def point_from_coords(text):
        col_name = text[0]
        row = int(text[1])
        return Point(row, COL_NAMES.index(col_name) + 1)