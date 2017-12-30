# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

from interface import ChessUserInterface
import re
import math


class ChessConsoleUserInterface(ChessUserInterface):
    _unicode_light_pieces = {'K': u'\u2654',
                             'Q': u'\u2655',
                             'R': u'\u2656',
                             'B': u'\u2657',
                             'N': u'\u2658',
                             'P': u'\u2659'}
    _unicode_dark_pieces = {'K': u'\u265A',
                            'Q': u'\u265B',
                            'R': u'\u265C',
                            'B': u'\u265D',
                            'N': u'\u265E',
                            'P': u'\u265F'}

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

            capture_by_piece = re.match('([KQRBN])x([a-h])([1-8])[+#]?', move_input)
            capture_by_pawn = re.match('([a-h])x([a-h])([1-8])[+#]?', move_input)

            pawn_move = re.match('([a-h])([1-8])[+#]?', move_input)
            piece_move = re.match('([KQRBN])([a-h])([1-8])[+#]?', move_input)
            specific_piece_move = re.match('([QRBN])([a-h])([a-h])([1-8])[+#]?', move_input)

            if capture_by_piece:
                piece = capture_by_piece.group(1)
                file = capture_by_piece.group(2)
                rank = capture_by_piece.group(3)
            elif capture_by_pawn:
                pawn = capture_by_pawn.group(1)
                file = capture_by_pawn.group(2)
                rank = capture_by_pawn.group(3)
            elif pawn_move:
                file = pawn_move.group(1)
                rank = pawn_move.group(2)

                pawns = self.filter_pieces(self.get_pieces_on_file(game, file), game.current_player, 'Pawn')
                pawn_moves = self.moves_for_pieces(pawns)

                pawn_move = self.find_move_for_coordinate(pawn_moves, file, rank, 'Move')

                if not pawn_move:
                    print('Invalid move.')
                    continue

                return pawn_move.piece, pawn_move.destination

            elif piece_move:
                piece = piece_move.group(1)
                file = piece_move.group(2)
                rank = piece_move.group(3)
            elif specific_piece_move:
                piece = specific_piece_move.group(1)
                piece_id = specific_piece_move.group(2)
                file = specific_piece_move.group(3)
                rank = specific_piece_move.group(4)
            elif move_input == 'O-O':
                print('King side castle')
            elif move_input == 'O-O-O':
                print('Queen side castle')
            else:
                print('Invalid move format. (see algebraic notation (chess))')
                continue

    def promote(self, game):
        new_piece = None

        while new_piece not in ['Q', 'R', 'B', 'N']:
            new_piece = input('Pawn promotion - choose a new piece: ')

        piece_dict = {'Q': 'Queen', 'R': 'Rook', 'B': 'Bishop', 'N': 'Knight'}

        return piece_dict[new_piece]

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
    def filter_pieces(piece_list, color, name):
        return list(filter(lambda x: x.color == color and x.name == name, piece_list))

    @staticmethod
    def moves_for_pieces(pieces):
        result = []

        for p in pieces:
            result += p.moves()

        return result

    @staticmethod
    def find_move_for_coordinate(move_list, file, rank, move_type):
        rank = int(rank)
        files = dict(zip(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], [i for i in range(0, 8)]))

        if 1 <= rank <= 8 and file in files.keys():
            for m in move_list:
                if m.type == move_type and m.destination[0] == files[file] and m.destination[1] == (rank - 1):
                    return m

        return None
