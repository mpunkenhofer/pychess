# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import pychess

from pychess.variant import variant


class Standard(variant.Variant):
    def __init__(self, board=None):
        if not board:
            board = pychess.board.StandardBoard()

        variant.Variant.__init__(self, board)

    def is_draw(self):
        if self.board.get_king(pychess.PieceColor.WHITE).is_stalemated():
            return True

        if self.board.get_king(pychess.PieceColor.BLACK).is_stalemated():
            return True

        if pychess.util.rules.insufficient_material(self.board):
            return True

        if pychess.util.rules.half_move_clock(self.board.move_history()) >= 50:
            return True

        return False

    def is_checkmated(self, color):
        return self.board.get_king(color).is_checkmated()


