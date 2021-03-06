# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

from pychess import pieces, moves


class Rook(pieces.Piece):
    def __init__(self, board, pos, color):
        pieces.Piece.__init__(self, board, pos, color, pieces.PieceType.ROOK)

    def get_moves(self):
        if self.diagonally_pinned():
            return []

        m = []
        p_x, p_y = self.position

        if self.file_pinned():
            squares = self.get_file_squares()
        elif self.rank_pinned():
            squares = self.get_rank_squares()
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
        return self.get_file_squares(ignored) + self.get_rank_squares(ignored)
