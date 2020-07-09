# -*- coding: utf-8 -*-

import numpy as np


# Exponential Random Numbers Generator
def exponential_generator(mean):
    random_uniform_num = np.random.uniform()
    return -mean * np.log(random_uniform_num)


# Expected Performance Measures
def get_expected_values(config):
    Lambda = config["arrival_rate"]
    Mu = config["service_rate"]

    if Lambda >= Mu:
        return {
            "Lambda": Lambda,
            "Mu": Mu,
            "Rho": 1,
            "Lq": None,
            "Wq": None,
            "L": None,
            "W": None,
            "Pn": None
        }

    Rho = Lambda / Mu  # Server utilization
    Lq = (Rho ** 2) / (1 - Rho)  # Average quantity of costumers in queue
    Wq = Lq / Lambda  # Average delay time in queue
    W = Wq + 1 / Mu  # Average delay time in the system
    L = Lambda * W  # Average quantity of costumers in the system
    Pn = [
        (1 - Rho) * (Rho ** n) for n in range(config["num_delays_required"])
    ]  # N Clients in queue probability array

    return {
        "Lambda": Lambda,
        "Mu": Mu,
        "Rho": Rho,
        "Lq": Lq,
        "Wq": Wq,
        "L": L,
        "W": W,
        "Pn": Pn
    }
