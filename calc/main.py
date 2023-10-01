import math
import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('calc.ui', self)  # Загружаем дизайн
        self.res = ''
        self.add_functions()

    def act(self):
        # if '+' in self.res:
        #     self.table.display(eval(self.res))
        # else:
        self.res = f'{eval(self.res)}' + self.sender().text()
        # self.table.display(eval(self.res))

    def sqrt(self):
        self.res = f'{round(math.sqrt(int(self.res)), 1)}'
        self.table.display(self.res)

    def eq(self):
        self.res = f'{eval(self.res)}'
        self.table.display(self.res)

    def factor(self):
        self.res = f'{math.factorial(int(self.res))}'
        self.table.display(self.res)

    def stepen(self):
        self.res = f'{eval(self.res)}' + '**'

    def vyvod(self):
        if self.table.value() == 0 or self.res[-1] in '-+*/^':
            self.table.display(f'{self.sender().text()}')
        else:
            self.table.display(f'{int(self.table.value())}' + self.sender().text())
        self.res += self.sender().text()

    def div(self):
        self.table.display(f'{eval(self.res)}')
        self.res = f'{eval(self.res)}' + '/'

    def dot(self):
        self.res = str(float(f'{eval(self.res)}+"."'))
        self.table.display(self.res)

    def add_functions(self):
        # self.table.display(self.btn2.text())
        # self.btn1.clicked.connect(lambda: self.write_number(self.btn_1.text()))
        self.btn1.clicked.connect(self.vyvod)
        self.btn2.clicked.connect(self.vyvod)
        self.btn3.clicked.connect(self.vyvod)
        self.btn4.clicked.connect(self.vyvod)
        self.btn5.clicked.connect(self.vyvod)
        self.btn6.clicked.connect(self.vyvod)
        self.btn7.clicked.connect(self.vyvod)
        self.btn8.clicked.connect(self.vyvod)
        self.btn9.clicked.connect(self.vyvod)
        self.btn0.clicked.connect(self.vyvod)

        self.btn_plus.clicked.connect(self.act)
        self.btn_minus.clicked.connect(self.act)
        self.btn_mult.clicked.connect(self.act)

        self.btn_eq.clicked.connect(self.eq)
        self.btn_sqrt.clicked.connect(self.sqrt)
        self.btn_fact.clicked.connect(self.factor)
        self.btn_pow.clicked.connect(self.stepen)
        self.btn_div.clicked.connect(self.div)
        self.btn_dot.clicked.connect(self.act)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec_())
