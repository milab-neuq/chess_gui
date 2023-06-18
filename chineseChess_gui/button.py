from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt


class Button(QPushButton):
    def __init__(self, parent=None, msg='', left=0, top=0):
        super().__init__(parent)
        self.setGeometry(left, top, 150, 50)
        self.setStyleSheet("background-color: rgb(72, 61, 139); color: rgb(255, 255, 255);")
        self.setText(msg)
        self.setFont(QFont('kaiti', 20))

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.drawText(self.rect(), Qt.AlignCenter, self.text())


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('PyQt Button Example')

        self.button = Button(self, 'Click me', 125, 125)
        self.button.clicked.connect(self.onButtonClick)

    def onButtonClick(self):
        print('Button clicked')


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
