# Some info...
def report(model):
    print(f'\n Average delay in queue: {model["total_of_delays"] / model["num_customers_delayed"]}')
    print(f'\n Average number of clients in queue: {model["area_num_in_queue"] / model["time"]}')
    print(f'\n Server utilization: {model["area_server_status"] / model["time"]}')
    print(f'\n Time simulation ended: {model["time"]}')

