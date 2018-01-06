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
        if self.board.get_king(PieceColor.WHITE).is_stalemated():
            return True

        if self.board.get_king(PieceColor.BLACK).is_stalemated():
            return True

        if self.insufficient_material():
            return True

        if self.fifty_move_rule():
            return True

        return False

    def is_checkmated(self, color):
        return self.board.get_king(color).is_checkmated()

    def insufficient_material(self):
        white_pieces = self.board.get_pieces(PieceColor.WHITE)
        black_pieces = self.board.get_pieces(PieceColor.BLACK)

        if len(white_pieces) > 1 or len(black_pieces) > 1:
            return False

        if white_pieces and not (white_pieces[0].is_knight() or white_pieces[0].is_bishop()):
            return False

        if black_pieces and not (black_pieces[0].is_knight() or black_pieces[0].is_bishop()):
            return False

        return True

    def fifty_move_rule(self):
        if len(self.board.move_history()) < 50:
            return False

        for i, m in enumerate(self.board.move_history()):
            if m.piece.is_pawn() and m.is_move():
                return False

            if m.is_capture():
                return False

            if i + 1 >= 50:
                return True

        return True
