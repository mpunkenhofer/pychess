# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

from pieces.piece import Piece


class Queen(Piece):
    def __init__(self, board, pos, color):
        Piece.__init__(self, board, pos, color, 'Queen', 'Q')

    def move(self, pos):
        pass

    def moves(self):
        pass
