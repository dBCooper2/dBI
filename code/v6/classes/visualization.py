import pandas as pd
import matplotlib.pyplot as plt
from dataclasses import dataclass

# TODO
@dataclass
class PieChart:
    data: list
    labels: list
    pass
    
    def output_plot(self):
        plt.style.use('Solarize_Light2')
        plt.pie(self.data, labels=self.labels)
        plt.show()

# TODO
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