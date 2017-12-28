# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

import pieces


class Knight(pieces.Piece):
    def __init__(self, board, pos, color):
        pieces.Piece.__init__(self, board, pos, color, 'Knight', 'N')

    def moves(self):
        return []
