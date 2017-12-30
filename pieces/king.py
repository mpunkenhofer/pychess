# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

import pieces


class King(pieces.Piece):
    def __init__(self, board, pos, color):
        pieces.Piece.__init__(self, board, pos, color, 'King', 'K')
        self._checked_by_cache = (-1, [])

    def get_moves(self):
        return []

    def protected_squares(self):
        return self.get_moves()

    def in_check(self):
        return len(self._checked_by_cache[1]) != 0

    def checked_by(self):
        if not (self._checked_by_cache[0] == len(self._board.history()) and self._checked_by_cache[1]):
            potential_checked_by_pieces = self._board.dark_pieces() if self.light() else self._board.light_pieces()
            checked_by = []

            for p in potential_checked_by_pieces:
                moves = p.moves()

                for m in moves:
                    if m.type() == 'Check':
                        checked_by.append(p)
                        break

            self._checked_by_cache = len(self._board.history()), checked_by

        return self._checked_by_cache[1]
