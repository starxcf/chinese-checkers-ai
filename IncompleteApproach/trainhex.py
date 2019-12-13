# -*- coding: utf-8 -*-
"""
Train agent to improve the rules
"""

from player import GamePlayer, PlayerType
import hexapwn
from agent.dumb import DumbAgent

if __name__ == '__main__':
    p1side = hexapwn.Player.white
    p2side = hexapwn.Player.black
    bot = DumbAgent("dumb.state")
    player1 = GamePlayer(p1side, PlayerType.computer, bot)
    player2 = GamePlayer(p2side, PlayerType.computer, bot)
    for episode in range(1, 10):
        result = hexapwn.play(player1, player2, False)
        bot.update(result)
    bot.save()
        