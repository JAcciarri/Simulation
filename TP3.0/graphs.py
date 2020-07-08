import matplotlib.pyplot as plt


def plot_sector(
    fig, measures_from_multiple_runs, expected_value, title, x_label, y_label, position
):
    ax = fig.add_subplot(2, 2, position)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    for measures in measures_from_multiple_runs:
        x, y = zip(*measures.items())
        ax.plot(x, y)
    ax.axhline(expected_value, color="red", linestyle="--")


def line_plot_stats(results, expected):
    fig = plt.figure()

    plot_sector(
        fig,
        [result["avg_num_in_queue"] for result in results],
        expected_value=expected["Lq"],
        title="Numero promedio de clientes en cola",
        x_label="Tiempo",
        y_label="Q(n)",
        position=1,
    )
    plot_sector(
        fig,
        [result["server_utilization"] for result in results],
        expected_value=expected["Phi"],
        title="Utilización del servidor",
        x_label="Tiempo",
        y_label="U(n)",
        position=2,
    )
    plot_sector(
        fig,
        [result["avg_delay_in_queue"] for result in results],
        expected_value=expected["Wq"],
        title="Demora promedio en cola",
        x_label="Numero de cliente",
        y_label="D(n)",
        position=3,
    )
    plt.show()
