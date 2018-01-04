# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

import sys

from pychess.variant import Standard
from pychess.pieces import PieceColor

from interface.console import ChessConsoleUserInterface


class Game:
    def __init__(self, variant, ui, player=PieceColor.WHITE):
        self.variant = variant
        self.ui = ui
        self.current_player = player

        self.ui.draw(self.variant.board)

    def move(self):
        self.ui.move(self.variant.board, self.current_player)
        self.ui.draw(self.variant.board)

        self.current_player = PieceColor.WHITE if self.current_player == PieceColor.BLACK else PieceColor.BLACK

    def game_over(self):
        if self.variant.is_draw():
            self.ui.game_over('draw')
            return True
        elif self.variant.is_checkmated(self.current_player):
            self.ui.game_over(self.current_player)
            return True
        else:
            return False


def main():
    chess_game = Game(Standard(), ChessConsoleUserInterface())

    while not chess_game.game_over():
        chess_game.move()


if __name__ == "__main__":
    sys.exit(main())
