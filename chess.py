# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

import sys

from general import Board
from interface.console import ChessConsoleUserInterface


class Chess:
    def __init__(self):
        self.__current_player = None

    def __init__(self, ui, player='light'):
        self.board = Board()
        self.ui = ui
        self.current_player = player

        self.ui.draw(self)

    def move(self):
        piece, move = self.ui.move(self)

        move = self.board.move(piece, move)

        if move.type == 'Promotion':
            new_piece = self.ui.promote(piece)
            self.board.promote(piece, new_piece)

        self.current_player = 'dark' if self.current_player == 'light' else 'light'

        self.ui.draw(self)

    def game_over(self):
        return False

    @property
    def current_player(self):
        return self.__current_player

    @current_player.setter
    def current_player(self, p):
        if p not in ['light', 'dark']:
            raise ValueError("current player can only be 'light' or 'dark'.")

        self.__current_player = p


def main():
    chess_game = Chess(ChessConsoleUserInterface())

    while not chess_game.game_over():
        chess_game.move()


if __name__ == "__main__":
    sys.exit(main())
