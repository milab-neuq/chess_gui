from PyQt5.QtWidgets import QMainWindow, QGridLayout, QHBoxLayout, QApplication, QAction, QSizePolicy
from PyQt5.QtGui import QIcon, QResizeEvent
from PyQt5.QtCore import pyqtSignal
from chessboard_interface import chessboard_interface
from net_setting_interface import net_setting_interface
from engine_interface import engine_interface
from player_interface import player_interface


class main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.chessboard_interface = chessboard_interface(self)
        self.player_interface = player_interface(self)
        self.net_setting_interface = net_setting_interface()
        self.engine_interface = engine_interface()
        self.init_main_window()
        self.connect_signal_to_slot()

    def connect_signal_to_slot(self):
        self.chessboard_interface.game_over_signal.connect(self.player_interface.game_over)
        self.chessboard_interface.resume_timer_signal.connect(self.player_interface.resume_timer)
        self.chessboard_interface.start_timer_signal.connect(self.player_interface.start_timer)
        self.chessboard_interface.pause_timer_signal.connect(self.player_interface.pause_timer)
        self.player_interface.black.withdraw_signal.connect(self.chessboard_interface.withdraw)
        self.player_interface.white.withdraw_signal.connect(self.chessboard_interface.withdraw)
        self.player_interface.TLE_game_over_signal.connect(self.chessboard_interface.TLE_game_over)

    def init_main_window(self):
        self.resize(1200, 850)
        self.setWindowTitle("NoGo")
        self.setWindowIcon(QIcon("image/棋盘icon.png"))

        self.init_menu()

        layout = QHBoxLayout(self)
        self.chessboard_interface.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.player_interface.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(self.chessboard_interface)
        layout.addWidget(self.player_interface)
        self.setLayout(layout)

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

    def init_menu(self):
        menu = self.menuBar()
        menu.setNativeMenuBar(False)

        game_menu = menu.addMenu("对局")

        new_game_act = QAction("新建对局", self)
        new_game_act.triggered.connect(self.new_game)
        game_menu.addAction(new_game_act)

        exit_game_act = QAction("退出", self)
        exit_game_act.triggered.connect(self.close)
        game_menu.addAction(exit_game_act)

        engine_menu = menu.addMenu("引擎")

        load_engine_act = QAction("加载AI引擎", self)
        load_engine_act.triggered.connect(self.engine_interface.load_engine)
        engine_menu.addAction(load_engine_act)

        unload_engine_act = QAction("卸载AI引擎", self)
        unload_engine_act.triggered.connect(self.engine_interface.unload_engine)
        engine_menu.addAction(unload_engine_act)

        net_menu = menu.addMenu("网络")

        net_setting_act = QAction("网络设置", self)
        net_setting_act.triggered.connect(self.net_setting_interface.net_setting)
        net_menu.addAction(net_setting_act)

        start_net_vs_act = QAction("开启网络对战", self)
        start_net_vs_act.triggered.connect(self.net_setting_interface.start_net_vs)
        net_menu.addAction(start_net_vs_act)

        close_net_vs_act = QAction("关闭网络对战", self)
        close_net_vs_act.triggered.connect(self.net_setting_interface.close_net_vs)
        net_menu.addAction(close_net_vs_act)

    def resizeEvent(self, a: QResizeEvent):
        super().resizeEvent(a)
        self.chessboard_interface.resize(self.height() - 100, self.height() - 50)
        self.player_interface.resize((self.height() - 100) // 3, self.height() - 50)
        self.player_interface.move(self.height() - 80, 20)

    def new_game(self):
        self.chessboard_interface.reset()
        self.player_interface.reset()
