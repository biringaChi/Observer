"""
Team SCAG Observer Pattern Implementation
main.py
"""

from PyQt6.QtWidgets import QApplication
from subject import Subject
from concrete1 import Concrete1
import sys

# start PyQt application
app = QApplication([])

# initialize subject and observers
s = Subject()
s.show()

o1 = Concrete1(s)
s.add_observer(o1)
o1.show()

# run the windows and exit when done
sys.exit(app.exec())
