import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QCheckBox, QLineEdit
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt

from p2_game import create_game, State
import rollout_bot as blue_bot
import random_bot as red_bot

BOTS = {'red': red_bot, 'blue': blue_bot}
square_width = 800
m=7
class Canvas(QWidget):
    def __init__(self, state):
        super().__init__()
        self.state = state
        self.UNDO_STACK = []
        self.RED_AI = False
        self.BLUE_AI = False

        self.mousePressEvent = self.handle_mouse_press

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.eraseRect(self.rect())
        step = square_width / self.state.game.width
        r = int(step / 7.0)
        w = int(step / 10.0)

        for i, j in self.state.game.h_lines:
            if i == self.state.game.width - 1:  # 跳过最右边的水平线
                continue
            if j == self.state.game.width :  # 跳过最下面的水平线
                continue
            x = int((i + 0.5) * step)
            y = int((j + 0.5) * step)
            if (i, j) in self.state.h_line_owners:
                owner = self.state.h_line_owners[(i, j)]
                painter.setPen(QPen(Qt.black, w))
                painter.drawLine(x, y, int(x + step), y)
            else:
                line_color = QColor(self.state.player_turn) if self.state.player_turn else Qt.black
                painter.setPen(QPen(line_color, w, Qt.DashLine))
                painter.drawLine(x, y, int(x + step), y)
                painter.drawPoint(x, y)
                painter.drawPoint(int(x + step), y)
                painter.drawPoint(int(x + step), y - 1)

        for i, j in self.state.game.v_lines:
            if j == self.state.game.width - 1:  # 跳过最下面的垂直线
                continue
            if i == self.state.game.width :  # 跳过最右边的垂直线
                continue

            x = int((i + 0.5) * step)
            y = int((j + 0.5) * step)
            if (i, j) in self.state.v_line_owners:
                owner = self.state.v_line_owners[(i, j)]
                painter.setPen(QPen(Qt.black, w))
                painter.drawLine(x, y, x, int(y + step))
            else:
                line_color = QColor(self.state.player_turn) if self.state.player_turn else Qt.black
                painter.setPen(QPen(line_color, w, Qt.DashLine))
                painter.drawLine(x, y, x, int(y + step))
                painter.drawPoint(x, y)
                painter.drawPoint(x - 1, y)
                painter.drawPoint(x, int(y + step))

        for i, j in self.state.game.boxes:
            x = int((i + 0.5) * step)
            y = int((j + 0.5) * step)
            if (i, j) in self.state.box_owners:
                owner = self.state.box_owners[(i, j)]
                painter.fillRect(x + r, y + r, int(step - 2 * r), int(step - 2 * r), QColor(owner))

        for i, j in self.state.game.dots:
            if i == self.state.game.width or j == self.state.game.width:
                continue
            x = int((i + 0.5) * step)
            y = int((j + 0.5) * step)
            painter.setPen(QPen(Qt.black))
            painter.setBrush(QColor(Qt.black))
            painter.drawEllipse(x - r, y - r, 2 * r, 2 * r)

        if not self.state.is_terminal():
            if self.state.player_turn == 'red' and self.RED_AI:
                self.think()
            elif self.state.player_turn == 'blue' and self.BLUE_AI:
                self.think()

    def handle_mouse_press(self, event):
        if self.state.player_turn == 'red' and self.RED_AI:
            print("Give the red guy a chance to think!")
            return
        if self.state.player_turn == 'blue' and self.BLUE_AI:
            print("The blue lady needs more time to think!")
            return

        x = event.pos().x()
        y = event.pos().y()

        step = square_width / self.state.game.width
        r = int(step / 3.0)

        for i, j in self.state.game.h_lines:
            if i == self.state.game.width:  # 跳过最右边的水平线
                continue
            line_x = round(i * step)
            line_y = round((j + 0.5) * step)
            if abs(line_x - x) <= r and abs(line_y - y) <= r:
                move = ('h', (i - 1, j))
                self.make_move(move)
                return

        for i, j in self.state.game.v_lines:
            if j == self.state.game.width:  # 跳过最下面的垂直线
                continue
            line_x = round((i + 0.5) * step)
            line_y = round(j * step)
            if abs(line_x - x) <= r and abs(line_y - y) <= r:
                move = ('v', (i, j - 1))
                self.make_move(move)
                return

        print("Invalid move!")

    def make_move(self, move):
        moves = self.state.legal_moves
        if move in moves:
            self.UNDO_STACK.append(self.state)
            next_state = self.state.copy()
            next_state.apply_move(move)
            self.state = next_state
            self.update()
        else:
            print(move, "not in legal moves!")

    def think(self):
        import threading

        class ThinkingThread(threading.Thread):
            def run(self):
                move = BOTS[self.state.player_turn].think(self.state.copy())
                self.make_move(move)

        ThinkingThread().start()

    def restart(self):
        game = create_game(m)
        initial_state = State(game)
        self.UNDO_STACK = [initial_state]
        self.state = initial_state
        self.update()

    def undo(self):
        if len(self.UNDO_STACK) > 1:
            self.UNDO_STACK.pop()
            self.state = self.UNDO_STACK[-1]
            self.update()


class MainWindow(QMainWindow):
    def __init__(self, width):
        super().__init__()
        self.setWindowTitle("Dots and Boxes")
        self.canvas = Canvas(State(create_game(width)))
        self.init_ui()

    def init_ui(self):
        main_widget = QWidget(self)
        layout = QVBoxLayout(main_widget)
        toolbar_layout = QHBoxLayout()
        layout.addLayout(toolbar_layout)
        layout.addWidget(self.canvas)

        undo_btn = QPushButton("Undo", self)
        undo_btn.clicked.connect(self.canvas.undo)
        toolbar_layout.addWidget(undo_btn)

        restart_btn = QPushButton("Restart", self)
        restart_btn.clicked.connect(self.canvas.restart)
        toolbar_layout.addWidget(restart_btn)

        red_ai_checkbox = QCheckBox("Red AI", self)
        red_ai_checkbox.stateChanged.connect(self.toggle_red_ai)
        toolbar_layout.addWidget(red_ai_checkbox)

        blue_ai_checkbox = QCheckBox("Blue AI", self)
        blue_ai_checkbox.stateChanged.connect(self.toggle_blue_ai)
        toolbar_layout.addWidget(blue_ai_checkbox)

        ai_thoughts_lineedit = QLineEdit(self)
        ai_thoughts_lineedit.setReadOnly(True)
        toolbar_layout.addWidget(ai_thoughts_lineedit)

        self.setCentralWidget(main_widget)

    def toggle_red_ai(self, state):
        self.canvas.RED_AI = state == Qt.Checked

    def toggle_blue_ai(self, state):
        self.canvas.BLUE_AI = state == Qt.Checked


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow(m)
    window.show()
    sys.exit(app.exec_())

