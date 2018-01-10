# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

from pychess.pieces import PieceColor, PieceType


def half_move_clock(move_history):
    for i, m in enumerate(reversed(move_history)):
        if m.piece.is_pawn() and m.is_move():
            return i
        elif not m.is_move():
            return i

    return len(move_history)


def insufficient_material(board):
    # TODO: This function is incomplete see: http://www.e4ec.org/immr.html

    white_pieces = board.get_pieces(PieceColor.WHITE)
    black_pieces = board.get_pieces(PieceColor.BLACK)

    if len(white_pieces) > 1 or len(black_pieces) > 1:
        return False

    if black_pieces and not white_pieces and black_pieces[0].type in [PieceType.KNIGHT, PieceType.BISHOP]:
        return True

    if white_pieces and not black_pieces and white_pieces[0].type in [PieceType.KNIGHT, PieceType.BISHOP]:
        return True

    return False
