# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 23:35:10 2019

@author: xcf
"""

import copy

__all__ = [
    'GameState',
]

from gameplay import MoveType, Point, Move
from hexapwn.board import Board, Player

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
        # Case of Not correct player's pawn
        if self.next_player != self.board.get(move.movefrom):
            return False
        # When moving
        if move.operation == MoveType.MOVE:
            # Case of target position occupied
            if self.board.get(move.moveto):
                return False
            # Case of not moving straight
            if move.movefrom[1] != move.moveto[1]:
                return False
            # Case of white going backward
            if self.board.get(move.movefrom) == Player.white and \
               move.movefrom[0] != move.moveto[0] + 1:
                return False
            # Case of black going backward
            if self.board.get(move.movefrom) == Player.black and \
               move.movefrom[0] != move.moveto[0] - 1:
                return False
        else:
            # Case of target illegal
            if self.board.get(move.moveto) != self.next_player.other:
                return False
            # Case of not moving diagnole
            if (move.movefrom[0] != move.moveto[0] + 1) and \
               (move.movefrom[0] != move.moveto[0] - 1):
                return False
        return True

    def legal_moves(self):
        moves = []
        # 1. Find legal pawns
        pawns = []
        for row in tuple(range(1, self.board.size + 1)):
            for col in tuple(range(1, self.board.size + 1)):
                pawn = Point(row, col)
                if self.board.get(pawn) == self.next_player:
                    pawns.append(pawn)
        
        for p in pawns:
            isBlack = (self.next_player == Player.black)
        # 2. See if it can move forward
            tar_point = Point(p[0] + 1, p[1]) if isBlack else Point(p[0] - 1, p[1])
            if not self.board.get(tar_point):
                moves.append(Move(p, MoveType.MOVE, tar_point))
        # 3. See if it can capture any thing
            tar_left = Point(tar_point[0], p[1] - 1)
            if self.board.is_on_grid(tar_left) and \
               self.board.get(tar_left) == self.next_player.other:
                moves.append(Move(p, MoveType.CAPTURE, tar_left))
            tar_right = Point(tar_point[0], p[1] + 1)
            if self.board.is_on_grid(tar_right) and \
               self.board.get(tar_right) == self.next_player.other:
                moves.append(Move(p, MoveType.CAPTURE, tar_right))
                
        return moves
    
    def reached_opposite(self, player):
        row_to_check = self.board.size if player == Player.black else 1
        for c in tuple(range(1, self.board.size + 1)):
            if self.board.get(Point(row_to_check, c)) == player:
                return True

    def is_over(self):
        if self.reached_opposite(Player.black):
            return True
        if self.reached_opposite(Player.white):
            return True
        if len(self.legal_moves()) == 0: 
            return True
        return False

    def winner(self):
        if self.reached_opposite(Player.black):
            return Player.black
        if self.reached_opposite(Player.white):
            return Player.white        
        return self.next_player.other
