"""
Team SCAG Observer Pattern Implementation
subject.py - our subject to be watched by our observers
"""

from PyQt6.QtWidgets import *


class Subject(QWidget):
    def __init__(self):
        # initialization
        super().__init__()
        self.observers = []
        self.data = ""

        # gui elements
        self.setWindowTitle("Subject")

        self.text = QTextEdit()
        btn = QPushButton('submit')
        btn.clicked.connect(lambda: self.notify_observers())

        layout = QGridLayout()
        self.setLayout(layout)

        layout.addWidget(self.text, 0, 0)
        layout.addWidget(btn, 1, 0)

    # adds an observer to the list
    def add_observer(self, o):
        self.observers.append(o)

    # removes an observer from the list
    def remove_observer(self, o):
        self.observers.remove(o)

    # tell all observers to check for an update
    # first update state of data then empty the text box for further use
    def notify_observers(self):
        self.data = self.text.toPlainText()
        for o in self.observers:
            o.update_subject()

        self.text.clear()

    # an observer will call this method to get the current state after being notified
    def get_state(self):
        return self
