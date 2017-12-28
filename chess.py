# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

import sys

from general import Board
from player.console import ChessConsolePlayer
from interface.console import ChessConsoleUserInterface


class Chess:
    def __init__(self, gui, players):
        self.board = Board()
        self.gui = gui
        self.players = players
        self.move_history = []

        self.current_player = self.players[0]

    def move(self):
        piece, move = self.gui.move(self.board, self.current_player)

        move = piece.move(move)
        self.move_history.append(move)

        self.current_player = self.players[0] if self.current_player != self.players[0] else self.players[1]

    def game_over(self):
        cmd = input('Enter q to quit!')

        if cmd == 'q':
            return True

        return False


def main():
    chess_game = Chess(ChessConsoleUserInterface(), (ChessConsolePlayer('white'), ChessConsolePlayer('black')))

    while not chess_game.game_over():
        chess_game.move()


if __name__ == "__main__":
    sys.exit(main())
