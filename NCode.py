#ส่วนของ module
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PySide6.QtGui import QMouseEvent
from Ncal import Ui_MainWindow
import sys

class Calculator(QtWidgets.QMainWindow, Ui_MainWindow):
    #!Don't know how it works so don't touch anything
    def __init__(self):
        super(Calculator, self).__init__()

        #Hide title bar
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.uif = Ui_MainWindow()
        self.uif.setupUi(self)
        self.uif.OutP.setAlignment(Qt.AlignRight)
        
        #Move Window
        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # Title bar
        self.uif.MyTitle.mouseMoveEvent = moveWindow
    #!~~~~~~~~~~~~~~~~

        #ปุ่มย่อและปิด
        self.uif.minimize.pressed.connect(self.btn_minimize)
        self.uif.xXx.pressed.connect(self.btn_exit)

        #ปุ่มสั่งงาน
        self.uif.Clear.pressed.connect(self.btn_clear)
        self.uif.divide.pressed.connect(self.btn_divide)
        self.uif.multiply.pressed.connect(self.btn_multiply)
        self.uif.minus.pressed.connect(self.btn_minus)
        self.uif.plus.pressed.connect(self.btn_plus)
        self.uif.ans.pressed.connect(self.btn_ans)

        #ปุ่มตัวเลข
        self.uif.nine.pressed.connect(self.btn_nine)
        self.uif.eight.pressed.connect(self.btn_eight)
        self.uif.seven.pressed.connect(self.btn_seven)
        self.uif.six.pressed.connect(self.btn_six)
        self.uif.five.pressed.connect(self.btn_five)
        self.uif.four.pressed.connect(self.btn_four)
        self.uif.three.pressed.connect(self.btn_three)
        self.uif.two.pressed.connect(self.btn_two)
        self.uif.one.pressed.connect(self.btn_one)
        self.uif.zero.pressed.connect(self.btn_zero)
        self.uif.dot.pressed.connect(self.btn_dot)
        
    #ส่วนย่อและปิด
    def btn_minimize(self):
        self.showNormal()
        self.showMinimized()

    def btn_exit(self):
        quit()

    #ส่วนแสดงผลตัวเลข
    def btn_nine(self):
        expr = self.uif.OutP.text()
        expr += '9'
        self.uif.OutP.setText(expr)
    def btn_eight(self):
        expr = self.uif.OutP.text()
        expr += '8'
        self.uif.OutP.setText(expr)
    def btn_seven(self):
        expr = self.uif.OutP.text()
        expr += '7'
        self.uif.OutP.setText(expr)
    def btn_six(self):
        expr = self.uif.OutP.text()
        expr += '6'
        self.uif.OutP.setText(expr)
    def btn_five(self):
        expr = self.uif.OutP.text()
        expr += '5'
        self.uif.OutP.setText(expr)
    def btn_four(self):
        expr = self.uif.OutP.text()
        expr += '4'
        self.uif.OutP.setText(expr)
    def btn_three(self):
        expr = self.uif.OutP.text()
        expr += '3'
        self.uif.OutP.setText(expr)
    def btn_two(self):
        expr = self.uif.OutP.text()
        expr += '2'
        self.uif.OutP.setText(expr)
    def btn_one(self):
        expr = self.uif.OutP.text()
        expr += '1'
        self.uif.OutP.setText(expr)
    def btn_zero(self):
        expr = self.uif.OutP.text()
        expr += '0'
        self.uif.OutP.setText(expr)
    def btn_dot(self):
        expr = self.uif.OutP.text()
        expr += '.'
        self.uif.OutP.setText(expr)
        
    #ส่วนแสดงผล
    def btn_clear(self):
        expr = ''
        self.uif.OutP.setText(expr)
    def btn_divide(self):
        expr = self.uif.OutP.text()
        expr += '/'
        self.uif.OutP.setText(expr)
    def btn_multiply(self):
        expr = self.uif.OutP.text()
        expr += '*'
        self.uif.OutP.setText(expr)
    def btn_minus(self):
        expr = self.uif.OutP.text()
        expr += '-'
        self.uif.OutP.setText(expr)
    def btn_plus(self):
        expr = self.uif.OutP.text()
        expr += '+'
        self.uif.OutP.setText(expr)
    def btn_ans(self):
        try:
            expr = self.uif.OutP.text()
            result = "%g"%(eval(expr))
        except Exception:
            result = "∞"
        self.uif.OutP.setText(result)
    
    #เลื่อนหน้าต่าง
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

#!อย่ายุ่งกับส่วนนี้
app = QtWidgets.QApplication(sys.argv)
Ncal = Calculator()
Ncal.show()
app.exec_()
#!~~~~~~~~~~~~~~~~