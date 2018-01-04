# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

from pychess import pieces, moves


class Queen(pieces.Piece):
    def __init__(self, board, pos, color):
        pieces.Piece.__init__(self, board, pos, color, pieces.PieceType.QUEEN)

    def get_moves(self):
        m = []
        p_x, p_y = self.position
        pining_piece = self.diagonal_pin_piece()

        # TODO file, rank pins

        if self.file_pin():
            squares = self.file_squares()
        elif self.rank_pin():
            squares = self.rank_squares()
        elif pining_piece and self.same_rising_diagonal(self, pining_piece):
            squares = self.rising_diagonal_squares()
        elif pining_piece and self.same_falling_diagonal(self, pining_piece):
            squares = self.falling_diagonal_squares()
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
        return self.diagonal_squares(ignored) + self.rank_squares(ignored) + self.file_squares(ignored)
