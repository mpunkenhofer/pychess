# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

import sys
from board import Board
from gui.console_interface import ConsoleInterface


class Chess:
    def __init__(self, gui):
        self.gui = gui
        self.board = Board()

    def draw(self):
        self.gui.draw_board(self.board)


def main():
    chess_game = Chess(ConsoleInterface())
    chess_game.draw()
    x = input('Enter anything to quit!')


if __name__ == "__main__":
    sys.exit(main())
