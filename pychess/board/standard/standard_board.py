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

    def move(self, move):
        if not move:
            raise RuntimeError('moves(piece, m): no moves!')

        if move.is_capture():
            self.capture(move)
        elif move.type in [moves.MoveTypes.PROMOTION, moves.MoveTypes.CAPTURE_PROMOTION]:
            self.promote(move)
        elif move.type in [moves.MoveTypes.KING_SIDE_CASTLE, moves.MoveTypes.QUEEN_SIDE_CASTLE]:
            self.castle(move)
        else:
            self.simple_move(move)

        self.history.append(move)

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

        piece.history.append(move)

        piece.position = move.destination
        self.pieces[move.destination] = piece

    def castle(self, move):
        king = self.pieces.pop(move.king.position)
        rook = self.pieces.pop(move.rook.position)

        # add moves also to piece history
        king.history.append(move)
        rook.history.append(move)

        if move.is_king_side_castle():
            king_pos, rook_pos = self.get_king_side_castle_positions(king.color)
        else:
            king_pos, rook_pos = self.get_queen_side_castle_positions(king.color)

        king.position = king_pos
        rook.position = rook_pos

        self.pieces[king.position] = king
        self.pieces[rook.position] = rook

    def simple_move(self, move):
        piece = self.pieces.pop(move.piece.position)

        piece.history.append(move)

        piece.position = move.destination
        self.pieces[move.destination] = piece

    def get_piece(self, pos):
        return self.pieces[pos]

    def in_board(self, pos):
        x, y = pos
        return 0 <= x < 8 and 0 <= y < 8

    def get_first_rank(self, color):
        return 0 if color == PieceColor.WHITE else 7

    def get_last_rank(self, color):
        return 7 if color == PieceColor.WHITE else 0

    def get_first_file(self, color):
        return 0 if color == PieceColor.WHITE else 7

    def get_last_file(self, color):
        return 7 if color == PieceColor.WHITE else 0

    def get_en_passant_rank(self, color):
        return 4 if color == PieceColor.WHITE else 3

    def get_king_side_castle_positions(self, color):
        return (6, 0), (5, 0) if color == PieceColor.WHITE else (6, 7), (5, 7)

    def get_queen_side_castle_positions(self, color):
        return (2, 0), (3, 0) if color == PieceColor.WHITE else (2, 7), (3, 7)

    def position_to_algebraic(self, pos):
        file, rank = pos
        rank = str(rank + 1)
        files = dict(zip([i for i in range(0, 8)], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']))

        return files[file] + rank
