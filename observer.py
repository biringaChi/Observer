"""
Team SCAG Observer Pattern Implementation
observer.py - super class to parent all concrete observers
"""

from PyQt6.QtWidgets import *


class Observer(QWidget):
    def __init__(self, subject):
        super().__init__()
        self.subject = subject.get_state()

    def update_subject(self):
        self.subject = self.subject.get_state()
        self.process_update()

    def process_update(self):
        pass
