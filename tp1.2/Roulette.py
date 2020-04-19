#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import random
import strategies as strats
from RouletteNumber import RouletteNumber


class Roulette(object):

    # Constructor and Instance Attributes
    def __init__(self):
        self.numbers = np.zeros(37, dtype=RouletteNumber)

        # Roulette's Numbers Initialization
        self.numbers[0] = RouletteNumber(0, 'green')
        for i in range(1, len(self.numbers), 2):
            if (i <= 10):
                self.numbers[i] = RouletteNumber(i, 'red')
                self.numbers[i+1] = RouletteNumber(i+1, 'black')
            elif (i <= 18):
                self.numbers[i] = RouletteNumber(i, 'black')
                self.numbers[i+1] = RouletteNumber(i+1, 'red')
            elif (i <= 28):
                self.numbers[i] = RouletteNumber(i, 'red')
                self.numbers[i+1] = RouletteNumber(i+1, 'black')
            else:
                self.numbers[i] = RouletteNumber(i, 'black')
                self.numbers[i+1] = RouletteNumber(i+1, 'red')

    # Strategy Settings
    def strategy(self, choise):
        games = int(input('How many games do you want to play? '))
        capital = 10000
        if (choise == 'number'):
            return strats.betToNumber(self.numbers, games, capital)
        elif (choise == 'color'):
            return strats.betToColor(self.numbers, games, capital)
        else:
            return strats.betAsSofovich(self.numbers, games, capital)
        
    # Getters and Setters
    def getNumbers(self):
        return self.numbers

    def setNumbers(self, numbers):
        self.numbers = numbers
