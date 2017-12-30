# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

from abc import ABC, abstractmethod


class Piece(ABC):
    @abstractmethod
    def __init__(self, board, pos, color, t='', letter=''):
        self._board = board
        self._position = pos
        self._color = color
        self._type = t
        self._letter = letter
        self._history = []
        self._cache = (-1, [])

    def moves(self):
        if not (self._cache[0] == len(self._board.history()) and self._cache[1]):
            self._cache = len(self._board.history()), self.get_moves()

        return self._cache[1]

    @abstractmethod
    def influenced_squares(self):
        pass

    @abstractmethod
    def get_moves(self):
        pass

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, name):
        self._type = name

    @property
    def letter(self):
        return self._letter

    @letter.setter
    def letter(self, letter):
        self._letter = letter

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, pos):
        self._position = pos

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        if not (color == 'light' or color == 'dark'):
            raise ValueError('color property can only be light or dark')

        self._color = color

    def history(self):
        return self._history

    def light(self):
        return self.color == 'light'

    def dark(self):
        return self.color == 'dark'

    @staticmethod
    def _get_move(pm, pos):
        for m in pm:
            if m.destination == pos:
                return m
        return None

