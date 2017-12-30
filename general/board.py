# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

from pieces import Pawn, Rook, King, Queen, Knight, Bishop
from general import MoveDirection

class Board:
    def __init__(self):
        self._history = []
        self.pieces = {}
        
        for i in range(0, 8):
            self.pieces[(i, 1)] = Pawn(self, (i, 1), 'light')
            self.pieces[(i, 6)] = Pawn(self, (i, 6), 'dark')

        self.light_rooks = [Rook(self, (0, 0), 'light'), Rook(self, (7, 0), 'light')]
        self.pieces[(0, 0)] = self.light_rooks[0]
        self.pieces[(7, 0)] = self.light_rooks[1]

        self.dark_rooks = [Rook(self, (0, 7), 'dark'), Rook(self, (7, 7), 'dark')]
        self.pieces[(0, 7)] = self.dark_rooks[0]
        self.pieces[(7, 7)] = self.dark_rooks[1]

        self.light_knights = [Knight(self, (1, 0), 'light'), Knight(self, (6, 0), 'light')]
        self.pieces[(1, 0)] = self.light_knights[0]
        self.pieces[(6, 0)] = self.light_knights[1]

        self.dark_knights = [Knight(self, (1, 7), 'dark'), Knight(self, (6, 7), 'dark')]
        self.pieces[(1, 7)] = self.dark_knights[0]
        self.pieces[(6, 7)] = self.dark_knights[1]

        self.light_bishops = [Bishop(self, (2, 0), 'light'), Bishop(self, (5, 0), 'light')]
        self.pieces[(2, 0)] = self.light_bishops[0]
        self.pieces[(5, 0)] = self.light_bishops[1]

        self.dark_bishops = [Bishop(self, (2, 7), 'dark'), Bishop(self, (5, 7), 'dark')]
        self.pieces[(2, 7)] = self.dark_bishops[0]
        self.pieces[(5, 7)] = self.dark_bishops[1]

        self.light_queens = [Queen(self, (3, 0), 'light')]
        self.pieces[(3, 0)] = self.light_queens[0]

        self.dark_queens = [Queen(self, (3, 7), 'dark')]
        self.pieces[(3, 7)] = self.dark_queens[0]

        self.light_king = King(self, (4, 0), 'light')
        self.pieces[(4, 0)] = self.light_king

        self.dark_king = King(self, (4, 7), 'dark')
        self.pieces[(4, 7)] = self.dark_king

    def get_pieces(self):
        return self.pieces

    def pieces_by_color(self, color):
        result = []

        for pos, piece in self.pieces.items():
            if piece.color == color and piece.name != 'King':
                result.append(piece)
        return result

    def light_pieces(self):
        return self.pieces_by_color('light')

    def dark_pieces(self):
        return self.pieces_by_color('dark')

    def get_light_king(self):
        return self.light_king

    def get_dark_king(self):
        return self.dark_king

    def get_light_queens(self):
        return self.light_queens

    def get_dark_queens(self):
        return self.dark_queens

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

    def history(self):
        return self._history

    def move(self, piece, move):
        move = piece.move(move)

        if not move:
            raise RuntimeError('board.move(piece, move): could not make the move!')

        self._history.append(move)

    def pieces_between(self, p1, p2):
        p1_x, p1_y, p2_x, p2_y = self.get_coordinates(p1, p2)

        pieces = []

        if self.same_rank(p1, p2):
            for x in range(min(p1_x + 1, p2_x + 1), max(p1_x, p2_x)):
                if (x, p1_y) in self.pieces:
                    pieces.append(self.pieces[(x, p1_y)])
            return pieces
        elif self.same_file(p1, p2):
            for y in range(min(p1_y + 1, p2_y + 1), max(p1_y, p2_y)):
                if (p1_x, y) in self.pieces:
                    pieces.append(self.pieces[(p1_x, y)])
            return pieces
        elif self.same_diagonal(p1, p2):
            y = min(p1_y + 1, p2_y + 1)
            x_range = range(min(p1_x + 1, p2_x + 1), max(p1_x, p2_x))

            if self.same_falling_diagonal(p1, p2):
                x_range = reversed(x_range)

            for x in x_range:
                if (x, y) in self.pieces:
                    pieces.append(self.pieces[(x, y)])
                y += 1

            return pieces
        else:
            return []

    def next_piece(self, p, direction, limit=None):
        try:
            p_x, p_y = p.position
        except AttributeError:
            p_x, p_y = p

        color = 1 if p.light() else -1

        if limit:
            try:
                limit_x, limit_y = limit.position
            except AttributeError:
                limit_x, limit_y = limit
        else:
            limit_x = limit_y = None

        if direction == MoveDirection.RankUp:
            for y in range(p_x + 1 * color, 8):
                if (limit_x, limit_y) == (p_x, y):
                    break
                if (p_x, y) in self.pieces:
                    return self.pieces[(p_x, y)]
        elif direction == MoveDirection.RankDown:
            for y in reversed(range(0, p_x - 1 * color)):
                if (limit_x, limit_y) == (p_x, y):
                    break
                if (p_x, y) in self.pieces:
                    return self.pieces[(p_x, y)]
        elif direction == MoveDirection.FileRight:
            for x in range(p_y + 1 * color, 8):
                if (limit_x, limit_y) == (x, p_y):
                    break
                if (x, p_y) in self.pieces:
                    return self.pieces[(x, p_y)]
        elif direction == MoveDirection.FileLeft:
            for x in reversed(range(0, p_y - 1 * color)):
                if (limit_x, limit_y) == (x, p_y):
                    break
                if (x, p_y) in self.pieces:
                    return self.pieces[(x, p_y)]
        elif direction == MoveDirection.RisingDiagonalUp:
            y = p_y + 1 * color
            for x in range(p_x + 1 * color, 8):
                if (limit_x, limit_y) == (x, y):
                    break
                if (x, y) in self.pieces:
                    return self.pieces[(x, y)]
                y += 1 * color
        elif direction == MoveDirection.RisingDiagonalDown:
            y = p_y - 1 * color
            for x in reversed(range(0, p_x - 1 * color)):
                if (limit_x, limit_y) == (x, y):
                    break
                if (x, y) in self.pieces:
                    return self.pieces[(x, y)]
                y -= 1 * color
        elif direction == MoveDirection.FallingDiagonalUp:
                y = p_y + 1 * color
                for x in reversed(range(0, p_x - 1 * color)):
                    if (limit_x, limit_y) == (x, y):
                        break
                    if (x, y) in self.pieces:
                        return self.pieces[(x, y)]
                    y += 1 * color
        elif direction == MoveDirection.FallingDiagonalDown:
                y = p_y - 1 * color
                for x in range(p_x + 1 * color, 8):
                    if (limit_x, limit_y) == (x, y):
                        break
                    if (x, y) in self.pieces:
                        return self.pieces[(x, y)]
                    y -= 1 * color

        return None

    def rank_pin(self, piece):
        king = self.light_king if piece.light() else self.dark_king

        if self.same_rank(king, piece) and len(self.pieces_between(king, piece)) == 0:
            rooks = self.dark_rooks if piece.light() else self.light_rooks
            queens = self.dark_queens if piece.light() else self.light_queens

            for r in rooks:
                if self.same_rank(r, piece) and len(self.pieces_between(r, piece)) == 0:
                    return True

            for q in queens:
                if self.same_rank(q, piece) and len(self.pieces_between(q, piece)) == 0:
                    return True
        else:
            return False

    def file_pin(self, piece):
        king = self.light_king if piece.light() else self.dark_king

        if self.same_file(king, piece) and len(self.pieces_between(king, piece)) == 0:
            rooks = self.dark_rooks if piece.light() else self.light_rooks
            queens = self.dark_queens if piece.light() else self.light_queens

            for r in rooks:
                if self.same_file(r, piece) and len(self.pieces_between(r, piece)) == 0:
                    return True

            for q in queens:
                if self.same_file(q, piece) and len(self.pieces_between(q, piece)) == 0:
                    return True

        return False

    def diagonal_pin(self, piece):
        king = self.light_king if piece.light() else self.dark_king

        if self.same_rising_diagonal(king, piece) and len(self.pieces_between(king, piece)) == 0:
            bishops = self.dark_bishops if piece.light() else self.light_bishops
            queens = self.dark_queens if piece.light() else self.light_queens

            for b in bishops:
                if self.same_rising_diagonal(b, piece) and len(self.pieces_between(b, piece)) == 0:
                    return True

            for q in queens:
                if self.same_rising_diagonal(q, piece) and len(self.pieces_between(q, piece)) == 0:
                    return True

        elif self.same_falling_diagonal(king, piece) and len(self.pieces_between(king, piece)) == 0:
            bishops = self.dark_bishops if piece.light() else self.light_bishops
            queens = self.dark_queens if piece.light() else self.light_queens

            for b in bishops:
                if self.same_falling_diagonal(b, piece) and len(self.pieces_between(b, piece)) == 0:
                    return True

            for q in queens:
                if self.same_falling_diagonal(q, piece) and len(self.pieces_between(q, piece)) == 0:
                    return True

        return False

    def square_attacked(self, x, y):
        pass

    def my_king(self, p):
        return self.light_king if p.light() else self.dark_king

    def enemy_king(self, p):
        return self.dark_king if p.light() else self.light_king

    @staticmethod
    def en_passant_rank(pawn):
        return pawn.position[1] == 4 if pawn.light() else pawn.position[1] == 3

    @staticmethod
    def get_coordinates(p1, p2):
        try:
            p1_x, p1_y = p1.position
        except AttributeError:
            p1_x, p1_y = p1

        try:
            p2_x, p2_y = p2.position
        except AttributeError:
            p2_x, p2_y = p2

        return p1_x, p1_y, p2_x, p2_y

    @staticmethod
    def same_rank(p1, p2):
        p1_x, p1_y, p2_x, p2_y = Board.get_coordinates(p1, p2)
        return p1_y == p2_y

    @staticmethod
    def same_file(p1, p2):
        p1_x, p1_y, p2_x, p2_y = Board.get_coordinates(p1, p2)
        return p1_x == p2_x

    @staticmethod
    def same_diagonal(p1, p2):
        p1_x, p1_y, p2_x, p2_y = Board.get_coordinates(p1, p2)

        # y = kx+d ... d = yi - xi
        falling = p1_y == p1_x + p2_y - p2_x
        rising = p1_y == -p1_x + p2_y + p2_x

        return falling or rising

    @staticmethod
    def same_rising_diagonal(p1, p2):
        p1_x, p1_y, p2_x, p2_y = Board.get_coordinates(p1, p2)

        return p1_y == -p1_x + p2_y + p2_x

    @staticmethod
    def same_falling_diagonal(p1, p2):
        p1_x, p1_y, p2_x, p2_y = Board.get_coordinates(p1, p2)

        return p1_y == p1_x + p2_y - p2_x

    @staticmethod
    def in_board(x, y):
        return 0 <= x < 8 and 0 <= y < 8
