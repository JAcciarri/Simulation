# -*- coding: utf-8 -*-

from processes import (
    event_report,
    initialize,
    timing,
    update_time_stats,
    arrive,
    depart,
    final_report,
)
from operator import itemgetter


def run_queue_simulation(config, first):
    # Initialize Run
    model, results_time = itemgetter("model", "results_time")(initialize(config))
    if first:
        # Run Information
        print("Single-server queuing system (M/M/1)")
        print("Mean interarrival time:", round(model["mean_interarrival"], 6), "minutes")
        print("Mean service time:", round(model["mean_service"], 6), "minutes")
        print("Number of customers:", round(model["num_delays_required"], 6), "\n")

    # Run the simulation while more delays are still needed
    while model["num_customers_delayed"] < model["num_delays_required"]:
        # Determine the next event
        next_event_type, model["time"] = timing(model["event_list"])
        # Update time-average statistical accumulators
        update_time_stats(model)
        # Invoke the appropriate event function
        if next_event_type == "arrival":
            arrive(model)
        elif next_event_type == "departure":
            depart(model)
        # Invoke the partial report generator
        event_report(results_time, model)
    # Invoke the final report generator and end the current run
    return final_report(results_time, model)


# Comparison between analytic and simulation results' values
def values_comparison(results, expected):
    print("\nRESULTS")
    print("\nModel Parameters")
    print("λ  (Arrival rate):", expected["Lambda"])
    print("μ  (Service rate):", expected["Mu"])

    print("\nAnalytic Performance Measures")
    print("ρ  (Server utilization):", expected["Rho"])
    print("Lq (Average quantity of costumers in queue):", expected["Lq"])
    print("Wq (Average delay time in queue):", expected["Wq"])
    print("L  (Average quantity of costumers in the system):", expected["L"])
    print("W  (Average delay time in the system):", expected["W"])
    print("Pn (N customers in queue probability), (0 ≤ N < 20):")
    print(expected["Pn"][:20])

    print("\nSimulation Performance Measures")
    print("ρ (server utilization):", "[Under Construction]")
    print()
