# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

from abc import ABC, abstractmethod


class Variant(ABC):
    @abstractmethod
    def __init__(self):
        self.board = None

    @abstractmethod
    def is_draw(self):
        pass

    @abstractmethod
    def is_checkmated(self, color):
        pass
