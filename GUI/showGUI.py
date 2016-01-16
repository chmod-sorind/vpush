from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtGui import QDialog
import sys
import os
import AppMainWindow
import telnetlib
import time


class MainDialog(QDialog, AppMainWindow.Ui_AppMainWindow):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        self.connect(self.BT_openFile, SIGNAL("clicked()"), self.openFile)
        self.connect(self.BT_cmdSend, SIGNAL("clicked()"), self.telnetConn)

    def openFile(self):
        fileLocation = os.environ['USERPROFILE'] + '\\Desktop'
        try:
            fileName = str(QFileDialog.getOpenFileName(None, 'Select Host List', fileLocation,
                                                       'File Filter (*.txt *.ini)')[0])
            with open(fileName) as IP:
                line = IP.read().splitlines()
            model = QStandardItemModel(self.LV_hostList)
            for ip in line:
                host_item = QStandardItem(ip)
                host_item.setCheckable(True)
                model.appendRow(host_item)
            self.LV_hostList.setModel(model)
        except:
            pass

    def telnetConn(self):
        pollingCount = self.SB_pollCount.value()
        telnetPort = self.TxB_telnetPort.text()
        command = self.TxB_telnetCommand.text()
        for n in range(1, pollingCount + 1):
            for f in self.LV_hostList.items():  # Here is the problem
                try:
                    telnet = telnetlib.Telnet(f, telnetPort)
                    telnet.write(command)
                    telnet.close()
                except:
                    pass


app = QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()
