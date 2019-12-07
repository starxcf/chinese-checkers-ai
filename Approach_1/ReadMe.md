# Approach_1 

## A Simple Monte Carlo Intelligent Agent for Strategy Board Game Playing 
- This is the repository for a Chinese Checkers agent trained with heuristics-guided Reinforcement Learning and Monte Carlo simulation.
- Code source is from https://github.com/JayGeisler/MonteCarlo_ChineseCheckers.git

## Main_PlayGame.py

Main Code that will run the settings and the game. AI player will compete with Random player for first 10 times, then AI player will compete with the
Greedy Player for 10 times. 

## Player.py, Setting.py and Exhibit.py

`Player.py` contains AI Player, Random Player and Greedy Player. AI Player uses Monte Carlo simulation to predict where the most likely to win move is on the current board state. Random player plays randomly. Greedy player always go with position with highest value. 
`Setting.py` is the board of the game, will return a list of the positions of the board pieces also the value of the players positions, the values are how close you are to the winning side. 
`Exhibit.py` is designed for graph.