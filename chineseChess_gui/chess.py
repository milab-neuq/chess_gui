from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QVBoxLayout
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor
from PyQt5.QtCore import Qt, QRect
import sys
import constant as constants


class Chessboard(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 550, 650)
        self.setWindowTitle('Chinese Chess')

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawChessboard(qp)
        qp.end()

    def drawChessboard(self, qp):
        # 绘制棋盘网格和边框的代码
        pass


class Pieces(QLabel):
    def __init__(self, player, x, y):
        super().__init__()
        self.initPiece(player, x, y)

    def initPiece(self, player, x, y):
        self.imagskey = self.getImagekey()
        self.image = QPixmap(constants.pieces_images[self.imagskey])
        self.x = x
        self.y = y
        self.player = player
        self.rect = QRect()

    def displaypieces(self, qp):
        self.rect.setLeft(constants.Start_X + self.x * constants.Line_Span - self.image.rect().width() / 2)
        self.rect.setTop(constants.Start_Y + self.y * constants.Line_Span - self.image.rect().height() / 2)
        qp.drawPixmap(self.rect, self.image)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.displaypieces(qp)
        qp.end()

    # 其他方法的实现保持不变


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        chessboard = Chessboard()
        piece = Pieces(constants.player1Color, 1, 1)

        # 将Chessboard和Pieces添加到主窗口中
        chessboardLayout = QVBoxLayout()
        chessboardLayout.addWidget(chessboard)
        chessboardLayout.addWidget(piece)
        self.setLayout(chessboardLayout)

        self.setWindowTitle('Chinese Chess')
        self.setGeometry(100, 100, 550, 650)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
