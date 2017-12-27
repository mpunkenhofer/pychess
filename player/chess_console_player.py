# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

from player.chess_player import ChessPlayer


class ChessConsolePlayer(ChessPlayer):
    def __init__(self, color):
        ChessPlayer.__init__(color)

    def move(self, board):
        pass
