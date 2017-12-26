# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

from pieces.piece import Piece


class Knight(Piece):
    def __init__(self, board, pos, color):
        Piece.__init__(self, board, pos, color, 'Knight', 'N')

    def move(self, pos):
        pass

    def moves(self):
        pass
