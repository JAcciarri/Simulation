# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

# Save any Plot
def save_plot(route, name):
    try:
        plt.savefig(route + name + ".png")
        print(name + " has been saved successfully")
    except:
        print(name + " has NOT been saved because a problem ocurred")


def plot_sector(fig, measures_from_multiple_runs, expected_value, title, x_label, y_label, position, save, name):
    ax = fig.add_subplot(2, 2, position)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    for measures in measures_from_multiple_runs:
        x, y = zip(*measures.items())
        ax.plot(x, y)
    if expected_value is not None:
        ax.axhline(expected_value, color="red", linestyle="--")

    if save["mode"]:
        route = save["route"]
        name = "graph_" + str(save["total"]) + "runs_" + name
        save_plot(route, name)


def line_plot_stats(results, expected, save):
    fig = plt.figure()

    plot_sector(
        fig,
        [result["avg_num_in_queue"] for result in results],
        expected_value=expected["Lq"],
        title="Numero promedio de clientes en cola",
        x_label="Tiempo",
        y_label="Q(n)",
        position=1,
        save=save,
        name="avg_num_in_queue",
    )
    plot_sector(
        fig,
        [result["server_utilization"] for result in results],
        expected_value=expected["Phi"],
        title="Utilización del servidor",
        x_label="Tiempo",
        y_label="U(n)",
        position=2,
        save=save,
        name="server_utilization",
    )
    plot_sector(
        fig,
        [result["avg_delay_in_queue"] for result in results],
        expected_value=expected["Wq"],
        title="Demora promedio en cola",
        x_label="Numero de cliente",
        y_label="D(n)",
        position=3,
        save=save,
        name="avg_delay_in_queue",
    )
    plt.show()
