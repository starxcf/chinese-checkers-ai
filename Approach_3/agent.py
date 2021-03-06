import random, re, datetime
import sys
import math
from queue import PriorityQueue
import copy
# sourced from https://github.com/AICourseTeamHatchet/ChineseCheckerAI

class MinimaxAgent(Agent):
    """
    This class implements the minimax algorithm, using alpha-beta pruning as well.
    """
    def late_game(self, agent_pos, opponent_pos):
        """
        This function is designed for evaluating the early game, contributing as a part of the
        whole evaluation function
        :param state: The current state
        :return: A value specifying the evaluation result
        """
        """
        # Another function that evaluates the late game
        terminate_state = [(1, 1), (2, 1), (2, 2), (3, 1), (3, 2), (3, 3), (4, 1), (4, 2), (4, 3), (4, 4)]
        for checker in agent_pos:
            if checker in terminate_state:
                eval_value += 1
        return eval_value
        """
        eval_value = 0
        for pos_a in agent_pos:
            eval_value += (pos_a[0])
        for pos_o in opponent_pos:
            eval_value -= (20 - pos_o[0])
        return eval_value

    def mid_game(self, agent_pos, opponent_pos):

        eval_value = 0
        # Calculate the sparsity of the distribution of checkers
        # We hope the checkers of one kind are close, and not too sparse from each other
        agent_sparsity_row = agent_pos[-1][0] - agent_pos[0][0]
        opponent_sparsity_row = opponent_pos[-1][0] - opponent_pos[0][0]
        eval_value = eval_value + (opponent_sparsity_row - agent_sparsity_row)

        # In this part, we take advantage of the opponent, using their checkers as well
        # This is evaluated by a rough L2 distance
        # Maybe too complicated
        """for i in range(10):
            l2_dis = math.sqrt((agent_pos[i][0] - opponent_pos[i][0]) ** 2 + (agent_pos[i][1] - opponent_pos[i][1]) ** 2)
            eval_value = eval_value + (19 - l2_dis)"""

        # We rather use the distance of columns
        for i in range(10):
            dis = abs(agent_pos[i][0] - opponent_pos[i][0])
            eval_value += dis

        return eval_value

    def early_game(self, agent_pos, opponent_pos):
        #opponent_pos = board.getPlayerPiecePositions(3 - state[0])
        # When in early game, a large probability is that our moves seldom depend on
        # the state of the opponent, we hope that checkers at the bottom moves out as fast
        # as possible
        eval_value = 0
        for pos in agent_pos:
            eval_value -= pos[0]

        return eval_value

    def eval_func(self, state):
        evaluate = 0
        board = state[1]
        agent_pos = board.getPlayerPiecePositions(state[0])
        opponent_pos = board.getPlayerPiecePositions(3 - state[0])
        agent_pos.sort()
        opponent_pos.sort()
        #print(self.early_game(agent_pos, opponent_pos), self.mid_game(agent_pos, opponent_pos),
        #      self.late_game(agent_pos, opponent_pos))

        alpha = 0
        beta = 1
        gamma = 100
        #print(agent_pos)

        evaluate += alpha * self.early_game(agent_pos, opponent_pos) + beta * self.mid_game(agent_pos, opponent_pos) + \
                    gamma * self.late_game(agent_pos, opponent_pos)
        #print (evaluate)

        return evaluate

    # Used for minimax pruning
    def takeDepth(self, action):
        return action[1][0] - action[0][0]

    def max_value(self, state, n, alpha, beta):
        """
        This function determines the maximum value for the current state.
        :param state: Current state for evaluating
        :param n: The depth for minimax search
        :param alpha: Parameter of the alpha-beta pruning, the smaller value
        :param beta: Parameter of the alpha-beta pruning, the larger value
        :return: The result value for the state
        """
        if n == 0:
            return self.eval_func(state)

        value = sys.maxsize * -1
        best_action = None

        actions = self.game.actions(state)
        actions.sort(key=self.takeDepth)
        for action in actions:
            value = max(value, self.min_value(self.game.succ(state, action), n-1, alpha, beta))
            if value >= beta:
                if n == 2:
                    return value, action
                else:
                    return value
            if value > alpha:
                alpha = value
                self.action = action
                best_action = action
        if n == 2:
            return value, best_action
        else:
            return value


    def min_value(self, state, n, alpha, beta):
        """
        This function determines the minimum value for the current state
        :param state: :)
        :param n: :)
        :param alpha: :)
        :param beta: :)
        :return: :)
        """
        if n == 0:
            return self.eval_func(state)

        value = sys.maxsize
        for action in self.game.actions(state):
            value = min(value, self.max_value(self.game.succ(state, action), n-1, alpha, beta))
            if value <= alpha:
                return value
            beta = min(value, beta)
        return value


    def minimax(self, state, n, alpha = sys.maxsize * -1, beta = sys.maxsize):
        value, action = self.max_value(state, n, alpha, beta)
        return action

    def getAction(self, state):
        legal_actions = self.game.actions(state)
        self.action = random.choice(legal_actions)

        player = self.game.player(state)
        n = 2 # Referring to the depth
        ### START CODE HERE ###
        best_action = None
        agent_pos = state[1].getPlayerPiecePositions(player)
        opponent_pos = state[1].getPlayerPiecePositions(3 - player)
        myFirst, myLast = getFirstLastElement(agent_pos, player)
        herFirst, herLast = getFirstLastElement(opponent_pos, 3 - player)

        best_action = self.minimax(state, n)

        if best_action == None:
            print ("random")
            pass
        else:
            self.action = best_action

# get the first and last element based on position and player
def getFirstLastElement(agent_pos, player):
    if player == 1:
        first = agent_pos[0][0]
        last = agent_pos[0][0]
        for position in agent_pos:
            if position[0] < first:
                first = position[0]
            if position[0] > last:
                last = position[0]
    else:
        first = agent_pos[0][0]
        last = agent_pos[0][0]
        for position in agent_pos:
            if position[0] > first:
                first = position[0]
            if position[0] < last:
                last = position[0]

    return first, last

# is the game starting battle with each other now
def isBattle(MyFirst, HerFirst, player):
    if player == 2:
        return (MyFirst - HerFirst >= 2)
    else:
        return (HerFirst - MyFirst >= 2)

# is the game going to the end of the state now
def isEnding(MyLast, HerLast, player, k = 0):
    if player == 1:
        return (MyLast + k <= HerLast)
    else:
        return (HerLast + k <= MyLast)

# getting vertical distance to goal state sum
def vertical_distance(agent_pos, player):
    distance = 0

    if player == 1:
        for position in agent_pos:
            distance += 20 - position[0]
    else:
        for position in agent_pos:
            distance += position[0]

    return distance

# getting the distance from all the nodes to the mid column line
def midline_distance(agent_pos, board):
    distance = 0

    for position in agent_pos:
        distance += abs(position[1] - board.getColNum(position[0]) / 2)

    return distance

# check if the chesses are too loose
def check_looseness(agent_pos):
    distance = 0
    average = 0

    for position in agent_pos:
        average += position[0] / 10
    for position in agent_pos:
        distance += abs(position[0] - average)

    return distance

# Check whether the player has reached the terminal state(actually not the same with the isEnd() function)
# This is a bool function
def player_win(agent_pos):
    terminal_state = [(1, 1), (2, 1), (2, 2), (3, 1), (3, 2), (3, 3), (4, 1), (4, 2), (4, 3), (4, 4)]
    for p in agent_pos:
        if p not in terminal_state:
            return False
    return True