import numpy as np
from PyQt5.QtCore import pyqtSignal, Qt, QPoint, QSize
from PyQt5.QtGui import QPainter, QPen, QMouseEvent, QResizeEvent, QFont
from PyQt5.QtWidgets import QWidget, QMessageBox

from chessboard import chessboard
from chess import chess


class chessboard_interface(QWidget):
    game_over_signal = pyqtSignal()
    resume_timer_signal = pyqtSignal(int)
    start_timer_signal = pyqtSignal(int)
    pause_timer_signal = pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.is_black_AI = False
        self.is_white_AI = False
        self.white_timer_started = False
        self.is_start = False
        self.board_len = 9
        self.chess_list = []
        self.chess_pos = []
        self.chessboard = chessboard(board_len=9)

        self.margin = 5
        self.grid_size = 78
        self.chess_size = 60
        self.setMinimumSize(800, 800)
        self.setMouseTracking(True)
        self.connect_signal_to_slot()

    def connect_signal_to_slot(self):
        pass

    def mousePressEvent(self, e: QMouseEvent):
        cor = self.get_mat_position(e.pos())
        self.put_chess(cor)

    def resizeEvent(self, e: QResizeEvent):
        super().resizeEvent(e)

        if e.oldSize().width() > 0:
            percentage = min(self.size().width() / e.oldSize().width(), self.size().height() / e.oldSize().height())
            self.grid_size = int(self.grid_size * percentage)
            self.chess_size = int(self.chess_size * percentage)

        left, top = self.__getMargin()
        for i in range(len(self.chess_list)):
            self.chess_list[i].resize_chess(self.chess_size)
            self.chess_list[i].move(self.chess_pos[i] * self.grid_size +
                                    QPoint(left - self.chess_size // 2, top - self.chess_size // 2))

    def get_mat_position(self, pos):
        """ 获取Qt坐标 """
        n = self.board_len
        left, top = self.__getMargin()
        poses = np.array(
            [[[i * self.grid_size + left, (self.board_len - 1 - j) * self.grid_size + top] for j in range(n)]
             for i in range(n)])
        # Qt坐标系与矩阵的相反
        distances = (poses[:, :, 0] - pos.x()) ** 2 + (poses[:, :, 1] - pos.y()) ** 2
        col, row = np.where(distances == distances.min())
        return col[0], row[0]

    def paintEvent(self, e):
        # 绘制棋盘
        super().paintEvent(e)
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing)
        # 绘制网格
        left, top = self.__getMargin()
        font = QFont()
        font.setPixelSize(25)
        font.setBold(True)
        font.setStyle(QFont.StyleNormal)
        painter.setFont(font)
        for i in range(self.board_len):
            x = y = self.margin + i * self.grid_size
            x = left + i * self.grid_size
            y = top + i * self.grid_size
            # 竖直线
            width = 2 if i in [0, self.board_len - 1] else 1
            painter.setPen(QPen(Qt.black, width))
            painter.drawText(x, self.width() - top + top // 2, chr(ord('A') + i))
            painter.drawLine(x, top, x, self.height() - top)
            # 水平线
            painter.drawText(left - left // 2, y, chr(ord('8') - i))
            painter.drawLine(left, y, self.width() - left - 1, y)
        # 绘制落子提示
        if len(self.chess_list) == 0:
            return
        pen = QPen(Qt.red, 20, Qt.SolidLine)
        painter.setPen(pen)
        last_chess = self.chess_list[-1]
        x, y = last_chess.pos().x(), last_chess.pos().y()
        painter.drawPoint(QPoint(x + self.chess_size // 5, y + self.chess_size // 5))
        self.update()

    def withdraw(self, withdraw_player):
        """ 悔棋 """
        if not self.is_start:
            self.show_warning("对局尚未开始!")
            return
        if len(self.chess_list) == 0:
            self.show_warning("无法悔棋!")
            return

        if self.chessboard.current_player == -withdraw_player:
            c = self.chess_list.pop()
            c.deleteLater()
            self.chess_pos.pop()
            self.pause_timer_signal.emit(self.chessboard.current_player)
            self.chessboard.withdraw()
            self.resume_timer_signal.emit(self.chessboard.current_player)
        else:
            for i in range(2):
                c = self.chess_list.pop()
                c.deleteLater()
                self.chess_pos.pop()
                self.chessboard.withdraw()

    def __getMargin(self):
        """ 获取棋盘边距 """
        left = (self.width() - (self.board_len - 1) * self.grid_size) // 2
        top = (self.height() - (self.board_len - 1) * self.grid_size) // 2
        return left, top

    def reset(self):
        self.chessboard.clear()
        for c in self.chess_list:
            c.deleteLater()
        self.chess_list.clear()
        self.chess_pos.clear()
        self.is_start = True
        self.white_timer_started = False

    def put_chess(self, pos):
        """ 落子 """
        if not self.is_start:
            self.show_warning("对局尚未开始！")
            return False
        x, y = pos
        location = x * self.chessboard.board_len + y
        ok = self.chessboard.do_action(location)
        if not ok:
            return False
        self.pause_timer_signal.emit(-self.chessboard.current_player)
        c = chess(self, color=-self.chessboard.current_player, size=self.chess_size)
        left, top = self.__getMargin()
        self.chess_pos.append(QPoint(x, self.board_len - 1 - y))
        chessPos = QPoint(x, self.board_len - 1 - y) * self.grid_size + QPoint(left - self.chess_size // 2, top - self.chess_size // 2)
        c.show()
        c.move(chessPos)
        self.chess_list.append(c)

        res = self.chessboard.is_game_over(location)

        if self.chessboard.current_player == chessboard.WHITE and self.white_timer_started is False:
            self.white_timer_started = True
            self.start_timer_signal.emit(self.chessboard.current_player)
        elif res == 0:
            self.resume_timer_signal.emit(self.chessboard.current_player)

        if res:
            if self.chessboard.current_player == self.chessboard.BLACK:
                self.show_meg("黑方获胜")
            else:
                self.show_meg("白方获胜")
            self.is_start = False
            self.game_over_signal.emit()

    def TLE_game_over(self):
        current_player = self.chessboard.current_player
        self.is_start = False
        self.game_over_signal.emit()
        if current_player == chessboard.BLACK:
            self.show_meg("黑方超时，白方获胜")
        else:
            self.show_meg("白方超时，黑方获胜")

    def show_warning(self, message):
        meg = QMessageBox()
        meg.setIcon(QMessageBox.Warning)
        meg.setText(message)
        meg.setWindowTitle("Error")
        meg.exec_()

    def show_meg(self, message):
        meg = QMessageBox()
        meg.setText(message)
        meg.setWindowTitle("对局结束")
        meg.exec_()
