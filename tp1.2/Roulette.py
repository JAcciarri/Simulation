import numpy as np
import random
from MyNumber import MyNumber

NUMBERS = []


def initializeRoulette():
    NUMBERS.append(MyNumber(0, 'green'))
    for i in range(0,5):
        NUMBERS.append(MyNumber( (i*2)+1, 'red'))
    for i in range(6,10):
        NUMBERS.append(MyNumber( i*2, 'red'))
    for i in range(9,14):
        NUMBERS.append(MyNumber( (i*2)+1, 'red'))
    for i in range(15,19):
        NUMBERS.append(MyNumber( (i*2), 'red'))

    for i in range(1,6):
        NUMBERS.append(MyNumber( (i*2), 'black'))
    for i in range(5,9):
        NUMBERS.append(MyNumber( (i*2)+1, 'black'))
    for i in range(14,18):
        NUMBERS.append(MyNumber( (i*2)+1, 'black'))
    for i in range(10,15):
        NUMBERS.append(MyNumber( (i*2), 'black'))

def betToNumber():
    games = int(input('How many games do you want to play? '))
    initCapital = capital = 1000
    betValue = 10
    graph = [initCapital]
    chosen = int(input('Choose your number: '))
    for i in range(games):
        capital -= betValue
        rand = np.random.randint(0, len(NUMBERS))
        if(rand==chosen):
            capital = capital + betValue * 36
        graph.append(capital)
    return graph

def betToColor():
    games = int(input('How many games do you want to play? '))
    initCapital = capital = 1000
    betValue = 10
    graph = [initCapital]
    myColor = str(input('Now choose a color: (red) or (black): '))
    while(myColor!='red' and myColor!='black'):
        myColor = str(input('Please choose a color: (red) or (black): '))

    for i in range(games):
        capital -= betValue
        rand = np.random.randint(0, 37)
        if(NUMBERS.__getitem__(rand).color == myColor):
            capital += (betValue * 2)
        graph.append(capital)
    return graph
    
def betAsSofovich():
    games = int(input('How many games do you want to play? '))
    initCapital = 100000000
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
            rand = np.random.randint(0, len(NUMBERS))
            if(rand!=notChosen_1 and rand!=notChosen_2):
                capital = capital + betValue * 36
            graph.append(capital)
    return graph
    
