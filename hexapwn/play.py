# -*- coding: utf-8 -*-
"""
Play Hexapwn, flexibale with the players being human or computer

@author: seanxiong
"""

__all__ = [
    'play',
]

import sys
from hexapwn.state import GameState, Move
from hexapwn.interface import checkcode, exitcode
from player import GamePlayer

def play(player1:GamePlayer, player2:GamePlayer, intercative=False):
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
        
    BOARD_SIZE = 4
    game = GameState.new_game(BOARD_SIZE)
    while not game.is_over():
        if (game.next_player in human_players):
            game.board.print_out()
            user_input = input(game.next_player.name + ' move - ')
            human_move = checkcode(user_input)
            if not human_move:
                continue
            if human_move[0] == exitcode():
                print("Byebye!")
                sys.exit()
            move = Move.init_from_code(human_move[0])
        else:
            if intercative: 
                game.board.print_out()
                print('Calculating...', end=" ")
            bot = player1.ai if player1 == game.next_player else player2.ai
            move = bot.select_move(game)
            if intercative: print('done.')
        game = game.apply_move(move)
        
    if intercative:
        game.board.print_out()
    return game