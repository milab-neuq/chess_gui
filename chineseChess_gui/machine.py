import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
import constant as constants
from chess import listPiecestoArr


class XiangqiApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Xiangqi App")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.status_label = QLabel("Status Label")
        self.layout.addWidget(self.status_label)

        self.button = QPushButton("Get Play Info")
        self.button.clicked.connect(self.get_play_info)
        self.layout.addWidget(self.button)

        self.setGeometry(200, 200, 300, 200)

    def get_play_info(self):
        listpieces = []  # Modify to include your list of pieces
        play_info = self.movedeep(listpieces, 1, constants.player2Color)
        self.status_label.setText(f"Play Info: {play_info}")

    def movedeep(self, listpieces, deepstep, player):
        # Existing movedeep code goes here, make sure to adjust the indentation

        piecesbest = None  # Replace None with your calculated best move

        return piecesbest


if __name__ == "__main__":
    app = QApplication(sys.argv)
    xiangqi_app = XiangqiApp()
    xiangqi_app.show()
    sys.exit(app.exec_())
