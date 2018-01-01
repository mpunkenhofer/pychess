# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

import pieces
import general


class Knight(pieces.Piece):
    def __init__(self, board, pos, color):
        pieces.Piece.__init__(self, board, pos, color, 'Knight', 'N')

    def get_moves(self):
        if self._board.diagonal_pin(self) or self._board.file_pin(self) or self._board.rank_pin(self):
            return []

        moves = []
        squares = self.influenced_squares()
        p_x, p_y = self.position

        for s in squares:
            if s in self._board.pieces:
                if self._board.pieces[s].color != self.color:
                    moves.append(general.CaptureMove(self, (p_x, p_y), s, self._board.pieces[s]))
            else:
                moves.append(general.Move(self, (p_x, p_y), s))

        return moves

    def get_influenced_squares(self):
        influenced = []
        c = 1 if self.light() else - 1
        p_x, p_y = self.position

        if general.Board.in_board(p_x - 1 * c, p_y + 2 * c):
            influenced.append((p_x - 1 * c, p_y + 2 * c))

        if general.Board.in_board(p_x - 1 * c, p_y - 2 * c):
            influenced.append((p_x - 1 * c, p_y - 2 * c))

        if general.Board.in_board(p_x + 1 * c, p_y + 2 * c):
            influenced.append((p_x + 1 * c, p_y + 2 * c))

        if general.Board.in_board(p_x + 1 * c, p_y - 2 * c):
            influenced.append((p_x + 1 * c, p_y - 2 * c))

        if general.Board.in_board(p_x - 2 * c, p_y + 1 * c):
            influenced.append((p_x - 2 * c, p_y + 1 * c))

        if general.Board.in_board(p_x - 2 * c, p_y - 1 * c):
            influenced.append((p_x - 2 * c, p_y - 1 * c))

        if general.Board.in_board(p_x + 2 * c, p_y + 1 * c):
            influenced.append((p_x + 2 * c, p_y + 1 * c))

        if general.Board.in_board(p_x + 2 * c, p_y - 1 * c):
            influenced.append((p_x + 2 * c, p_y - 1 * c))

        return influenced

