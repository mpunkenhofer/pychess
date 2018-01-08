# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import pychess.util.position

from pychess.board import StandardBoard
from pychess.pieces import King, Queen, Rook, Bishop, Knight, Pawn, PieceColor

from pychess import moves


class SetupBoard(StandardBoard):
    def __init__(self, fen_string='',
                 white_short_castle=True, white_long_castle=True, black_short_castle=True, black_long_castle=True):
        StandardBoard.__init__(self)

        self.enable_white_short_castle = white_short_castle
        self.enable_white_long_castle = white_long_castle
        self.enable_black_short_castle = black_short_castle
        self.enable_black_long_castle = black_long_castle

        self.pieces.clear()

        if fen_string:
            self.setup_board(fen_string)

    def setup_board(self, fen_string):
        fen_elements = fen_string.split(' ')

        if not fen_elements or len(fen_elements) < 4:
            raise ValueError('corrupt fen string')

        piece_string = fen_elements[0]
        active_color = fen_elements[1]
        castling = fen_elements[2]
        en_passant_target_square = fen_elements[3]
        # half_move_clock = fen_elements[4]
        # full_move_clock = fen_elements[5]

        if active_color not in ['w', 'b']:
            raise ValueError('corrupt fen string')

        ranks = piece_string.split('/')

        for i, r in enumerate(ranks):
            expanded_rank = ''
            for c in r:
                if c.isdigit():
                    expanded_rank += '.' * int(c)
                else:
                    expanded_rank += c
            ranks[i] = expanded_rank

        for y, rank in enumerate(reversed(ranks)):
            for x, p in enumerate(rank):
                if p.lower() in ['p', 'r', 'n', 'b', 'q', 'k']:
                    piece_type = p.lower()
                    color = PieceColor.BLACK if p.islower() else PieceColor.WHITE
                    pos = (x, y)

                    piece_dict = {'p': Pawn(self, pos, color),
                                  'k': King(self, pos, color),
                                  'q': Queen(self, pos, color),
                                  'r': Rook(self, pos, color),
                                  'b': Bishop(self, pos, color),
                                  'n': Knight(self, pos, color)}

                    self.put_piece(piece_dict[piece_type])

        white_king = self.get_king(PieceColor.WHITE)
        black_king = self.get_king(PieceColor.BLACK)

        if not white_king or not black_king:
            raise ValueError('missing a king!')

        if 'K' not in castling:
            self.enable_white_short_castle = False
        if 'Q' not in castling:
            self.enable_white_long_castle = False
        if 'k' not in castling:
            self.enable_black_short_castle = False
        if 'q' not in castling:
            self.enable_black_long_castle = False

        try:
            if en_passant_target_square != '-':
                color = PieceColor.BLACK if active_color == 'w' else PieceColor.WHITE
                c = 1 if color == PieceColor.WHITE else -1

                pos = pychess.util.position.from_algebraic(en_passant_target_square)

                origin = pos[0], pos[1] - 1 * c
                destination = pos[0], pos[1] + 1 * c

                piece = self.pieces[destination]

                if piece.color != color or not piece.is_pawn():
                    raise ValueError('corrupt fen string')

                move = moves.Move(piece, origin, destination)

                piece.history.append(move)
                self.history.append((move, move.to_algebraic()))
        except ValueError:
            raise ValueError('corrupt fen string')
        except KeyError:
            raise ValueError('corrupt fen string')

        # TODO: incorporate halfmove_clock and fullmove_clock (mainly usefull for pgns and 50-move-rule)

    def put_piece(self, piece):
        if piece.position in self.pieces:
            raise ValueError('position occupied!')

        if piece.is_king():
            king = self.get_king(piece.color)

            if king:
                raise ValueError("one color can only have one king!")

            other_king = self.get_king(piece.other_color())

            if other_king and piece.position in other_king.influenced_squares():
                raise ValueError("can't put king on a square next to the other king!")
        elif piece.is_pawn() and self.is_last_rank(piece.color, piece.position):
            raise ValueError("can't put pawn on the last rank!")

        self.pieces[piece.position] = piece

