__all__ = [
    'Agent',
]

class Agent:
    def __init__(self, savedpath=""):
        self.load(savedpath)
        
    def select_move(self, game_state):
        raise NotImplementedError()

    def load(self, path):
        self.path = path
        
    def save(self):
        raise NotImplementedError()
