from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from random import randint

class NimStrikesBack(QWidget):
    def __init__(self):
        super(NimStrikesBack, self).__init__()
        self.initUI()

    def initUI(self):
        self.X = randint(1, 100)
        self.Y = randint(1, 10)
        self.Z = randint(1, 10)
        self.remaining_turns = 10

        self.lbl_X = QLabel(str(self.X))
        self.lbl_remaining_turns = QLabel("Remaining Turns: " + str(self.remaining_turns))
        self.result_label = QLabel()

        self.btnp = QPushButton("+ " + str(self.Y))
        self.btnp.clicked.connect(self.increase_X)

        self.btnm = QPushButton("- " + str(self.Z))
        self.btnm.clicked.connect(self.decrease_X)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl_X)
        vbox.addWidget(self.btnp)
        vbox.addWidget(self.btnm)
        vbox.addWidget(self.lbl_remaining_turns)
        vbox.addWidget(self.result_label)

        self.setLayout(vbox)
        self.setWindowTitle('Nim Strikes Back')
        self.show()

    def increase_X(self):
        self.X += self.Y
        self.lbl_X.setText(str(self.X))
        self.remaining_turns -= 1
        self.lbl_remaining_turns.setText("Remaining Turns: " + str(self.remaining_turns))
        self.check_game_state()

    def decrease_X(self):
        self.X -= self.Z
        self.lbl_X.setText(str(self.X))
        self.remaining_turns -= 1
        self.lbl_remaining_turns.setText("Remaining Turns: " + str(self.remaining_turns))
        self.check_game_state()

    def check_game_state(self):
        if self.X == 0:
            self.result_label.setText("Congratulations! You won!")
            self.reset_game()
        elif self.remaining_turns == 0:
            self.result_label.setText("Game over! You lost!")
            self.reset_game()

    def reset_game(self):
        self.X = randint(1, 100)
        self.Y = randint(1, 10)
        self.Z = randint(1, 10)
        self.remaining_turns = 10
        self.lbl_X.setText(str(self.X))
        self.lbl_remaining_turns.setText("Remaining Turns: " + str(self.remaining_turns))
        self.result_label.setText("")

if __name__ == '__main__':
    app = QApplication([])
    game = NimStrikesBack()
    app.exec_()