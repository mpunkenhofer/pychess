# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import re


def from_algebraic(board, active_color, algebraic_move):
    algebraic_move = re.sub('[+#]', '', algebraic_move)  # remove check/checkmate characters

    pieces = board.filter_pieces(color=active_color)
    move_dict = {}

    for p in pieces:
        for move in p.moves():
            k = move.to_algebraic()

            if k not in move_dict:
                move_dict[k] = move

    return move_dict[algebraic_move] if algebraic_move in move_dict else None
