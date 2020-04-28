# -*- coding: utf-8 -*-

import numpy as np
import graphing as g

# Only Number
def betToNumber(roulette, typeof):
    capital = roulette.getInitCapital()
    betValue = 1
    capitalGraph = [capital]
    frGraph = []
    fr = 0
    graphs = []
    chosen = int(float(input('Choose your number:')))
    for i in range(1, roulette.getGames()):
        if (typeof == "limited" and betValue>capital):
            graphs.append(capitalGraph)
            graphs.append(frGraph)
            return graphs

        capital -= betValue
        rand = np.random.randint(0, len(roulette.getNumbers()))
        if(rand == chosen):
            capital += betValue * 36
            fr += 1
        capitalGraph.append(capital)
        frGraph.append(fr/i)

    graphs.append(capitalGraph)
    graphs.append(frGraph)
    print('Final capital: ', capital)
    print("Your total play time would be about: " + str(roulette.getGames() * roulette.getBetTime() // 60) + " min")
    print()
    return graphs


# Only Color
def betToColor(roulette, typeof):
    capital = roulette.getInitCapital()
    betValue = 1
    capitalGraph = [capital]
    frGraph = []
    fr = 0
    graphs = []
    myColor = ""
    while(myColor != 'red' and myColor != 'black'):
        myColor = str(input('Please choose a color: (red) or (black): '))

    for i in range(1, roulette.getGames()):
        if (typeof == "limited" and betValue>capital):
            graphs.append(capitalGraph)
            graphs.append(frGraph)
            return graphs

        capital -= betValue
        rand = np.random.randint(0, 37)
        if(roulette.getNumbers()[rand].color == myColor):
            capital += betValue * 2
            fr += 1
        frGraph.append(fr/i)
        capitalGraph.append(capital)
    
    graphs.append(capitalGraph)
    graphs.append(frGraph)
    print('Final capital: ', capital)
    print("Your total play time would be about: " + str(roulette.getGames() * roulette.getBetTime() // 60) + " min")
    print()
    return graphs

# Gerardo Sofovich's Strategy
def betAsSofovich(roulette, typeof):
    # This will probably be deleted
    capital = 100000
    betValue = 100
    capitalGraph = [capital]
    frGraph = []
    fr = 0
    graphs = []
    notChosen_1 = int(float(input('Choose your NOT chosen number 1: ')))
    notChosen_2 = int(float(input('Choose your NOT chosen number 2: ')))
    for i in range(1, roulette.getGames()):
        if (typeof == "limited" and betValue>capital):
            graphs.append(capitalGraph)
            graphs.append(frGraph)
            return graphs

        capital -= (betValue * 35)
        rand = np.random.randint(0, len(roulette.getNumbers()))
        
        if(rand != notChosen_1 and rand != notChosen_2):
            capital += betValue * 36
            fr += 1
        capitalGraph.append(capital)
        frGraph.append(fr/i)

    print('Final capital: ', capital)
    print("Your total play time would be about: " + str(roulette.getGames() * roulette.getBetTime() // 60) + " min")
    print()
    graphs.append(capitalGraph)
    graphs.append(frGraph)
    return graphs

# Classic and Modified Martingale
def betMartingale(roulette, typeof):
    capital = roulette.getInitCapital()
    betValue = initBetValue = 1
    capitalGraph = [capital]
    frGraph = []
    fr = 0
    graphs = []
    modified = ""
    while(modified != 'Y' and modified != 'N'):
        modified = str.upper(str(input('There are two types of Martingale. Classic and Modified. The default is Classic. Do you want to change to Modified? (Y/N) ')))

    myColor = ""
    while(myColor != 'red' and myColor != 'black'):
        myColor = str(input('Please choose a color: (red) or (black): '))

    for i in range(1, roulette.getGames()):
        if (typeof == "limited" and betValue>capital):
            graphs.append(capitalGraph)
            graphs.append(frGraph)
            return graphs
            
        capital -= betValue
        rand = np.random.randint(0, 37)
        color = roulette.getNumbers()[rand].color
        if(color == myColor):
            capital += betValue * 2
            fr += 1

        # Duplicate previous bet (modified: adds +1 units)
        if(myColor != color):
            if (modified == 'Y'):
                betValue = betValue * 2 + 1
            else:
                betValue = betValue * 2
        else:
            # Reinitialize betValue to 1
            betValue = initBetValue
        
        capitalGraph.append(capital)
        frGraph.append(fr/i)

    print('Final capital: ', capital)
    print("Your total play time would be about: " + str(roulette.getGames() * roulette.getBetTime() // 60) + " min")
    print()
    graphs.append(capitalGraph)
    graphs.append(frGraph)
    return graphs

# D'Alembert Strategy
def betDalembert(roulette, typeof):
    capital = roulette.getInitCapital()
    betValue = initBetValue = 1
    graph = [capital]

    myColor = ""
    while(myColor != 'red' and myColor != 'black'):
        myColor = str(input('Please choose a color: (red) or (black): '))

    for i in range(roulette.getGames()):
        capital -= betValue
        rand = np.random.randint(0, 37)
        color = roulette.getNumbers()[rand].color
        if(color == myColor):
            capital += betValue * 2
            if(betValue > 0):
                betValue -= 1
            else:
                betValue = 1
        else:
            betValue += 1
        graph.append(capital)
    print('Final capital: ', capital)
    print("Your total play time would be about: " + str(roulette.getGames() * roulette.getBetTime() // 60) + " min")
    print()
    return graph
