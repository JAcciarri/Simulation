# -*- coding: utf-8 -*-

import numpy as np


# Only Number
def betToNumber(roulette):
    capital = roulette.getInitCapital()
    betValue = roulette.getBetValue()
    fr = 0
    zeroCapital = False
    graphsLimited = {"capital": [capital], "frec": []}
    graphsUnlimited = {"capital": [capital], "frec": []}
    chosen = int(float(input('Choose your number:')))
    for i in range(1, roulette.getGames()):
        capital -= betValue
        rand = np.random.randint(0, len(roulette.getNumbers()))
        if(rand == chosen):
            capital += betValue * 36
            fr += 1

        graphsUnlimited["capital"].append(capital)
        graphsUnlimited["frec"].append(fr/i)

        if (capital <= 0):
            zeroCapital = True
        
        if (zeroCapital):
            graphsLimited["capital"].append(0)
            graphsLimited["frec"].append(0)
        else:
            graphsLimited["capital"].append(capital)
            graphsLimited["frec"].append(fr/i)

    print('Final capital: ', capital)
    print("Your total play time would be about: " + str(roulette.getGames() * roulette.getBetTime() // 60) + " min")
    print()

    # Array conversion
    graphsLimited["capital"] = np.array(graphsLimited["capital"])
    graphsUnlimited["capital"] = np.array(graphsUnlimited["capital"])
    graphsLimited["frec"] = np.array(graphsLimited["frec"])
    graphsUnlimited["frec"] = np.array(graphsUnlimited["frec"])

    return graphsLimited, graphsUnlimited

# Only Color
def betToColor(roulette):
    capital = roulette.getInitCapital()
    betValue = roulette.getBetValue()
    fr = 0
    zeroCapital = False
    graphsLimited = {"capital": [capital], "frec": []}
    graphsUnlimited = {"capital": [capital], "frec": []}
    myColor = ""
    while(myColor != 'red' and myColor != 'black'):
        myColor = str(input('Please choose a color: (red) or (black): '))

    for i in range(1, roulette.getGames()):
        capital -= betValue
        rand = np.random.randint(0, 37)
        if(roulette.getNumbers()[rand].color == myColor):
            capital += betValue * 2
            fr += 1

        graphsUnlimited["capital"].append(capital)
        graphsUnlimited["frec"].append(fr/i)

        if (capital <= 0):
            graphsLimited["capital"].append(0)
            graphsLimited["frec"].append(0)
        else:
            graphsLimited["capital"].append(capital)
            graphsLimited["frec"].append(fr/i)

    print('Final capital: ', capital)
    print("Your total play time would be about: " + str(roulette.getGames() * roulette.getBetTime() // 60) + " min")
    print()

    # Array conversion
    graphsLimited["capital"] = np.array(graphsLimited["capital"])
    graphsUnlimited["capital"] = np.array(graphsUnlimited["capital"])
    graphsLimited["frec"] = np.array(graphsLimited["frec"])
    graphsUnlimited["frec"] = np.array(graphsUnlimited["frec"])

    return graphsLimited, graphsUnlimited

# Gerardo Sofovich's Strategy
def betAsSofovich(roulette):
    capital = 100000
    betValue = roulette.getBetValue()
    fr = 0
    zeroCapital = False
    graphsLimited = {"capital": [capital], "frec": []}
    graphsUnlimited = {"capital": [capital], "frec": []}
    notChosen_1 = int(float(input('Choose your NOT chosen number 1: ')))
    notChosen_2 = int(float(input('Choose your NOT chosen number 2: ')))
    
    for i in range(1, roulette.getGames()):
        capital -= (betValue * 35)
        rand = np.random.randint(0, len(roulette.getNumbers()))
        
        if(rand != notChosen_1 and rand != notChosen_2):
            capital += betValue * 36
            fr += 1
        
        graphsUnlimited["capital"].append(capital)
        graphsUnlimited["frec"].append(fr/i)

        if (capital <= 0):
            zeroCapital = True
        
        if (zeroCapital):
            graphsLimited["capital"].append(0)
            graphsLimited["frec"].append(0)
        else:
            graphsLimited["capital"].append(capital)
            graphsLimited["frec"].append(fr/i)

    print('Final capital: ', capital)
    print("Your total play time would be about: " + str(roulette.getGames() * roulette.getBetTime() // 60) + " min")
    print()
    
    # Array conversion
    graphsLimited["capital"] = np.array(graphsLimited["capital"])
    graphsUnlimited["capital"] = np.array(graphsUnlimited["capital"])
    graphsLimited["frec"] = np.array(graphsLimited["frec"])
    graphsUnlimited["frec"] = np.array(graphsUnlimited["frec"])

    return graphsLimited, graphsUnlimited

# Classic and Modified Martingale
def betMartingale(roulette):
    capital = roulette.getInitCapital()
    betValue = roulette.getBetValue()
    fr = 0
    zeroCapital = False
    graphsLimited = {"capital": [capital], "frec": []}
    graphsUnlimited = {"capital": [capital], "frec": []}
    modified = ""
    while(modified != 'Y' and modified != 'N'):
        modified = str.upper(str(input('There are two types of Martingale. Classic and Modified. The default is Classic. Do you want to change to Modified? (Y/N) ')))

    myColor = ""
    while(myColor != 'red' and myColor != 'black'):
        myColor = str(input('Please choose a color: (red) or (black): '))

    for i in range(1, roulette.getGames()):   
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
            betValue = roulette.getBetValue()
        
        graphsUnlimited["capital"].append(capital)
        graphsUnlimited["frec"].append(fr/i)

        if (capital <= 0):
            zeroCapital = True

        if (zeroCapital):
            graphsLimited["capital"].append(0)
            graphsLimited["frec"].append(0)
        else:
            graphsLimited["capital"].append(capital)
            graphsLimited["frec"].append(fr/i)

    print('Final capital: ', capital)
    print("Your total play time would be about: " + str(roulette.getGames() * roulette.getBetTime() // 60) + " min")
    print()
    
    # Array conversion
    graphsLimited["capital"] = np.array(graphsLimited["capital"])
    graphsUnlimited["capital"] = np.array(graphsUnlimited["capital"])
    graphsLimited["frec"] = np.array(graphsLimited["frec"])
    graphsUnlimited["frec"] = np.array(graphsUnlimited["frec"])

    return graphsLimited, graphsUnlimited

# D'Alembert Strategy
def betDalembert(roulette):
    capital = roulette.getInitCapital()
    betValue = roulette.getBetValue()
    fr = 0
    graphsLimited = {"capital": [capital], "frec": []}
    graphsUnlimited = {"capital": [capital], "frec": []}

    myColor = ""
    while(myColor != 'red' and myColor != 'black'):
        myColor = str(input('Please choose a color: (red) or (black): '))

    for i in range(1, roulette.getGames()):
        capital -= betValue
        rand = np.random.randint(0, 37)
        color = roulette.getNumbers()[rand].color
        if(color == myColor):
            capital += betValue * 2
            fr += 1
            if(betValue > 0):
                betValue -= 1
            else:
                betValue = 1
        else:
            betValue += 1
        
        graphsUnlimited["capital"].append(capital)
        graphsUnlimited["frec"].append(fr/i)

        if (capital <= 0):
            zeroCapital = True
        
        if (zeroCapital):
            graphsLimited["capital"].append(0)
            graphsLimited["frec"].append(0)
        else:
            graphsLimited["capital"].append(capital)
            graphsLimited["frec"].append(fr/i)

    print('Final capital: ', capital)
    print("Your total play time would be about: " + str(roulette.getGames() * roulette.getBetTime() // 60) + " min")
    print()
    
    # Array conversion
    graphsLimited["capital"] = np.array(graphsLimited["capital"])
    graphsUnlimited["capital"] = np.array(graphsUnlimited["capital"])
    graphsLimited["frec"] = np.array(graphsLimited["frec"])
    graphsUnlimited["frec"] = np.array(graphsUnlimited["frec"])

    return graphsLimited, graphsUnlimited
