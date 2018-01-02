# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

from interface import ChessUserInterface
import re
import math


class ChessConsoleUserInterface(ChessUserInterface):
    _piece_dict = {'Q': 'Queen', 'R': 'Rook', 'B': 'Bishop', 'N': 'Knight', 'K': 'King'}

    def __init__(self):
        ChessUserInterface.__init__(self)

    def draw(self, game):
        for y in reversed(range(0, 8)):
            for x in range(0, 8):
                if (x, y) in game.board.pieces:
                    if game.board.pieces[(x, y)].light():
                        print(game.board.pieces[(x, y)].letter, end='')
                    else:
                        print(game.board.pieces[(x, y)].letter.lower(), end='')
                else:
                    print('.', end='')

            print()

    def move(self, game):
        while True:
            move_input = input(str(int(math.ceil((len(game.board.history()) + 1) / 2))) + ': ')

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

                piece = self.get_piece_on_square(game, file, rank)

                if piece:
                    print(piece.moves())
                else:
                    print('No piece on ' + file + rank)
            elif capture_by_piece:
                piece = capture_by_piece.group(1)
                file = capture_by_piece.group(2)
                rank = capture_by_piece.group(3)

                pieces = game.board.filter_pieces(self._piece_dict[piece], game.current_player)
                piece_moves = self.moves_for_pieces(pieces)

                piece_move = self.find_move_for_coordinate(piece_moves, file, rank, 'Capture')

                if not self.make_move(game, piece_move):
                    continue
                else:
                    return
            elif capture_by_pawn_promotion:
                pawn = capture_by_pawn_promotion.group(1)
                file = capture_by_pawn_promotion.group(2)
                rank = capture_by_pawn_promotion.group(3)
                piece = capture_by_pawn_promotion.group(4)

                pawns = self.filter_pieces(self.get_pieces_on_file(game, pawn), game.current_player, 'Pawn')
                pawn_moves = self.moves_for_pieces(pawns)

                pawn_move = self.find_move_for_coordinate(pawn_moves, file, rank, 'Capture Promotion')

                self.set_promote_into(pawn_move, piece)

                if not self.make_move(game, pawn_move):
                    continue
                else:
                    return
            elif capture_by_pawn:
                pawn = capture_by_pawn.group(1)
                file = capture_by_pawn.group(2)
                rank = capture_by_pawn.group(3)

                pawns = self.filter_pieces(self.get_pieces_on_file(game, pawn), game.current_player, 'Pawn')
                pawn_moves = self.moves_for_pieces(pawns)

                pawn_move = self.find_move_for_coordinate(pawn_moves, file, rank, 'Capture')

                if not self.make_move(game, pawn_move):
                    continue
                else:
                    return
            elif pawn_move:
                file = pawn_move.group(1)
                rank = pawn_move.group(2)

                pawns = self.filter_pieces(self.get_pieces_on_file(game, file), game.current_player, 'Pawn')
                pawn_moves = self.moves_for_pieces(pawns)

                pawn_move = self.find_move_for_coordinate(pawn_moves, file, rank, 'Move')

                if not self.make_move(game, pawn_move):
                    continue
                else:
                    return
            elif pawn_promotion:
                file = pawn_promotion.group(1)
                rank = pawn_promotion.group(2)
                piece = pawn_promotion.group(3)

                pawns = self.filter_pieces(self.get_pieces_on_file(game, file), game.current_player, 'Pawn')
                pawn_moves = self.moves_for_pieces(pawns)

                pawn_move = self.find_move_for_coordinate(pawn_moves, file, rank, 'Promotion')

                self.set_promote_into(pawn_move, piece)

                if not self.make_move(game, pawn_move):
                    continue
                else:
                    return
            elif piece_move:
                piece = piece_move.group(1)
                file = piece_move.group(2)
                rank = piece_move.group(3)

                pieces = game.board.filter_pieces(self._piece_dict[piece], game.current_player)
                piece_moves = self.moves_for_pieces(pieces)

                piece_move = self.find_move_for_coordinate(piece_moves, file, rank, 'Move')

                if not self.make_move(game, piece_move):
                    continue
                else:
                    return
            elif specific_capture_by_piece:
                piece = specific_piece_move.group(1)
                piece_id = specific_piece_move.group(2)
                file = specific_piece_move.group(3)
                rank = specific_piece_move.group(4)

                pieces = game.board.filter_pieces(self._piece_dict[piece], game.current_player)
                piece_moves = self.moves_for_pieces(pieces)

                piece_move = self.find_move_for_coordinate(piece_moves, file, rank, 'Capture', piece_id)

                if not self.make_move(game, piece_move):
                    continue
                else:
                    return
            elif specific_piece_move:
                piece = specific_piece_move.group(1)
                piece_id = specific_piece_move.group(2)
                file = specific_piece_move.group(3)
                rank = specific_piece_move.group(4)

                pieces = game.board.filter_pieces(self._piece_dict[piece], game.current_player)
                piece_moves = self.moves_for_pieces(pieces)

                piece_move = self.find_move_for_coordinate(piece_moves, file, rank, 'Move', piece_id)

                if not self.make_move(game, piece_move):
                    continue
                else:
                    return
            elif move_input == 'O-O':
                print('King side castle')
            elif move_input == 'O-O-O':
                print('Queen side castle')
            else:
                print('Invalid move format. (see algebraic notation (chess))')
                continue

    def game_over(self, winner):
        if winner == 'light':
            print('1-0')
        elif winner == 'dark':
            print('0-1')
        else:
            print('1/2-1/2')

    def set_promote_into(self, move, letter):
        if move.type not in ['Promotion', 'Capture Promotion']:
            raise ValueError('set_promote_into: can only be set for promotion type moves')

        move.promoted_piece_name = self._piece_dict[letter]

    @staticmethod
    def make_move(game, move):
        if not move:
            print('Invalid move.')
            return False
        else:
            game.board.move(move)
            return True

    @staticmethod
    def get_pieces_on_file(game, file):
        files = dict(zip(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], [i for i in range(0, 8)]))
        pieces = []

        if file not in files:
            raise ValueError('get_pieces_on_rank: invalid rank')

        for pos, piece in game.board.pieces.items():
            if pos[0] == files[file]:
                pieces.append(piece)

        return pieces

    @staticmethod
    def get_pieces_on_rank(game, rank):
        rank = int(rank)
        pieces = []

        if not 1 <= rank <= 8:
            raise ValueError('get_pieces_on_file: invalid rank')

        for pos, piece in game.board.pieces.items():
            if pos[1] == rank - 1:
                pieces.append(piece)

        return pieces

    @staticmethod
    def get_piece_on_square(game, file, rank):
        rank = int(rank)
        files = dict(zip(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], [i for i in range(0, 8)]))

        if 1 <= rank <= 8 and file in files.keys():
            if (files[file], rank - 1) in game.board.pieces:
                return game.board.pieces[(files[file], rank - 1)]

        return None

    @staticmethod
    def filter_pieces(piece_list, color, name):
        return list(filter(lambda x: x.color == color and x.type == name, piece_list))

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
                if id:
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
