# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

import pieces
import general


class King(pieces.Piece):
    def __init__(self, board, pos, color):
        pieces.Piece.__init__(self, board, pos, color, 'King', 'K')
        self._checked_by_cache = (-1, [])

    def get_moves(self):
        moves = []
        squares = self.influenced_squares()
        p_x, p_y = self.position

        for s in squares:
            if self._board.protected_square(s, self._board.enemy_color(self)):
                continue

            if s in self._board.pieces:
                if self._board.pieces[s].color != self.color:
                    moves.append(general.CaptureMove(self, (p_x, p_y), s, self._board.pieces[s]))
            else:
                moves.append(general.Move(self, (p_x, p_y), s))

        castle_king_side = self.king_side_castle()
        castle_queen_side = self.queen_side_castle()
        
        if castle_king_side:
            moves.append(castle_king_side)
            
        if castle_queen_side:
            moves.append(castle_queen_side)
            
        return moves

    def get_influenced_squares(self):
        influenced = []

        c = 1 if self.light() else -1
        p_x, p_y = self.position

        if general.Board.in_board(p_x - 1 * c, p_y - 1 * c):
            influenced.append((p_x - 1 * c, p_y - 1 * c))

        if general.Board.in_board(p_x, p_y - 1 * c):
            influenced.append((p_x, p_y - 1 * c))

        if general.Board.in_board(p_x + 1 * c, p_y - 1 * c):
            influenced.append((p_x + 1 * c, p_y - 1 * c))

        if general.Board.in_board(p_x + 1 * c, p_y):
            influenced.append((p_x + 1 * c, p_y))

        if general.Board.in_board(p_x + 1 * c, p_y + 1 * c):
            influenced.append((p_x + 1 * c, p_y + 1 * c))

        if general.Board.in_board(p_x, p_y + 1 * c):
            influenced.append((p_x, p_y + 1 * c))

        if general.Board.in_board(p_x - 1 * c, p_y + 1 * c):
            influenced.append((p_x - 1 * c, p_y + 1 * c))

        if general.Board.in_board(p_x - 1 * c, p_y):
            influenced.append((p_x - 1 * c, p_y))

        return influenced

    def in_check(self):
        return len(self.checked_by()) > 0

    def checkmated(self):
        if self.in_check():
            my_pieces = self._board.light_pieces() if self.light() else self._board.dark_pieces()

            for p in my_pieces:
                if len(p.moves()) != 0:
                    return False

            if len(self.get_moves()) != 0:
                return False

            return True
        else:
            return False

    def stalemated(self):
        if not self.in_check():
            my_pieces = self._board.light_pieces() if self.light() else self._board.dark_pieces()

            for p in my_pieces:
                if len(p.moves()) != 0:
                    return False

            if len(self.get_moves()) != 0:
                return False

            return True
        else:
            return False

    def checked_by(self):
        if not (self._checked_by_cache[0] == len(self._board.history()) and self._checked_by_cache[1]):
            potential_checked_by_pieces = self._board.dark_pieces() if self.light() else self._board.light_pieces()
            checked_by = []

            for p in potential_checked_by_pieces:
                for m in p.get_moves():
                    if m.type == 'Check':
                        checked_by.append(p)
                        break

            self._checked_by_cache = len(self._board.history()), checked_by

        return self._checked_by_cache[1]

    def king_side_castle(self):
        rook = self._board.king_side_rook(self.color)
        
        if len(self.history()) > 0 or len(rook.history()) > 0:
            return None

        if not self._board.first_rank(self) or not self._board.first_rank(rook):
            return None

        if self._board.pieces_between(self, rook):
            return None

        if self.in_check():
            return None

        p_x, p_y = self.position
        
        king_pos, rook_pos = general.Board.king_side_castle_positions(self.color)
        
        for x in range(min(p_x + 1, king_pos[0] + 1), max(p_x, king_pos[0])):
            if self._board.protected_square((x, p_y), self._board.enemy_color(self)):
                return None
            
        castle_move = general.KingSideCastleMove(self, (p_x, p_y), king_pos, rook_pos, self, rook)
        
        return castle_move

    def queen_side_castle(self):
        rook = self._board.queen_side_rook(self.color)

        if len(self.history()) > 0 or len(rook.history()) > 0:
            return None

        if not self._board.first_rank(self) or not self._board.first_rank(rook):
            return None

        if self._board.pieces_between(self, rook):
            return None

        if self.in_check():
            return None

        p_x, p_y = self.position

        king_pos, rook_pos = general.Board.queen_side_castle_positions(self.color)

        for x in range(min(p_x + 1, king_pos[0] + 1), max(p_x, king_pos[0])):
            if self._board.protected_square((x, p_y), self._board.enemy_color(self)):
                return None

        castle_move = general.QueenSideCastleMove(self, (p_x, p_y), king_pos, rook_pos, self, rook)

        return castle_move
