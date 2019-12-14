# -*- coding: utf-8 -*-

__all__ = [
    'GameState',
]

import math, copy
from gameplay import MoveType, Point, Move
from cchecker.board import Board, Player

class GameState:
    def __init__(self, board, next_player, move):
        self.board = board
        self.next_player = next_player
        self.last_move = move

    def apply_move(self, move):
        """Return the new GameState after applying the move."""
        if not self.is_valid_move(move):
            print("Move not valid! Please re-enter.")
            return GameState(self.board, self.next_player, self.last_move)
        
        next_board = copy.deepcopy(self.board)
        next_board.place(self.next_player, move.moveto)
        next_board.remove(self.next_player, move.movefrom)
        return GameState(next_board, self.next_player.other, move)
    
    def copy(self): 
        return copy.deepcopy(self) 
    
    @classmethod
    def new_game(cls, board_size):
        board = Board(board_size)
        return GameState(board, Player.white, None)

    def is_valid_move(self, move):
        if self.board.get(move.moveto): # Target occupied
            return False
        if self.isonestepmove(move):
            return True
        if self.isjumpmove(move):
            return True
        return False
        
    def legal_moves(self):pass
        
    
    def is_over(self):pass
        
    def isonestepmove(self, move):
        ''' Not all 8 around are legal moves, only 6 are. '''
        fromx = move.movefrom.col
        fromy = move.movefrom.row
        tox = move.moveto.col
        toy = move.moveto.row
        if math.abs(fromx-tox) > 1 or math.abs(fromy-toy) > 1: # Not neibour
            return False
        if fromx == tox + 1 and fromy == toy + 1: # Not legal neibour
            return False
        if fromx == tox - 1 and fromy == toy - 1: # Not legal neibour
            return False
        return True
        
    def isjumpmove(self, move):pass
        