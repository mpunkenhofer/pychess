# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#


def to_string_array(board):
    file_diff = board.get_top_right()[0] - board.get_bottom_left()[0]
    rank_diff = board.get_top_right()[1] - board.get_bottom_left()[0]

    string_array = []

    for y in reversed(range(0, rank_diff + 1)):
        rank = ''

        for x in range(0, file_diff + 1):
            if board.piece_on((x, y)):
                piece = board.get_piece((x, y))
                if piece.is_white():
                    rank += piece.shorthand()
                else:
                    rank += piece.shorthand().lower()
            else:
                rank += '.'

        string_array.append(rank)

    return string_array
