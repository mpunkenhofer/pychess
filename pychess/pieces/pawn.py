# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

from pychess import pieces, moves


class Pawn(pieces.Piece):
    def __init__(self, board, pos, c):
        pieces.Piece.__init__(self, board, pos, c, pieces.PieceType.PAWN)

    def get_moves(self):
        return self.pawn_moves() + self.pawn_attacks() + self.en_passant()

    def get_influenced_squares(self, ignored):
        # influenced doesn't care about pins
        influenced = []
        c = 1 if self.is_white() else -1
        p_x, p_y = self.position

        if self.board.in_board((p_x + 1 * c, p_y + 1 * c)):
            influenced.append((p_x + 1 * c, p_y + 1 * c))

        if self.board.in_board((p_x - 1 * c, p_y + 1 * c)):
            influenced.append((p_x - 1 * c, p_y + 1 * c))

        return influenced

    def pawn_moves(self):
        if self.diagonal_pin() or self.rank_pin():
            return []

        m = []
        c = 1 if self.is_white() else -1
        p_x, p_y = self.position

        if not self.history and self.board.in_board((p_x, p_y + 2 * c)) and \
                not self.pieces_between((p_x, p_y + 3 * c)):
            m.append(moves.Move(self, (p_x, p_y), (p_x, p_y + 2 * c)))

        if self.board.in_board((p_x, p_y + 1 * c)) and \
                not self.pieces_between((p_x, p_y + 2 * c)):
            if self.board.is_last_rank(self.color, (p_x, p_y + 1 * c)):
                m += self.generate_all_promotions((p_x, p_y), (p_x, p_y + 1 * c))
            else:
                m.append(moves.Move(self, (p_x, p_y), (p_x, p_y + 1 * c)))

        return m

    def pawn_attacks(self):
        if self.file_pin() or self.rank_pin():
            return []

        m = []
        squares = self.influenced_squares()
        p_x, p_y = self.position

        for s in squares:
            if s in self.board.pieces:
                if self.board.pieces[s].color != self.color:
                    if self.board.pieces[s] == self.board.get_enemy_king(self.color):
                        m.append(moves.Attack(self, (p_x, p_y), s))
                    elif self.board.is_last_rank(self.color, s):
                        m += self.generate_all_promotions((p_x, p_y), s, self.board.pieces[s])
                    else:
                        m.append(moves.Capture(self, (p_x, p_y), s, self.board.pieces[s]))

        return m

    def en_passant(self):
        if self.file_pin() or self.rank_pin():
            return []

        m = []
        c = 1 if self.is_white() else -1
        p_x, p_y = self.position

        if self.board.is_en_passant_rank(self.color, self.position):
            last_move = self.board.history[-1]

            if last_move and last_move.piece.is_pawn() and last_move.piece.color != self.color and \
                    abs(last_move.origin[1] - last_move.destination[1]) > 1:
                left = (p_x - 1 * c, p_y)
                right = (p_x + 1 * c, p_y)

                if last_move.piece.position == left:
                    m.append(moves.Capture(self, (p_x, p_y), (left[0], left[1] + 1 * c), self.board.pieces[left]))
                elif last_move.piece.position == right:
                    m.append(moves.Capture(self, (p_x, p_y), (right[0], right[1] + 1 * c), self.board.pieces[right]))
        return m

    def generate_all_promotions(self, origin, destination, capture=None):
        promotions = []
        promoted_pieces = [pieces.Queen(self.board, destination, self.color),
                           pieces.Rook(self.board, destination, self.color),
                           pieces.Bishop(self.board, destination, self.color),
                           pieces.Knight(self.board, destination, self.color)]

        for p in promoted_pieces:
            if capture:
                promotions.append(moves.CapturePromotion(self, origin, destination, capture, p))
            else:
                promotions.append(moves.Promotion(self, origin, destination, p))

        return promotions
