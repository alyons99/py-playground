import sys
from PyQt5.QtWidgets import(QApplication, QWidget, QLabel, 
                            QPushButton, QVBoxLayout, QHBoxLayout)

from PyQt5.QtCore import QTimer, QTime, Qt

#inherit from QWidget
class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    #create the application
    app = QApplication(sys.argv)
    #create stopwatch object
    stopwatch = Stopwatch()
    #show stopwatch
    stopwatch.show()
    #prevent application from closing while its running
    sys.exit(app.exec_())