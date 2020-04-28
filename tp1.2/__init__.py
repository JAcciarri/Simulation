# -*- coding: utf-8 -*-

'''
UTN FRRO - Simulation 2020
TP1.2 - Roulette: Economic and Mathematical Analysis

Authors: Joshua Acciarri (44823) & Nicolás Antonelli (44852)
Professor: Torres, Juan
Final Date: 01/05/2020

Python Libraries/Modules Used:
    - Numpy: Random Numbers and Array Manipulation
    - Pyplot: Matplotlib Module for Graph Plotting

Classes/Other Files:
    -RouletteNumber: Object with a value from 0 to 36, and a color
    -Roulette: Object (European Roulette) that contains 37 RouletteNumbers and Strategy methods
    -Strategies: File with the definition of all strategies we use
'''

from matplotlib import pyplot as plt
from Roulette import Roulette
from strategies import *
from graphing import letsGraph

def select(opt):
    roulette.configurePlayer()
    graphs = []
    if (opt == 1):
       graphsLim = betToNumber(roulette, "limited")
       graphsUnlim = betToNumber(roulette, "infinite")
       letsGraph(graphsLim, graphsUnlim)
            
    elif (opt == 2):
       graphsLim = betToColor(roulette, "limited")
       graphsUnlim = betToColor(roulette, "infinite")
       letsGraph(graphsLim, graphsUnlim)

    elif (opt == 3):
       graphsLim = betAsSofovich(roulette, "limited")
       graphsUnlim = betAsSofovich(roulette, "infinite")
       letsGraph(graphsLim, graphsUnlim)
    elif (opt == 4):
       graphsLim = betMartingale(roulette, "limited")
       graphsUnlim = betMartingale(roulette, "infinite")
       letsGraph(graphsLim, graphsUnlim)
    elif (opt == 5):
       graphsLim = betDalembert(roulette, "limited")
       graphsUnlim = betDalembert(roulette, "infinite")
       letsGraph(graphsLim, graphsUnlim)
    else:
        print('Good Bye!\n')
        exit()

# Main
if __name__ == '__main__':
    roulette = Roulette()
    strat = -1
    while (strat != 0):
        print('ROULETTE SIMULATOR')
        print('Welcome. Do you want to play?')
        print()
        while(strat not in [0, 1, 2, 3, 4, 5]):
            strat = int(float(input('Please choose a strategy: (1 or 2 or 3 or 4 or 5)\n1: Bet to a single number\n2: Bet to a color\n3: Bet AS Sofovich\n4: Bet Martingale (Classic and Modified)\n5: Bet D\'Alambert\n\n0: Exit Game\n')))
        print()
        # Exit Game
        if (strat == 0):
            exit()
        
        select(strat)
        # Default Strat to -1 for re-start game simulator correctly
        strat = -1

