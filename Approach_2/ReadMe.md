# Approach_2

## Heuristics-guided Reinforcement Learning and Monte Carlo Tree Search

-	Second approach for Strategy Board Game Playing Artificial Intelligence Agent 
-	Source Code is from https://github.com/kenziyuliu/PythonChineseCheckers.git` in your terminal

Three kinds of player have been designed for comparison against each other: a `random player` that moves randomly, a `greedy player` that moves to the highest value point each move, and an AI player with intelligent movements guided by Monte Carlo Tree Search (MCTS).

## Setting and Framework
Board.py, Board.utils.py, data_generators.py, evaluate_models.py contain the settings for the board, default framework, and some utilities. 

## Player.py
Contains the algorithm for the Greedy player and AI Player.

## Game.py
It runs the chinese checker game board between an AI player and Greedy player for 10000 iterations. 

## Train.py and Train_on_greedy.py
It contains the self-training code and generates the game. 

## MCTS.py
It contains foundation logic for Monte Carlo Tree Search.
