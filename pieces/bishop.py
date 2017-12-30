# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

import pieces


class Bishop(pieces.Piece):
    def __init__(self, board, pos, color):
        pieces.Piece.__init__(self, board, pos, color, 'Bishop', 'B')

    def get_moves(self):
        return []

    def protected_squares(self):
        return self.get_moves()
