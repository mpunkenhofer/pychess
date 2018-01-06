# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

from pychess import variant
from pychess.board.standard import StandardBoard
from pychess.pieces import PieceColor
from pychess.util import rules


class Standard(variant.Variant):
    def __init__(self):
        variant.Variant.__init__(self)
        self.board = StandardBoard()

    def is_draw(self):
        if self.board.get_king(PieceColor.WHITE).is_stalemated():
            return True

        if self.board.get_king(PieceColor.BLACK).is_stalemated():
            return True

        if rules.insufficient_material(self.board):
            return True

        if rules.half_move_clock(self.board.move_history()) >= 50:
            return True

        return False

    def is_checkmated(self, color):
        return self.board.get_king(color).is_checkmated()


