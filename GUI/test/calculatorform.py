import sys
from PySide import QtCore, QtGui

from ui_calculatorform import Ui_CalculatorForm


class CalculatorForm(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_CalculatorForm()

        self.ui.setupUi(self)

    @QtCore.Slot(int)
    def on_inputSpinBox1_valueChanged(self, value):
        self.ui.outputWidget.setText(str(value + self.ui.inputSpinBox2.value()))

    @QtCore.Slot(int)
    def on_inputSpinBox2_valueChanged(self, value):
        self.ui.outputWidget.setText(str(value + self.ui.inputSpinBox1.value()))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    calculator = CalculatorForm()
    calculator.show()
    sys.exit(app.exec_())