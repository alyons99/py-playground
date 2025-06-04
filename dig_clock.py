import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTime, QTimer, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class Dig_Clock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(650,300,600,200)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 150px;"
                                      "color: #39FF14;"
                                    )
                                      #"background-color: black;") redundant
        self.setStyleSheet("background-color: black;")
        font_id = QFontDatabase.addApplicationFont("digital-7.ttf")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)
        #self.updateTime()

    def updateTime(self):
        curr = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(curr)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = Dig_Clock()
    clock.show()
    #execute method
    sys.exit(app.exec_())