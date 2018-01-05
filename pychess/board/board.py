# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

from pychess import pieces
from abc import ABC, abstractmethod


class Board(ABC):
    @abstractmethod
    def __init__(self):
        self.history = []
        self.pieces = None

        self.white_long_castle = self.white_short_castle = self.black_short_castle = self.black_long_castle = True

    @abstractmethod
    def move(self, move):
        pass

    @abstractmethod
    def get_bottom_left(self):
        pass

    @abstractmethod
    def get_top_right(self):
        pass

    @abstractmethod
    def get_en_passant_rank(self, color):
        pass

    @abstractmethod
    def get_short_castle_positions(self, color):
        pass

    @abstractmethod
    def get_long_castle_positions(self, color):
        pass

    @abstractmethod
    def get_piece(self, pos):
        pass

    def filter_pieces(self, type=None, color=None):
        filtered = []

        for _, p in self.pieces.items():
            if type and type != p.type:
                continue
            if color and color != p.color:
                continue

            filtered.append(p)

        return filtered

    def get_all_pieces(self, color=None):
        if color:
            return [p for p in self.filter_pieces(color=color)]
        else:
            return [p for _, p in self.pieces.items()]

    def get_pieces(self, color=None):
        if color:
            return [p for p in self.filter_pieces(color=color) if not p.is_king()]
        else:
            return [p for _, p in self.pieces.items() if not p.is_king()]

    def get_king(self, color):
        return self.filter_pieces(pieces.PieceType.KING, color)[0]

    def get_queens(self, color):
        return self.filter_pieces(pieces.PieceType.QUEEN, color)

    def get_rooks(self, color):
        return self.filter_pieces(pieces.PieceType.ROOK, color)

    def get_bishops(self, color):
        return self.filter_pieces(pieces.PieceType.BISHOP, color)

    def get_knights(self, color):
        return self.filter_pieces(pieces.PieceType.KNIGHT, color)

    def get_pawns(self, color):
        return self.filter_pieces(pieces.PieceType.PAWN, color)

    def get_enemy_king(self, color):
        return self.get_king(pieces.PieceColor.WHITE if color == pieces.PieceColor.BLACK else pieces.PieceColor.BLACK)

    def in_board(self, pos):
        x, y = pos
        bot_x, bot_y = self.get_bottom_left()
        top_x, top_y = self.get_top_right()
        return bot_x <= x <= top_x and bot_y <= y <= top_y

    def get_first_rank(self, color):
        return self.get_bottom_left()[1] if color == pieces.PieceColor.WHITE else self.get_top_right()[1]

    def get_last_rank(self, color):
        return self.get_top_right()[1] if color == pieces.PieceColor.WHITE else self.get_bottom_left()[1]

    def get_first_file(self, color):
        return self.get_bottom_left()[0] if color == pieces.PieceColor.WHITE else self.get_top_right()[0]

    def get_last_file(self, color):
        return self.get_top_right()[0] if color == pieces.PieceColor.WHITE else self.get_bottom_left()[0]

    def is_first_rank(self, color, pos):
        _, y = pos
        return y == self.get_first_rank(color)

    def is_last_rank(self, color, pos):
        _, y = pos
        return y == self.get_last_rank(color)

    def is_en_passant_rank(self, color, pos):
        _, y = pos
        return y == self.get_en_passant_rank(color)

    def is_first_file(self, color, pos):
        x, _ = pos
        return x == self.get_first_file(color)

    def is_last_file(self, color, pos):
        x, _ = pos
        return x == self.get_last_file(color)


