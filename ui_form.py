# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGroupBox, QLabel,
    QRadioButton, QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 400)
        Widget.setMinimumSize(QSize(800, 400))
        Widget.setMaximumSize(QSize(800, 400))
        self.groupBox_3 = QGroupBox(Widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(530, 10, 150, 132))
        font = QFont()
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(30, 65, 81, 24))
        self.label_10.setFont(font)
        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 65, 21, 24))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.label_9.setFont(font1)
        self.groupBox_2 = QGroupBox(Widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(250, 10, 250, 132))
        self.groupBox_2.setFont(font)
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 30, 67, 24))
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 65, 67, 24))
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 100, 81, 24))
        self.doubleSpinBox_1 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_1.setObjectName(u"doubleSpinBox_1")
        self.doubleSpinBox_1.setGeometry(QRect(90, 30, 80, 24))
        self.doubleSpinBox_1.setFont(font)
        self.doubleSpinBox_1.setMinimum(0.000000000000000)
        self.doubleSpinBox_1.setMaximum(9999.989999999999782)
        self.doubleSpinBox_2 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setGeometry(QRect(90, 65, 80, 24))
        self.doubleSpinBox_2.setMaximum(9999.989999999999782)
        self.doubleSpinBox_3 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        self.doubleSpinBox_3.setGeometry(QRect(90, 100, 80, 24))
        self.doubleSpinBox_3.setMinimum(0.000000000000000)
        self.doubleSpinBox_3.setMaximum(9999.989999999999782)
        self.doubleSpinBox_3.setValue(0.000000000000000)
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(180, 30, 67, 24))
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(180, 65, 67, 24))
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(180, 100, 67, 24))
        self.groupBox_1 = QGroupBox(Widget)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.groupBox_1.setGeometry(QRect(10, 10, 210, 132))
        self.groupBox_1.setFont(font)
        self.radioButton_1 = QRadioButton(self.groupBox_1)
        self.radioButton_1.setObjectName(u"radioButton_1")
        self.radioButton_1.setGeometry(QRect(10, 30, 44, 24))
        self.radioButton_3 = QRadioButton(self.groupBox_1)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(10, 100, 53, 24))
        self.radioButton_2 = QRadioButton(self.groupBox_1)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(10, 60, 120, 34))
        self.label_2 = QLabel(self.groupBox_1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(170, 65, 31, 24))
        self.label_2.setFont(font)
        self.label_1 = QLabel(self.groupBox_1)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(150, 65, 31, 24))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Widget", u"Result:", None))
        self.label_10.setText("")
        self.label_9.setText(QCoreApplication.translate("Widget", u"E=", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"Parameters:", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Current:", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Voltage:", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"Speed:", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"A", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"V", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"mm/min", None))
        self.groupBox_1.setTitle(QCoreApplication.translate("Widget", u"Processes, coefficient K:", None))
        self.radioButton_1.setText(QCoreApplication.translate("Widget", u"12", None))
        self.radioButton_3.setText(QCoreApplication.translate("Widget", u"141", None))
        self.radioButton_2.setText(QCoreApplication.translate("Widget", u"111 114 131\n"
"135 136 137", None))
        self.label_2.setText("")
        self.label_1.setText(QCoreApplication.translate("Widget", u"K=", None))
    # retranslateUi

