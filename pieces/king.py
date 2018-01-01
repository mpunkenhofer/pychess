# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

import pieces
import general


class King(pieces.Piece):
    def __init__(self, board, pos, color):
        pieces.Piece.__init__(self, board, pos, color, 'King', 'K')
        self._checked_by_cache = (-1, [])

    def get_moves(self):
        moves = []
        squares = self.get_influenced_squares()
        p_x, p_y = self.position

        for s in squares:
            if self._board.protected_square(s, self._board.enemy_color(self)):
                continue

            if s in self._board.pieces:
                if self._board.pieces[s].color != self.color:
                    moves.append(general.CaptureMove(self, (p_x, p_y), s, self._board.pieces[s]))
            else:
                moves.append(general.Move(self, (p_x, p_y), s))

        self.king_side_castle()
        self.queen_side_castle()

        return moves

    def get_influenced_squares(self):
        influenced = []

        c = 1 if self.light() else -1
        p_x, p_y = self.position

        if general.Board.in_board(p_x - 1 * c, p_y - 1 * c):
            influenced.append((p_x - 1 * c, p_y - 1 * c))

        if general.Board.in_board(p_x, p_y - 1 * c):
            influenced.append((p_x, p_y - 1 * c))

        if general.Board.in_board(p_x + 1 * c, p_y - 1 * c):
            influenced.append((p_x + 1 * c, p_y - 1 * c))

        if general.Board.in_board(p_x + 1 * c, p_y):
            influenced.append((p_x + 1 * c, p_y))

        if general.Board.in_board(p_x + 1 * c, p_y + 1 * c):
            influenced.append((p_x + 1 * c, p_y + 1 * c))

        if general.Board.in_board(p_x, p_y + 1 * c):
            influenced.append((p_x, p_y + 1 * c))

        if general.Board.in_board(p_x - 1 * c, p_y + 1 * c):
            influenced.append((p_x - 1 * c, p_y + 1 * c))

        if general.Board.in_board(p_x - 1 * c, p_y):
            influenced.append((p_x - 1 * c, p_y))

        return influenced

    def in_check(self):
        return len(self.checked_by()) > 0

    def checkmated(self):
        if self.in_check():
            my_pieces = self._board.light_pieces() if self.light() else self._board.dark_pieces()

            for p in my_pieces:
                if len(p.moves()) != 0:
                    return False

            if len(self.get_moves()) != 0:
                return False

            return True
        else:
            return False

    def stalemated(self):
        if not self.in_check():
            my_pieces = self._board.light_pieces() if self.light() else self._board.dark_pieces()

            for p in my_pieces:
                if len(p.moves()) != 0:
                    return False

            if len(self.get_moves()) != 0:
                return False

            return True
        else:
            return False

    def checked_by(self):
        if not (self._checked_by_cache[0] == len(self._board.history()) and self._checked_by_cache[1]):
            potential_checked_by_pieces = self._board.dark_pieces() if self.light() else self._board.light_pieces()
            checked_by = []

            for p in potential_checked_by_pieces:
                for m in p.get_moves():
                    if m.type == 'Check':
                        checked_by.append(p)
                        break

            self._checked_by_cache = len(self._board.history()), checked_by

        return self._checked_by_cache[1]

    def queen_side_castle(self):
        pass

    def king_side_castle(self):
        pass
