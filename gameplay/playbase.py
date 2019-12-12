# -*- coding: utf-8 -*-
"""
Player abstraction base class

@author: Sean
"""

__all__ = [    
    'Point',
    'MoveType',
    'Move',
    'play',
]

import sys,enum
from collections import namedtuple
from gameplay.playerbase import GamePlayer

COL_NAMES = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Point(namedtuple('Point', 'row col')):pass
#    def __deepcopy__(self, memodict={}):
        # These are very immutable.
#        return self
    
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

def play(player1:GamePlayer, player2:GamePlayer, gamestate, interface,
         boardsize=4, intercative=False):
    assert(player1 != player2)
    human_players = []
    ai_players = []
    if player1.isHuman():
        human_players.append(player1.playerside)
    else:
        ai_players.append(player1.playerside)
        
    if player2.isHuman():
        human_players.append(player2.playerside)
    else:
        ai_players.append(player2.playerside)
        
    game = gamestate.new_game(boardsize)
    while not game.is_over():
        if (game.next_player in human_players):
            interface.printboard(game.board, COL_NAMES)
            user_input = input(game.next_player.name + ' move - ')
            human_move = interface.checkcode(user_input)
            if not human_move:
                continue
            if human_move[0] == interface.exitcode():
                print("Byebye!")
                sys.exit()
            move = Move.init_from_code(human_move[0])
        else:
            if intercative:
                interface.printboard(game.board.copy(), COL_NAMES)
                print('Calculating...', end=" ")
            bot = player1.ai if player1 == game.next_player else player2.ai
            move = bot.select_move(game)
            if intercative: print('done.')
        game = game.apply_move(move)
        
    if intercative:
        interface.printboard(game.board.copy(), COL_NAMES)
    return game