"""
Team SCAG Observer Pattern Implementation
concrete3.py - implementation for the third concrete observer
"""

from PyQt6.QtWidgets import *
from observer import Observer
import pyqtgraph


class Swapcase(Observer, QWidget):
    def __init__(self, subject):
        super().__init__(subject)
        self.data = ""

        # gui elements
        self.setWindowTitle("Swapcase")

        layout = QGridLayout()
        self.setLayout(layout)

        self.text = QTextEdit()
        layout.addWidget(self.text, 0, 0)

    # override of the "abstract" method
    def update_subject(self):
        self.subject = self.subject.get_state()
        self.data = self.subject.data.swapcase()
        self.text.setText(self.data)
