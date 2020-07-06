# Some info...
def update_time_avg_stats(model):
    time_since_last_event = model["time"] - model["time_last_event"]
    model["time_last_event"] = model["time"]

    model["area_num_in_queue"] += time_since_last_event * model["num_in_queue"]
    model["area_server_status"] += time_since_last_event * int(model["server_busy"])
