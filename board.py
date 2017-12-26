# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

from pieces.pawn import Pawn
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King


class Board:
    def __init__(self):
        
        self.pieces = {}
        
        for i in range(0, 8):
            self.pieces[(i, 1)] = Pawn(self.pieces, (i, 1), 'light')
            self.pieces[(i, 6)] = Pawn(self.pieces, (i, 6), 'dark')

        self.light_rooks = [Rook(self.pieces, (0, 0), 'light'), Rook(self.pieces, (7, 0), 'light')]
        self.pieces[(0, 0)] = self.light_rooks[0]
        self.pieces[(7, 0)] = self.light_rooks[1]

        self.dark_rooks = [Rook(self.pieces, (0, 7), 'dark'), Rook(self.pieces, (7, 7), 'dark')]
        self.pieces[(0, 7)] = self.dark_rooks[0]
        self.pieces[(7, 7)] = self.dark_rooks[1]

        self.light_knights = [Knight(self.pieces, (1, 0), 'light'), Knight(self.pieces, (6, 0), 'light')]
        self.pieces[(1, 0)] = self.light_knights[0]
        self.pieces[(6, 0)] = self.light_knights[1]

        self.dark_knights = [Knight(self.pieces, (1, 7), 'dark'), Knight(self.pieces, (6, 7), 'dark')]
        self.pieces[(1, 7)] = self.dark_knights[0]
        self.pieces[(6, 7)] = self.dark_knights[1]

        self.light_bishops = [Bishop(self.pieces, (2, 0), 'light'), Bishop(self.pieces, (5, 0), 'light')]
        self.pieces[(2, 0)] = self.light_bishops[0]
        self.pieces[(5, 0)] = self.light_bishops[1]

        self.dark_bishops = [Bishop(self.pieces, (2, 7), 'dark'), Bishop(self.pieces, (5, 7), 'dark')]
        self.pieces[(2, 7)] = self.dark_bishops[0]
        self.pieces[(5, 7)] = self.dark_bishops[1]

        self.light_queen = Queen(self.pieces, (3, 0), 'light')
        self.pieces[(3, 0)] = self.light_queen

        self.dark_queen = Queen(self.pieces, (3, 7), 'dark')
        self.pieces[(3, 7)] = self.dark_queen

        self.light_king = King(self.pieces, (4, 0), 'light')
        self.pieces[(4, 0)] = self.light_king

        self.dark_king = King(self.pieces, (4, 7), 'dark')
        self.pieces[(4, 7)] = self.dark_king

    def get_pieces(self):
        return self.pieces

    def get_light_king(self):
        return self.light_king

    def get_dark_king(self):
        return self.dark_king

    def get_light_queen(self):
        return self.light_queen

    def get_dark_queen(self):
        return self.dark_queen

    def get_light_rooks(self):
        return self.light_rooks

    def get_dark_rooks(self):
        return self.dark_rooks

    def get_light_bishops(self):
        return self.light_bishops

    def get_dark_bishops(self):
        return self.dark_bishops

    def get_light_knights(self):
        return self.light_knights

    def get_dark_knights(self):
        return self.dark_knights

