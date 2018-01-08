# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import math

from pychess import pieces
from abc import ABC, abstractmethod
from pychess.util import rules
from pychess.util import position


class Board(ABC):
    @abstractmethod
    def __init__(self):
        self.history = []
        self.pieces = None

        self.enable_white_long_castle = self.enable_white_short_castle = True
        self.enable_black_short_castle = self.enable_black_long_castle = True

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

    @abstractmethod
    def piece_on(self, pos):
        pass

    @abstractmethod
    def _move(self, move):
        pass

    def move(self, move):
        algebraic_move = move.to_algebraic()

        move.piece.history.append(move)
        self.history.append((move, algebraic_move))

        self._move(move)

        check = '+' if self.get_enemy_king(move.piece.color).in_check() else ''
        check = '#' if self.get_enemy_king(move.piece.color).is_checkmated() else check

        if check:
            self.history[-1] = (move, algebraic_move + check)

    def algebraic_history(self):
        return [h for _, h in self.history]

    def move_history(self):
        return [m for m, _ in self.history]

    def get_last_move(self):
        if self.history:
            return self.history[-1][0]
        else:
            return None

    def fen(self):
        file_diff = self.get_top_right()[0] - self.get_bottom_left()[0]
        rank_diff = self.get_top_right()[1] - self.get_bottom_left()[0]

        ranks = []

        for y in reversed(range(0, rank_diff + 1)):
            rank = ''
            space_count = 0
            for x in range(0, file_diff + 1):
                if self.piece_on((x, y)):

                    if space_count > 0:
                        rank += str(space_count)
                    space_count = 0

                    piece = self.get_piece((x, y))
                    rank += piece.shorthand() if piece.is_white() else piece.shorthand().lower()
                else:
                    space_count += 1

            if space_count > 0:
                rank += str(space_count)

            ranks.append(rank)

        last_move = self.get_last_move()

        if not last_move:
            active_color = 'w'
        else:
            active_color = 'b' if last_move.piece.is_white() else 'w'

        white_king = self.get_king(pieces.PieceColor.WHITE)
        black_king = self.get_king(pieces.PieceColor.BLACK)

        castling = 'K' if self.enable_white_short_castle and \
            not self.king_or_rook_moved(white_king, self.get_king_side_rook(pieces.PieceColor.WHITE)) else ''
        castling += 'Q' if self.enable_white_long_castle and \
            not self.king_or_rook_moved(white_king, self.get_queen_side_rook(pieces.PieceColor.WHITE)) else ''

        castling += 'k' if self.enable_black_short_castle and \
            not self.king_or_rook_moved(black_king, self.get_king_side_rook(pieces.PieceColor.BLACK)) else ''
        castling += 'q' if self.enable_black_long_castle and \
            not self.king_or_rook_moved(black_king, self.get_queen_side_rook(pieces.PieceColor.BLACK)) else ''

        en_passant_target_square = self.en_passant_square()

        half_move_clock = str(rules.half_move_clock(self.move_history()))

        full_move_clock = str(int(math.ceil((len(self.move_history()) + 1) / 2)))

        return '/'.join(ranks) + ' ' + active_color + ' ' + castling + ' ' + en_passant_target_square + ' ' + \
               half_move_clock + ' ' + full_move_clock

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
        filtered_king = self.filter_pieces(pieces.PieceType.KING, color)
        if filtered_king:
            return filtered_king[0]
        else:
            return None

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

    @staticmethod
    def king_or_rook_moved(king, rook):
        if not king or not rook:
            return True

        if not king.is_king() or not rook.is_rook():
            return True

        if len(king.history) > 0 or len(rook.history) > 0:
            return True

        return False

    def en_passant_square(self):
        m = self.get_last_move()

        if m and m.piece.is_pawn() and abs(m.destination[1] - m.origin[1]) > 1:
            c = 1 if m.piece.is_white() else -1
            return position.to_algebraic((m.piece.position[0], m.piece.position[1] - 1 * c), self)

        return '-'
