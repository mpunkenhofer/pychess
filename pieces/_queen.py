# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

from pieces import Piece


class Queen(Piece):
    def __init__(self, board, pos, color):
        Piece.__init__(self, board, pos, color, 'Queen', 'Q')

    def moves(self):
        return []
