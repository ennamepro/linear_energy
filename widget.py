# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Show "?" question marks at K coefficient an Linear energy

        self.ui.label_2.setText("?")
        self.ui.label_10.setText("?")

        self.ui.doubleSpinBox_1.valueChanged.connect(self.calculation)
        self.ui.doubleSpinBox_2.valueChanged.connect(self.calculation)
        self.ui.doubleSpinBox_3.valueChanged.connect(self.calculation)

        self.ui.radioButton_1.clicked.connect(self.calculation)
        self.ui.radioButton_2.clicked.connect(self.calculation)
        self.ui.radioButton_3.clicked.connect(self.calculation)

    def calculation(self):
        if self.ui.radioButton_1.isChecked():
            self.ui.label_2.setText("1")
            k = 1
        elif self.ui.radioButton_2.isChecked():
            self.ui.label_2.setText("0.8")
            k = 0.8
        elif self.ui.radioButton_3.isChecked():
            self.ui.label_2.setText("0.6")
            k = 0.6
        else:
            k = 0
        a = self.ui.doubleSpinBox_1.value()
        v = self.ui.doubleSpinBox_2.value()
        s = self.ui.doubleSpinBox_3.value()
        if s == 0:
            self.ui.label_10.setText("ꝏ")
        else:
            self.ui.label_10.setText(str(round(k*a*v/s,2)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
