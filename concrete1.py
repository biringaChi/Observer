from PyQt6.QtWidgets import *
from observer import Observer
import pyqtgraph


class Concrete1(Observer):
    def __init__(self, subject):
        super().__init__(subject)

        # add gui code here, use self.subject for data

    def process_update(self):
        # add refresh code here, use self.subject for data
        pass
