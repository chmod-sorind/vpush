from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtGui import QDialog
import sys
import os
import AppMainWindow
import telnetlib
import time


class MainDialog(QMainWindow, QDialog, AppMainWindow.Ui_AppMainWindow):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        self.connect(self.BT_openFile, SIGNAL("clicked()"), self.openFile)
        self.connect(self.BT_cmdSend, SIGNAL("clicked()"), self.telnetConn)
        self.connect(self.BT_addItemToList, SIGNAL("clicked()"), self.addHostToList) # NOT WORKING YET
        self.RB_batchTelnet.clicked.connect(self.batchTelnet)
        self.RB_oneTimeTel.clicked.connect(self.oneTimeTelEnable)

    def oneTimeTelEnable(self):
        self.SB_pollCount.setEnabled(False)
        self.SB_pollInterval.setEnabled(False)

    def batchTelnet(self):
        self.SB_pollCount.setEnabled(True)
        self.SB_pollInterval.setEnabled(True)

    def addHostToList(self): # NOT WORKING YET
        model = QStandardItemModel(self.LV_hostList)
        item = QStandardItem(self.TxB_addIPtoList.text())
        item.setCheckable(True)
        item.setEditable(True)
        model.insertRow(0, item)
        self.LV_hostList.setModel(model)

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
                host_item.setEditable(False)
                model.appendRow(host_item)
            self.LV_hostList.setModel(model)
        except:
            pass

    def telnetConn(self): # pollingCount, telnetPort, command
        self.pollingCount = self.SB_pollCount.value()
        self.telnetPort = self.TxB_telnetPort.text()
        self.command = self.TxB_telnetCommand.text()
        for n in range(1, self.pollingCount + 1):
            for f in self.LV_hostList.item():  # Here is the problem
                #try:
                telnet = telnetlib.Telnet(f, self.telnetPort)
                telnet.write(self.command)
                telnet.close()
                #except:
                    #pass


app = QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()
