# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ncal.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(480, 630)
        MainWindow.setMinimumSize(QtCore.QSize(480, 630))
        MainWindow.setMaximumSize(QtCore.QSize(480, 630))
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.OutP = QtWidgets.QLineEdit(self.centralwidget)
        self.OutP.setGeometry(QtCore.QRect(0, 30, 480, 100))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(36)
        self.OutP.setFont(font)
        self.OutP.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.OutP.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.OutP.setFrame(True)
        self.OutP.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.OutP.setDragEnabled(False)
        self.OutP.setReadOnly(True)
        self.OutP.setClearButtonEnabled(False)
        self.OutP.setObjectName("OutP")
        self.Clear = QtWidgets.QPushButton(self.centralwidget)
        self.Clear.setGeometry(QtCore.QRect(0, 130, 120, 100))
        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setPointSize(28)
        self.Clear.setFont(font)
        self.Clear.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.Clear.setObjectName("Clear")
        self.divide = QtWidgets.QPushButton(self.centralwidget)
        self.divide.setGeometry(QtCore.QRect(120, 130, 120, 100))
        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setPointSize(28)
        self.divide.setFont(font)
        self.divide.setStyleSheet("background-color: rgb(255, 153, 51);")
        self.divide.setObjectName("divide")
        self.multiply = QtWidgets.QPushButton(self.centralwidget)
        self.multiply.setGeometry(QtCore.QRect(240, 130, 120, 100))
        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setPointSize(28)
        self.multiply.setFont(font)
        self.multiply.setStyleSheet("background-color: rgb(255, 153, 51);")
        self.multiply.setObjectName("multiply")
        self.minus = QtWidgets.QPushButton(self.centralwidget)
        self.minus.setGeometry(QtCore.QRect(360, 130, 120, 100))
        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setPointSize(28)
        self.minus.setFont(font)
        self.minus.setStyleSheet("background-color: rgb(255, 153, 51);")
        self.minus.setObjectName("minus")
        self.seven = QtWidgets.QPushButton(self.centralwidget)
        self.seven.setGeometry(QtCore.QRect(0, 230, 120, 100))
        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setPointSize(28)
        self.seven.setFont(font)
        self.seven.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.seven.setObjectName("seven")
        self.eight = QtWidgets.QPushButton(self.centralwidget)
        self.eight.setGeometry(QtCore.QRect(120, 230, 120, 100))
        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setPointSize(28)
        self.eight.setFont(font)
        self.eight.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.eight.setObjectName("eight")
        self.nine = QtWidgets.QPushButton(self.centralwidget)
        self.nine.setGeometry(QtCore.QRect(240, 230, 120, 100))
        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setPointSize(28)
        self.nine.setFont(font)
        self.nine.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.nine.setObjectName("nine")
        self.plus = QtWidgets.QPushButton(self.centralwidget)
        self.plus.setGeometry(QtCore.QRect(360, 230, 120, 200))
        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setPointSize(28)
        self.plus.setFont(font)
        self.plus.setStyleSheet("background-color: rgb(255, 153, 51);")
        self.plus.setObjectName("plus")
        self.four = QtWidgets.QPushButton(self.centralwidget)
        self.four.setGeometry(QtCore.QRect(0, 330, 120, 100))
        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setPointSize(28)
        self.four.setFont(font)
        self.four.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.four.setObjectName("four")
        self.five = QtWidgets.QPushButton(self.centralwidget)
        self.five.setGeometry(QtCore.QRect(120, 330, 120, 100))
        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setPointSize(28)
        self.five.setFont(font)
        self.five.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.five.setObjectName("five")
        self.six = QtWidgets.QPushButton(self.centralwidget)
        self.six.setGeometry(QtCore.QRect(240, 330, 120, 100))
        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setPointSize(28)
        self.six.setFont(font)
        self.six.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.six.setObjectName("six")
        self.ans = QtWidgets.QPushButton(self.centralwidget)
        self.ans.setGeometry(QtCore.QRect(360, 430, 120, 200))
        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setPointSize(28)
        self.ans.setFont(font)
        self.ans.setStyleSheet("background-color: rgb(255, 153, 51);")
        self.ans.setObjectName("ans")
        self.three = QtWidgets.QPushButton(self.centralwidget)
        self.three.setGeometry(QtCore.QRect(240, 430, 120, 100))
        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setPointSize(28)
        self.three.setFont(font)
        self.three.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.three.setObjectName("three")
        self.two = QtWidgets.QPushButton(self.centralwidget)
        self.two.setGeometry(QtCore.QRect(120, 430, 120, 100))
        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setPointSize(28)
        self.two.setFont(font)
        self.two.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.two.setObjectName("two")
        self.one = QtWidgets.QPushButton(self.centralwidget)
        self.one.setGeometry(QtCore.QRect(0, 430, 120, 100))
        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setPointSize(28)
        self.one.setFont(font)
        self.one.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.one.setObjectName("one")
        self.dot = QtWidgets.QPushButton(self.centralwidget)
        self.dot.setGeometry(QtCore.QRect(240, 530, 120, 100))
        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setPointSize(28)
        self.dot.setFont(font)
        self.dot.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.dot.setObjectName("dot")
        self.zero = QtWidgets.QPushButton(self.centralwidget)
        self.zero.setGeometry(QtCore.QRect(0, 530, 240, 100))
        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setPointSize(28)
        self.zero.setFont(font)
        self.zero.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.zero.setObjectName("zero")
        self.MyTitle = QtWidgets.QLabel(self.centralwidget)
        self.MyTitle.setGeometry(QtCore.QRect(0, 0, 400, 30))
        self.MyTitle.setMouseTracking(True)
        self.MyTitle.setAutoFillBackground(False)
        self.MyTitle.setStyleSheet("font: 10pt \"ROG Fonts\";\n"
"color: white;")
        self.MyTitle.setTextFormat(QtCore.Qt.RichText)
        self.MyTitle.setObjectName("MyTitle")
        self.xXx = QtWidgets.QPushButton(self.centralwidget)
        self.xXx.setGeometry(QtCore.QRect(440, 0, 40, 30))
        self.xXx.setStyleSheet("color: white\n"
";\n"
"font: 8pt \"ROG Fonts\";")
        self.xXx.setObjectName("xXx")
        self.minimize = QtWidgets.QPushButton(self.centralwidget)
        self.minimize.setGeometry(QtCore.QRect(400, 0, 40, 30))
        self.minimize.setStyleSheet("color: white\n"
";\n"
"font: 8pt \"ROG Fonts\";")
        self.minimize.setObjectName("minimize")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Noey\'s Cal"))
        self.Clear.setText(_translate("MainWindow", "C"))
        self.divide.setText(_translate("MainWindow", "/"))
        self.multiply.setText(_translate("MainWindow", "*"))
        self.minus.setText(_translate("MainWindow", "-"))
        self.seven.setText(_translate("MainWindow", "7"))
        self.eight.setText(_translate("MainWindow", "8"))
        self.nine.setText(_translate("MainWindow", "9"))
        self.plus.setText(_translate("MainWindow", "+"))
        self.four.setText(_translate("MainWindow", "4"))
        self.five.setText(_translate("MainWindow", "5"))
        self.six.setText(_translate("MainWindow", "6"))
        self.ans.setText(_translate("MainWindow", "="))
        self.three.setText(_translate("MainWindow", "3"))
        self.two.setText(_translate("MainWindow", "2"))
        self.one.setText(_translate("MainWindow", "1"))
        self.dot.setText(_translate("MainWindow", "."))
        self.zero.setText(_translate("MainWindow", "0"))
        self.MyTitle.setText(_translate("MainWindow", "Noey\'s Calculator"))
        self.xXx.setText(_translate("MainWindow", "( X )"))
        self.minimize.setText(_translate("MainWindow", "( _ )"))
