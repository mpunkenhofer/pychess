# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

from abc import ABC, abstractmethod


class ChessGUI(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def draw_board(self, board):
        pass

    @abstractmethod
    def choose_piece(self, board):
        pass

    @abstractmethod
    def move_piece(self, piece):
        pass
