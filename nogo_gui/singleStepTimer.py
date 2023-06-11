import time

from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel


class singleStepTimer(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)

        self.time = QTime(0, 0, 0)
        self.start_time = None

        self.init_label()

    def init_label(self):
        self.setMinimumSize(250, 30)
        self.setAlignment(Qt.AlignCenter)
        self.setText("single time: 00:00:00")
        self.setFont(QFont('Arial', 13))

    def reset_timer(self):
        self.timer.stop()
        self.time.setHMS(0, 0, 0)
        self.start_time = None
        self.setText("single time: " + str(self.time.toString('hh:mm:ss')))

    def resume_timer(self):
        self.time.setHMS(0, 0, 0)
        self.start_time = time.perf_counter()
        self.timer.start(50)

    def start_timer(self):
        self.time.setHMS(0, 0, 0)
        self.start_time = time.perf_counter()  # 记录开始计时的时间点
        self.timer.start(50)  # 1000毫秒 = 1秒

    def pause_timer(self):
        self.timer.stop()

    def update_time(self):
        now = time.perf_counter()
        # 计算计时时间
        elapsed_time = now - self.start_time
        self.time.setHMS(0, 0, 0)
        self.time = self.time.addMSecs(int(elapsed_time * 1000))
        self.setText("single time: " + str(self.time.toString('hh:mm:ss')))
