# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

import sys
from general.board import Board
from gui.chess_console_gui import ChessConsoleGUI


class Chess:
    def __init__(self, gui):
        self.gui = gui
        self.board = Board()

    def draw(self):
        self.gui.draw_board(self.board)

    def move(self):
        piece = self.gui.choose_piece(self.board)
        move = self.gui.move_piece(self.board, piece)
        piece.move(move)

    def game_over(self):
        cmd = input('Enter q to quit!')

        if cmd == 'q':
            return True

        return False


def main():
    chess_game = Chess(ChessConsoleGUI())

    while not chess_game.game_over():
        chess_game.move()
        chess_game.draw()


if __name__ == "__main__":
    sys.exit(main())
