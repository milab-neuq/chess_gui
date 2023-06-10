from copy import deepcopy
from queue import Queue

import numpy as np


class chessboard:
    EMPTY = 0
    WHITE = -1
    BLACK = 1

    def __init__(self, board_len=9):
        self.board_len = board_len
        self.current_player = self.BLACK
        self.board = self.get_init_board()
        self.previous_action = []

    def get_init_board(self):
        return np.zeros(self.board_len ** 2, dtype=int)

    def clear(self):
        self.board = self.get_init_board()
        self.previous_action.clear()
        self.current_player = self.BLACK

    def copy(self):
        return deepcopy(self)

    def in_board(self, x, y):
        return 0 <= x < self.board_len and 0 <= y < self.board_len

    def get_location(self, x, y):
        return x * self.board_len + y

    def is_game_over(self, action):
        """
        0 not over
        1 lose
        """
        dx = [0, 1, 0, -1, 0]
        dy = [1, 0, -1, 0, 0]
        vis = np.zeros((self.board_len, self.board_len), dtype=int)

        for d in range(5):
            x = action // self.board_len + dx[d]
            y = action % self.board_len + dy[d]
            if self.in_board(x, y) == 0 or self.board[self.get_location(x, y)] == self.EMPTY or vis[x][y]:
                continue
            alive = 0
            q = Queue(self.board_len ** 2)
            vis[x][y] = 1
            q.put((x, y))
            while not q.empty():
                curX, curY = q.get()
                for i in range(4):
                    nextX = curX + dx[i]
                    nextY = curY + dy[i]
                    if self.in_board(nextX, nextY) == 0 or vis[nextX][nextY] == 1:
                        continue
                    if self.board[self.get_location(nextX, nextY)] == self.board[self.get_location(curX, curY)]:
                        vis[nextX][nextY] = 1
                        q.put((nextX, nextY))
                    if self.board[self.get_location(nextX, nextY)] == self.EMPTY:
                        alive = 1
            if alive == 0:
                return 1
        return 0

    def do_action(self, action):
        if self.board[action] != self.EMPTY:
            return False
        self.previous_action.append(action)
        self.board[action] = self.current_player
        self.current_player = -self.current_player
        return True

    def withdraw(self):
        action = self.previous_action.pop()
        self.board[action] = self.EMPTY
        self.current_player = -self.current_player
