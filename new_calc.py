from new_calc_ui import *

resultLabel = ''

def numberEvent(self):
    self.button1_0.clicked.connect(lambda x : self.addNumber('0'))
    self.button1_1.clicked.connect(lambda x : self.addNumber('1'))
    self.button1_2.clicked.connect(lambda x : self.addNumber('2'))
    self.button1_3.clicked.connect(lambda x : self.addNumber('3'))
    self.button1_4.clicked.connect(lambda x : self.addNumber('4'))
    self.button1_5.clicked.connect(lambda x : self.addNumber('5'))
    self.button1_6.clicked.connect(lambda x : self.addNumber('6'))
    self.button1_7.clicked.connect(lambda x : self.addNumber('7'))
    self.button1_8.clicked.connect(lambda x : self.addNumber('8'))
    self.button1_9.clicked.connect(lambda x : self.addNumber('9'))
#    self.buttonPlus.clicked.connect()

def addNumber(self, a):
    global resultLabel
    if (len(resultLabel) == 1) and (resultLabel[0] == '0'):
        if a == '0':
            pass
        else:
            resultLabel = a
    else:
        resultLabel += a
    self.result.setText(resultLabel)

Ui_New_calc.numberEvent = numberEvent
Ui_New_calc.addNumber = addNumber

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    New_calc = QtWidgets.QMainWindow()
    ui = Ui_New_calc()
    ui.setupUi(New_calc)
    ui.numberEvent()
    New_calc.show()
    sys.exit(app.exec_())
