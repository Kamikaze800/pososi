import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Calculator")
        self.layout = QVBoxLayout()
        self.secondary_label = QLabel()
        self.layout.addWidget(self.secondary_label)
        self.buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', 'CE', '+'],
            ['.', '±',  '='],
        ]

        self.text_edit = QLabel()
        self.layout.addWidget(self.text_edit)

        self.button_layout = QVBoxLayout()
        for row in self.buttons:
            h_layout = QHBoxLayout()
            for button_text in row:
                button = QPushButton(button_text)
                button.clicked.connect(self.handle_button_click)
                h_layout.addWidget(button)
            self.button_layout.addLayout(h_layout)

        self.layout.addLayout(self.button_layout)
        self.setLayout(self.layout)

    def handle_button_click(self):
        button = self.sender()
        clicked_text = button.text()
        current_text = self.secondary_label.text() + self.text_edit.text()

        if clicked_text in '+-/*':
            self.secondary_label.setText(f'{self.text_edit.text()}{clicked_text}')
            self.text_edit.setText('')
        elif clicked_text == '=':
            try:
                result = str(eval(current_text))
                self.text_edit.setText(result)
            except Exception as e:
                self.text_edit.setText('Error')
                print(e)
        else:
            self.text_edit.setText(self.text_edit.text() + clicked_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())