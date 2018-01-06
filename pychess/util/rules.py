# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

from pychess.pieces import PieceColor


def half_move_clock(move_history):
    for i, m in enumerate(reversed(move_history)):
        if m.piece.is_pawn() and m.is_move():
            return i
        elif not m.is_move():
            return i

    return len(move_history)


def insufficient_material(board):
        white_pieces = board.get_pieces(PieceColor.WHITE)
        black_pieces = board.get_pieces(PieceColor.BLACK)

        if len(white_pieces) > 1 or len(black_pieces) > 1:
            return False

        if white_pieces and not (white_pieces[0].is_knight() or white_pieces[0].is_bishop()):
            return False

        if black_pieces and not (black_pieces[0].is_knight() or black_pieces[0].is_bishop()):
            return False

        return True
