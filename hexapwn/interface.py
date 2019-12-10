# -*- coding: utf-8 -*-
"""
Text insterface for Hexapwn

@author: xcf
"""

__all__ = [
    'checkcode',
    'exitcode',
    'welcomemsg',
    'gameend',
]

import re

def checkcode(code):
    ''' Check to see if input is legal'''
    legal_input = "[A-Z][0-9](-|x)[A-Z][0-9]"
    validcode = re.fullmatch(legal_input, code)
    if not validcode:
        print("Invalid move code. Please try again.")
    return validcode

def exitcode():
    return "Q0-Q0"

def welcomemsg():
    text = ("==============================\n"
    "= Welcome to Sean's Hexapawn =\n"
    "==============================\n"
    "- To move your pawn, type in the coords e.g B3-B2\n"
    "- To capture an opponent pawn when possible, use x. e.g. B2xA1\n"
    "Enjoy! -- Game by Sean XIONG @ UofT\n")
    return text

def gameend(game):
    winner = game.winner()
    if winner is None:
        print("Something went wrong, there should not be a draw.")
    else:
        print('Winner: ' + str(winner))
        
def printboard(board, colnames):
    col_or_rows = tuple(range(1, board.size + 1))
    print('  ', end = '')
    for c in col_or_rows:
        print(' ', colnames[c-1], end='')
    print('\n--', end='')
    for c in col_or_rows:
        print('---', end='')
    print('')
    for row in col_or_rows:
        pieces = []
        for col in col_or_rows:
            piece = board.get(Point(row, col))
            if piece == Player.white:
                pieces.append('W')
            elif piece == Player.black:
                pieces.append('B')
            else:
                pieces.append(' ')
        print('%d|  %s' % (row, '  '.join(pieces)))