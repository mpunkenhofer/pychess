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
        self.__position = pos
        self.__color = color
        self.__name = name
        self.__letter = letter

    def move(self, pos):
        moves = self.moves()

        if pos in moves:
            piece = self.board.pop(self.position)
            piece.position = pos
            self.board[pos] = piece

    @abstractmethod
    def moves(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def letter(self):
        return self.__letter

    @letter.setter
    def letter(self, letter):
        self.__letter = letter

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, pos):
        self.__position = pos

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


class Move:
    def __init__(self):
        self.__origin = (-1, -1)
        self.__destination = (-1, -1)
        self.__capture = None

