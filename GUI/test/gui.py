from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtGui import QDialog
import sys
import dialog_rc

class MainDialog(QDialog, dialog_rc.Ui_Dialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

app = QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()
