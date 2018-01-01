# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

import pieces
import general


class Bishop(pieces.Piece):
    def __init__(self, board, pos, color):
        pieces.Piece.__init__(self, board, pos, color, 'Bishop', 'B')

    def get_moves(self):
        if self._board.file_pin(self) or self._board.rank_pin(self):
            return []

        moves = []
        p_x, p_y = self.position
        pining_piece = self._board.diagonal_pin_piece(self)

        if self._board.file_pin(self):
            squares = self._board.get_move_squares(self, general.MoveDirection.FileLeft)
            squares += self._board.get_move_squares(self, general.MoveDirection.FileRight)
        elif self._board.rank_pin(self):
            squares = self._board.get_move_squares(self, general.MoveDirection.RankUp)
            squares += self._board.get_move_squares(self, general.MoveDirection.RankDown)
        elif pining_piece and general.Board.same_rising_diagonal(self, pining_piece):
            squares = self._board.get_move_squares(self, general.MoveDirection.RisingDiagonalUp)
            squares += self._board.get_move_squares(self, general.MoveDirection.RisingDiagonalDown)
        elif pining_piece and general.Board.same_falling_diagonal(self, pining_piece):
            squares = self._board.get_move_squares(self, general.MoveDirection.RisingDiagonalUp)
            squares += self._board.get_move_squares(self, general.MoveDirection.RisingDiagonalDown)
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

        influenced += self._board.get_move_squares(self, general.MoveDirection.RisingDiagonalUp)
        influenced += self._board.get_move_squares(self, general.MoveDirection.RisingDiagonalDown)
        influenced += self._board.get_move_squares(self, general.MoveDirection.FallingDiagonalUp)
        influenced += self._board.get_move_squares(self, general.MoveDirection.FallingDiagonalDown)

        return influenced
