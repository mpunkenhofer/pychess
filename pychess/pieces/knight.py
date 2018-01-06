# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

from pychess import pieces, moves


class Knight(pieces.Piece):
    def __init__(self, board, pos, color):
        pieces.Piece.__init__(self, board, pos, color, pieces.PieceType.KNIGHT)

    def get_moves(self):
        if self.diagonally_pinned() or self.file_pinned() or self.rank_pinned():
            return []

        m = []
        squares = self.influenced_squares()
        p_x, p_y = self.position

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
        influenced = []
        c = 1 if self.is_white() else - 1
        p_x, p_y = self.position

        if self.board.in_board((p_x - 1 * c, p_y + 2 * c)):
            influenced.append((p_x - 1 * c, p_y + 2 * c))

        if self.board.in_board((p_x - 1 * c, p_y - 2 * c)):
            influenced.append((p_x - 1 * c, p_y - 2 * c))

        if self.board.in_board((p_x + 1 * c, p_y + 2 * c)):
            influenced.append((p_x + 1 * c, p_y + 2 * c))

        if self.board.in_board((p_x + 1 * c, p_y - 2 * c)):
            influenced.append((p_x + 1 * c, p_y - 2 * c))

        if self.board.in_board((p_x - 2 * c, p_y + 1 * c)):
            influenced.append((p_x - 2 * c, p_y + 1 * c))

        if self.board.in_board((p_x - 2 * c, p_y - 1 * c)):
            influenced.append((p_x - 2 * c, p_y - 1 * c))

        if self.board.in_board((p_x + 2 * c, p_y + 1 * c)):
            influenced.append((p_x + 2 * c, p_y + 1 * c))

        if self.board.in_board((p_x + 2 * c, p_y - 1 * c)):
            influenced.append((p_x + 2 * c, p_y - 1 * c))

        return influenced

