# -*- coding: utf-8 -*-
"""
Player abstraction base class

@author: Sean
"""

__all__ = [
    'PlayerType',
    'GamePlayer',
    'Point',
    'MoveType',
    'Move',
]

import enum
from collections import namedtuple

class PlayerType(enum.Enum):
    human = 0
    computer = 1

class GamePlayer:
    def __init__(self, player, ptype, agent):        
        self.playerside = player
        self.playertype = ptype
        self.ai = agent
        
    def isHuman(self):
        if self.playertype == PlayerType.human:
            return True
        else:
            return False
        
    def isComputer(self):
        return not self.isHuman()
    
    def __eq__(self, src):
        if type(src) == int:
            return src == self.playerside
        elif type(src) == GamePlayer:
            return src.playerside == self.playerside
        else:
            return False
        
class Point(namedtuple('Point', 'row col')):
    def __deepcopy__(self, memodict={}):
        # These are very immutable.
        return self
    
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