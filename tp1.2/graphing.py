from matplotlib import pyplot as plt
import numpy as np

def letsGraph(graphsLim, graphsUnlim):
    #if min(graph) >= 0:
            #   plt.ylim(bottom=0, top=max(graph)*1.1)
            #else:
            #   plt.ylim(bottom=min(graph)*1.1, top=max(graph)*1.1)
    #fig = plt.gcf()
    #fig.canvas.set_window_title("Strategy Analysis")
    
    #plt.axhline(roulette.getInitCapital(), color='red', linestyle='--', label="Init Capital")
    
    plt.title("Strategy Analisis")

    plt.subplot(2,2,1)
    plt.plot(graphsUnlim[0], label="Capital")
    plt.legend(loc="upper right")
    plt.title('UNLIMITED CAPITAL')
    plt.ylabel('Capital')
    plt.xlabel('N(Bets)')
    
    plt.subplot(2,2,2)
    plt.plot(graphsLim[0], label="Capital")
    plt.legend(loc="upper right")
    plt.title('LIMITED CAPITAL')
    plt.ylabel('Capital')
    plt.xlabel('N(Bets)')
    
    plt.subplot(2,2,3)
    plt.bar(np.arange(len(graphsUnlim[1])), graphsUnlim[1], width = 0.5, label="RF")
    plt.legend(loc="upper right")
    plt.title('RELATIVE FREQUENCY (UNLIM)')
    plt.ylabel('RF')
    plt.xlabel('N(Bets)')

    plt.subplot(2,2,4)
    plt.bar(np.arange(len(graphsLim[1])), graphsLim[1], width = 0.7, label="RF")
    plt.legend(loc="upper right")
    plt.title('RELATIVE FREQUENCY (LIM)')
    plt.ylabel('RF')
    plt.xlabel('N(Bets)')

    plt.show()




