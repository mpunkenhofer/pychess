# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

from pieces.piece import Piece
from general.board import Board
from general.move import Move
from general.move import MoveTypes


class Pawn(Piece):
    def __init__(self, board, pos, color):
        Piece.__init__(self, board, pos, color, 'Pawn', 'P')

    def moves(self):
        moves = []
        color = 1 if self.light() else -1
        p_x, p_y = self.position

        # pawn push
        if len(self.history) < 1 and Board.in_board(p_x, p_y + 2 * color) and len(
                self.board.pieces_between(p_x, p_y, p_x, p_y + 2 * color)) == 0:
            moves.append(Move(self.position, (p_x, p_y + 2 * color), MoveTypes.MOVE))

        if Board.in_board(p_x, p_y + 1 * color) and len(self.board.pieces_between(p_x, p_y, p_x, p_y + 1 * color)) == 0:
            moves.append(Move(self.position, (p_x, p_y + 1 * color), MoveTypes.MOVE))

        # captures
        if (p_x + 1 * color, p_y + 1 * color) in self.board.pieces \
                and self.board.pieces[(p_x + 1 * color, p_y + 1 * color)].dark():
            moves.append(Move(self.position, (p_x + 1, p_y + 1), MoveTypes.CAPTURE))
        if (p_x - 1 * color, p_y + 1 * color) in self.board.pieces \
                and self.board.pieces[(p_x - 1 * color, p_y + 1 * color)].dark():
            moves.append(Move(self.position, (p_x - 1 * color, p_y + 1 * color), MoveTypes.CAPTURE))

        return moves
