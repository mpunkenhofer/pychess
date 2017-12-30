# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

from abc import ABC, abstractmethod


class ChessUserInterface(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def draw(self, game):
        pass

    @abstractmethod
    def move(self, game):
        pass

    @abstractmethod
    def promote(self, game):
        pass
