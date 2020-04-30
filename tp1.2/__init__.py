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
    -Graphing: File with common Plotting functions
'''

from Roulette import Roulette
from graphing import letsGraph
from strategies import *
import matplotlib.pyplot as plt

def select(opt):
    
    # Roulette Settings
    roulette.configurePlayer()

    # Arrays for multiple Game Results (Recommended: 5 to 10)
    results = 6
    resultsLimited = []
    resultsUnlimited = []
    
    # Type of Strategy
    for i in range(results):
        if (opt == 1):
            graphsLim, graphsUnlim = betToNumber(roulette) 
        elif (opt == 2):
            graphsLim, graphsUnlim = betToColor(roulette)
        elif (opt == 3):
            graphsLim, graphsUnlim = betAsSofovich(roulette)
        elif (opt == 4):
            graphsLim, graphsUnlim = betMartingale(roulette)
        elif (opt == 5):
            graphsLim, graphsUnlim = betDalembert(roulette)
        elif (opt == 6):
            graphsLim, graphsUnlim = betFibonacci(roulette)
        elif (opt == 7):
            graphsLim, graphsUnlim = betASSantE(roulette)
        else:
            print('Good Bye!\n')
            exit()

        # Adding current results to the array of results
        resultsLimited.append(graphsLim)
        resultsUnlimited.append(graphsUnlim)
    
    # Call graphing's function for the first game results
    title = "Roulette Strategy Analysis, one result game"
    letsGraph(resultsLimited[0], resultsUnlimited[1], roulette.getInitCapital(), title)

    # Averages Calculation
    graphsLim["capital"]   = (resultsLimited[0]["capital"]   + resultsLimited[1]["capital"]   + resultsLimited[2]["capital"]   + resultsLimited[3]["capital"]   + resultsLimited[4]["capital"]   + resultsLimited[5]["capital"])   / results
    graphsUnlim["capital"] = (resultsUnlimited[0]["capital"] + resultsUnlimited[1]["capital"] + resultsUnlimited[2]["capital"] + resultsUnlimited[3]["capital"] + resultsUnlimited[4]["capital"] + resultsUnlimited[5]["capital"]) / results
    graphsLim["frec"]      = (resultsLimited[0]["frec"]      + resultsLimited[1]["frec"]      + resultsLimited[2]["frec"]      + resultsLimited[3]["frec"]      + resultsLimited[4]["frec"]      + resultsLimited[5]["frec"])      / results
    graphsUnlim["frec"]    = (resultsUnlimited[0]["frec"]    + resultsUnlimited[1]["frec"]    + resultsUnlimited[2]["frec"]    + resultsUnlimited[3]["frec"]    + resultsUnlimited[4]["frec"]    + resultsUnlimited[5]["frec"])    / results

    # Call graphing's function for every game result
    title = "Roulette Strategy Analysis, all results games"
    letsGraph(graphsLim, graphsUnlim, roulette.getInitCapital(), title)

    # Visualize all the graphics
    plt.show()


# Main
if __name__ == '__main__':
    roulette = Roulette()
    strat = -1
    while (strat != 0):
        # Menu
        print('ROULETTE SIMULATOR')
        print('Welcome. Do you want to play?')
        print()
        inputMsg = 'Please choose a strategy: (number from 1 to 6)\n'
        inputMsg += '1: Bet to a single number\n2: Bet to a color\n3: Bet AS Sofovich\n4: Bet Martingale (Classic and Modified)\n'
        inputMsg += '5: Bet D\'Alambert\n6: Bet Fibonacci (Bet fixed to 1)\n7: Bet AS SantE (Original Strategy)\n\n0: Exit Game\n'
        while(strat not in [0, 1, 2, 3, 4, 5, 6, 7]):
            strat = int(float(input(inputMsg)))
        print()
        # Exit Game
        if (strat == 0):
            exit()
        
        select(strat)
        # Default Strat to -1 for re-start game simulator correctly
        strat = -1
