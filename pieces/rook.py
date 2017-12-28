# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

import pieces


class Rook(pieces.Piece):
    def __init__(self, board, pos, color):
        pieces.Piece.__init__(self, board, pos, color, 'Rook', 'R')

    def moves(self):
        return []
