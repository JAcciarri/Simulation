#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
UTN FRRO - Simulation 2020
TP1.2 - Roulette Economic and Mathematical Analysis

Authors: Joshua Acciarri (44823) & Nicolás Antonelli (44852)
Professor: Torres, Juan
Final Date: 01/05/2020

Python Libraries/Modules Used:
    - Numpy: Random Numbers and Array Manipulation
    - Pyplot: Matplotlib Module for Graph Plotting

"""

from Roulette import Roulette
from matplotlib import pyplot as plt
from strategies import betToNumber, betToColor, betAsSofovich, betMartingale



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
        else:
            print('Good Bye!\n')
            exit()
        plt.plot(graph)


# Main
if __name__ == '__main__':
    roulette = Roulette()
    strat = -1
    while (strat != 0):
        print('ROULETTE SIMULATOR')
        print('Welcome. Do you want to play?')
        print()
        while(strat != 0 and strat != 1 and strat != 2 and strat != 3 and strat != 4):
            strat = int(input('Please choose a strategy: (1 or 2 or 3 or 4)\n1: Bet to a single number\n2: Bet to a color\n3: Bet AS Sofovich\n4: Bet Martingale\n0: Exit Game\n'))
        print()
        select(strat)
        strat = -1
        # Graph
        plt.ylabel('Capital')
        plt.xlabel('N (bets)')
        plt.show()
