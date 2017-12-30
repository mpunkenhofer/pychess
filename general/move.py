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


class Move(MoveTypes):
    def __init__(self, p, o, d):
        MoveTypes.__init__(self, p, o, d, 'Move')


class CheckMove(MoveTypes):
    def __init__(self, p, o, d):
        MoveTypes.__init__(self, p, o, d, 'Check')


class PromoteMove(MoveTypes):
    def __init__(self, p, o, d):
        MoveTypes.__init__(self, p, o, d, 'Promotion')
        self._promoted_piece = None

    @property
    def promoted_piece(self):
        return self._promoted_piece

    @promoted_piece.setter
    def promoted_piece(self, p):
        self._promoted_piece = p


class CaptureMove(MoveTypes):
    def __init__(self, p, o, d, cp):
        MoveTypes.__init__(self, p, o, d, 'Capture')
        self._captured_piece = cp

    @property
    def captured_piece(self):
        return self._captured_piece

    @captured_piece.setter
    def captured_piece(self, p):
        self._captured_piece = p


class MoveDirection(Enum):
    RankUp = auto()
    RankDown = auto()
    FileLeft = auto()
    FileRight = auto()
    FallingDiagonalUp = auto()
    FallingDiagonalDown = auto()
    RisingDiagonalUp = auto()
    RisingDiagonalDown = auto()
