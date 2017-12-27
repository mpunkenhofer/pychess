# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

from abc import ABC, abstractmethod


class MoveTypes(ABC):
    @abstractmethod
    def __init__(self, p, d):
        self.__piece = p
        self.__destination = d

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


class Move(MoveTypes):
    def __init__(self, p, d):
        MoveTypes.__init__(self, p, d)


class CaptureMove(MoveTypes):
    def __init__(self, p, d):
        MoveTypes.__init__(self, p, d)
        self.__captured_piece = None

    def __init__(self, p, d, captured_piece):
        self.__init__(p, d)
        self.__captured_piece = captured_piece

    @property
    def captured_piece(self):
        return self.__captured_piece

    @captured_piece.setter
    def captured_piece(self, p):
        self.__captured_piece = p

