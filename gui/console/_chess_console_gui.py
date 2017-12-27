# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

from gui import ChessGUI
import re


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
        while True:
            move_input = input(current_player.color + ': ')

            if len(move_input) < 2:
                print('Invalid move format. (See chess move notation)')
                continue

            capture_by_piece = re.match('([KQRBN])x([a-h])([1-8]).?', move_input)
            capture_by_pawn = re.match('([a-h])x([a-h])([1-8]).?', move_input)

            pawn_move = re.match('([a-h])([1-8]).?', move_input)
            piece_move = re.match('([KQRBN])([a-h])([1-8]).?', move_input)
            specific_piece_move = re.match('([QRBN])([a-h])([a-h])([1-8]).?', move_input)

            if capture_by_piece:
                piece = capture_by_piece.group(1)
                file = capture_by_piece.group(2)
                rank = capture_by_piece.group(3)
            elif capture_by_pawn:
                pawn = capture_by_pawn.group(1)
                file = capture_by_pawn.group(2)
                rank = capture_by_pawn.group(3)
            elif pawn_move:
                file = pawn_move.group(1)
                rank = pawn_move.group(2)
            elif piece_move:
                piece = piece_move.group(1)
                file = piece_move.group(2)
                rank = piece_move.group(3)
            elif specific_piece_move:
                piece = specific_piece_move.group(1)
                piece_id = specific_piece_move.group(2)
                file = specific_piece_move.group(3)
                rank = specific_piece_move.group(4)
            








