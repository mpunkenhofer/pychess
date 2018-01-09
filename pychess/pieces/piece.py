# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

from abc import ABC, abstractmethod
from enum import Enum


class PieceType(Enum):
    KING = 'King'
    QUEEN = 'Queen'
    ROOK = 'Rook'
    BISHOP = 'Bishop'
    KNIGHT = 'Knight'
    PAWN = 'Pawn'


class PieceColor(Enum):
    WHITE = 'white'
    BLACK = 'black'


class Piece(ABC):
    @abstractmethod
    def __init__(self, board, pos, c, t):
        self.board = board
        self.position = pos
        self.color = c
        self.type = t
        self.history = []

        self._move_cache = (-1, [])
        self._influence_cache = (-1, [])

    @abstractmethod
    def get_moves(self):
        """
        Get all available moves for this piece

        :return: a list of available moves
        """

    @abstractmethod
    def get_influenced_squares(self, ignored):
        """
        Get a list of all influenced squares regardless if the move is possible or not

        :param ignored: pieces which are to be ignored during finding influenced squares
        :return: a list of all influenced squares
        """

    def is_king(self):
        return self.type == PieceType.KING

    def is_queen(self):
        return self.type == PieceType.QUEEN

    def is_rook(self):
        return self.type == PieceType.ROOK

    def is_bishop(self):
        return self.type == PieceType.BISHOP

    def is_knight(self):
        return self.type == PieceType.KNIGHT

    def is_pawn(self):
        return self.type == PieceType.PAWN

    def is_white(self):
        return self.color == PieceColor.WHITE

    def is_black(self):
        return self.color == PieceColor.BLACK

    def other_color(self):
        return PieceColor.WHITE if self.color == PieceColor.BLACK else PieceColor.BLACK

    def shorthand(self):
        shorthand_dict = {PieceType.KING: 'K',
                          PieceType.QUEEN: 'Q',
                          PieceType.ROOK: 'R',
                          PieceType.BISHOP: 'B',
                          PieceType.KNIGHT: 'N',
                          PieceType.PAWN: 'P'}

        return shorthand_dict[self.type]

    def moves(self):
        if not (self._move_cache[0] == len(self.board.history) and self._move_cache[1]):
            self._move_cache = len(self.board.history), self.get_moves()

        if self.is_king():
            return self._move_cache[1]

        king = self.board.get_king(self.color)

        if not king.in_check():
            return self._move_cache[1]

        checker = king.checked_by()

        if len(checker) > 1:
            return []

        return self.block_checker(checker[0]) + self.capture_checker(checker[0])

    def influenced_squares(self):
        if not (self._influence_cache[0] == len(self.board.history) and self._influence_cache[1]):
            self._influence_cache = len(self.board.history), self.get_influenced_squares(None)

        return self._influence_cache[1]

    def block_checker(self, checker):
        return [m for m in self._move_cache[1]
                if m.is_move() and Piece.is_between(m.destination, checker, self.board.get_king(self.color))]

    def capture_checker(self, checker):
        captures = []

        for m in self._move_cache[1]:
            if m.is_capture() and m.captured_piece == checker:
                captures.append(m)

        return captures

    def pieces_between(self, p):
        p1_x, p1_y = self.position

        try:
            p2_x, p2_y = p.position
        except AttributeError:
            p2_x, p2_y = p

        pieces = []

        if self.same_rank(self, p):
            for x in range(min(p1_x + 1, p2_x + 1), max(p1_x, p2_x)):
                if (x, p1_y) in self.board.pieces:
                    pieces.append(self.board.pieces[(x, p1_y)])
            return pieces
        elif self.same_file(self, p):
            for y in range(min(p1_y + 1, p2_y + 1), max(p1_y, p2_y)):
                if (p1_x, y) in self.board.pieces:
                    pieces.append(self.board.pieces[(p1_x, y)])
            return pieces
        elif self.same_diagonal(self, p):
            y = min(p1_y + 1, p2_y + 1)
            x_range = range(min(p1_x + 1, p2_x + 1), max(p1_x, p2_x))

            if self.same_falling_diagonal(self, p):
                x_range = reversed(x_range)

            for x in x_range:
                if (x, y) in self.board.pieces:
                    pieces.append(self.board.pieces[(x, y)])
                y += 1

            return pieces
        else:
            return []

    def rank_pinned(self):
        return self.rank_pin_piece() is not None

    def rank_pin_piece(self):
        king = self.board.get_king(self.color)

        if self.same_rank(king, self) and not self.pieces_between(king):
            rooks = self.board.get_rooks(self.other_color())
            queens = self.board.get_queens(self.other_color())

            for r in rooks:
                if self.same_rank(r, self) and not self.pieces_between(r):
                    return r

            for q in queens:
                if self.same_rank(q, self) and not self.pieces_between(q):
                    return q
        else:
            return None

    def file_pinned(self):
        return self.file_pin_piece() is not None

    def file_pin_piece(self):
        king = self.board.get_king(self.color)

        if self.same_file(king, self) and not self.pieces_between(king):
            rooks = self.board.get_rooks(self.other_color())
            queens = self.board.get_queens(self.other_color())

            for r in rooks:
                if self.same_file(r, self) and not self.pieces_between(r):
                    return r

            for q in queens:
                if self.same_file(q, self) and not self.pieces_between(q):
                    return q

        return None

    def diagonally_pinned(self):
        return self.diagonal_pin_piece() is not None

    def diagonal_pin_piece(self):
        king = self.board.get_king(self.color)

        if self.same_rising_diagonal(king, self) and not self.pieces_between(king):
            bishops = self.board.get_bishops(self.other_color())
            queens = self.board.get_queens(self.other_color())

            for b in bishops:
                if self.same_rising_diagonal(b, self) and not self.pieces_between(b):
                    return b

            for q in queens:
                if self.same_rising_diagonal(q, self) and not self.pieces_between(q):
                    return q

        elif self.same_falling_diagonal(king, self) and not self.pieces_between(king):
            bishops = self.board.get_bishops(self.other_color())
            queens = self.board.get_queens(self.other_color())

            for b in bishops:
                if self.same_falling_diagonal(b, self) and not self.pieces_between(b):
                    return b

            for q in queens:
                if self.same_falling_diagonal(q, self) and not self.pieces_between(q):
                    return q

        return None

    def get_diagonal_squares(self, ignored=None):
        return self.get_rising_diagonal_squares(ignored) + self.get_falling_diagonal_squares(ignored)

    def get_rising_diagonal_squares(self, ignored=None):
        if ignored is None:
            ignored = []

        squares = []
        p_x, p_y = self.position
        c = 1 if self.is_white() else -1

        # rising diagonal up
        y = p_y + 1 * c
        for x in range(p_x + 1, self.board.get_last_file(self.color) + 1) if self.is_white() \
                else reversed(range(self.board.get_last_file(self.color), p_x)):
            if not self.board.in_board((x, y)):
                break

            squares.append((x, y))
            if (x, y) in self.board.pieces and self.board.pieces[(x, y)] not in ignored:
                break
            y += 1 * c

        # rising diagonal down
        y = p_y - 1 * c
        for x in reversed(range(self.board.get_first_file(self.color), p_x)) if self.is_white() \
                else range(p_x + 1, self.board.get_first_file(self.color) + 1):
            if not self.board.in_board((x, y)):
                break

            squares.append((x, y))
            if (x, y) in self.board.pieces and self.board.pieces[(x, y)] not in ignored:
                break
            y -= 1 * c

        return squares

    def get_falling_diagonal_squares(self, ignored=None):
        if ignored is None:
            ignored = []

        squares = []
        p_x, p_y = self.position
        c = 1 if self.is_white() else -1

        # falling diagonal up
        y = p_y + 1 * c
        for x in reversed(range(self.board.get_first_file(self.color), p_x)) if self.is_white() \
                else range(p_x + 1, self.board.get_first_file(self.color) + 1):
            if not self.board.in_board((x, y)):
                break

            squares.append((x, y))
            if (x, y) in self.board.pieces and self.board.pieces[(x, y)] not in ignored:
                break
            y += 1 * c

        # falling diagonal down
        y = p_y - 1 * c
        for x in range(p_x + 1, self.board.get_last_file(self.color) + 1) if self.is_white() \
                else reversed(range(self.board.get_last_file(self.color), p_x)):
            if not self.board.in_board((x, y)):
                break

            squares.append((x, y))
            if (x, y) in self.board.pieces and self.board.pieces[(x, y)] not in ignored:
                break
            y -= 1 * c

        return squares

    def get_rank_squares(self, ignored=None):
        if ignored is None:
            ignored = []

        squares = []
        p_x, p_y = self.position

        # right
        for x in range(p_x + 1, self.board.get_last_file(self.color) + 1) if self.is_white() \
                else reversed(range(self.board.get_last_file(self.color), p_x)):
            squares.append((x, p_y))
            if (x, p_y) in self.board.pieces and self.board.pieces[(x, p_y)] not in ignored:
                break

        # left
        for x in reversed(range(self.board.get_first_file(self.color), p_x)) if self.is_white() \
                else range(p_x + 1, self.board.get_first_file(self.color) + 1):
            squares.append((x, p_y))
            if (x, p_y) in self.board.pieces and self.board.pieces[(x, p_y)] not in ignored:
                break

        return squares

    def get_file_squares(self, ignored=None):
        if ignored is None:
            ignored = []

        squares = []
        p_x, p_y = self.position

        # up
        for y in range(p_y + 1, self.board.get_last_rank(self.color) + 1) if self.is_white() \
                else reversed(range(self.board.get_last_rank(self.color), p_y)):
            squares.append((p_x, y))
            if (p_x, y) in self.board.pieces and self.board.pieces[(p_x, y)] not in ignored:
                break

        # down
        for y in reversed(range(self.board.get_first_rank(self.color), p_y)) if self.is_white() \
                else range(p_y + 1, self.board.get_first_rank(self.color) + 1):
            squares.append((p_x, y))
            if (p_x, y) in self.board.pieces and self.board.pieces[(p_x, y)] not in ignored:
                break

        return squares

    @staticmethod
    def is_between(square, p1, p2):
        p1_x, p1_y = p1.position
        p2_x, p2_y = p2.position

        if Piece.same_rank(p1, p2) and Piece.same_rank(square, p2):
            for x in range(min(p1_x + 1, p2_x + 1), max(p1_x, p2_x)):
                if (x, p1_y) == square:
                    return True
        elif Piece.same_file(p1, p2) and Piece.same_file(square, p2):
            for y in range(min(p1_y + 1, p2_y + 1), max(p1_y, p2_y)):
                if (p1_x, y) == square:
                    return True
        elif Piece.same_diagonal(p1, p2) and Piece.same_diagonal(square, p2):
            if Piece.same_falling_diagonal(p1, p2):
                x_range = range(min(p1_x + 1, p2_x + 1), max(p1_x, p2_x))
                y = max(p1_y - 1, p2_y - 1)
                increment = -1
            else:
                x_range = range(min(p1_x + 1, p2_x + 1), max(p1_x, p2_x))
                y = min(p1_y + 1, p2_y + 1)
                increment = 1

            for x in x_range:
                if (x, y) == square:
                    return True
                y += increment

        return False

    @staticmethod
    def same_rank(p1, p2):
        p1_x, p1_y, p2_x, p2_y = Piece.get_coordinates(p1, p2)
        return p1_y == p2_y

    @staticmethod
    def same_file(p1, p2):
        p1_x, p1_y, p2_x, p2_y = Piece.get_coordinates(p1, p2)
        return p1_x == p2_x

    @staticmethod
    def same_diagonal(p1, p2):
        return Piece.same_rising_diagonal(p1, p2) or Piece.same_falling_diagonal(p1, p2)

    @staticmethod
    def same_falling_diagonal(p1, p2):
        p1_x, p1_y, p2_x, p2_y = Piece.get_coordinates(p1, p2)

        return p1_y == -p1_x + p2_y + p2_x

    @staticmethod
    def same_rising_diagonal(p1, p2):
        p1_x, p1_y, p2_x, p2_y = Piece.get_coordinates(p1, p2)

        return p1_y == p1_x + p2_y - p2_x

    @staticmethod
    def get_coordinates(p1, p2=None):
        try:
            p1_x, p1_y = p1.position
        except AttributeError:
            p1_x, p1_y = p1

        if not p2:
            return p1_x, p1_y

        try:
            p2_x, p2_y = p2.position
        except AttributeError:
            p2_x, p2_y = p2

        return p1_x, p1_y, p2_x, p2_y
