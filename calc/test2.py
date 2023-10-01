import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLabel

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Калькулятор")
        self.setGeometry(100, 100, 400, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        self.create_ui()

        self.current_input = "0"
        self.operator = None
        self.clear_on_next = False

    def create_ui(self):
        self.main_label = QLabel(self)
        self.main_label.setText("0")
        self.main_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.main_layout.addWidget(self.main_label)

        button_grid = QGridLayout()

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "+", "="
        ]

        row, col = 0, 0
        for button_text in buttons:
            button = QPushButton(button_text)
            button.clicked.connect(lambda _, text=button_text: self.on_button_click(text))
            button_grid.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        self.main_layout.addLayout(button_grid)

        clear_button = QPushButton("C")
        clear_button.clicked.connect(self.clear)
        clear_entry_button = QPushButton("CE")
        clear_entry_button.clicked.connect(self.clear_entry)
        plus_minus_button = QPushButton("±")
        plus_minus_button.clicked.connect(self.toggle_sign)

        button_layout = QVBoxLayout()
        button_layout.addWidget(clear_button)
        button_layout.addWidget(clear_entry_button)
        button_layout.addWidget(plus_minus_button)

        self.main_layout.addLayout(button_layout)

    def clear(self):
        self.current_input = "0"
        self.operator = None
        self.update_display()

    def clear_entry(self):
        self.current_input = "0"
        self.update_display()

    def on_button_click(self, button_text):
        if self.clear_on_next:
            self.clear()
        if self.current_input == "0" or self.current_input == "-0":
            self.current_input = button_text
        else:
            self.current_input += button_text
        self.update_display()

    def toggle_sign(self):
        if self.current_input != "0":
            if self.current_input[0] == "-":
                self.current_input = self.current_input[1:]
            else:
                self.current_input = "-" + self.current_input
            self.update_display()

    def set_operator(self, operator):
        if self.operator is not None:
            self.calculate()
        self.operator = operator

    def calculate(self):
        try:
            if self.operator:
                result = eval(self.current_input)
                if result == int(result):
                    self.current_input = str(int(result))
                else:
                    self.current_input = "{:.10f}".format(result)
                self.operator = None
        except ZeroDivisionError:
            self.current_input = "ОШИБКА"
        finally:
            self.clear_on_next = True
            self.update_display()

    def update_display(self):
        if len(self.current_input) > 11:
            self.main_label.setText("E")
        else:
            self.main_label.setText(self.current_input.lstrip("0"))
            self.clear_on_next = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())