# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

from abc import ABC


class MoveTypes(ABC):
    def __init__(self, p, d, t):
        self.__piece = p
        self.__destination = d
        self.__type = t

    @property
    def piece(self):
        return self.__piece

    @piece.setter
    def piece(self, p):
        self.__piece = p

    @property
    def destination(self):
        return self.__destination

    @destination.setter
    def destination(self, d):
        self.__destination = d

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, t):
        self.__type = t


class Move(MoveTypes):
    def __init__(self, p, d):
        MoveTypes.__init__(self, p, d, 'Move')


class CaptureMove(MoveTypes):
    def __init__(self, p, d, cp):
        self.__init__(p, d, 'Capture')
        self.captured_piece = cp

    @property
    def captured_piece(self):
        return self.__captured_piece

    @captured_piece.setter
    def captured_piece(self, p):
        self.__captured_piece = p

