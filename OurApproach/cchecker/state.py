"""
Chinese checker game status logic. This class handles most of the game logic

@author: Sean, Bill and Alexandra
"""

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
        
    def legal_moves(self):
        result = []
        # map to check already explored moves
        check_map = np.zeros((BOARD_WIDTH, BOARD_HEIGHT), dtype='uint8')
        # expand to each directions without jump
        result.append(checker_pos)
        check_map[checker_pos] = 1
        for walk_dir in self.directions:
            row, col = tuple(map(operator.add, checker_pos, walk_dir))
            if not board_utils.is_valid_pos(row, col):
                continue
            if self.board[row, col, 0] == 0:
                result.append((row, col))
                check_map[row, col] = 1

        # check continous jump moves
        self.board[checker_pos[0], checker_pos[1], 0] = 0;              # Remove current checker before checking
        self.valid_checker_jump_moves(result, check_map, checker_pos)
        self.board[checker_pos[0], checker_pos[1], 0] = cur_player;     # Put back current checker
        result.remove(checker_pos)                                      # Don't allow staying
        return result
    
    def is_over(self):
        cur_board = self.board[:, :, 0]
        one_win = two_win = True
        for k in range(BOARD_WIDTH - ROWS_OF_CHECKERS, BOARD_WIDTH):
            if one_win:
                up_diag = cur_board.diagonal(k)
                if not np.array_equal(up_diag, [PLAYER_ONE]*len(up_diag)):
                    one_win = False
            if two_win:
                down_diag = cur_board.diagonal(-k)
                if not np.array_equal(down_diag, [PLAYER_TWO]*len(down_diag)):
                    two_win = False

            if not one_win and not two_win:
                return 0

        return PLAYER_ONE if one_win else PLAYER_TWO
        
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
        
    def isjumpmove(self, move):
                curr_row, curr_col = checker_pos
        # expand with jump
        for walk_dir in self.directions:
            step = 1
            row_inc, col_inc = walk_dir
            row, col = curr_row + row_inc, curr_col + col_inc
            valid_pos = True

            # Go along the direction to find the first checker and record steps
            while True:
                if not board_utils.is_valid_pos(row, col):
                    valid_pos = False
                    break
                if self.board[row, col, 0] != 0:
                    break
                step += 1
                row += row_inc
                col += col_inc

            if not valid_pos:
                continue

            # Continue in the direction to find the mirror move
            for i in range(step):
                row += row_inc
                col += col_inc
                if not board_utils.is_valid_pos(row, col) or self.board[row, col, 0] != 0:
                    valid_pos = False
                    break

            if not valid_pos:
                continue

            # get the row and col ready to jump
            # check whether the destination is visited
            if check_map[row, col] == 1:
                continue

            # store moves
            valid_moves.append((row, col))
            check_map[row][col] = 1
            self.valid_checker_jump_moves(valid_moves, check_map, (row, col))

if __name__ == '__main__':
    b = Board(5)
    cchecker.printboard(b,'ABCDEFGHIJKLMNOPQRSTUVWXYZ')    