# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

import pieces
import general


class Pawn(pieces.Piece):
    def __init__(self, board, pos, color):
        pieces.Piece.__init__(self, board, pos, color, 'Pawn', 'P')

    def moves(self):
        moves = []
        color = 1 if self.light() else -1
        p_x, p_y = self.position

        if not self.board.diagonal_pin(self) or not self.board.rank_pin(self):
            # pawn push
            if len(self.history) < 1 and general.Board.in_board(p_x, p_y + 2 * color) and len(
                    self.board.pieces_between_coords(p_x, p_y, p_x, p_y + 3 * color)) == 0:
                moves.append(general.Move(self, (p_x, p_y + 2 * color)))

            if general.Board.in_board(p_x, p_y + 1 * color) and len(
                    self.board.pieces_between_coords(p_x, p_y, p_x, p_y + 2 * color)) == 0:
                moves.append(general.Move(self, (p_x, p_y + 1 * color)))

        if not self.board.file_pin(self):
            # captures
            if (p_x + 1 * color, p_y + 1 * color) in self.board.pieces \
                    and self.board.pieces[(p_x + 1 * color, p_y + 1 * color)].dark():
                moves.append(general.CaptureMove(self,
                                                 (p_x + 1, p_y + 1),
                                                 self.board.pieces[(p_x + 1 * color, p_y + 1 * color)]))
            if (p_x - 1 * color, p_y + 1 * color) in self.board.pieces \
                    and self.board.pieces[(p_x - 1 * color, p_y + 1 * color)].dark():
                moves.append(general.CaptureMove(self,
                                                 (p_x - 1 * color, p_y + 1 * color),
                                                 self.board.pieces[(p_x - 1 * color, p_y + 1 * color)]))

        return moves
