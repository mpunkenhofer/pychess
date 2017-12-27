# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

from abc import ABC, abstractmethod


class MoveTypes(ABC):
    @abstractmethod
    def __init__(self, o, d):
        self.__origin = o
        self.__destination = d

    @property
    def origin(self):
        return self.__origin

    @origin.setter
    def origin(self, o):
        self.__origin = o

    @property
    def destination(self):
        return self.__destination

    @destination.setter
    def destination(self, d):
        self.__destination = d


class Move(MoveTypes):
    def __init__(self, o, d):
        MoveTypes.__init__(self, o, d)


class CaptureMove(MoveTypes):
    def __init__(self, o, d):
        MoveTypes.__init__(self, o, d)
        self.__captured_piece = None

    def __init__(self, o, d, captured_piece):
        self.__init__(o, d)
        self.__captured_piece = captured_piece

    @property
    def captured_piece(self):
        return self.__captured_piece

    @captured_piece.setter
    def captured_piece(self, p):
        self.__captured_piece = p

