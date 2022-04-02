"""
Team SCAG Observer Pattern Implementation
concrete2.py - implementation for the second concrete observer
"""

from PyQt6.QtWidgets import *
from observer import Observer
import pyqtgraph


class Backwards(Observer, QWidget):
    def __init__(self, subject):
        super().__init__(subject)
        self.data = ""

        # gui elements
        self.setWindowTitle("Backwards")

        layout = QGridLayout()
        self.setLayout(layout)

        self.text = QTextEdit()
        layout.addWidget(self.text, 0, 0)

    # override of the "abstract" method
    def update_subject(self):
        self.subject = self.subject.get_state()
        self.data = ''.join(reversed(self.subject.data))
        self.text.setText(self.data)
