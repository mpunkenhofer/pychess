# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

from pychess import moves, board

from pychess.pieces import King, Queen, Rook, Bishop, Knight, Pawn, PieceColor


class StandardBoard(board.Board):
    def __init__(self):
        board.Board.__init__(self)

        self.pieces = {(4, 0): King(self, (4, 0), PieceColor.WHITE), (4, 7): King(self, (4, 7), PieceColor.BLACK),
                       (3, 0): Queen(self, (3, 0), PieceColor.WHITE), (3, 7): Queen(self, (3, 7), PieceColor.BLACK),
                       (0, 0): Rook(self, (0, 0), PieceColor.WHITE), (7, 0): Rook(self, (7, 0), PieceColor.WHITE),
                       (0, 7): Rook(self, (0, 7), PieceColor.BLACK), (7, 7): Rook(self, (7, 7), PieceColor.BLACK),
                       (2, 0): Bishop(self, (2, 0), PieceColor.WHITE), (5, 0): Bishop(self, (5, 0), PieceColor.WHITE),
                       (2, 7): Bishop(self, (2, 7), PieceColor.BLACK), (5, 7): Bishop(self, (5, 7), PieceColor.BLACK),
                       (1, 0): Knight(self, (1, 0), PieceColor.WHITE), (6, 0): Knight(self, (6, 0), PieceColor.WHITE),
                       (1, 7): Knight(self, (1, 7), PieceColor.BLACK), (6, 7): Knight(self, (6, 7), PieceColor.BLACK)}

        for i in range(0, 8):
            self.pieces[(i, 1)] = Pawn(self, (i, 1), PieceColor.WHITE)
            self.pieces[(i, 6)] = Pawn(self, (i, 6), PieceColor.BLACK)

        self.king_side_rooks = self.pieces[(7, 0)], self.pieces[(7, 7)]
        self.queen_side_rooks = self.pieces[(0, 0)], self.pieces[(0, 7)]

    def _move(self, move):
        if not move:
            raise RuntimeError('moves(piece, m): no moves!')

        if move.is_capture():
            self.capture(move)
        elif move.type in [moves.MoveTypes.PROMOTION, moves.MoveTypes.CAPTURE_PROMOTION]:
            self.promote(move)
        elif move.type in [moves.MoveTypes.SHORT_CASTLE, moves.MoveTypes.LONG_CASTLE]:
            self.castle(move)
        else:
            self.simple_move(move)

        return move

    def promote(self, move):
        if move.piece.is_pawn():
            if move.is_capture_promotion():
                # remove captured piece
                self.pieces.pop(move.captured_piece.position)

            self.pieces.pop(move.piece.position)  # remove pawn
            self.pieces[move.destination] = move.promoted_piece

    def capture(self, move):
        # remove captured piece
        self.pieces.pop(move.captured_piece.position)

        piece = self.pieces.pop(move.piece.position)

        piece.position = move.destination
        self.pieces[move.destination] = piece

    def castle(self, move):
        king = self.pieces.pop(move.king.position)
        rook = self.pieces.pop(move.rook.position)

        king_pos, rook_pos = self.get_short_castle_positions(king.color) if move.is_king_side_castle() \
            else self.get_long_castle_positions(king.color)

        king.position = king_pos
        rook.position = rook_pos

        self.pieces[king.position] = king
        self.pieces[rook.position] = rook

    def simple_move(self, move):
        piece = self.pieces.pop(move.piece.position)

        piece.position = move.destination
        self.pieces[move.destination] = piece

    def get_bottom_left(self):
        return 0, 0

    def get_top_right(self):
        return 7, 7

    def get_piece(self, pos):
        return self.pieces[pos]

    def piece_on(self, pos):
        return pos in self.pieces

    def get_en_passant_rank(self, color):
        return 4 if color == PieceColor.WHITE else 3

    def get_short_castle_positions(self, color):
        return ((6, 0), (5, 0)) if color == PieceColor.WHITE else ((6, 7), (5, 7))

    def get_long_castle_positions(self, color):
        return ((2, 0), (3, 0)) if color == PieceColor.WHITE else ((2, 7), (3, 7))

    def get_queen_side_rook(self, color):
        return self.queen_side_rooks[0] if color == PieceColor.WHITE else self.queen_side_rooks[1]

    def get_king_side_rook(self, color):
        return self.king_side_rooks[0] if color == PieceColor.WHITE else self.king_side_rooks[1]
