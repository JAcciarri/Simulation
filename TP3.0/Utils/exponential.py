import numpy as np

# Some info...
def exponential(mean):
    random_uniform_num = np.random.uniform()
    return -mean * np.log(random_uniform_num)