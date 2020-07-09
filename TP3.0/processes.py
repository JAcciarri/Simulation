# -*- coding: utf-8 -*-

from utils import exponential_generator
from queue import Queue


# Model Initialization
def initialize(config):
    return {
        "model": {
            # Config parameters
            "mean_interarrival": 1 / config["arrival_rate"],
            "mean_service": 1 / config["service_rate"],
            "num_delays_required": config["num_delays_required"],
            # Simulation clock
            "time": 0.0,
            # Queue
            "time_arrival_queue": Queue(maxsize=0),
            # Statistical counters
            "num_customers_delayed": 0,
            "area_num_in_queue": 0.0,
            "area_num_in_system": 0.0,
            "area_server_status": 0.0,
            "total_of_delays": 0.0,
            # State variables
            "num_in_queue": 0,
            "server_busy": False,
            "time_last_event": 0.0,
            # Event list
            "event_list": {
                "arrival": exponential_generator(1 / config["arrival_rate"]),
                "departure": float("inf")
            },
        },
        "results_time": {
            "avg_delay_in_queue":   {},
            "avg_num_in_queue":     {},
            "avg_delay_in_system":  {},
            "avg_num_in_system":    {},
            "server_utilization":   {},
            "total_time": 0
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
    model["area_num_in_queue"] += time_since_last_event * model["num_in_queue"]
    model["area_num_in_system"] += (time_since_last_event * model["num_in_queue"] + int(model["server_busy"]))
    model["area_server_status"] += time_since_last_event * int(model["server_busy"])
    model["time_last_event"] = model["time"]


# Arrival Event
def arrive(model):
    model["event_list"]["arrival"] = model["time"] + exponential_generator(model["mean_interarrival"])
    if model["server_busy"]:
        model["num_in_queue"] += 1
        model["time_arrival_queue"].put(model["time"])
    else:
        model["num_customers_delayed"] += 1
        model["server_busy"] = True
        model["event_list"]["departure"] = model["time"] + exponential_generator(model["mean_service"])


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
        model["event_list"]["departure"] = model["time"] + exponential_generator(model["mean_service"])


# Report Generator
def report(results_time, model):
    # Average time in queue
    results_time["avg_delay_in_queue"][model["num_customers_delayed"]] = (
        model["total_of_delays"] / model["num_customers_delayed"]
    )
    # Average quantity of costumers in queue
    results_time["avg_num_in_queue"][model["time"]] = model["area_num_in_queue"] / model["time"] 

    # Average time in the system
    results_time["avg_delay_in_system"][model["num_customers_delayed"]] = (
        (model["total_of_delays"] / model["num_customers_delayed"]) + (model["mean_interarrival"])
    )

    # Average Average quantity of costumers in the system
    results_time["avg_num_in_system"][model["time"]] = model["area_num_in_system"] / model["time"]

    # Server utilization
    results_time["server_utilization"][model["time"]] = model["area_server_status"] / model["time"]

    # Total time
    results_time["total_time"] = model["time"]
