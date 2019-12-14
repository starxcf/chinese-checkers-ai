# Chinese Checkers Playing Artificial Intelligence Agent

### Project by Sean Xiong, Bill Zizek, and Alexandra Yue
### SCS 3547 - Intelligent Agents & Reinforcement Learning
### https://github.com/starxcf/chinese-checkers-ai.git


# Description

Herein, we've designed a Python-based program to evaluate the playing performance and strategy of various intelligent agents on different board games. Each board game has a unique configuration of a board, playing pieces,  and rules. Stemming from this, each game has a unique strategy to maximize success in winning the game. Considering the technical and time requirements of training, optimization, and other factors, we propose analyzing intelligent agents in a simple micro-environment before scaling to a larger, more complex environment. To begin with, the intelligent agent's performance will be screened using the rules and board for **Hexapawn**. Certain AI will then be selected after critical evaluation and tested using a larger and more complex playing environment in **Chinese Checkers**. 

The **objectives** of this work are two-fold:
1. Support multiple game environments (Hexapawn and Chinese Checkers)
2. Support multiple Intelligent Agents (AI) of varying degree of sophistication

# Instructions

There are two entry points for the program depending on the board game selected:  `play*.py`  and  `train*.py`.  We suggest starting with Hexapawn.

Play can then be done with a human player, computer player, or both. `train*.py` is then intended for the AI to learn by playing with itself or other AI.

# Methods and Analysis

In the Approach_1, three kinds of player types have been designed for comparison: `random player` that moves randomly, `greedy player` that moves to highest value point every time, and an `AI player` with intelligent movements based on training. The `AI player` is powered by a very simple Monte Carlo (MC) simulation. In a MC simulation, you play the game by starting in a random state (not necessarily the beginning) and play until the end while recording states, actions, and rewards within the confines of the game. A caveat with a simple MC approach is that there is no guarantee it will actually visit all the possible states of the game. However in our analysis, the AI player consistently outperformed the random player in all test cases. Based on the engineering of the intelligent AI player, over the long run the AI player will have a higher win % than the greedy player.

![MCS performance](./Approach_2/MC_winning_move_Trial100.png)
> Above we can see running times on the X-axis across 100 trials and the # of moves to victory on the Y-axis. As such, a positive # indicates a win by the MCTS agent and negative indicates a loss. In red, we see the simple Monte Carlo simulation dominate in performance over a random-moving player. In blue, we can see the mixed performance against a greedy player.

In Approach_2, the AI Player is way more sophisticated and well trained through playing hundreds of games against itself. As a result of this, it has a high chance to beat the greedy player over a long run. This is done in part through a heuristics-guided Reinforcement Learning and Monte Carlo Tree Search (MCTS). The general idea behind a MCTS is simple - given the state of the game, choose the most promising move. A MCTS consists of four phsaes: selection, expansion, simulation, and backpropagation. The algorithm starts at a root node and moves down the action tree until a leaf node is reached. Then, if the leaf node does not terminate the game then more child nodes are created according to available actions. Next the simulation phase involves taking random actions to get to a new state. This is done until a terminal state is reached. The value of the terminal state is then back propagated and the involved nodes are updated with the simulation results while tracking the number of visits to each node. MCTS search doesn't require any knowledge about the domain but can take many iterations to converge to a good solution.

In a proposed Approach_3, the AI player is enabled by a minimax algorithm with alpha-beta pruning. The value of each leaf board state can be approximated by a linear evaluation function based on the total distance to the opponent's corner, total distance to the centre line, and sum of vertical advancements. This agent was not fully implemented with our board due to time and resources constraints. 

In all approaches, the AI Player generally has a much higher chance to win the game when competing against the other player in the long run. 
