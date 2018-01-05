# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

import pychess.pieces
import copy

from enum import Enum
from abc import ABC, abstractmethod

from pychess.util import position


class MoveTypes(Enum):
    MOVE = 'Move'
    CAPTURE = 'Capture'
    PROMOTION = 'Promotion'
    CAPTURE_PROMOTION = 'Capture Promotion'
    SHORT_CASTLE = 'King Side Castle'
    LONG_CASTLE = 'Queen Side Castle'
    ATTACK = 'Attack'


class MoveType(ABC):
    @abstractmethod
    def __init__(self, p, o, d, t):
        self.piece = p
        self.origin = o
        self.destination = d
        self.type = t

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
        return self.type == MoveTypes.SHORT_CASTLE

    def is_queen_side_castle(self):
        return self.type == MoveTypes.LONG_CASTLE

    def is_attack(self):
        return self.type == MoveTypes.ATTACK

    def to_algebraic(self):
        pass

    def get_piece_id(self):
        if self.piece.is_pawn() or self.piece.is_king():
            return ''

        same_pieces = [p for p in self.piece.board.filter_pieces(self.piece.type, self.piece.color)
                       if not p == self.piece]

        if len(same_pieces) > 0:
            pieces_with_same_destination = []

            for p in same_pieces:
                for m in p.moves():
                    if m.destination == self.destination:
                        pieces_with_same_destination.append(p)
                        break

            if not pieces_with_same_destination:
                return ''

            same_file = False

            for p in pieces_with_same_destination:
                if pychess.pieces.Piece.same_file(p, self.piece):
                    same_file = True
                    break

            algebraic_pos = position.to_algebraic(self.origin, self.piece.board)

            return algebraic_pos[1] if same_file else algebraic_pos[0]

        return ''


class Move(MoveType):
    def __init__(self, p, o, d):
        MoveType.__init__(self, p, o, d, MoveTypes.MOVE)

    def to_algebraic(self):
        if self.piece.is_pawn():
            return position.to_algebraic(self.destination, self.piece.board)
        else:
            piece_id = self.get_piece_id()
            return self.piece.shorthand() + piece_id + position.to_algebraic(self.destination, self.piece.board)


class Capture(MoveType):
    def __init__(self, p, o, d, captured_piece):
        MoveType.__init__(self, p, o, d, MoveTypes.CAPTURE)

        self.captured_piece = captured_piece

    def to_algebraic(self):
        if self.piece.is_pawn():
            return position.to_algebraic(self.piece.board, self.origin)[0] + 'x' + \
                   position.to_algebraic(self.destination, self.piece.board)
        else:
            piece_id = self.get_piece_id()

            return self.piece.shorthand() + piece_id + 'x' + \
                   position.to_algebraic(self.destination, self.piece.board)


class Promotion(MoveType):
    def __init__(self, p, o, d, promoted_piece):
        MoveType.__init__(self, p, o, d, MoveTypes.PROMOTION)
        self.promoted_piece = promoted_piece

    def to_algebraic(self):
        return position.to_algebraic(self.destination, self.piece.board) + '=' + \
               self.promoted_piece.shorthand()


class CapturePromotion(MoveType):
    def __init__(self, p, o, d, captured_piece, promoted_piece):
        MoveType.__init__(self, p, o, d, MoveTypes.CAPTURE_PROMOTION)
        self.captured_piece = captured_piece
        self.promoted_piece = promoted_piece

    def to_algebraic(self):
        return position.to_algebraic(self.origin, self.piece.board)[0] + 'x' + \
               position.to_algebraic(self.destination, self.piece.board) + '=' + \
               self.promoted_piece.shorthand()


class ShortCastle(MoveType):
    def __init__(self, p, o, k, r):
        MoveType.__init__(self, p, o, None, MoveTypes.SHORT_CASTLE)
        self.king = k
        self.rook = r

    def to_algebraic(self):
        return 'O-O'


class LongCastle(MoveType):
    def __init__(self, p, o, k, r):
        MoveType.__init__(self, p, o, None, MoveTypes.LONG_CASTLE)
        self.king = k
        self.rook = r

    def to_algebraic(self):
        return 'O-O-O'


class Attack(MoveType):
    def __init__(self, p, o, d):
        MoveType.__init__(self, p, o, d, MoveTypes.ATTACK)

    def to_algebraic(self):
        return 'A ' + position.to_algebraic(self.destination, self.piece.board)

