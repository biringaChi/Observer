from PyQt6.QtWidgets import *
from observer import Observer
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pyqtgraph


class Concrete1(Observer):
    def __init__(self, subject):
        super().__init__(subject)

        # add gui code here, use self.subject for data
    
    def scatter_plot(self, data):
        sns.scatterplot(x = data[0], y = data[1])

    def process_update(self):
        # add refresh code here, use self.subject for data
        return self.scatter_plot(self.subject)