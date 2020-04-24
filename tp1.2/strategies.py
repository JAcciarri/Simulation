#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def betToNumber(roulette):
    capital = roulette.getInitCapital()
    betValue = 1
    graph = [capital]
    chosen = int(float(input('Choose your number: ')))
    for i in range(roulette.getGames()):
        capital -= betValue
        rand = np.random.randint(0, len(roulette.getNumbers()))
        if(rand == chosen):
            capital = capital + betValue * 36
        graph.append(capital)
    print()
    return graph

def betToColor(roulette):
    capital = roulette.getInitCapital()
    betValue = 1
    graph = [capital]
    myColor = ""
    while(myColor != 'red' and myColor != 'black'):
        myColor = str(input('Please choose a color: (red) or (black): '))

    for i in range(roulette.getGames()):
        capital -= betValue
        rand = np.random.randint(0, 37)
        if(roulette.getNumbers()[rand].color == myColor):
            capital += (betValue * 2)
        graph.append(capital)
    print()
    return graph
    
def betAsSofovich(roulette):
    # This will probably be deleted
    capital = roulette.getInitCapital()
    betValue = 100
    graph = [capital]
    notChosen_1 = int(float(input('Choose your NOT chosen number 1: ')))
    notChosen_2 = int(float(input('Choose your NOT chosen number 2: ')))
    for i in range(roulette.getGames()):
        capital -= (betValue * 35)
        rand = np.random.randint(0, len(roulette.getNumbers()))
        if(rand != notChosen_1 and rand != notChosen_2):
            capital = capital + betValue * 36
        graph.append(capital)
    return graph

# Classic and Modified Martingale
def betMartingale(roulette):
    capital = roulette.getInitCapital()
    betValue = 1
    graph = [capital]
    modified = ""
    while(modified != 'Y' and modified != 'N'):
        modified = str.upper(str(input('There are two types of Martingale. Classic and Modified. The default is Classic. Do you want to change to Modified? (Y/N) ')))

    myColor = ""
    while(myColor != 'red' and myColor != 'black'):
        myColor = str(input('Please choose a color: (red) or (black): '))

    for i in range(roulette.getGames()):
        capital -= betValue
        rand = np.random.randint(0, 37)
        color = roulette.getNumbers()[rand].color
        if(roulette.getNumbers()[rand].color == myColor):
            capital += (betValue * 2)
        graph.append(capital)

        # Duplicate previous bet (modified: adds +1 units)
        if(myColor != color):
            if (modified == 'Y'):
                betValue = betValue * 2 + 1
            else:
                betValue = betValue * 2
        else:
            # Reinitialize betValue to 1
            capital += betValue * 2
            betValue = 1
        graph.append(capital)
    print('Final capital: ', capital)
    print()
    return graph
