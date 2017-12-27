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
        return self.light_moves() if self.light() else self.dark_moves()

    def light_moves(self):
        moves = []
        p_x, p_y = self.position

        # pawn push
        if Board.in_board(p_x, p_y + 2) and len(self.history) < 1 and len(
                self.board.pieces_between(p_x, p_y, p_x, p_y + 2)) == 0:
            moves.append(Move(self.position, (p_x, p_y + 2), MoveTypes.MOVE))

        if Board.in_board(p_x, p_y + 1) and len(self.board.pieces_between(p_x, p_y, p_x, p_y + 1)) == 0:
            moves.append(Move(self.position, (p_x, p_y + 1), MoveTypes.MOVE))

        # captures
        if (p_x + 1, p_y + 1) in self.board.pieces and self.board.pieces[(p_x + 1, p_y + 1)].dark():
            moves.append(Move(self.position, (p_x + 1, p_y + 1), MoveTypes.CAPTURE))
        if (p_x - 1, p_y + 1) in self.board.pieces and self.board.pieces[(p_x - 1, p_y + 1)].dark():
            moves.append(Move(self.position, (p_x - 1, p_y + 1), MoveTypes.CAPTURE))

        return moves

    def dark_moves(self):
        moves = []
        p_x, p_y = self.position

        # pawn push
        if Board.in_board(p_x, p_y - 2) and len(self.history) < 1 and len(
                self.board.pieces_between(p_x, p_y, p_x, p_y - 2)) == 0:
            moves.append(Move(self.position, (p_x, p_y - 2), MoveTypes.MOVE))

        if Board.in_board(p_x, p_y - 1) and len(self.board.pieces_between(p_x, p_y, p_x, p_y - 1)) == 0:
            moves.append(Move(self.position, (p_x, p_y - 1), MoveTypes.MOVE))

        # captures
        if self.dark() and (p_x - 1, p_y - 1) in self.board.pieces and self.board.pieces[(p_x - 1, p_y - 1)].light():
            moves.append(Move(self.position, (p_x - 1, p_y - 1), MoveTypes.CAPTURE))
        if self.dark() and (p_x + 1, p_y - 1) in self.board.pieces and self.board.pieces[(p_x + 1, p_y - 1)].light():
            moves.append(Move(self.position, (p_x + 1, p_y - 1), MoveTypes.CAPTURE))

        return moves
