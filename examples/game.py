# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

import sys

from examples.interface.console import ChessConsoleUserInterface

from pychess.variant import Standard
from pychess.pieces import PieceColor


class Game:
    def __init__(self, variant, ui, player=PieceColor.WHITE):
        self.variant = variant
        self.ui = ui
        self.current_player = player

        self.ui.draw()

    def move(self):
        self.ui.move(self.current_player)
        self.ui.draw()

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
    variant = Standard()
    chess_game = Game(variant, ChessConsoleUserInterface(variant.board))

    while not chess_game.game_over():
        chess_game.move()


if __name__ == "__main__":
    sys.exit(main())