`import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QWidget, QRadioButton, QButtonGroup, \
    QVBoxLayout, QCheckBox, QLineEdit, QPlainTextEdit


# осталось добавить условие победы
class MacOrder(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        layout = QVBoxLayout(self)
        self.ch1 = QCheckBox('Чизбургер', self)
        self.ch2 = QCheckBox('Гамбургер', self)
        self.ch3 = QCheckBox('Кока-кола', self)
        self.ch4 = QCheckBox('Наггетсы', self)
        order_btn = QPushButton('заказать', self)
        self.result = QPlainTextEdit('Ваш заказ', self)
        order_btn.clicked.connect(self.run)
        self.menu_checkboxes = [self.ch1, self.ch2, self.ch3, self.ch4]
        layout.addWidget(self.ch1)
        layout.addWidget(self.ch2)
        layout.addWidget(self.ch3)
        layout.addWidget(self.ch4)
        layout.addWidget(order_btn)
        layout.addWidget(self.result)

    def run(self):
        tr = []
        self.result.setPlainText('')
        for i in range(len(self.menu_checkboxes)):
            if self.menu_checkboxes[i].checkState():
                # self.result.appendPlainText(f'{self.menu_checkboxes [i].text()}')
                tr.append(f'{self.menu_checkboxes[i].text()}')
        self.result.setPlainText('Ваш заказ:\n')
        for el in tr:
            self.result.appendPlainText(el)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MacOrder()
    window.show()
    sys.exit(app.exec())
`