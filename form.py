# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(709, 897)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(20, 30, 661, 871))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 90, 91, 20))
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 130, 91, 20))
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setEnabled(False)
        self.label.setGeometry(QtCore.QRect(50, 90, 91, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setEnabled(False)
        self.label_2.setGeometry(QtCore.QRect(50, 130, 51, 21))
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.tab_2)
        self.line.setGeometry(QtCore.QRect(30, 150, 311, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.tab_2)
        self.line_2.setGeometry(QtCore.QRect(30, 110, 311, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.tab_2)
        self.line_3.setGeometry(QtCore.QRect(330, 90, 20, 101))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setEnabled(False)
        self.label_4.setGeometry(QtCore.QRect(350, 80, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.tab_2)
        self.comboBox.setEnabled(False)
        self.comboBox.setGeometry(QtCore.QRect(370, 120, 45, 20))
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setEnabled(False)
        self.label_5.setGeometry(QtCore.QRect(290, 90, 21, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setEnabled(False)
        self.label_6.setGeometry(QtCore.QRect(290, 130, 21, 16))
        self.label_6.setObjectName("label_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setGeometry(QtCore.QRect(370, 160, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.graphicsView = QtWidgets.QGraphicsView(self.tab_2)
        self.graphicsView.setEnabled(False)
        self.graphicsView.setGeometry(QtCore.QRect(0, 250, 661, 561))
        self.graphicsView.setObjectName("graphicsView")
        self.line_5 = QtWidgets.QFrame(self.tab_2)
        self.line_5.setGeometry(QtCore.QRect(0, 190, 631, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setEnabled(False)
        self.label_8.setGeometry(QtCore.QRect(20, 200, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setScaledContents(False)
        self.label_8.setObjectName("label_8")
        self.line_6 = QtWidgets.QFrame(self.tab_2)
        self.line_6.setGeometry(QtCore.QRect(0, 70, 631, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 40, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(140, -10, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        self.label_9.setScaledContents(False)
        self.label_9.setObjectName("label_9")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(110, 40, 331, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 40, 101, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.line_7 = QtWidgets.QFrame(self.tab_2)
        self.line_7.setGeometry(QtCore.QRect(20, 90, 20, 101))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.buttonBox_2 = QtWidgets.QDialogButtonBox(self.tab_2)
        self.buttonBox_2.setGeometry(QtCore.QRect(420, 820, 156, 23))
        self.buttonBox_2.setAutoFillBackground(True)
        self.buttonBox_2.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_2.setObjectName("buttonBox_2")
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(510, 210, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setEnabled(False)
        self.pushButton_5.setGeometry(QtCore.QRect(510, 160, 81, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.line_8 = QtWidgets.QFrame(self.tab_2)
        self.line_8.setGeometry(QtCore.QRect(480, 80, 20, 111))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setEnabled(False)
        self.label_11.setGeometry(QtCore.QRect(500, 90, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(520, 120, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.line_9 = QtWidgets.QFrame(self.tab_2)
        self.line_9.setGeometry(QtCore.QRect(620, 10, 20, 231))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setEnabled(False)
        self.label_3.setGeometry(QtCore.QRect(50, 170, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setGeometry(QtCore.QRect(210, 169, 61, 21))
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Suma powierzchni"))
        self.label_2.setText(_translate("Dialog", "Średnia"))
        self.label_4.setText(_translate("Dialog", "Wybierz jednostkę"))
        self.comboBox.setItemText(0, _translate("Dialog", "m2"))
        self.comboBox.setItemText(1, _translate("Dialog", "km2"))
        self.comboBox.setItemText(2, _translate("Dialog", "ha"))
        self.comboBox.setItemText(3, _translate("Dialog", "a"))
        self.label_5.setText(_translate("Dialog", "m2"))
        self.label_6.setText(_translate("Dialog", "m2"))
        self.pushButton_3.setText(_translate("Dialog", "Odśwież"))
        self.label_8.setText(_translate("Dialog", "Wykres % udziału klasy w łącznej sumie powierzchni zaznaczonych obiektów"))
        self.pushButton_4.setText(_translate("Dialog", "Otwórz"))
        self.label_9.setText(_translate("Dialog", "Wczytaj plik i oblicz statystyki dla wybranych obiektów"))
        self.pushButton_2.setText(_translate("Dialog", "Zaznacz obiekty"))
        self.pushButton.setText(_translate("Dialog", "Rysuj"))
        self.pushButton_5.setText(_translate("Dialog", "Wyczyść liste"))
        self.label_11.setText(_translate("Dialog", "Liczba obiektów"))
        self.lineEdit.setText(_translate("Dialog", "0"))
        self.label_3.setText(_translate("Dialog", "Liczba unikatowych klas"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Statystki"))
