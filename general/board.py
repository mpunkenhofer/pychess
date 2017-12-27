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

    def pieces_between(self, p1, p2):
        p1_x, p1_y = p1.position
        p2_x, p2_y = p2.position

        if self.same_rank(p1, p2):
            return self.pieces_between(p1_x, p1_y, p2_x, p2_y)
        elif self.same_file(p1, p2):
            return self.pieces_between(p1_x, p1_y, p2_x, p2_y)
        elif self.same_diagonal(p1, p2):
            pieces = []

            if self.falling_diagonal(p1, p2):
                pieces.append(self.pieces_on_falling_diagonal(p1_x, p1_y, p2_x, p2_y))
            if self.rising_diagonal(p1, p2):
                pieces.append(self.pieces_on_rising_diagonal(p1_x, p1_y, p2_x, p2_y, 1))

            return pieces
        else:
            return []

    def pieces_between(self, x1, y1, x2, y2):
        pieces = []

        if self.falling_diagonal(x1, y1, x2, y2):
            return pieces.append(self.pieces_on_falling_diagonal(x1, y1, x2, y2))

        if self.rising_diagonal(x1, y1, x2, y2):
            return pieces.append(self.pieces_on_rising_diagonal(x1, y1, x2, y2))

        for x in range(min(x1, x2), max(x1 + 1, x2 + 1)):
            for y in range(min(y1, y2), max(y1 + 1, y2 + 1)):
                if (x, y) in self.pieces:
                    pieces.append(self.pieces[(x, y)])

        return pieces

    def pieces_on_falling_diagonal(self, x1, y1, x2, y2):
        pieces = []
        y = min(y1, y2)

        for x in reversed(range(min(x1, x2), max(x1 + 1, x2 + 1))):
            if (x, y) in self.pieces:
                pieces.append(self.pieces[(x, y)])
            y += 1

        return pieces

    def pieces_on_rising_diagonal(self, x1, y1, x2, y2):
        pieces = []
        y = min(y1, y2)

        for x in range(min(x1, x2), max(x1 + 1, x2 + 1)):
            if (x, y) in self.pieces:
                pieces.append(self.pieces[(x, y)])
            y += 1

        return pieces

    def rank_pin(self, piece):
        king = self.light_king if piece.light() else self.dark_king

        if self.same_rank(king, piece) and len(self.pieces_between(king, piece)) == 0:
            return True
        else:
            return False

    def file_pin(self, piece):
        king = self.light_king if piece.light() else self.dark_king

        if self.same_file(king, piece) and len(self.pieces_between(king, piece)) == 0:
            return True
        else:
            return False

    def diagonal_pin(self, piece):
        king = self.light_king if piece.light() else self.dark_king

        if self.rising_diagonal(king, piece) and len(self.pieces_on_rising_diagonal(king, piece)) == 0:
            return True
        elif self.falling_diagonal(king, piece) and len(self.pieces_on_falling_diagonal(king, piece)) == 0:
            return True
        else:
            return False

    @staticmethod
    def same_rank(p1, p2):
        p1_x, p1_y = p1.position
        p2_x, p2_y = p2.position

        return p1_x == p2_x

    @staticmethod
    def same_file(p1, p2):
        p1_x, p1_y = p1.position
        p2_x, p2_y = p2.position

        return p1_y == p2_y

    @staticmethod
    def same_diagonal(p1, p2):
        p1_x, p1_y = p1.position
        p2_x, p2_y = p2.position

        # y = kx+d ... d = yi - xi
        falling = p1_y == p1_x + p2_y - p2_x
        rising = p1_y == -p1_x + p2_y + p2_x

        return falling or rising

    @staticmethod
    def rising_diagonal(p1, p2):
        p1_x, p1_y = p1.position
        p2_x, p2_y = p2.position

        return p1_y == -p1_x + p2_y + p2_x

    @staticmethod
    def falling_diagonal(p1, p2):
        p1_x, p1_y = p1.position
        p2_x, p2_y = p2.position

        return p1_y == p1_x + p2_y - p2_x

    @staticmethod
    def rising_diagonal(x1, y1, x2, y2):
        return y1 == -x1 + y2 + x2

    @staticmethod
    def falling_diagonal(x1, y1, x2, y2):
        return y1 == x1 + y2 - x2

    @staticmethod
    def in_board(x, y):
        return 0 <= x < 8 and 0 <= y < 8

