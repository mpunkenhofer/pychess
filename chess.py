# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

import sys
from general import Board
from gui.console import ChessConsoleGUI


class Chess:
    def __init__(self, gui):
        self.gui = gui
        self.board = Board()

    def move(self):
        piece, move = self.gui.move(self.board)
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
