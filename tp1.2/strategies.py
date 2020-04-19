#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def betToNumber(numbers, games, initCapital):
    capital = initCapital
    betValue = 10
    graph = [initCapital]
    chosen = int(input('Choose your number: '))
    for i in range(games):
        capital -= betValue
        rand = np.random.randint(0, len(numbers))
        if(rand == chosen):
            capital = capital + betValue * 36
        graph.append(capital)
    return graph

def betToColor(numbers, games, initCapital):
    capital = initCapital
    betValue = 10
    graph = [initCapital]
    myColor = str(input('Now choose a color: (red) or (black): '))
    while(myColor != 'red' and myColor != 'black'):
        myColor = str(input('Please choose a color: (red) or (black): '))

    for i in range(games):
        capital -= betValue
        rand = np.random.randint(0, 37)
        if(numbers[rand].color == myColor):
            capital += (betValue * 2)
        graph.append(capital)
    return graph
    
def betAsSofovich(numbers, games, initCapital):
    capital = initCapital
    betValue = 1000000
    graph = [initCapital]
    notChosen_1 = int(input('Choose your NOT chosen number 1: '))
    notChosen_2 = int(input('Choose your NOT chosen number 2: '))
    for _ in range(2):
        graph.clear()
        graph.append(initCapital) 
        capital = 100000000  
        for i in range(games):
            capital -= (betValue * 35)
            rand = np.random.randint(0, len(numbers))
            if(rand != notChosen_1 and rand != notChosen_2):
                capital = capital + betValue * 36
            graph.append(capital)
    return graph
