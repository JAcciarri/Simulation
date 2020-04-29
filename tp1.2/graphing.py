# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import numpy as np

def letsGraph(graphsLim, graphsUnlim, initCapital, title):
    
    # First Graph Settings
    fig, axs = plt.subplots(2,2)
    fig.canvas.set_window_title(title)
    
    # Subplot Settings
    axs[0, 0].plot(graphsUnlim["capital"], label="Capital")
    axs[0, 0].set_title('UNLIMITED CAPITAL')
    axs[0, 0].axhline(initCapital, color='red', linestyle='--', label="Init Capital")
    plt.setp(axs[0, 0], ylabel="Capital")
    
    axs[0, 1].plot(graphsLim["capital"], label="Capital")
    axs[0, 1].set_title('LIMITED CAPITAL')
    axs[0, 1].axhline(initCapital, color='red', linestyle='--', label="Init Capital")
    plt.setp(axs[0, 1], ylabel="Capital")
    
    axs[1, 0].bar(np.arange(len(graphsUnlim["frec"])), graphsUnlim["frec"], width = 0.5, label="RF")
    axs[1, 0].set_title('RELATIVE FREQUENCY (UNLIM)')
    plt.setp(axs[1, 0], ylabel="RF")
    
    axs[1, 1].bar(np.arange(len(graphsLim["frec"])), graphsLim["frec"], width = 0.7, label="RF")
    axs[1, 1].set_title('RELATIVE FREQUENCY (LIM)')
    plt.setp(axs[1, 1], ylabel="RF")
    
    # Vertical Axis Limits
    if (min(graphsLim["capital"]) < 0 or min(graphsUnlim["capital"]) < 0):
        axs[0, 0].set_ylim(bottom=min(graphsUnlim["capital"])*1.1, top=max(graphsUnlim["capital"])*1.1)
        axs[0, 1].set_ylim(bottom=min(graphsLim["capital"])*1.1, top=max(graphsLim["capital"])*1.1)
    else:
        axs[0, 0].set_ylim(bottom=0, top=max(graphsUnlim["capital"])*1.1)
        axs[0, 1].set_ylim(bottom=0, top=max(graphsLim["capital"])*1.1)

    # Graph Details
    for ax in fig.get_axes():
        ax.grid(True)
        ax.legend()
        plt.setp(ax, xlabel="Número de Tiradas")
    fig.tight_layout()
