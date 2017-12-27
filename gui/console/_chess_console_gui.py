# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

from gui._chess_gui import ChessGUI


class ChessConsoleGUI(ChessGUI):
    def __init__(self):
        ChessGUI.__init__(self)

    def draw_board(self, board):
        for y in reversed(range(0, 8)):
            for x in range(0, 8):
                if (x, y) in board.pieces:
                    if board.pieces[(x, y)].light():
                        print(board.pieces[(x, y)].letter, end='')
                    else:
                        print(board.pieces[(x, y)].letter.lower(), end='')
                else:
                    print('.', end='')

            print()

    def move(self, board, current_player):
        pass

