# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

import sys
from pieces.pawn import Pawn
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King
from gui.console_interface import ConsoleInterface


class Chess:
    def __init__(self, gui):
        self.gui = gui
        self.board = {}

        for i in range(0, 8):
            self.board[(i, 1)] = Pawn(self.board, (i, 1), 'light')
            self.board[(i, 6)] = Pawn(self.board, (i, 6), 'dark')

        self.board[(0, 0)] = Rook(self.board, (0, 0), 'light')
        self.board[(7, 0)] = Rook(self.board, (7, 0), 'light')
        self.board[(0, 7)] = Rook(self.board, (0, 7), 'dark')
        self.board[(7, 7)] = Rook(self.board, (7, 7), 'dark')

        self.board[(1, 0)] = Knight(self.board, (1, 0), 'light')
        self.board[(6, 0)] = Knight(self.board, (6, 0), 'light')
        self.board[(1, 7)] = Knight(self.board, (1, 7), 'dark')
        self.board[(6, 7)] = Knight(self.board, (6, 7), 'dark')

        self.board[(2, 0)] = Bishop(self.board, (2, 0), 'light')
        self.board[(5, 0)] = Bishop(self.board, (5, 0), 'light')
        self.board[(2, 7)] = Bishop(self.board, (2, 7), 'dark')
        self.board[(5, 7)] = Bishop(self.board, (5, 7), 'dark')

        self.board[(3, 0)] = Queen(self.board, (3, 0), 'light')
        self.board[(3, 7)] = Queen(self.board, (3, 7), 'dark')

        self.board[(4, 0)] = King(self.board, (4, 0), 'light')
        self.board[(4, 7)] = King(self.board, (4, 7), 'dark')

    def draw(self):
        self.gui.draw_board(self.board)


def main():
    chess_game = Chess(ConsoleInterface())
    chess_game.draw()
    x = input('Enter anything to quit!')


if __name__ == "__main__":
    sys.exit(main())
