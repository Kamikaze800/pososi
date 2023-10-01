import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Calculator")
        self.layout = QVBoxLayout()
        self.secondary_label = QLabel()
        self.layout.addWidget(self.secondary_label)
        self.number_buttons = [QPushButton('0'), QPushButton('1'), QPushButton('2'), QPushButton('3'), QPushButton('4'),
                               QPushButton('5'), QPushButton('6'), QPushButton('7'), QPushButton('8'), QPushButton('9')]
        for i in self.number_buttons:
            i.clicked.connect(self.handle_button_click)
            self.layout.addWidget(i)

        self.clear_button = QPushButton('C')
        self.clear_button.clicked.connect(self.clear_c)
        self.layout.addWidget(self.clear_button)

        self.clear_entry_button = QPushButton('CE')
        self.clear_entry_button.clicked.connect(self.clear_e)
        self.layout.addWidget(self.clear_entry_button)

        self.main_label = QLabel('xxx')
        self.layout.addWidget(self.main_label)


        self.button_layout = QVBoxLayout()
        # for row in self.buttons:
        #     h_layout = QHBoxLayout()
        #     for button_text in row:
        #         button = QPushButton(button_text)
        #         button.clicked.connect(self.handle_button_click)
        #         h_layout.addWidget(button)
        #     self.button_layout.addLayout(h_layout)

        # self.layout.addLayout(self.button_layout)
        self.setLayout(self.layout)

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
            except Exception as e:
                self.main_label.setText('Error')
                print(e)
        else:
            self.main_label.setText(self.text_edit.text() + clicked_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
