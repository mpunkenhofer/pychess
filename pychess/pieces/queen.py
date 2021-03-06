# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

from pychess import pieces, moves


class Queen(pieces.Piece):
    def __init__(self, board, pos, color):
        pieces.Piece.__init__(self, board, pos, color, pieces.PieceType.QUEEN)

    def get_moves(self):
        m = []
        p_x, p_y = self.position
        pining_piece = self.diagonal_pin_piece()

        if self.file_pinned():
            squares = self.get_file_squares()
        elif self.rank_pinned():
            squares = self.get_rank_squares()
        elif pining_piece and self.same_rising_diagonal(self, pining_piece):
            squares = self.get_rising_diagonal_squares()
        elif pining_piece and self.same_falling_diagonal(self, pining_piece):
            squares = self.get_falling_diagonal_squares()
        else:
            squares = self.influenced_squares()

        for s in squares:
            if s in self.board.pieces:
                if self.board.pieces[s].color != self.color:
                    if self.board.pieces[s] == self.board.get_enemy_king(self.color):
                        m.append(moves.Attack(self, (p_x, p_y), s))
                    else:
                        m.append(moves.Capture(self, (p_x, p_y), s, self.board.pieces[s]))
            else:
                m.append(moves.Move(self, (p_x, p_y), s))

        return m

    def get_influenced_squares(self, ignored):
        return self.get_diagonal_squares(ignored) + self.get_rank_squares(ignored) + self.get_file_squares(ignored)
