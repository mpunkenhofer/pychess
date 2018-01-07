# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import re
import math
import pychess.pieces

from pychess.util import position

from examples.interface import ChessUserInterface


class ChessConsoleUserInterface(ChessUserInterface):
    def __init__(self, board):
        ChessUserInterface.__init__(self, board)

    def draw(self):
        self.draw_board(self.board)

    @staticmethod
    def draw_board(board):
        file_diff = board.get_top_right()[0] - board.get_bottom_left()[0]
        rank_diff = board.get_top_right()[1] - board.get_bottom_left()[0]

        for y in reversed(range(0, rank_diff + 1)):
            for x in range(0, file_diff + 1):
                if board.piece_on((x, y)):
                    piece = board.get_piece((x, y))
                    if piece.is_white():
                        print(piece.shorthand(), end='')
                    else:
                        print(piece.shorthand().lower(), end='')
                else:
                    print('.', end='')
            print()

    def move(self, player):
        move_input = self.get_input()

        while not self.valid_input(move_input):
            print('Invalid move format. (see algebraic notation for chess)')
            move_input = self.get_input()

        if self.is_command(move_input):
            self.do_command(move_input)
            return self.move(player)

        move = self.find_move(self.board.get_all_pieces(player), move_input)

        if not move:
            print('Invalid move.')
            return self.move(player)
        else:
            return self.board.move(move)

    def game_over(self, loser):
        self.print_history()
        if loser == pychess.pieces.PieceColor.BLACK:
            print('1-0')
        elif loser == pychess.pieces.PieceColor.WHITE:
            print('0-1')
        else:
            print('1/2-1/2')

    def print_history(self):
        history = self.board.algebraic_history()
        longest = max(map(lambda x: len(x), history)) + 1

        print()

        for i, m in enumerate(history):
            if i % 2 == 0:
                print(str(int(i / 2 + 1)) + '. ', end='')
                print('{move: <{width}}'.format(move=m, width=longest),  end='')
            else:
                print(m, end='')
                print()

        print('\n')

    def get_input(self):
        return input(str(int(math.ceil((len(self.board.move_history()) + 1) / 2))) + ': ')

    def valid_input(self, move_input):
        move_input = re.sub('[+#]', '', move_input)

        patterns = ['p ([a-h])([1-8])',
                    '([KQRBN])x([a-h])([1-8])',
                    '([a-h])x([a-h])([1-8])=([QRBN])',
                    '([a-h])x([a-h])([1-8])',
                    '([KQRBN])([a-h]|[1-8])x([a-h])([1-8])',
                    '([a-h])([1-8])',
                    '([a-h])([18])=([QRBN])',
                    '([KQRBN])([a-h])([1-8])',
                    '([QRBN])([a-h]|[1-8])([a-h])([1-8])',
                    'O-O', 'O-O-O', 'fen', 'history']

        for p in patterns:
            if re.match(p, move_input):
                return True

        return False

    def is_command(self, move_input):
        return move_input[0] == 'p' or move_input == 'fen' or move_input == 'history'

    def do_command(self, cmd):
        if cmd[0] == 'p':
            _, value = cmd.split(' ')
            self.display_moves(value)
        elif cmd == 'history':
            self.print_history()
        elif cmd == 'fen':
            print(self.board.fen())

    def display_moves(self, piece):
        piece = self.find_piece(piece)

        if not piece:
            print('No piece on: ' + piece)
        else:
            moves = [m.to_algebraic() for m in piece.moves()]
            print('[' + ', '.join(moves) + ']')

    def find_piece(self, piece):
        for p in self.board.get_all_pieces():
            if position.to_algebraic(p.position, self.board) == piece:
                return p

        return None

    def find_move(self, pieces, move_input):
        move_dict = self.build_move_dict(pieces)

        return move_dict[move_input] if move_input in move_dict else None

    def build_move_dict(self, pieces):
        move_dict = {}

        for p in pieces:
            for move in p.moves():
                k = move.to_algebraic()
                if not k:
                    continue

                if k not in move_dict:
                    move_dict[k] = move

        return move_dict
