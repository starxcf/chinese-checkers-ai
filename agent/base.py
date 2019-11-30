__all__ = [
    'Agent',
]

class Agent:
    def __init__(self, p):
        self.player = p
        
    def select_move(self, game_state):
        raise NotImplementedError()

    def load(self):
        raise NotImplementedError()
        
    def save(self):
        raise NotImplementedError()

class 