from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
from chessboard import chessboard


class chess(QLabel):
    def __init__(self, parent=None, color=None, size=None):
        super().__init__(parent)
        self.color = color
        if color == chessboard.BLACK:
            self.pixmap = QPixmap("image/black.png")
        else:
            self.pixmap = QPixmap("image/white.png")

        self.setPixmap(self.pixmap.scaled(
            size, size, Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def resize_chess(self, size):
        self.resize(size, size)
        self.setPixmap(self.pixmap.scaled(
            size, size, Qt.KeepAspectRatio, Qt.SmoothTransformation))
