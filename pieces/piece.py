# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

from abc import ABC, abstractmethod


class Piece(ABC):
    @abstractmethod
    def __init__(self, board, pos, color, name='', letter=''):
        self.board = board
        self.position = pos
        self.color = color
        self.name = name
        self.__letter = letter

    @abstractmethod
    def move(self, pos):
        pass

    @abstractmethod
    def moves(self):
        pass

    @property
    def letter(self):
        return self.__letter

    @letter.setter
    def letter(self, letter):
        self.__letter = letter

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if not (color == 'light' or color == 'dark'):
            raise ValueError('color property can only be light or dark')

        self.__color = color

    def light(self):
        return self.color == 'light'

    def dark(self):
        return self.color == 'dark'

