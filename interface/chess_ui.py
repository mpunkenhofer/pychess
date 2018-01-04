# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

from abc import ABC, abstractmethod


class ChessUserInterface(ABC):
    @abstractmethod
    def __init__(self, board):
        self.board = board

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def move(self, player):
        pass

    @abstractmethod
    def game_over(self, loser):
        pass
