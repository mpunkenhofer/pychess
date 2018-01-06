# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

from pychess import pieces, moves


class King(pieces.Piece):
    def __init__(self, board, pos, color):
        pieces.Piece.__init__(self, board, pos, color, pieces.PieceType.KING)
        self._checked_by_cache = (-1, [])

    def get_moves(self):
        m = []
        squares = self.influenced_squares()
        p_x, p_y = self.position

        for s in squares:
            if self.protected_square(s):
                continue

            if s in self.board.pieces:
                if self.board.pieces[s].color != self.color:
                    m.append(moves.Capture(self, (p_x, p_y), s, self.board.pieces[s]))
            else:
                m.append(moves.Move(self, (p_x, p_y), s))

        castle_short = self.short_castle()
        castle_long = self.long_castle()
        
        if castle_short:
            m.append(castle_short)
            
        if castle_long:
            m.append(castle_long)
            
        return m

    def get_influenced_squares(self, ignored):
        influenced = []

        c = 1 if self.is_white() else -1
        p_x, p_y = self.position

        if self.board.in_board((p_x - 1 * c, p_y - 1 * c)):
            influenced.append((p_x - 1 * c, p_y - 1 * c))

        if self.board.in_board((p_x, p_y - 1 * c)):
            influenced.append((p_x, p_y - 1 * c))

        if self.board.in_board((p_x + 1 * c, p_y - 1 * c)):
            influenced.append((p_x + 1 * c, p_y - 1 * c))

        if self.board.in_board((p_x + 1 * c, p_y)):
            influenced.append((p_x + 1 * c, p_y))

        if self.board.in_board((p_x + 1 * c, p_y + 1 * c)):
            influenced.append((p_x + 1 * c, p_y + 1 * c))

        if self.board.in_board((p_x, p_y + 1 * c)):
            influenced.append((p_x, p_y + 1 * c))

        if self.board.in_board((p_x - 1 * c, p_y + 1 * c)):
            influenced.append((p_x - 1 * c, p_y + 1 * c))

        if self.board.in_board((p_x - 1 * c, p_y)):
            influenced.append((p_x - 1 * c, p_y))

        return influenced

    def in_check(self):
        return len(self.checked_by()) > 0

    def is_checkmated(self):
        if self.in_check():
            if self.moves():
                return False

            for p in self.board.get_pieces(self.color):
                if p.moves():
                    return False

            return True

        return False

    def is_stalemated(self):
        if not self.in_check():
            if self.moves():
                return False

            for p in self.board.get_pieces(self.color):
                if p.moves():
                    return False

            return True

        return False

    def checked_by(self):
        if not (self._checked_by_cache[0] == len(self.board.history) and self._checked_by_cache[1]):
            checked_by = []

            for p in self.board.get_pieces(self.other_color()):
                for m in p.get_moves():
                    if m.is_attack():
                        checked_by.append(p)
                        break

            self._checked_by_cache = len(self.board.history), checked_by

        return self._checked_by_cache[1]

    def protected_square(self, square):
        for p in self.board.get_pieces(self.other_color()):
            for i in p.get_influenced_squares([self]):
                if i == square:
                    return True
        return False

    def short_castle(self):
        short_castle_enabled = self.board.enable_white_short_castle if self.is_white() \
            else self.board.enable_black_short_castle

        if not short_castle_enabled:
            return None

        rook_pos = (self.board.get_last_file(self.color) if self.is_white()
                    else self.board.get_first_file(self.color), self.board.get_first_rank(self.color))

        if rook_pos not in self.board.pieces:
            return None

        rook = self.board.pieces[rook_pos]
        
        if self.history or rook.history:
            return None

        if not self.board.is_first_rank(self.color, self.position) \
                or not self.board.is_first_rank(self.color, rook.position):
            return None

        if self.pieces_between(rook):
            return None

        if self.in_check():
            return None

        p_x, p_y = self.position
        
        king_pos, rook_pos = self.board.get_short_castle_positions(self.color)
        
        for x in range(min(p_x + 1, king_pos[0] + 1), max(p_x, king_pos[0])):
            if self.protected_square((x, p_y)):
                return None
            
        castle_move = moves.ShortCastle(self, (p_x, p_y), self, rook)
        
        return castle_move

    def long_castle(self):
        long_castle_enabled = self.board.enable_white_long_castle if self.is_white() \
            else self.board.enable_black_long_castle

        if not long_castle_enabled:
            return None

        rook_pos = (self.board.get_first_file(self.color) if self.is_white()
                    else self.board.get_last_file(self.color), self.board.get_first_rank(self.color))

        if rook_pos not in self.board.pieces:
            return None

        rook = self.board.pieces[rook_pos]

        if self.history or rook.history:
            return None

        if not self.board.is_first_rank(self.color, self.position) \
                or not self.board.is_first_rank(rook.color, rook.position):
            return None

        if self.pieces_between(rook):
            return None

        if self.in_check():
            return None

        p_x, p_y = self.position

        king_pos, rook_pos = self.board.get_long_castle_positions(self.color)

        for x in range(min(p_x + 1, king_pos[0] + 1), max(p_x, king_pos[0])):
            if self.protected_square((x, p_y)):
                return None

        castle_move = moves.LongCastle(self, (p_x, p_y), self, rook)

        return castle_move

