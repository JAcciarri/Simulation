from Utils.exponential import exponential

# Some info...
def arrive(model):
    model["event_list"]["arrival"] = model["time"] + exponential(
        model["mean_interarrival"]
    )
    if model["server_busy"]:
        model["num_in_queue"] += 1
        model["time_arrival_queue"].put(model["time"])
        print(model["time_arrival_queue"].qsize())
    else:
        model["num_customers_delayed"] += 1
        model["server_busy"] = True
        model["event_list"]["departure"] = model["time"] + exponential(
            model["mean_service"]
        )
