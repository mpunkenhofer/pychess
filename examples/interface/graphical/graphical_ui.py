# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

from examples.interface import ChessUserInterface


class ChessGraphicalUserInterface(ChessUserInterface):
    def __init__(self, board):
        ChessUserInterface.__init__(self, board)

    def draw(self):
        # TODO implement
        pass

    def move(self, player):
        # TODO implement
        pass

    def game_over(self, loser):
        # TODO implement
        pass
