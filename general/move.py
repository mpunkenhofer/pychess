# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

from enum import Enum


class MoveTypes(Enum):
    MOVE = 0
    CAPTURE = 1
    KING_SIDE_CASTLE = 2
    QUEEN_SIDE_CASTLE = 3


class Move:
    def __init__(self):
        self.__origin = None
        self.__destination = None
        self.__type = None

    def __init__(self, o, d, t):
        self.__origin = o
        self.__destination = d
        self.__type = t

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

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, t):
        self.__type = t
