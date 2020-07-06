from Utils.exponential import exponential

# Model Initialization
def initialize(model):
    model["mean_interarrival"] = 1.0
    model["mean_service"] = 0.5
    model["num_delays_required"] = 1000
    model["server_busy"] = False
    model["time"] = 0.0  # Simulation Clock
    # num_in_queue = 0
    # time_last_event = 0.0
    # next_event_type = -1
    # --Statistical Counters--
    # num_customers_delayed = 0
    # total_of_delays = 0.0
    # area_num_in_queue = 0.0
    # area_server_status = 0.0
    # --Initialize event list--
    model["event_list"]["arrival"] = model["time"] + exponential(
        model["mean_interarrival"]
    )
    model["event_list"]["departure"] = float("inf")
