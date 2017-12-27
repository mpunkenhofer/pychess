# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

from pieces import Piece


class King(Piece):
    def __init__(self, board, pos, color):
        Piece.__init__(self, board, pos, color, 'King', 'K')

    def moves(self):
        return []