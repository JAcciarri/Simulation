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

def cdf_plots(x, analytic, simulated):
    fig, axs = plt.subplots(2,1)
    fig.canvas.set_window_title("CDFs")
    axs[0].plot(x, analytic)
    axs[1].plot(x, simulated, 'ro')
    plt.show()
    # UNDER CONSTRUCTION...

# TO-DO...
