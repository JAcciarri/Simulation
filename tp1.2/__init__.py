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


def select(opt):
    if (opt == 0):
        print('Good Bye!\n')
        exit()
    else:
        roulette.configurePlayer()
        if (opt == 1):
            graph = betToNumber(roulette)
            plt.title('Bet to a single number')
            
        elif (opt == 2):
            graph = betToColor(roulette)
            plt.title('Bet to a color')
        elif (opt == 3):
            graph = betAsSofovich(roulette)
            plt.title('Bet AS Sofovich')
        elif (opt == 4):
            graph = betMartingale(roulette)
            plt.title('Bet Martingale')
        elif (opt == 5):
            graph = betDalembert(roulette)
            plt.title('Bet D\'Alembert')
        else:
            print('Good Bye!\n')
            exit()
        plt.plot(graph)
        return graph


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
        
        # Graph
        graph = select(strat)
        if min(graph) >= 0:
            plt.ylim(bottom=0, top=max(graph)*1.1)
        else:
            plt.ylim(bottom=min(graph)*1.1, top=max(graph)*1.1)
        fig = plt.gcf()
        fig.canvas.set_window_title("Strategy Analysis")
        plt.ylabel('Capital')
        plt.xlabel('N (bets)')
        plt.axhline(roulette.getInitCapital(), color='red', linestyle='--', label="Init Capital")
        plt.legend()
        plt.show()

        # Default Strat to -1 for re-start game simulator correctly
        strat = -1
