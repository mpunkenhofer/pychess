# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

import pieces


class Queen(pieces.Piece):
    def __init__(self, board, pos, color):
        pieces.Piece.__init__(self, board, pos, color, 'Queen', 'Q')

    def get_moves(self):
        return []

    def get_influenced_squares(self):
        return self.get_moves()

