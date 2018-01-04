# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

import re
import math

from interface import ChessUserInterface

from pychess.pieces import PieceColor, PieceType
from pychess.moves import MoveTypes


class ChessConsoleUserInterface(ChessUserInterface):
    def __init__(self):
        ChessUserInterface.__init__(self)

        self.piece_dict = {'Q': PieceType.QUEEN,
                           'R': PieceType.ROOK,
                           'B': PieceType.BISHOP,
                           'N': PieceType.KNIGHT,
                           'K': PieceType.KING}

    def draw(self, board):
        for y in reversed(range(0, 8)):
            for x in range(0, 8):
                if (x, y) in board.pieces:
                    if board.pieces[(x, y)].is_white():
                        print(board.pieces[(x, y)].shorthand(), end='')
                    else:
                        print(board.pieces[(x, y)].shorthand().lower(), end='')
                else:
                    print('.', end='')

            print()

    def move(self, board, player):
        while True:
            move_input = input(str(int(math.ceil((len(board.history) + 1) / 2))) + ': ')

            move_input = re.sub('[+#]', '', move_input)

            possible_moves = re.match('p ([a-h])([1-8])', move_input)
            capture_by_piece = re.match('([KQRBN])x([a-h])([1-8])', move_input)
            capture_by_pawn_promotion = re.match('([a-h])x([a-h])([1-8])=([QRBN])', move_input)
            capture_by_pawn = re.match('([a-h])x([a-h])([1-8])', move_input)
            specific_capture_by_piece = re.match('([KQRBN])([a-h]|[1-8])x([a-h])([1-8])', move_input)

            pawn_move = re.match('([a-h])([1-8])', move_input)
            pawn_promotion = re.match('([a-h])([18])=([QRBN])', move_input)
            piece_move = re.match('([KQRBN])([a-h])([1-8])', move_input)
            specific_piece_move = re.match('([QRBN])([a-h]|[1-8])([a-h])([1-8])', move_input)

            if possible_moves:
                file = possible_moves.group(1)
                rank = possible_moves.group(2)

                piece = self.get_piece_on_square(board, file, rank)

                if piece:
                    self.display_moves(board, piece)
                else:
                    print('No piece on ' + file + rank)
            elif capture_by_piece:
                piece = capture_by_piece.group(1)
                file = capture_by_piece.group(2)
                rank = capture_by_piece.group(3)

                pieces = board.filter_pieces(self.piece_dict[piece], player)
                piece_moves = self.moves_for_pieces(pieces)

                piece_move = self.find_move_for_coordinate(piece_moves, file, rank, MoveTypes.CAPTURE)

                if not self.make_move(board, piece_move):
                    continue
                else:
                    return
            elif capture_by_pawn_promotion:
                pawn = capture_by_pawn_promotion.group(1)
                file = capture_by_pawn_promotion.group(2)
                rank = capture_by_pawn_promotion.group(3)
                piece = capture_by_pawn_promotion.group(4)

                pawns = self.filter_pieces(self.get_pieces_on_file(board, pawn), player, PieceType.PAWN)
                pawn_moves = self.moves_for_pieces(pawns)

                pawn_move = self.find_move_for_coordinate(pawn_moves, file, rank, MoveTypes.CAPTURE_PROMOTION)

                if not self.make_move(board, pawn_move):
                    continue
                else:
                    return
            elif capture_by_pawn:
                pawn = capture_by_pawn.group(1)
                file = capture_by_pawn.group(2)
                rank = capture_by_pawn.group(3)

                pawns = self.filter_pieces(self.get_pieces_on_file(board, pawn), player, PieceType.PAWN)
                pawn_moves = self.moves_for_pieces(pawns)

                pawn_move = self.find_move_for_coordinate(pawn_moves, file, rank, MoveTypes.CAPTURE)

                if not self.make_move(board, pawn_move):
                    continue
                else:
                    return
            elif pawn_move:
                file = pawn_move.group(1)
                rank = pawn_move.group(2)

                pawns = self.filter_pieces(self.get_pieces_on_file(board, file), player, PieceType.PAWN)
                pawn_moves = self.moves_for_pieces(pawns)

                pawn_move = self.find_move_for_coordinate(pawn_moves, file, rank, MoveTypes.MOVE)

                if not self.make_move(board, pawn_move):
                    continue
                else:
                    return
            elif pawn_promotion:
                file = pawn_promotion.group(1)
                rank = pawn_promotion.group(2)
                piece = pawn_promotion.group(3)

                pawns = self.filter_pieces(self.get_pieces_on_file(board, file), player, PieceType.PAWN)
                pawn_moves = self.moves_for_pieces(pawns)

                pawn_move = self.find_move_for_coordinate(pawn_moves, file, rank, MoveTypes.PROMOTION)

                self.set_promote_into(pawn_move, piece)

                if not self.make_move(board, pawn_move):
                    continue
                else:
                    return
            elif piece_move:
                piece = piece_move.group(1)
                file = piece_move.group(2)
                rank = piece_move.group(3)

                pieces = board.filter_pieces(self.piece_dict[piece], player)
                piece_moves = self.moves_for_pieces(pieces)

                piece_move = self.find_move_for_coordinate(piece_moves, file, rank, MoveTypes.MOVE)

                if not self.make_move(board, piece_move):
                    continue
                else:
                    return
            elif specific_capture_by_piece:
                piece = specific_piece_move.group(1)
                piece_id = specific_piece_move.group(2)
                file = specific_piece_move.group(3)
                rank = specific_piece_move.group(4)

                pieces = board.filter_pieces(self.piece_dict[piece], player)
                piece_moves = self.moves_for_pieces(pieces)

                piece_move = self.find_move_for_coordinate(piece_moves, file, rank, MoveTypes.CAPTURE, piece_id)

                if not self.make_move(board, piece_move):
                    continue
                else:
                    return
            elif specific_piece_move:
                piece = specific_piece_move.group(1)
                piece_id = specific_piece_move.group(2)
                file = specific_piece_move.group(3)
                rank = specific_piece_move.group(4)

                pieces = board.filter_pieces(self.piece_dict[piece], player)
                piece_moves = self.moves_for_pieces(pieces)

                piece_move = self.find_move_for_coordinate(piece_moves, file, rank, MoveTypes.MOVE, piece_id)

                if not self.make_move(board, piece_move):
                    continue
                else:
                    return
            elif move_input in ['O-O', 'O-O-O']:
                move = self.get_castle_move(board, move_input, player)

                if not self.make_move(board, move):
                    continue
                else:
                    return
            else:
                print('Invalid moves format. (see algebraic notation (chess))')
                continue

    def game_over(self, loser):
        if loser == PieceColor.BLACK:
            print('1-0')
        elif loser == PieceColor.WHITE:
            print('0-1')
        else:
            print('1/2-1/2')

    @staticmethod
    def make_move(board, move):
        if not move:
            print('Invalid move.')
            return False
        else:
            board.move(move)
            return True

    @staticmethod
    def get_pieces_on_file(board, file):
        files = dict(zip(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], [i for i in range(0, 8)]))
        pieces = []

        if file not in files:
            raise ValueError('get_pieces_on_rank: invalid rank')

        for pos, piece in board.pieces.items():
            if pos[0] == files[file]:
                pieces.append(piece)

        return pieces

    @staticmethod
    def get_pieces_on_rank(board, rank):
        rank = int(rank)
        pieces = []

        if not 1 <= rank <= 8:
            raise ValueError('get_pieces_on_file: invalid rank')

        for pos, piece in board.pieces.items():
            if pos[1] == rank - 1:
                pieces.append(piece)

        return pieces

    @staticmethod
    def get_piece_on_square(board, file, rank):
        rank = int(rank)
        files = dict(zip(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], [i for i in range(0, 8)]))

        if 1 <= rank <= 8 and file in files.keys():
            if (files[file], rank - 1) in board.pieces:
                return board.pieces[(files[file], rank - 1)]

        return None

    @staticmethod
    def filter_pieces(piece_list, color, type):
        return list(filter(lambda x: x.color == color and x.type == type, piece_list))

    @staticmethod
    def moves_for_pieces(pieces):
        result = []

        for p in pieces:
            result += p.moves()

        return result

    @staticmethod
    def find_move_for_coordinate(move_list, file, rank, move_type, piece_id=None):
        rank = int(rank)
        files = dict(zip(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], [i for i in range(0, 8)]))

        if 1 <= rank <= 8 and file in files.keys():
            for m in move_list:
                if piece_id:
                    try:
                        piece_id = int(piece_id)
                        if m.type == move_type and m.origin[1] == piece_id and \
                                m.destination[0] == files[file] and m.destination[1] == (rank - 1):
                            return m
                    except ValueError:
                        if piece_id in files.keys() and m.type == move_type and m.origin[0] == id and \
                                m.destination[1] == piece_id and m.destination[1] == (rank - 1):
                            return m
                if m.type == move_type and m.destination[0] == files[file] and m.destination[1] == (rank - 1):
                    return m

        return None

    @staticmethod
    def get_castle_move(board, castle_type, color):
        king = board.get_king(color)

        king_moves = king.moves()

        for m in king_moves:
            if castle_type == 'O-O' and m.is_king_side_castle():
                return m
            elif castle_type == 'O-O-O' and m.is_queen_side_castle():
                return m

        return None

    @staticmethod
    def display_moves(board, piece):
        moves = piece.moves()

        moves_str = []

        for m in moves:
            if m.is_move():
                if piece.is_pawn():
                    moves_str.append(board.position_to_algebraic(m.destination))
                else:
                    moves_str.append(m.piece.shorthand() + board.position_to_algebraic(m.destination))
            elif m.is_capture():
                if piece.is_pawn():
                    moves_str.append(board.position_to_algebraic(m.origin)[0] + 'x' +
                                     board.position_to_algebraic(m.destination))
                else:
                    moves_str.append(m.piece.shorthand() + 'x' + board.position_to_algebraic(m.destination))
            elif m.is_promotion():
                moves_str.append(board.position_to_algebraic(m.destination) + '=' + m.promted_piece.shorthand())
            elif m.is_capture_promotion():
                moves_str.append(board.position_to_algebraic(m.origin)[0] + 'x' +
                                 board.position_to_algebraic(m.destination) + '=' + m.promted_piece.shorthand())
            elif m.is_king_side_castle():
                moves_str.append('O-O')
            elif m.is_queen_side_castle():
                moves_str.append('O-O-O')
            elif m.is_attack():
                moves_str.append('A ' + board.position_to_algebraic(m.destination))
            else:
                moves_str.append('???')

        print('[' + ', '.join(moves_str) + ']')
