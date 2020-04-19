#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
UTN FRRO - Simulation 2020
TP1.2 - Roulette Economic and Mathematical Analysis

Authors: Joshua Acciarri (44823) & Nicolás Antonelli (44852)
Professor: Torres, Juan
Final Date: 15/04/2020

Python Libraries/Modules Used:
    - Numpy: Random Numbers, Statistical Functions, Array Manipulation
    - Pyplot: Matplotlib Module for Graph Plotting
    - Time: Module used for processing time measurement

Note: All Printed Messages and Plotted Graphs are in SPANISH
"""

from Roulette import Roulette
from matplotlib import pyplot as plt


def select(opt):
    if (opt == 1):
        graph = roulette.strategy('number')
        plt.title('Bet to a single number')
    elif (opt == 2):
        graph = roulette.strategy('color')
        plt.title('Bet to a color')
    else:
        graph = roulette.strategy('sofovich')
        plt.title('Bet AS Sofovich')
    plt.plot(graph)


# Main
if __name__ == '__main__':
    roulette = Roulette()
    print('ROULETTE SIMULATOR')
    print('Welcome. Do you want to play?')
    print()
    strat = 0
    while(strat != 1 and strat != 2 and strat != 3):
        strat = int(input('Please choose a strategy: (1 or 2 or 3)\n1: Bet to a single number\n2: Bet to a color\n3: Bet AS Sofovich\n'))
    print()
    select(strat)

    # Graph
    plt.ylabel('Capital')
    plt.xlabel('N (bets)')
    plt.show()
