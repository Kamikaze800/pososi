import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Calculator")

        self.layout = QVBoxLayout()

        self.secondary_label = QLabel('')
        self.layout.addWidget(self.secondary_label)

        self.main_label = QLabel('')
        self.layout.addWidget(self.main_label)

        self.but_act = QHBoxLayout()

        self.number_buttons = [QPushButton('0'), QPushButton('1'), QPushButton('2'), QPushButton('3'), QPushButton('4'),
                               QPushButton('5'), QPushButton('6'), QPushButton('7'), QPushButton('8'), QPushButton('9')]
        ind = 0
        self.button_layout = QVBoxLayout()
        for i in self.number_buttons:
            if ind % 3 == 0:
                self.but_act.addLayout(self.button_layout)
                self.button_layout = QVBoxLayout()

            i.clicked.connect(self.handle_button_click)
            self.button_layout.addWidget(i)
            ind += 1

        self.clear_button = QPushButton('C')
        self.clear_button.clicked.connect(self.clear_c)
        self.button_layout.addWidget(self.clear_button)

        self.clear_entry_button = QPushButton('CE')
        self.clear_entry_button.clicked.connect(self.clear_e)
        self.button_layout.addWidget(self.clear_entry_button)

        self.float_point_button = QPushButton('.')
        self.float_point_button.clicked.connect(self.handle_button_click)
        self.button_layout.addWidget(self.float_point_button)

        self.but_act.addLayout(self.button_layout)

        self.button_layout2 = QVBoxLayout()

        self.divide_button = QPushButton('/')
        self.divide_button.clicked.connect(self.handle_button_click)
        self.button_layout2.addWidget(self.divide_button)

        self.multiply_button = QPushButton('*')
        self.multiply_button.clicked.connect(self.handle_button_click)
        self.button_layout2.addWidget(self.multiply_button)

        self.substract_button = QPushButton('-')
        self.substract_button.clicked.connect(self.handle_button_click)
        self.button_layout2.addWidget(self.substract_button)

        self.add_button = QPushButton('+')
        self.add_button.clicked.connect(self.handle_button_click)
        self.button_layout2.addWidget(self.add_button)

        self.plus_minus_button = QPushButton('±')
        self.plus_minus_button.clicked.connect(self.plus_minus_but)
        self.button_layout2.addWidget(self.plus_minus_button)

        self.equals_button = QPushButton('=')
        self.equals_button.clicked.connect(self.handle_button_click)
        self.button_layout2.addWidget(self.equals_button)

        self.but_act.addLayout(self.button_layout2)

        self.layout.addLayout(self.but_act)

        # self.button_layout = QVBoxLayout()
        # for row in self.buttons:
        #     h_layout = QHBoxLayout()
        #     for button_text in row:
        #         button = QPushButton(button_text)
        #         button.clicked.connect(self.handle_button_click)
        #         h_layout.addWidget(button)
        #     self.button_layout.addLayout(h_layout)

        # self.layout.addLayout(self.button_layout)
        self.setLayout(self.layout)

    def plus_minus_but(self):
        self.main_label.setText(f'-{self.main_label.text()}')

    def clear_c(self):
        self.secondary_label.setText('')
        self.main_label.setText('')

    def clear_e(self):
        self.main_label.setText('')

    def handle_button_click(self):
        button = self.sender()
        clicked_text = button.text()
        current_text = self.secondary_label.text() + self.main_label.text()

        if clicked_text in '+-/*':
            self.secondary_label.setText(f'{self.main_label.text()}{clicked_text}')
            self.main_label.setText('')
        elif clicked_text == '=':
            try:
                result = str(eval(current_text))
                self.main_label.setText(result)
                self.secondary_label.setText('')
            except Exception as e:
                self.main_label.setText('Error')
                print(e)
        else:
            self.main_label.setText(self.main_label.text() + clicked_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
