#Approach_2
-	Second approach for Strategy Board Game Playing Artificial Intelligence Agent 
-	Source Code is from https://github.com/kenziyuliu/PythonChineseCheckers.git` in your terminal

There are couple reinforcement learning techniques that were implemented in this project to teach an agent to learn how to play Chinese Checker. Three kinds of player have been designed for comparison purpose: random player that moves randomly, greedy player that moves to highest value point every time, an AI player with intelligent moves. 

#Setting and Framework
Board.py, Board.utils.py, data_generators.py, evaluate_models.py contains setting for the board, default framework, and some utilise

#Player.py
It contains algorithm for Greedy player and AI Player

#Game.py
It runs the chinese checker between AI player and Greedy player for 10000 times. 

#Train.py and Train_on_greedy.py
It contains the self-training and generate the game 

#MCTS.py
It contains fundation logics for Monte Carlo Tree Search 
