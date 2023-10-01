import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QWidget, QRadioButton, QButtonGroup


# осталось добавить условие победы
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tic Tac Toe")

        layout = QGridLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.button_group = QButtonGroup()

        rb1 = QRadioButton("X")
        rb1.setChecked(True)
        self.rb1 = rb1
        self.button_group.addButton(rb1)
        layout.addWidget(rb1, 4, 0)

        rb2 = QRadioButton("0")
        self.button_group.addButton(rb2)
        layout.addWidget(rb2, 4, 2)

        new_game = QPushButton('new', self)
        self.new_game = new_game
        self.new_game.clicked.connect(self.new)
        layout.addWidget(self.new_game, 4, 1)
        self.layout = layout

        self.buttons = []
        self.schet = 0

        self.spawn()

    def spawn(self):
        for i in range(3):
            row = []
            for j in range(3):
                button = QPushButton()
                button.setFixedSize(100, 100)
                button.clicked.connect(lambda x: self.on_button_clicked(self.schet, i, j))
                self.layout.addWidget(button, i, j)
                row.append(button)
            self.buttons.append(row)

    def new(self):
        self.spawn()
        self.schet = 0

    def on_button_clicked(self, schet, i, j):
        button = self.sender()
        # if self.rb1.text() == "X"

        if self.rb1.isChecked():
            if schet % 2:
                button.setText('0')
            else:
                button.setText('X')
        else:
            if schet % 2:
                button.setText('X')
            else:
                button.setText('0')

        self.schet += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
