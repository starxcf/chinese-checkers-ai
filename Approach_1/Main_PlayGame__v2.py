from Player import MC_Player, Ordered_Player, Random_Player
from Setting import ChineseCheckers
import matplotlib.pyplot as plt
import numpy as np


'''
where 2 players and the board will be init and then play a game 
ime limit will be set on each player 
'''

import numpy as np
#import matplotlib.pyplot as plt

PURPLE = 1
WHITE = 2


def experiment():
    cc = ChineseCheckers()
    c = 0
    moves = cc.move_ordering(PURPLE)
    values = np.zeros(len(moves))
    count = np.zeros(len(moves))
    cc.print_graph_board()
    y = 0
    MC_R = []
    MC_G = []
    while y <2:
        if y == 0: 
            p1 = MC_Player(PURPLE)
            p2 = Random_Player(WHITE)
            print("AI Player against Random Player")
            score = []
        else: 
            p1 = MC_Player(PURPLE)
            p2 = Ordered_Player(WHITE)
            print("-------------------------------")
            print("AI Player against Greedy Player")
            MC_R = score
            score = []
            
        for x in range(100):
            cc.reset()
            cc.update_graph_board()
            winner = 0
            eps = np.random.uniform()
            if eps > 0.5:
                move_i = np.argmax(values)
                move = moves[move_i]
                cc.play_move(move[0], move[1], PURPLE)
            else:
                move_i = np.random.randint(len(moves))
                move = moves[move_i]
                cc.play_move(move[0], move[1], PURPLE)
    
            count[move_i] += 1
            while(c < 50):
                c += 1
                p2.play_move(cc)
                cc.update_graph_board()
                if cc.terminal() == WHITE:
                    winner = WHITE
                    score.append(c*-1)
                    print("Trial",x+1," Other Player wins with total move of", c)
                    break
                p1.play_move(cc)
                cc.update_graph_board()
                if cc.terminal() == PURPLE:
                    score.append(c)
                    print("Trial",x+1,"AI Player wins with total move of", c)
                    winner = PURPLE
                    break
            if winner == PURPLE:
                values[move_i] = values[move_i] + \
                    (1-values[move_i])/(count[move_i])
            else:
                values[move_i] = values[move_i] + \
                    (0-values[move_i])/(count[move_i])
            c = 0
        y+=1
    MC_G = score
    print("Finish")
    print(MC_R, MC_G)
    x_axis =np.arange(1,100,1)
    plt.plot(x_axis, MC_R, 'r--', x_axis,MC_G, 'bs')
    plt.grid(True)
    plt.xlabel('trail')
    plt.ylabel('MC_winning_move')    
    plt.show()

experiment()
