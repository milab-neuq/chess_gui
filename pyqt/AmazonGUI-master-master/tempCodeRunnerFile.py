essboard.draw_xy(i, j, ARROW)
                        # 画框
                        m, n = self.coordinate_transform_map2pixel(i, j)
                        if self.piece_now == WHITE:
                            self.arrow_white_frame.setPixmap(QPixmap('img/white_frame.png'))
                            self.arrow_white_frame.setGeometry(m, n, CHESS_PIECE, CHESS_PIECE)
                            print("SetArrow",'——>坐标:', i, j, '白