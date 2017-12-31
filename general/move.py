# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

from abc import ABC
from enum import Enum, auto


class MoveTypes(ABC):
    def __init__(self, p, o, d, t):
        self._piece = p
        self._origin = o
        self._destination = d
        self._type = t

    @property
    def piece(self):
        return self._piece

    @piece.setter
    def piece(self, p):
        self._piece = p

    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, o):
        self._origin = o

    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, d):
        self._destination = d

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, t):
        self._type = t

    def algebraic_destination(self):
        files = dict(zip([i for i in range(0, 8)], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']))

        return files[self.destination[0]] + str(self.destination[1] + 1)

    def algebraic_origin(self):
        files = dict(zip([i for i in range(0, 8)], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']))

        return files[self.origin[0]] + str(self.origin[1] + 1)


class Move(MoveTypes):
    def __init__(self, p, o, d):
        MoveTypes.__init__(self, p, o, d, 'Move')

    def __repr__(self):
        if self.piece.type == 'Pawn':
            return self.algebraic_destination()
        else:
            return self.piece.letter + self.algebraic_destination()


class CheckMove(MoveTypes):
    def __init__(self, p, o, d):
        MoveTypes.__init__(self, p, o, d, 'Check')

    def __repr__(self):
        if self.piece.type == 'Pawn':
            return self.algebraic_destination() + '+'
        else:
            return self.piece.letter + self.algebraic_destination() + '+'


class PromoteMove(MoveTypes):
    def __init__(self, p, o, d):
        MoveTypes.__init__(self, p, o, d, 'Promotion')
        self._promoted_piece_name = None
        self._promoted_piece = None

    def __repr__(self):
        p = self.promoted_piece_name if self.promoted_piece_name else '?'
        return self.algebraic_destination() + '=' + p

    @property
    def promoted_piece(self):
        return self._promoted_piece

    @promoted_piece.setter
    def promoted_piece(self, p):
        self._promoted_piece = p

    @property
    def promoted_piece_name(self):
        return self._promoted_piece_name

    @promoted_piece_name.setter
    def promoted_piece_name(self, p):
        self._promoted_piece_name = p


class CapturePromoteMove(MoveTypes):
    def __init__(self, p, o, d, cp):
        MoveTypes.__init__(self, p, o, d, 'Capture Promotion')
        self._captured_piece = cp
        self._promoted_piece_name = None
        self._promoted_piece = None

    def __repr__(self):
        p = self.promoted_piece_name if self.promoted_piece_name else '?'

        if self.piece.type == 'Pawn':
            return self.algebraic_origin()[0] + 'x' + self.algebraic_destination() + '=' + p
        else:
            return self.piece.letter + 'x' + self.algebraic_destination() + '=' + p

    @property
    def captured_piece(self):
        return self._captured_piece

    @captured_piece.setter
    def captured_piece(self, p):
        self._captured_piece = p

    @property
    def promoted_piece(self):
        return self._promoted_piece

    @promoted_piece.setter
    def promoted_piece(self, p):
        self._promoted_piece = p

    @property
    def promoted_piece_name(self):
        return self._promoted_piece_name

    @promoted_piece_name.setter
    def promoted_piece_name(self, p):
        self._promoted_piece_name = p


class CaptureMove(MoveTypes):
    def __init__(self, p, o, d, cp):
        MoveTypes.__init__(self, p, o, d, 'Capture')
        self._captured_piece = cp

    def __repr__(self):
        if self.piece.type == 'Pawn':
            return self.algebraic_origin()[0] + 'x' + self.algebraic_destination()
        else:
            return self.piece.letter + 'x' + self.algebraic_destination()

    @property
    def captured_piece(self):
        return self._captured_piece

    @captured_piece.setter
    def captured_piece(self, p):
        self._captured_piece = p


class KingSideCastleMove(MoveTypes):
    def __init__(self, p, o, d, k, r):
        MoveTypes.__init__(self, p, o, d, 'King Side Castle')
        self._king = k
        self._rook = r

    def __repr__(self):
        return 'O-O'

    @property
    def king(self):
        return self._king

    @king.setter
    def king(self, k):
        self._king = k

    @property
    def rook(self):
        return self._king

    @rook.setter
    def rook(self, r):
        self._rook = r


class QueenSideCastleMove(MoveTypes):
    def __init__(self, p, o, d, k, r):
        MoveTypes.__init__(self, p, o, d, 'Queen Side Castle')
        self._king = k
        self._rook = r

    def __repr__(self):
        return 'O-O-O'

    @property
    def king(self):
        return self._king

    @king.setter
    def king(self, k):
        self._king = k

    @property
    def rook(self):
        return self._king

    @rook.setter
    def rook(self, r):
        self._rook = r


class MoveDirection(Enum):
    RankUp = auto()
    RankDown = auto()
    FileLeft = auto()
    FileRight = auto()
    FallingDiagonalUp = auto()
    FallingDiagonalDown = auto()
    RisingDiagonalUp = auto()
    RisingDiagonalDown = auto()
