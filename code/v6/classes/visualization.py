import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
from dataclasses import dataclass


# TODO: Implement Saving to File & Style Features
class PieChart:
    def __init__(self, data: list, labels: list, style: str):
        self.data = data
        self.labels = labels
        self.style = style
        self.set_style()

    def set_style(self):
        plt.style.use(self.style)

    def output_plot(self):
        plt.pie(self.data, labels=self.labels)
        plt.show()

# TODO: REDO WITH MPLFINANCE
@dataclass
class LineGraph:
    xlabel: str
    ylabel: str
    title: str
    xdata: list
    ydata: list

    def output_plot(self):
        plt.style.use('Solarize_Light2')
        plt.plot(self.xdata, self.ydata)
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.show()

# TODO
@dataclass
class Histogram:
    pass

# TODO
@dataclass
class ScatterPlot:
    pass