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
        self.history = []

    def move(self, pos):
        move = self.get_move(self.moves(), pos)

        if move:
            piece = self.board.pieces.pop(move.piece.position)
            piece.position = move.destination
            self.board.pieces[move.destination] = piece
            self.history.append(move)

            return move
        else:
            return None

    @staticmethod
    def get_move(pm, pos):
        for m in pm:
            if m.destination == pos:
                return m
        return None

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

    def get_piece_history(self):
        return self.history

    def light(self):
        return self.color == 'light'

    def dark(self):
        return self.color == 'dark'

