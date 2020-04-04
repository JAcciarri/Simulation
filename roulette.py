from random import randint, seed
import matplotlib.pyplot as plt
import numpy as np

MY_NUMBER = int(input('Choose your roulette number(0-36): '))
while(MY_NUMBER<0 or MY_NUMBER>36):
    myNumber = int(input('Choose your roulette number (0-36): '))
#Set a convenient value for N (ITERATIONS)
ITERATIONS = abs(int(input('How many iterations do you want?: ')))

fr_array = []
mean_array = []
std_array = []
var_array = []
values = []
base_array = np.arange(37)
#general_mean_array = [18]

for _ in range(5):
    count = 0
    fr_array.clear()
    mean_array.clear()
    std_array.clear()
    var_array.clear()
    values.clear()

    for n in range(ITERATIONS):
        rand = randint(0, 36)
        values.append(rand)
        if (rand == MY_NUMBER):
            count+=1
        fr_array.append(count / (n+1))
        mean_array.append(np.mean(values))
        std_array.append(np.std(values))
        var_array.append(np.var(values))
        """
        tempvalue = general_mean_array[n]
        print('Taken ', str(general_mean_array[n]))
        general_mean_array.pop(n)
        general_mean_array.append(np.mean( [mean_array[n], tempvalue] ))
        print(general_mean_array)
        """

    plt.subplot(2, 2, 1)
    plt.ylim(0, 0.15)
    plt.plot(fr_array)

    plt.subplot(2, 2, 2)
    plt.plot(mean_array)

    plt.subplot(2, 2, 3)
    plt.plot(var_array)

    plt.subplot(2, 2, 4)
    plt.plot(std_array)

plt.title('Roulette Simulator')

plt.subplot(2, 2, 1)
plt.plot([0,ITERATIONS], [1/len(base_array), 1/len(base_array)], label="Expected RF")
plt.legend(loc="lower right")
plt.title('Relative Frequency')
plt.ylabel('RF for number ' + str(MY_NUMBER))
plt.xlabel('N(iteration)')

plt.subplot(2, 2, 2)
plt.plot([0,ITERATIONS], [np.mean(base_array), np.mean(base_array)], label="Expected MV")
plt.legend(loc="lower right")
plt.title('Mean Value')
plt.ylabel('MV')
plt.xlabel('N(iteration)')

plt.subplot(2, 2, 3)
plt.plot([0,ITERATIONS], [np.var(base_array), np.var(base_array)], label="Expected V")
plt.legend(loc="lower right")
plt.title('Variance')
plt.ylabel('V')
plt.xlabel('N(iteration)')

plt.subplot(2, 2, 4)
plt.plot([0,ITERATIONS], [np.std(base_array), np.std(base_array)], label="Expected STD")
plt.legend(loc="lower right")
plt.ylabel('STD')
plt.xlabel('N(iteration)')
plt.title('Standard Deviation')

plt.show()
