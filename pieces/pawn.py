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

    def get_moves(self):
        moves = self.pawn_moves()
        moves += self.pawn_attacks()
        moves += self.en_passant()

        moves = general.Board.king_checked_moves(moves, self._board.my_king(self))

        return moves

    def influenced_squares(self):
        # influenced doesn't care about pins
        influenced = []
        color = 1 if self.light() else -1
        p_x, p_y = self.position

        if general.Board.in_board(p_x + 1 * color, p_y + 1 * color):
            influenced.append((p_x + 1 * color, p_y + 1 * color))

        if general.Board.in_board(p_x - 1 * color, p_y + 1 * color):
            influenced.append((p_x - 1 * color, p_y + 1 * color))

        return influenced

    def pawn_moves(self):
        moves = []
        color = 1 if self.light() else -1
        p_x, p_y = self.position

        if not self._board.diagonal_pin(self) or not self._board.rank_pin(self):
            # pawn push
            if len(self.history()) < 1 and general.Board.in_board(p_x, p_y + 2 * color) and len(
                    self._board.pieces_between(self, (p_x, p_y + 3 * color))) == 0:
                moves.append(general.Move(self, (p_x, p_y), (p_x, p_y + 2 * color)))

            if general.Board.in_board(p_x, p_y + 1 * color) and len(
                    self._board.pieces_between(self, (p_x, p_y + 2 * color))) == 0:
                # Promotion Move
                if general.Board.second_last_rank(self):
                    moves.append(general.PromoteMove(self, (p_x, p_y), (p_x, p_y + 1 * color)))
                else:
                    moves.append(general.Move(self, (p_x, p_y), (p_x, p_y + 1 * color)))

        return moves

    def pawn_attacks(self):
        moves = []
        color = 1 if self.light() else -1
        p_x, p_y = self.position

        if not self._board.file_pin(self):
            if (p_x + 1 * color, p_y + 1 * color) in self._board.pieces and \
                    self._board.pieces[(p_x + 1 * color, p_y + 1 * color)].color != self.color:
                if self._board.pieces[(p_x + 1 * color, p_y + 1 * color)] == self._board.enemy_king(self):
                    moves.append(general.CheckMove(self, (p_x, p_y), (p_x + 1 * color, p_y + 1 * color)))
                else:
                    moves.append(general.CaptureMove(self,
                                                     (p_x, p_y),
                                                     (p_x + 1 * color, p_y + 1 * color),
                                                     self._board.pieces[(p_x + 1 * color, p_y + 1 * color)]))
            if (p_x - 1 * color, p_y + 1 * color) in self._board.pieces and \
                    self._board.pieces[(p_x - 1 * color, p_y + 1 * color)].color != self.color:
                if self._board.pieces[(p_x - 1 * color, p_y + 1 * color)] == self._board.enemy_king(self):
                    moves.append(general.CheckMove(self, (p_x, p_y), (p_x - 1 * color, p_y + 1 * color)))
                else:
                    moves.append(general.CaptureMove(self,
                                                     (p_x, p_y),
                                                     (p_x - 1 * color, p_y + 1 * color),
                                                     self._board.pieces[(p_x - 1 * color, p_y + 1 * color)]))

        return moves

    def en_passant(self):
        moves = []
        color = 1 if self.light() else -1
        p_x, p_y = self.position

        if general.Board.en_passant_rank(self):
            last_move = self._board.history()[-1]

            if last_move and last_move.piece == 'Pawn' and last_move.piece.color != self.color and \
                    abs(last_move.origin[1] - last_move.destination[1]) > 1:
                left = (p_x - 1 * color, p_y)
                right = (p_x + 1 * color, p_y)

                if last_move.piece.position == left:
                    moves.append(general.CaptureMove(self,
                                                     (p_x, p_y),
                                                     (left[0], left[1] + 1 * color),
                                                     self._board.pieces[left]))
                elif last_move.piece.position == right:
                    moves.append(general.CaptureMove(self,
                                                     (p_x, p_y),
                                                     (right[0], right[1] + 1 * color),
                                                     self._board.pieces[right]))
        return moves
