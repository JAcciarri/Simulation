# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import seaborn as sns


# Save any Plot (Not Implemented yet)
def save_plot(route, name):
    try:
        plt.savefig(route + name + ".png")
        print(name + " has been saved successfully")
    except:
        print(name + " has NOT been saved because a problem ocurred")

# TO-DO...
