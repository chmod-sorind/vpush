from PySide import QtCore, QtGui

class Ui_AppMainWindow(object):
    def setupUi(self, AppMainWindow):
        AppMainWindow.setObjectName("AppMainWindow")
        AppMainWindow.resize(364, 388)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AppMainWindow.sizePolicy().hasHeightForWidth())
        AppMainWindow.setSizePolicy(sizePolicy)
        AppMainWindow.setMinimumSize(QtCore.QSize(364, 388))
        AppMainWindow.setMaximumSize(QtCore.QSize(429, 474))
        self.centralWidget = QtGui.QWidget(AppMainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.LV_hostList = QtGui.QListView(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LV_hostList.sizePolicy().hasHeightForWidth())
        self.LV_hostList.setSizePolicy(sizePolicy)
        self.LV_hostList.setMinimumSize(QtCore.QSize(100, 100))
        self.LV_hostList.setMaximumSize(QtCore.QSize(200, 360))
        self.LV_hostList.setObjectName("LV_hostList")
        self.verticalLayout_6.addWidget(self.LV_hostList)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.RB_oneTimeTel = QtGui.QRadioButton(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RB_oneTimeTel.sizePolicy().hasHeightForWidth())
        self.RB_oneTimeTel.setSizePolicy(sizePolicy)
        self.RB_oneTimeTel.setCursor(QtCore.Qt.PointingHandCursor)
        self.RB_oneTimeTel.setChecked(True)
        self.RB_oneTimeTel.setObjectName("RB_oneTimeTel")
        self.verticalLayout_3.addWidget(self.RB_oneTimeTel)
        self.RB_batchTelnet = QtGui.QRadioButton(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RB_batchTelnet.sizePolicy().hasHeightForWidth())
        self.RB_batchTelnet.setSizePolicy(sizePolicy)
        self.RB_batchTelnet.setCursor(QtCore.Qt.PointingHandCursor)
        self.RB_batchTelnet.setObjectName("RB_batchTelnet")
        self.verticalLayout_3.addWidget(self.RB_batchTelnet)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SB_pollCount = QtGui.QSpinBox(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SB_pollCount.sizePolicy().hasHeightForWidth())
        self.SB_pollCount.setSizePolicy(sizePolicy)
        self.SB_pollCount.setMinimumSize(QtCore.QSize(62, 22))
        self.SB_pollCount.setMaximumSize(QtCore.QSize(62, 22))
        self.SB_pollCount.setProperty("value", 1)
        self.SB_pollCount.setObjectName("SB_pollCount")
        self.SB_pollCount.setEnabled(False)
        self.horizontalLayout.addWidget(self.SB_pollCount)
        self.label = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.SB_pollInterval = QtGui.QSpinBox(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SB_pollInterval.sizePolicy().hasHeightForWidth())
        self.SB_pollInterval.setSizePolicy(sizePolicy)
        self.SB_pollInterval.setMinimumSize(QtCore.QSize(62, 22))
        self.SB_pollInterval.setMaximumSize(QtCore.QSize(62, 22))
        self.SB_pollInterval.setProperty("value", 1)
        self.SB_pollInterval.setObjectName("SB_pollInterval")
        self.SB_pollInterval.setEnabled(False)
        self.horizontalLayout_2.addWidget(self.SB_pollInterval)
        self.label_2 = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.TxB_telnetPort = QtGui.QLineEdit(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TxB_telnetPort.sizePolicy().hasHeightForWidth())
        self.TxB_telnetPort.setSizePolicy(sizePolicy)
        self.TxB_telnetPort.setMaximumSize(QtCore.QSize(278, 20))
        self.TxB_telnetPort.setObjectName("TxB_telnetPort")
        self.verticalLayout_2.addWidget(self.TxB_telnetPort)
        self.TxB_telnetCommand = QtGui.QLineEdit(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TxB_telnetCommand.sizePolicy().hasHeightForWidth())
        self.TxB_telnetCommand.setSizePolicy(sizePolicy)
        self.TxB_telnetCommand.setMaximumSize(QtCore.QSize(278, 20))
        self.TxB_telnetCommand.setObjectName("TxB_telnetCommand")
        self.verticalLayout_2.addWidget(self.TxB_telnetCommand)
        self.TxB_addIPtoList = QtGui.QLineEdit(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TxB_addIPtoList.sizePolicy().hasHeightForWidth())
        self.TxB_addIPtoList.setSizePolicy(sizePolicy)
        self.TxB_addIPtoList.setMinimumSize(QtCore.QSize(110, 20))
        self.TxB_addIPtoList.setMaximumSize(QtCore.QSize(300, 20))
        self.TxB_addIPtoList.setObjectName("TxB_addIPtoList")
        self.TxB_addIPtoList.setEnabled(False)
        self.verticalLayout_2.addWidget(self.TxB_addIPtoList)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.BT_addItemToList = QtGui.QPushButton(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BT_addItemToList.sizePolicy().hasHeightForWidth())
        self.BT_addItemToList.setSizePolicy(sizePolicy)
        self.BT_addItemToList.setMinimumSize(QtCore.QSize(145, 25))
        self.BT_addItemToList.setMaximumSize(QtCore.QSize(300, 25))
        self.BT_addItemToList.setObjectName("BT_addItemToList")
        self.BT_addItemToList.setEnabled(False)
        self.verticalLayout_4.addWidget(self.BT_addItemToList)
        self.BT_openFile = QtGui.QPushButton(self.centralWidget)
        self.BT_openFile.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BT_openFile.sizePolicy().hasHeightForWidth())
        self.BT_openFile.setSizePolicy(sizePolicy)
        self.BT_openFile.setMinimumSize(QtCore.QSize(145, 25))
        self.BT_openFile.setMaximumSize(QtCore.QSize(300, 25))
        self.BT_openFile.setObjectName("BT_openFile")
        self.verticalLayout_4.addWidget(self.BT_openFile)
        self.BT_cmdSend = QtGui.QPushButton(self.centralWidget)
        self.BT_cmdSend.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BT_cmdSend.sizePolicy().hasHeightForWidth())
        self.BT_cmdSend.setSizePolicy(sizePolicy)
        self.BT_cmdSend.setMinimumSize(QtCore.QSize(146, 23))
        self.BT_cmdSend.setMaximumSize(QtCore.QSize(280, 23))
        self.BT_cmdSend.setObjectName("BT_cmdSend")
        self.verticalLayout_4.addWidget(self.BT_cmdSend)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.LV_logLines = QtGui.QListView(self.centralWidget)
        self.LV_logLines.setMaximumSize(QtCore.QSize(600, 100))
        self.LV_logLines.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.LV_logLines.setObjectName("LV_logLines")
        self.verticalLayout_7.addWidget(self.LV_logLines)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        AppMainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(AppMainWindow)
        QtCore.QMetaObject.connectSlotsByName(AppMainWindow)

    def retranslateUi(self, AppMainWindow):
        AppMainWindow.setWindowTitle(QtGui.QApplication.translate("AppMainWindow", "Telnet Asistant V1.2-1", None, QtGui.QApplication.UnicodeUTF8))
        self.RB_oneTimeTel.setText(QtGui.QApplication.translate("AppMainWindow", "One Time VPush", None, QtGui.QApplication.UnicodeUTF8))
        self.RB_batchTelnet.setText(QtGui.QApplication.translate("AppMainWindow", "Batch VPush", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AppMainWindow", "Count               ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AppMainWindow", "Interval", None, QtGui.QApplication.UnicodeUTF8))
        self.TxB_telnetPort.setPlaceholderText(QtGui.QApplication.translate("AppMainWindow", "Telnet PORT", None, QtGui.QApplication.UnicodeUTF8))
        self.TxB_telnetCommand.setPlaceholderText(QtGui.QApplication.translate("AppMainWindow", "Telnet Command", None, QtGui.QApplication.UnicodeUTF8))
        self.TxB_addIPtoList.setPlaceholderText(QtGui.QApplication.translate("AppMainWindow", "Host IP", None, QtGui.QApplication.UnicodeUTF8))
        self.BT_addItemToList.setText(QtGui.QApplication.translate("AppMainWindow", "Add Host to List", None, QtGui.QApplication.UnicodeUTF8))
        self.BT_openFile.setText(QtGui.QApplication.translate("AppMainWindow", "Select Host List", None, QtGui.QApplication.UnicodeUTF8))
        self.BT_cmdSend.setText(QtGui.QApplication.translate("AppMainWindow", "Send Command", None, QtGui.QApplication.UnicodeUTF8))
        self.LV_logLines.setWhatsThis(QtGui.QApplication.translate("AppMainWindow", "<html><head/><body><p>This is Shit</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

