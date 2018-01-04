# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

from pychess import pieces, moves


class Rook(pieces.Piece):
    def __init__(self, board, pos, color):
        pieces.Piece.__init__(self, board, pos, color, pieces.PieceType.ROOK)

    def get_moves(self):
        if self.diagonal_pin():
            return []

        m = []
        p_x, p_y = self.position

        if self.file_pin():
            squares = self.file_squares()
        elif self.rank_pin():
            squares = self.rank_squares()
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
        return self.file_squares(ignored) + self.rank_squares(ignored)
