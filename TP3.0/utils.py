# -*- coding: utf-8 -*-

import numpy as np


# Exponential Random Numbers Generator
def exponential_generator(mean):
    random_uniform_num = np.random.uniform()
    return -mean * np.log(random_uniform_num)


# Expected Performance Measures
def get_expected_values(config):
    lmbda = config["arrival_rate"]
    mu = config["service_rate"]

    if lmbda >= mu:
        return {"Rho": 1, "Lq": None, "Wq": None, "L": None, "W": None, "Pn": None}

    Rho = lmbda / mu  # Server utilization
    Lq = (Rho ** 2) / (1 - Rho)  # Average customers' quantity in queue
    Wq = Lq / lmbda  # Average delay time in queue
    W = Wq + 1 / mu  # Average delay time in the system
    L = lmbda * W  # Average customers' quantity in the system
    Pn = [
        (1 - Rho) * (Rho ** n) for n in range(config["num_delays_required"])
    ]  # N Clients in queue probability array

    return {"Rho": Rho, "Lq": Lq, "Wq": Wq, "L": L, "W": W, "Pn": Pn}
