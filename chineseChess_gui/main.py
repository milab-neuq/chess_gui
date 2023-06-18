import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QRect

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = QColor(255, 255, 255)
LINE_COLOR = QColor(0, 0, 0)
START_X = 50
START_Y = 50
LINE_SPAN = 50

# Piece colors
player1Color = QColor(255, 0, 0)
player2Color = QColor(0, 0, 255)


class Button(QPushButton):
    def __init__(self, parent, text, x, y):
        super().__init__(parent)
        self.setText(text)
        self.setGeometry(x, y, 100, 50)


class Piece:
    def __init__(self, player, x, y):
        self.player = player
        self.x = x
        self.y = y

    def display(self, painter):
        painter.setBrush(self.player)
        painter.drawEllipse(QRect(self.x, self.y, LINE_SPAN, LINE_SPAN))


class MainGame(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Python代码大全-中国象棋")
        self.setGeometry(100, 100, SCREEN_WIDTH, SCREEN_HEIGHT)

        self.button_go = Button(self, "重新开始", SCREEN_WIDTH - 100, 300)

        self.piecesList = []

        self.start_game()

    def start_game(self):
        self.piecesInit()

        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        self.drawChessboard(painter)
        self.piecesDisplay(painter)

    def drawChessboard(self, painter):
        mid_end_y = START_Y + 4 * LINE_SPAN
        min_start_y = START_Y + 5 * LINE_SPAN

        painter.setPen(QPen(LINE_COLOR, 1))
        for i in range(0, 9):
            x = START_X + i * LINE_SPAN
            if i == 0 or i == 8:
                y = START_Y + i * LINE_SPAN
                painter.drawLine(x, START_Y, x, START_Y + 9 * LINE_SPAN)
            else:
                painter.drawLine(x, START_Y, x, mid_end_y)
                painter.drawLine(x, min_start_y, x, START_Y + 9 * LINE_SPAN)

        for i in range(0, 10):
            x = START_X + i * LINE_SPAN
            y = START_Y + i * LINE_SPAN
            painter.drawLine(START_X, y, START_X + 8 * LINE_SPAN, y)

        speed_dial_start_x = START_X + 3 * LINE_SPAN
        speed_dial_end_x = START_X + 5 * LINE_SPAN
        speed_dial_y1 = START_Y + 0 * LINE_SPAN
        speed_dial_y2 = START_Y + 2 * LINE_SPAN
        speed_dial_y3 = START_Y + 7 * LINE_SPAN
        speed_dial_y4 = START_Y + 9 * LINE_SPAN

        painter.drawLine(speed_dial_start_x, speed_dial_y1, speed_dial_end_x, speed_dial_y2)
        painter.drawLine(speed_dial_start_x, speed_dial_y2, speed_dial_end_x, speed_dial_y1)
        painter.drawLine(speed_dial_start_x, speed_dial_y3, speed_dial_end_x, speed_dial_y4)
        painter.drawLine(speed_dial_start_x, speed_dial_y4, speed_dial_end_x, speed_dial_y3)

    def piecesInit(self):
        # Clear the pieces list
        self.piecesList.clear()

        # Player 1 pieces
        for i in range(0, 5):
            x = START_X + i * LINE_SPAN
            y = START_Y + 2 * LINE_SPAN
            self.piecesList.append(Piece(player1Color, x, y))

        # Player 2 pieces
        for i in range(0, 5):
            x = START_X + i * LINE_SPAN
            y = START_Y + 7 * LINE_SPAN
            self.piecesList.append(Piece(player2Color, x, y))

    def piecesDisplay(self, painter):
        for piece in self.piecesList:
            piece.display(painter)

    def buttonClicked(self):
        self.piecesInit()
        self.update()

    def resizeEvent(self, event):
        self.update()

    def setupUI(self):
        self.button_go.clicked.connect(self.buttonClicked)

    def closeEvent(self, event):
        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = MainGame()
    game.setupUI()
    sys.exit(app.exec_())
