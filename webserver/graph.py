import json
import matplotlib
import matplotlib.pyplot as plt
import mpld3

matplotlib.pyplot.switch_backend("Agg")


def make_graphs(parsed):
    """
    A method that produces Histograms used to compare execution time for different 8-tile puzzles using Matplotlib
    :param parsed:Dictionary obtained by parsing the JSON file produced as a result of the 8-puzzle solver
    :return: A set of HTML codes that represent the plot produced using Matplotlib thanks to the D3.JS library
    """
    html = dict()  # output set
    # for each puzzle
    for puzzle in parsed.keys():
        # figure initialization
        fig, ax = plt.subplots()

        # for each algorithm
        for algorithm in parsed[puzzle]["times"].keys():
            b = ax.bar(
                algorithm,
                parsed[puzzle]["times"][algorithm],
                label="{}:{}s".format(
                    algorithm, round(parsed[puzzle]["times"][algorithm], 10)
                ),
            )
        # due to a bug of mpld3 I'm not able to show the various algorithms on the x-axis, so I'm hiding the values
        ax.get_xaxis().set_ticklabels([])
        # shows the legend of the histogram
        ax.legend()
        ax.set_ylabel("Execution time in seconds")
        # generating the D3.JS code for the current figure
        html[puzzle] = mpld3.fig_to_html(plt.gcf())
        # closing the current figure in order to generate the next one
        plt.close(plt.gcf())
    return html
