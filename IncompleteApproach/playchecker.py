# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 23:08:43 2019

@author: Sean, Bill and Alexandra
"""

import gameplay as g
import cchecker
import agent
from agent.dumb import DumbAgent

if __name__ == '__main__':
    print(cchecker.welcomemsg())
#    p1side = cchecker.Player.white
#    p2side = cchecker.Player.black
#    player1 = g.GamePlayer(p1side, g.PlayerType.human, agent.Agent())
#    player2 = g.GamePlayer(p2side, g.PlayerType.computer, DumbAgent())
#    result = g.play(player1, player2, cchecker.GameState, cchecker.interface)
#    cchecker.gameend(result)
#        import cchecker.interface as iface
    b = cchecker.Board(5)
    cchecker.printboard(b,'ABCDEFGHIJKLMNOPQRSTUVWXYZ')