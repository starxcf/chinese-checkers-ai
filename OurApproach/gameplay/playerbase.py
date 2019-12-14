# -*- coding: utf-8 -*-
"""
Player abstraction base class

@author: Sean
"""

__all__ = [
    'PlayerType',
    'GamePlayer',
]

import enum

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
        