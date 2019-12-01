# -*- coding: utf-8 -*-
"""
Play Hexapwn in a dumb way

@author: seanxiong
"""

from player import GamePlayer, PlayerType
import hexapwn
import agent
from agent.dumb import DumbAgent

if __name__ == '__main__':
    print(hexapwn.welcomemsg())
    p1side = hexapwn.Player.white
    p2side = hexapwn.Player.black
    player1 = GamePlayer(p1side, PlayerType.human, agent.Agent())
    player2 = GamePlayer(p2side, PlayerType.computer, DumbAgent())
    result = hexapwn.play(player1, player2, True)
    hexapwn.gameend(result)