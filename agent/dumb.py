# -*- coding: utf-8 -*-
"""
A dumb agent that just play randomly

@author: sean xiong
"""

import random
from agent import Agent

class DumbAgent(Agent):
    def __init__(self, p):
        Agent.__init__(self, p)
    
    def select_move(self, game_state):
        return random.choice(game_state.legal_moves())
    
    def load(self):
        print("pretend to load")
        
    def save(self):
        print("pretend to save")
        
    def update(self):
        print("pretend to update")