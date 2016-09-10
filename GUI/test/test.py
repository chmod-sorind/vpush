import sys
from PySide.QtCore import *
from PySide.QtGui import *

class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.groupbox = QGroupBox('ASD')
        self.layout = QHBoxLayout()
        self.btnlayout = QHBoxLayout()
        self.btn1 = QPushButton('Button I')
        self.btn2 = QPushButton('Button II')
        self.btnlayout.addWidget(self.btn1)
        self.btnlayout.addWidget(self.btn2)
        self.layout.addLayout(self.btnlayout)
        self.editor = QTextEdit()
        self.layout.addWidget(self.editor)
        self.layout.addWidget(self.groupbox)
        self.groupbox.addWidget(self.editor)
        self.setLayout(self.layout)


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('My Application')
        self.setMinimumSize(400, 300)
        #self.setMaximumSize(400, 200)
        self.apptab = QTabWidget()
        self.setCentralWidget(self.apptab)
        self.apptab.addTab(MyWidget(), 'Tab I')
        self.show()

def main():
    app = QApplication(sys.argv)
    main = MyWindow()
    sys.exit(app.exec_())

if __name__== '__main__':
    main()