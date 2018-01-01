# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

import pieces
import general


class Rook(pieces.Piece):
    def __init__(self, board, pos, color):
        pieces.Piece.__init__(self, board, pos, color, 'Rook', 'R')

    def get_moves(self):
        if self._board.diagonal_pin(self):
            return []

        moves = []
        p_x, p_y = self.position

        if self._board.file_pin(self):
            squares = self._board.get_move_squares(self, general.MoveDirection.FileLeft)
            squares += self._board.get_move_squares(self, general.MoveDirection.FileRight)
        elif self._board.rank_pin(self):
            squares = self._board.get_move_squares(self, general.MoveDirection.RankUp)
            squares += self._board.get_move_squares(self, general.MoveDirection.RankDown)
        else:
            squares = self.influenced_squares()

        for s in squares:
            if s in self._board.pieces:
                if self._board.pieces[s].color != self.color:
                    moves.append(general.CaptureMove(self, (p_x, p_y), s, self._board.pieces[s]))
            else:
                moves.append(general.Move(self, (p_x, p_y), s))

        return moves

    def get_influenced_squares(self):
        influenced = []

        influenced += self._board.get_move_squares(self, general.MoveDirection.RankUp)
        influenced += self._board.get_move_squares(self, general.MoveDirection.RankDown)
        influenced += self._board.get_move_squares(self, general.MoveDirection.FileLeft)
        influenced += self._board.get_move_squares(self, general.MoveDirection.FileRight)

        return influenced

