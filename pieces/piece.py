# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

import general
from abc import ABC, abstractmethod


class Piece(ABC):
    @abstractmethod
    def __init__(self, board, pos, c, t='', letter=''):
        self._board = board
        self._position = pos
        self._color = c
        self._type = t
        self._letter = letter
        self._history = []
        self._move_cache = (-1, [])
        self._influence_cache = (-1, [])

    def moves(self):
        if not (self._move_cache[0] == len(self._board.history()) and self._move_cache[1]):
            self._move_cache = len(self._board.history()), self.get_moves()

        if self.type == 'King':
            return self._move_cache[1]

        king = self._board.my_king(self)

        if not king.in_check():
            return self._move_cache[1]

        checker = king.checked_by()

        if len(checker) > 1:
            return []

        moves = self.block_checker(checker)
        moves += self.capture_checker(checker)

        return moves

    def influenced_squares(self):
        if not (self._influence_cache[0] == len(self._board.history()) and self._influence_cache[1]):
            self._influence_cache = len(self._board.history()), self.get_influenced_squares()

        return self._influence_cache[1]

    @abstractmethod
    def get_moves(self):
        pass

    @abstractmethod
    def get_influenced_squares(self):
        pass

    def block_checker(self, checker):
        blocking_moves = set()

        for m in self._move_cache[1]:
            if checker.type == 'Rook' or 'Queen':
                if general.Board.same_rank(m.destination, checker):
                    blocking_moves.add(m)
                elif general.Board.same_file(m.destination, checker):
                    blocking_moves.add(m)
            if checker.type == 'Bishop' or 'Queen':
                if general.Board.same_diagonal(m.destination, checker):
                    blocking_moves.add(m)

        return list(blocking_moves)

    def capture_checker(self, checker):
        captures = []

        for m in self._move_cache[1]:
            if m.type == 'Capture' and m.piece == checker:
                captures.append(m)

        return captures

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

