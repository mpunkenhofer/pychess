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

