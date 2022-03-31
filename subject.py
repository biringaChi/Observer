"""
Team SCAG Observer Pattern Implementation
subject.py - our subject to be watched by our observers
"""

from PyQt6.QtWidgets import *
import numpy as np


class Subject(QWidget):
    def __init__(self):
        super().__init__()
        self.observers = []
        self.data = np.array([[1, 2, 3, 4, 5], [0, 0, 0, 0, 0]])

        # add gui code here, make sure something calls notify_observers() (like a button)

    def add_observer(self, o):
        self.observers.append(o)

    def remove_observer(self, o):
        self.observers.remove(o)

    def notify_observers(self):
        for o in self.observers:
            o.update_subject()

    def get_state(self):
        return self.data
