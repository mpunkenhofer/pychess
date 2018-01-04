# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

from enum import Enum
from abc import ABC, abstractmethod


class MoveTypes(Enum):
    MOVE = 'Move'
    CAPTURE = 'Capture'
    PROMOTION = 'Promotion'
    CAPTURE_PROMOTION = 'Capture Promotion'
    KING_SIDE_CASTLE = 'King Side Castle'
    QUEEN_SIDE_CASTLE = 'Queen Side Castle'
    ATTACK = 'Attack'


class MoveType(ABC):
    @abstractmethod
    def __init__(self, p, o, d, t):
        self.piece = p
        self.origin = o
        self.destination = d
        self.type = t
        self.check = False

        self.promoted_piece = self.captured_piece = self.king = self.rook = None

    def is_move(self):
        return self.type == MoveTypes.MOVE

    def is_capture(self):
        return self.type == MoveTypes.CAPTURE

    def is_promotion(self):
        return self.type == MoveTypes.PROMOTION

    def is_capture_promotion(self):
        return self.type == MoveTypes.CAPTURE_PROMOTION

    def is_king_side_castle(self):
        return self.type == MoveTypes.KING_SIDE_CASTLE

    def is_queen_side_castle(self):
        return self.type == MoveTypes.KING_SIDE_CASTLE

    def is_attack(self):
        return self.type == MoveTypes.ATTACK

    def to_algebraic(self, board):

        if self.is_move():
            if self.piece.is_pawn():
                return self.position_to_algebraic(board, self.destination)
            else:
                return self.piece.shorthand() + self.position_to_algebraic(board, self.destination)
        elif self.is_capture():
            if self.piece.is_pawn():
                return self.position_to_algebraic(board, self.origin)[0] + 'x' + \
                       self.position_to_algebraic(board, self.destination)
            else:
                return self.piece.shorthand() + 'x' + self.position_to_algebraic(board, self.destination)
        elif self.is_promotion():
            return self.position_to_algebraic(board, self.destination) + '=' + self.promoted_piece.shorthand()
        elif self.is_capture_promotion():
            return self.position_to_algebraic(board, self.origin)[0] + 'x' + \
                             self.position_to_algebraic(board, self.destination) + '=' + self.promoted_piece.shorthand()
        elif self.is_king_side_castle():
            return 'O-O'
        elif self.is_queen_side_castle():
            return 'O-O-O'
        elif self.is_attack():
            return 'A ' + self.position_to_algebraic(board, self.destination)
        else:
            return ''

    @staticmethod
    def position_to_algebraic(board, pos):
        file_diff = board.get_top_right()[0] - board.get_bottom_left()[0]
        rank_diff = board.get_top_right()[1] - board.get_bottom_left()[0]

        files = {board.get_bottom_left()[0] + (i - ord('a')): chr(i) for i in range(ord('a'), ord('a') + file_diff + 1)}
        ranks = {board.get_bottom_left()[1] + (i - 1): str(i) for i in range(1, 1 + rank_diff + 1)}

        return files[pos[0]] + ranks[pos[1]]


class Move(MoveType):
    def __init__(self, p, o, d):
        MoveType.__init__(self, p, o, d, MoveTypes.MOVE)


class Capture(MoveType):
    def __init__(self, p, o, d, captured_piece):
        MoveType.__init__(self, p, o, d, MoveTypes.CAPTURE)
        self.captured_piece = captured_piece


class Promotion(MoveType):
    def __init__(self, p, o, d, promoted_piece):
        MoveType.__init__(self, p, o, d, MoveTypes.PROMOTION)
        self.promoted_piece = promoted_piece


class CapturePromotion(MoveType):
    def __init__(self, p, o, d, captured_piece, promoted_piece):
        MoveType.__init__(self, p, o, d, MoveTypes.CAPTURE_PROMOTION)
        self.captured_piece = captured_piece
        self.promoted_piece = promoted_piece


class KingSideCastle(MoveType):
    def __init__(self, p, o, k, r):
        MoveType.__init__(self, p, o, None, MoveTypes.KING_SIDE_CASTLE)
        self.king = k
        self.rook = r


class QueenSideCastle(MoveType):
    def __init__(self, p, o, k, r):
        MoveType.__init__(self, p, o, None, MoveTypes.QUEEN_SIDE_CASTLE)
        self.king = k
        self.rook = r


class Attack(MoveType):
    def __init__(self, p, o, d):
        MoveType.__init__(self, p, o, d, MoveTypes.ATTACK)

