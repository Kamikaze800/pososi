import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QSlider

SCREEN_SIZE = [400, 400]


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, *SCREEN_SIZE)
        self.setWindowTitle('Отображение картинки')

        ## Изображение
        self.pixmap = QPixmap('orig.jpg')
        # Если картинки нет, то QPixmap будет пустым,
        # а исключения не будет
        self.image = QLabel(self)
        self.image.move(80, 60)
        self.image.resize(250, 250)
        # Отображаем содержимое QPixmap в объекте QLabel
        self.slider = QSlider(self)
        # self.slider.setRange(0, 1)
        self.slider.valueChanged.connect(self.run)
        self.image.setPixmap(self.pixmap)

    def run(self):
        self.image.putalpha(self.slider.value())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())