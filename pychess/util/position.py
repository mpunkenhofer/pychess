# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#


def to_algebraic(pos, board=None):
    if not pos:
        raise ValueError('position_to_algebraic: pos argument is None')

    if not board:
        file_diff = rank_diff = 7
    else:
        file_diff = board.get_top_right()[0] - board.get_bottom_left()[0]
        rank_diff = board.get_top_right()[1] - board.get_bottom_left()[0]

    files = {board.get_bottom_left()[0] + (i - ord('a')): chr(i) for i in range(ord('a'), ord('a') + file_diff + 1)}
    ranks = {board.get_bottom_left()[1] + (i - 1): str(i) for i in range(1, 1 + rank_diff + 1)}

    return files[pos[0]] + ranks[pos[1]]


def from_algebraic(pos, board=None):
    return ''
