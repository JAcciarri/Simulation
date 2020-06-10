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

# Plot for a comparative between Analytic and Simulated CDFs
def cdf_plots(x, y, sim_x, sim_y):
    fig = plt.figure()
    plt.plot(x, y, 'b-', label="Analytic CDF")
    plt.plot(sim_x, sim_y, 'r.', label="Simulated CDF") 
    fig.canvas.set_window_title("Analytic vs Simulated CDFs")
    plt.grid()
    plt.legend()
    # plt.save...

def graphing_show_all():
    plt.show()
