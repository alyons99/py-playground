import sys
from PyQt5.QtWidgets import(QApplication, QWidget, QLabel, 
                            QPushButton, QVBoxLayout, QHBoxLayout)

from PyQt5.QtCore import QTimer, QTime, Qt

#inherit from QWidget
class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        #create our time object with default values of 0
        self.time = QTime(0, 0, 0, 0)
        #the text label
        self.time_label = QLabel("00:00:00.00", self)
        #create buttons. Start, stop, and clear widgets
        self.start_button = QPushButton("START", self)
        self.stop_button = QPushButton("STOP", self)
        self.clear_button = QPushButton("CLEAR", self)
        self.timer = QTimer(self)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Stopwatch")

        #create our layout and add widgets to the layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)

        #create a horizontal layout for our buttons
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.clear_button)

        #set the main vertical layout and add the horizontal w/ buttons
        self.setLayout(vbox)
        vbox.addLayout(hbox)

        #come pseudo-css for our buttons and label
        self.time_label.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("""
                           QPushButton, QLabel {
                                padding: 10px;
                            }
                            QPushButton{
                                font-size: 25px;
                            }
                            QLabel {
                                font-size: 120px;
                                background-color: #ADD8E6;
                                border-radius: 20px;
                            }
                           """)
        
        #give a signal check on click to begin our other functions
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.clear_button.clicked.connect(self.clear)
        
        #update the display
        self.timer.timeout.connect(self.update)

    def start(self):
        #time is set to 10ms
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def clear(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        second = time.second()
        ms = time.msec() // 10

        return f"{hours:02}:{minutes:02}:{second:02}.{ms:02}"

    def update(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))

if __name__ == "__main__":
    #create the application
    app = QApplication(sys.argv)
    #create stopwatch object
    stopwatch = Stopwatch()
    #show stopwatch
    stopwatch.show()
    #prevent application from closing while its running
    sys.exit(app.exec_())