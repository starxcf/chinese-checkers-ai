# -*- coding: utf-8 -*-
"""
Play Hexapwn in a dumb way

@author: seanxiong
"""

import gameplay as g
import hexapwn
import agent
from agent.dumb import DumbAgent

if __name__ == '__main__':
    print(hexapwn.welcomemsg())
    p1side = hexapwn.Player.white
    p2side = hexapwn.Player.black
    player1 = g.GamePlayer(p1side, g.PlayerType.human, agent.Agent())
    player2 = g.GamePlayer(p2side, g.PlayerType.computer, DumbAgent())
    result = g.play(player1, player2, hexapwn.GameState, hexapwn.interface)
    hexapwn.gameend(result)