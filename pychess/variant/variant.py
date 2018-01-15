# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

from abc import ABC, abstractmethod


class Variant(ABC):
    @abstractmethod
    def __init__(self, board=None):
        self.board = board

    @abstractmethod
    def is_draw(self):
        """
        Returns true if the game is drawn

        :return boolean
        """

    @abstractmethod
    def is_checkmated(self, color):
        """
        Returns true if the player represented by color is checkmated

        :param color: color representing player
        :return boolean
        """
