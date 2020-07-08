import numpy as np


# Exponential Random Numbers Generator
def exponential_generator(mean):
    random_uniform_num = np.random.uniform()
    return -mean * np.log(random_uniform_num)


def get_expected_values(config):
    lmbda = 1 / config["mean_interarrival"]
    mu = 1 / config["mean_service"]

    Phi = lmbda / mu
    Lq = (Phi ** 2) / (1 - Phi)
    Wq = Lq / lmbda

    return {
        "Phi": Phi,
        "Wq": Wq,
        "Lq": Lq,
    }
