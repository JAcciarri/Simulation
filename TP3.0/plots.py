# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

# Save any Plot
def save_plot(route, name):
    try:
        plt.savefig(route + name + ".png")
        print(name + " has been saved successfully")
    except:
        print(name + " has NOT been saved because a problem ocurred")


def plot_sector(measures_from_multiple_runs, expected_value, title, x_label, y_label, save, name):
    fig = plt.figure()
    fig.canvas.set_window_title(title)
    plt.title(title)
    for measures in measures_from_multiple_runs:
        x, y = zip(*measures.items())
        plt.plot(x, y)
    if expected_value is not None:
        plt.axhline(expected_value, color="red", linestyle="--", label="expected value")
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.tight_layout()
    plt.margins(0.02)
    plt.grid()
    plt.legend()

    if save["mode"]:
        route = save["route"]
        name = "graph_" + str(save["total"]) + "runs_" + name
        save_plot(route, name)


def line_plot_stats(results, expected, save):
    plot_sector(
        [result["avg_num_in_queue"] for result in results],
        expected_value=expected["Lq"],
        title="Average customers' quantity in queue",
        x_label="Time",
        y_label="Q(n)",
        save=save,
        name="avg_num_in_queue",
    )
    plot_sector(
        [result["server_utilization"] for result in results],
        expected_value=expected["Phi"],
        title="Server utilization",
        x_label="Time",
        y_label="U(n)",
        save=save,
        name="server_utilization",
    )
    plot_sector(
        [result["avg_delay_in_queue"] for result in results],
        expected_value=expected["Wq"],
        title="Average Delay in queue",
        x_label="Customer number",
        y_label="D(n)",
        save=save,
        name="avg_delay_in_queue",
    )
    plt.show()
