# -*- coding: utf-8 -*-

import numpy as np
from queue import Queue


# Exponential Random Numbers Generator
def exponential_generator(mean):
    random_uniform_num = np.random.uniform()
    return -mean * np.log(random_uniform_num)


# Model Initialization
def initialize(config):
    return {
        # Initial parameters
        "mean_interarrival": config["mean_interarrival"],
        "mean_service": config["mean_service"],
        "num_delays_required": config["num_delays_required"],
        # Statistical counters
        "num_customers_delayed": 0,
        "area_num_in_queue": 0.0,
        "area_server_status": 0.0,
        "total_of_delays": 0.0,
        "num_in_queue": 0,
        "server_busy": False,
        "time": 0.0,  # Simulation Clock
        "time_arrival_queue": Queue(maxsize=0),
        "time_last_event": 0.0,
        "event_list": {
            "arrival": exponential_generator(config["mean_interarrival"]),
            "departure": float("inf"),
        },
    }


# Determination of the next event's type and time
def timing(event_list):
    next_event_type = min(event_list, key=event_list.get)
    next_event_time = event_list[next_event_type]

    return (next_event_type, next_event_time)


# Update time-average statistical accumulators
def update_time_stats(model):
    time_since_last_event = model["time"] - model["time_last_event"]
    model["time_last_event"] = model["time"]

    model["area_num_in_queue"] += time_since_last_event * model["num_in_queue"]
    model["area_server_status"] += time_since_last_event * int(model["server_busy"])


# Arrival Event
def arrive(model):
    model["event_list"]["arrival"] = model["time"] + exponential_generator(
        model["mean_interarrival"]
    )
    if model["server_busy"]:
        model["num_in_queue"] += 1
        model["time_arrival_queue"].put(model["time"])
        print(model["time_arrival_queue"].qsize(), end=", ")
    else:
        model["num_customers_delayed"] += 1
        model["server_busy"] = True
        model["event_list"]["departure"] = model["time"] + exponential_generator(
            model["mean_service"]
        )


# Departure Event
def depart(model):
    if model["num_in_queue"] == 0:
        model["server_busy"] = False
        model["event_list"]["departure"] = float("inf")
    else:
        model["num_in_queue"] -= 1
        delay = model["time"] - model["time_arrival_queue"].get()
        model["total_of_delays"] += delay
        model["num_customers_delayed"] += 1
        model["event_list"]["departure"] = model["time"] + exponential_generator(
            model["mean_service"]
        )


# Report Generator
def report(model):
    result = {
        "avg_delay_in_queue": model["total_of_delays"] / model["num_customers_delayed"],
        "avg_num_in_queue": model["area_num_in_queue"] / model["time"],
        "server_utilization": model["area_server_status"] / model["time"],
        "total_time": model["time"],
    }
    print(f"\n\nFinal Report:")
    print(f'Average delay in queue: {result["avg_delay_in_queue"]}')
    print(f'Average number of clients in queue: {result["avg_num_in_queue"]}')
    print(f'Server utilization: {result["server_utilization"]}')
    print(f'Time simulation ended: {result["total_time"]}')
    print()
    return result
