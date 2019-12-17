# -*- coding: utf-8 -*-
"""
Pleay Chinese checker game Human vs Computer

@author: Sean, Bill and Alexandra
"""

import gameplay as g
import cchecker
import agent
from agent.dumb import DumbAgent
from agent.alphabeta import AlphaBetaAgent
from agent.MCTS import MCTS

if __name__ == '__main__':
    print(cchecker.welcomemsg())
    p1side = cchecker.Player.white
    p2side = cchecker.Player.black
    player1 = g.GamePlayer(p1side, g.PlayerType.human, agent.Agent())
    player2 = g.GamePlayer(p2side, g.PlayerType.computer, DumbAgent())
#    player2 = g.GamePlayer(p2side, g.PlayerType.computer, AlphaBetaAgent())
#    player2 = g.GamePlayer(p2side, g.PlayerType.computer, MCTS())
    result = g.play(player1, player2, cchecker.GameState, cchecker.interface)
    cchecker.gameend(result)