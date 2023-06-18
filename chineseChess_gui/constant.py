from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QPainter, QColor, QPen
from PyQt5.QtCore import Qt

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 650
Start_X = 50
Start_Y = 50
Line_Span = 60

player1Color = 1
player2Color = 2
overColor = 3

BG_COLOR = QColor(200, 200, 200)
Line_COLOR = QColor(255, 255, 200)
TEXT_COLOR = QColor(255, 0, 0)

# 定义颜色
BLACK = QColor(0, 0, 0)
WHITE = QColor(255, 255, 255)
RED = QColor(255, 0, 0)
GREEN = QColor(0, 255, 0)
BLUE = QColor(0, 0, 255)

repeat = 0

pieces_images = {
    'b_rook': QPixmap("images/s2/b_c.gif"),
    'b_elephant': QPixmap("images/s2/b_x.gif"),
    'b_king': QPixmap("images/s2/b_j.gif"),
    'b_knigh': QPixmap("images/s2/b_m.gif"),
    'b_mandarin': QPixmap("images/s2/b_s.gif"),
    'b_cannon': QPixmap("images/s2/b_p.gif"),
    'b_pawn': QPixmap("images/s2/b_z.gif"),

    'r_rook': QPixmap("images/s2/r_c.gif"),
    'r_elephant': QPixmap("images/s2/r_x.gif"),
    'r_king': QPixmap("images/s2/r_j.gif"),
    'r_knigh': QPixmap("images/s2/r_m.gif"),
    'r_mandarin': QPixmap("images/s2/r_s.gif"),
    'r_cannon': QPixmap("images/s2/r_p.gif"),
    'r_pawn': QPixmap("images/s2/r_z.gif"),
}


class GameWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.setWindowTitle("Xiangqi Game")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw background
        painter.fillRect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, BG_COLOR)

        # Draw lines
        pen = QPen(Line_COLOR)
        pen.setWidth(2)
        painter.setPen(pen)
        for i in range(9):
            x = Start_X + i * Line_Span
            painter.drawLine(x, Start_Y, x, Start_Y + 9 * Line_Span)
        for j in range(10):
            y = Start_Y + j * Line_Span
            painter.drawLine(Start_X, y, Start_X + 8 * Line_Span, y)

        # Draw pieces
        for piece in pieces:
            x = Start_X + piece.x * Line_Span - piece.image.width() / 2
            y = Start_Y + piece.y * Line_Span - piece.image.height() / 2
            painter.drawPixmap(x, y, piece.image)

    def displayPieces(self):
        self.update()


class Pieces:
    def __init__(self, player, x, y):
        self.imagskey = self.getImagekey()
        self.image = pieces_images[self.imagskey]
        self.x = x
        self.y = y
        self.player = player

    def getImagekey(self):
        # Implementation of the method
        pass


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    gameWindow = GameWindow()

    pieces = []
    piece = Pieces(player1Color, 1, 1)
    pieces.append(piece)

    gameWindow.show()
    sys.exit(app.exec_())
