# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

from pychess import variant
from pychess.board.standard import StandardBoard
from pychess.pieces import PieceColor


class Standard(variant.Variant):
    def __init__(self):
        variant.Variant.__init__(self)
        self.board = StandardBoard()

    def is_draw(self):
        if self.board.get_king(PieceColor.WHITE).is_stalemated() \
                or self.board.get_king(PieceColor.BLACK).is_stalemated():
            return True

        return False

    def is_checkmated(self, color):
        return self.board.get_king(color).is_checkmated()
