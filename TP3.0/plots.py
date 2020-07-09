# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt


# Save any plot
def save_plot(route, name):
    try:
        plt.savefig(route + name + ".png")
        print(name + " has been saved successfully")
    except:
        print(name + " has NOT been saved because a problem ocurred")


# Plot every individual graph
def plot_one(measures_from_multiple_runs, expected_value, title, x_label, y_label, save, name):
    fig = plt.figure()
    fig.canvas.set_window_title(title)
    plt.title(title)
    for measures in measures_from_multiple_runs:
        x, y = zip(*measures.items())
        plt.plot(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    if expected_value is not None:
        plt.axhline(expected_value, color="red", linestyle="--", label="expected value")
        plt.legend()

    plt.tight_layout()
    plt.margins(0.02)
    plt.grid()

    if save["mode"]:
        route = save["route"]
        file_name = "graph_" + str(save["runs"]) + "runs_" + str(save["delays"]) + "delays_"
        file_name += "config" + str(save["config"]) + "_" + name
        save_plot(route, file_name)


# Specification of all the graphs to plot
def plot_results(results, expected, save):
    # Average quantity of costumers in queue
    plot_one(
        [result["avg_num_in_queue"] for result in results],
        expected_value=expected["Lq"],
        title="Average quantity of costumers in queue",
        x_label="Time",
        y_label="q(n)",
        save=save,
        name="avg_num_in_queue",
    )

    # Average delay time in queue
    plot_one(
        [result["avg_delay_in_queue"] for result in results],
        expected_value=expected["Wq"],
        title="Average delay time in queue",
        x_label="Customer number",
        y_label="d(n)",
        save=save,
        name="avg_delay_time_in_queue",
    )

    # Average quantity of costumers in the system
    plot_one(
        [result["avg_num_in_system"] for result in results],
        expected_value=expected["L"],
        title="Average quantity of costumers in the system",
        x_label="Time",
        y_label="Q(n)",
        save=save,
        name="avg_num_in_the_system",
    )

    # Average delay time in the system
    plot_one(
        [result["avg_delay_in_system"] for result in results],
        expected_value=expected["W"],
        title="Average delay time in the system",
        x_label="Customer number",
        y_label="D(n)",
        save=save,
        name="avg_delay_time_in_the_system",
    )

    # Server utilization
    plot_one(
        [result["server_utilization"] for result in results],
        expected_value=expected["Rho"],
        title="Server utilization",
        x_label="Time",
        y_label="U(n)",
        save=save,
        name="server_utilization",
    )

    # Show all the plots
    plt.show()
