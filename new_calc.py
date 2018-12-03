from new_calc_ui import *

def numberEvent(self):      # Event가 발생하면 실행되는 함수들
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
    self.buttonClear.clicked.connect(self.clearFunc)

def clearFunc(self):
    self.afterExpression = ''
    self.expression = ''
    self.seenLabel = ''
    self.inOper = False
    self.result.setText('')
    print("Cleared Expression.")

def resultFunc(self):   # = 을 눌렀을 때
    if len(self.expression) == 0:
        return
    if not self.inOper:
        return

    self.expression += self.result.text()
    print('Second : ', self.expression)
    self.expression = eval(self.expression)
    self.expression = str(self.expression)
    print('RESULT : ', self.expression)
    self.result.setText(self.expression)

    self.afterExpression = self.result.text()
    self.expression = ''
    self.seenLabel = ''
    self.inOper = False

    # if self.oper:
    #     self.sec  ond = self.result.text()
    #
    #     self.resultLabel = str(eval(self.first + self.oper + self.second))
    #
    #     self.first = ''
    #     self.second = ''
    #     self.oper = ''
    #
    #     self.result.setText(str(self.resultLabel))

def operator(self, a):      # 연산자를 눌렀을 때
    print("Clicked operator (Inoper): ", self.inOper, self.expression)

    self.expression += self.afterExpression
    self.afterExpression = ''
    if len(self.expression) == 0:
        return
    if self.inOper:
        return
    self.expression += a
    self.seenLabel = '0'
    self.inOper = True
    self.result.setText(self.seenLabel)
    print('Add OPER : ', self.expression)

    # if not self.oper:    # if not self.oper:
    #     self.first = self.result.text()
    #     self.resultLabel = '0'
    #     self.result.setText(self.resultLabel)
    #     self.oper = a
    #     print(self.first)
    #     self.first = self.result.text()
    #     self.resultLabel = '0'
    #     self.result.setText(self.resultLabel)
    #     self.oper = a
    #     print(self.first)

def addNumber(self, a):     # 숫자를 눌렀을 때

    self.seenLabel += a
    self.seenLabel = str(int(self.seenLabel))    # Ex) '000001' -> '1'
    self.result.setText(self.seenLabel)

    self.afterExpression = self.seenLabel
    print('AFTER : ', self.afterExpression)

    # if (len(self.resultLabel) == 1) and (self.resultLabel[0] == '0'):
    #     if a == '0':
    #         pass
    #     else:
    #         self.resultLabel = a
    # else:
    #     self.resultLabel += a
    # self.result.setText(self.resultLabel)


Ui_New_calc.numberEvent = numberEvent
Ui_New_calc.addNumber = addNumber
Ui_New_calc.operator = operator
Ui_New_calc.resultFunc = resultFunc
Ui_New_calc.clearFunc = clearFunc

Ui_New_calc.afterExpression = ''
Ui_New_calc.expression = ''
Ui_New_calc.seenLabel = ''
Ui_New_calc.inOper = False  #연산자가 있는지

# Remove Code
# Ui_New_calc.resultLabel = ''
# Ui_New_calc.first = ''
# Ui_New_calc.second = ''
# Ui_New_calc.oper = ''


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    New_calc = QtWidgets.QMainWindow()
    ui = Ui_New_calc()
    ui.setupUi(New_calc)
    ui.numberEvent()
    New_calc.show()
    sys.exit(app.exec_())
