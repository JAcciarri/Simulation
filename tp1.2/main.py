from MyNumber import MyNumber
import Roulette as R
import numpy as np
from matplotlib import pyplot as plt


def opt1():
    graph = R.betToNumber()
    plt.title('Bet to a single number')
    plt.plot(graph)

def opt2():
    graph = R.betToColor()
    plt.title('Bet to a color')
    plt.plot(graph)
def opt3():
    graph = R.betAsSofovich()
    plt.title('Bet AS Sofovich')
    plt.plot(graph)

def switch(opt):
    switcher = {
        1: opt1,
        2: opt2,
        3: opt3,
    }
    return switcher.get(opt)()



#MAIN   
R.initializeRoulette()
print('Welcome. Choose your strategy:')
strat = int(input('1: Bet to a single number\n2: Bet to a color\n3: Bet AS Sofovich\n' ))
while(strat!=1 and strat!=2 and strat!=3):
    strat = int(input('Please choose a strategy (1 or 2 or 3)\n1: Bet to a single number\n2: Bet to a color\n3: Bet AS Sofovich\n'))

switch(strat)

plt.ylabel('Capital')
plt.xlabel('N (bets)')
plt.show()
