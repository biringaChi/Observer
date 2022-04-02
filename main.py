"""
Team SCAG Observer Pattern Implementation
main.py
"""

from PyQt6.QtWidgets import QApplication
from subject import Subject
from concrete1 import AllLines
from concrete2 import Backwards
from concrete3 import Swapcase
import sys

# start PyQt application
app = QApplication([])

# initialize subject and observers
s = Subject()

o1 = AllLines(s)
s.add_observer(o1)

o2 = Backwards(s)
s.add_observer(o2)

o3 = Swapcase(s)
s.add_observer(o3)

o3.show()
o2.show()
o1.show()
s.show()

# run the windows and exit when done
sys.exit(app.exec())
