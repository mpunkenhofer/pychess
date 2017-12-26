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
        self.letter = letter

    @abstractmethod
    def move(self, pos):
        pass

    @abstractmethod
    def moves(self):
        pass
