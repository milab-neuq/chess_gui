import time

from PyQt5.QtCore import Qt, QTimer, QTime, pyqtSignal
from PyQt5.QtGui import QResizeEvent, QFont
from PyQt5.QtWidgets import QWidget, QLabel, QMessageBox


class totalStepTimer(QLabel):
    TLE_game_over_signal = pyqtSignal()

    def __init__(self, parent=None, time_limit=None):
        super().__init__(parent)
        self.timelimit = time_limit

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)

        self.time = QTime(0, 0, 0)
        self.start_time = None
        self.pause_time = None

        self.init_label()

    def init_label(self):
        self.setMinimumSize(250, 30)
        self.setAlignment(Qt.AlignCenter)
        self.setText("total time:    00:00:00")
        self.setFont(QFont('Arial', 13))

    def reset_timer(self):
        self.timer.stop()
        self.time.setHMS(0, 0, 0)
        self.start_time = None
        self.pause_time = None
        self.setText("total time:    " + str(self.time.toString('hh:mm:ss')))

    def resume_timer(self):
        now = time.perf_counter()
        # 计算暂停时间
        pause_duration = now - self.pause_time
        self.start_time += pause_duration  # 把暂停时间加入开始计时的时间点
        self.pause_time = None
        self.timer.start(50)

    def start_timer(self):
        self.start_time = time.perf_counter()  # 记录开始计时的时间点
        self.timer.start(50)  # 1000毫秒 = 1秒

    def pause_timer(self):
        self.timer.stop()
        self.pause_time = time.perf_counter()    # 记录暂停计时的时间点

    def update_time(self):
        now = time.perf_counter()
        # 计算计时时间
        elapsed_time = now - self.start_time
        self.time.setHMS(0, 0, 0)
        self.time = self.time.addMSecs(int(elapsed_time * 1000))
        self.setText("total time:    " + str(self.time.toString('hh:mm:ss')))
        if self.time >= self.timelimit:
            self.TLE_game_over_signal.emit()

    def show_warning(self, message):
        meg = QMessageBox()
        meg.setText(message)
        meg.setIcon(QMessageBox.Warning)
        meg.exec_()
