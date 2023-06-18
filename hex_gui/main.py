
from PyQt5.QtWidgets import QApplication
from hex_chess.hex_main_window import HexMainWindow


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = HexMainWindow(board_size=11)
    window.show()

    sys.exit(app.exec_())