# Form implementation generated from reading ui file '.\show.ui'
#
# Created: Wed Dec 16 16:50:15 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(335, 107)
        MainWindow.setCursor(QtCore.Qt.ArrowCursor)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.textEdit = QtGui.QLineEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 151, 20))
        self.textEdit.setText("")
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 20, 121, 21))
        self.pushButton.setObjectName("pushButton")
        #MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 335, 21))
        self.menuBar.setObjectName("menuBar")
        #MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        #MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        #MainWindow.insertToolBarBreak(self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        #MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton, self.textEdit)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "My Application", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "Type something here!", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))

