from PyQt5.QtCore import Qt, QTime, pyqtSignal
from PyQt5.QtGui import QResizeEvent
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from player import player
from chessboard import chessboard


class player_interface(QWidget):
    TLE_game_over_signal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.black = player(self, color=chessboard.BLACK, time_limit=QTime(0, 15, 0))
        self.white = player(self, color=chessboard.WHITE, time_limit=QTime(0, 15, 0))
        self.init_widget()
        self.connect_signal_to_slot()

    def connect_signal_to_slot(self):
        self.black.TLE_game_over_signal.connect(self.TLE_game_over)
        self.white.TLE_game_over_signal.connect(self.TLE_game_over)

    def init_widget(self):
        # self.setGeometry(800, 20, 300, 800)
        self.setMinimumSize(300, 800)
        self.setStyleSheet("border: 1px solid black;")
        layout = QVBoxLayout(self)
        layout.addWidget(self.black)
        layout.addWidget(self.white)
        self.setLayout(layout)

    def resizeEvent(self, e: QResizeEvent):
        super().resizeEvent(e)
        self.black.resize(self.width(), self.height() // 2)
        self.white.resize(self.width(), self.height() // 2)

    def reset(self):
        self.black.reset_timer()
        self.white.reset_timer()

    def resume_timer(self, current_player):
        self.black.resume_timer(current_player)
        self.white.resume_timer(current_player)

    def start_timer(self, current_player):
        self.black.start_timer(current_player)
        self.white.start_timer(current_player)

    def pause_timer(self, current_player):
        self.black.pause_timer(current_player)
        self.white.pause_timer(current_player)

    def game_over(self):
        self.black.pause_timer(chessboard.BLACK)
        self.white.pause_timer(chessboard.WHITE)

    def TLE_game_over(self):
        self.TLE_game_over_signal.emit()
