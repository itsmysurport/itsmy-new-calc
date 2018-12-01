from new_calc_ui import *

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
    self.buttonPlus.clicked.connect(lambda x : self.operator('+'))
    self.buttonMinus.clicked.connect(lambda x : self.operator('-'))
    self.buttonMulti.clicked.connect(lambda x : self.operator('*'))
    self.buttonDivide.clicked.connect(lambda x : self.operator('/'))
    self.resultButton.clicked.connect(self.resultFunc)

def resultFunc(self):
    if self.oper:
        self.second = self.result.text()

        self.resultLabel = str(eval(self.first + self.oper + self.second))
        
        self.first = ''
        self.second = ''
        self.oper = ''

        self.result.setText(str(self.resultLabel))

def operator(self, a):
    if not self.oper:
        self.first = self.result.text()
        self.resultLabel = '0'
        self.result.setText(self.resultLabel)
        self.oper = a
        print(self.first)

def addNumber(self, a):
    if (len(self.resultLabel) == 1) and (self.resultLabel[0] == '0'):
        if a == '0':
            pass
        else:
            self.resultLabel = a
    else:
        self.resultLabel += a
    self.result.setText(self.resultLabel)

Ui_New_calc.numberEvent = numberEvent
Ui_New_calc.addNumber = addNumber
Ui_New_calc.operator = operator
Ui_New_calc.resultFunc = resultFunc

Ui_New_calc.resultLabel = ''
Ui_New_calc.first = ''
Ui_New_calc.second = ''
Ui_New_calc.oper = ''

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    New_calc = QtWidgets.QMainWindow()
    ui = Ui_New_calc()
    ui.setupUi(New_calc)
    ui.numberEvent()
    New_calc.show()
    sys.exit(app.exec_())
