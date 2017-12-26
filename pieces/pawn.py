# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

from pieces.piece import Piece


class Pawn(Piece):
    def __init__(self, board, pos, color):
        Piece.__init__(self, board, pos, color, 'Pawn', 'P')

    def moves(self):
        pass
