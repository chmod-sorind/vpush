from PySide import QtCore, QtGui


class DigitalClock(QtGui.QLCDNumber):
    def __init__(self, parent=None):
        super(DigitalClock, self).__init__(parent)

        self.setSegmentStyle(QtGui.QLCDNumber.Filled)

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        self.showTime()

        self.setWindowTitle("Digital Clock")
        self.resize(1200, 480)

    def showTime(self):
        time = QtCore.QTime.currentTime()
        print time
        text = time.toString('hh:mm')
        print text
        if (time.second() % 3) == 0:
            text = text[:2] + ' ' + text[3:]

        self.display(text)


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())