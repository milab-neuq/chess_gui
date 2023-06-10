from PyQt5.QtCore import QTime, pyqtSignal, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

from chessboard import chessboard
from totalStepTimer import totalStepTimer
from singleStepTimer import singleStepTimer


class player(QWidget):
    withdraw_signal = pyqtSignal(int)
    TLE_game_over_signal = pyqtSignal()

    def __init__(self, parent=None, color=None, time_limit=None):
        super().__init__(parent)
        self.totalStepTimer = totalStepTimer(self, time_limit)
        self.singleStepTimer = singleStepTimer(self)
        self.color = color
        self.init_widget()
        self.connect_signal_to_slot()

    def connect_signal_to_slot(self):
        self.totalStepTimer.TLE_game_over_signal.connect(self.TLE_game_over)

    def TLE_game_over(self):
        self.TLE_game_over_signal.emit()

    def init_widget(self):
        self.resize(250, 250)
        self.setMinimumSize(250, 200)
        layout = QVBoxLayout()

        player_name_label = QLabel(self)

        font = QFont()
        font.setPixelSize(25)
        font.setBold(True)
        font.setStyle(QFont.StyleNormal)

        player_name_label.setFont(font)
        player_name_label.setAlignment(Qt.AlignCenter)
        if self.color == chessboard.BLACK:
            player_name_label.setText("黑方（先手）")
        else:
            player_name_label.setText("白方（后手）")
        player_name_label.resize(100, 30)
        player_name_label.setMinimumSize(100, 30)

        withdraw_button = QPushButton(self)
        withdraw_button.setText("悔棋")
        withdraw_button.clicked.connect(self.withdraw)
        withdraw_button.resize(60, 50)
        withdraw_button.setMinimumSize(60, 50)

        layout.addWidget(player_name_label)
        layout.addWidget(self.totalStepTimer)
        layout.addWidget(self.singleStepTimer)

        layout.addWidget(withdraw_button)
        self.setLayout(layout)

    def withdraw(self):
        self.withdraw_signal.emit(self.color)

    def reset_timer(self):
        self.totalStepTimer.reset_timer()
        self.singleStepTimer.reset_timer()
        if self.color == chessboard.BLACK:
            self.start_timer(self.color)

    def resume_timer(self, current_player):
        if current_player != self.color:
            return
        self.totalStepTimer.resume_timer()
        self.singleStepTimer.resume_timer()

    def start_timer(self, current_player):
        if current_player != self.color:
            return
        self.totalStepTimer.start_timer()
        self.singleStepTimer.start_timer()

    def pause_timer(self, current_player):
        if current_player != self.color:
            return
        self.totalStepTimer.pause_timer()
        self.singleStepTimer.pause_timer()
