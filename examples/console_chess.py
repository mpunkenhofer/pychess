# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import re
import sys
import math

from pychess.variant import Standard
from pychess.pieces import PieceColor
from pychess.util import position
from pychess.util.board import to_string_array


class ConsoleInterfaceChess:
    def __init__(self, variant, player=PieceColor.WHITE):
        self.variant = variant
        self.current_player = player
        self.print_board()

    def move(self):
        move_input = self.get_input()

        while not self.valid_input(move_input):
            print('Invalid move format. (see algebraic notation for chess)')
            move_input = self.get_input()

        if self.is_command(move_input):
            self.do_command(move_input)
        else:
            try:
                self.variant.board.algebraic_move(self.current_player, move_input)
                self.print_board()
            except RuntimeError:
                print('Invalid move.')

            self.current_player = PieceColor.BLACK if self.current_player == PieceColor.WHITE else PieceColor.WHITE

    def game_over(self):
        if self.variant.is_draw():
            print('1/2-1/2')
            self.print_history()
            return True
        elif self.variant.is_checkmated(self.current_player):
            print('1-0' if self.current_player == PieceColor.BLACK else '0-1')
            self.print_history()
            return True
        else:
            return False

    def print_history(self):
        history = self.variant.board.algebraic_history()
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
        return input(str(int(math.ceil((len(self.variant.board.move_history()) + 1) / 2))) + ': ')

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
            print(self.variant.board.fen())

    def display_moves(self, square):
        piece = self.find_piece(square)

        if not piece:
            print('No piece on: ' + square)
        else:
            moves = [m.to_algebraic() for m in piece.moves()]
            print('[' + ', '.join(moves) + ']')

    def find_piece(self, square):
        for p in self.variant.board.get_all_pieces(PieceColor.WHITE):
            if position.to_algebraic(p.position, self.variant.board) == square:
                return p

        for p in self.variant.board.get_all_pieces(PieceColor.BLACK):
            if position.to_algebraic(p.position, self.variant.board) == square:
                return p

        return None

    def print_board(self):
        for l in to_string_array(self.variant.board):
            print(l)


def main():
    chess_game = ConsoleInterfaceChess(Standard())

    while not chess_game.game_over():
        chess_game.move()


if __name__ == "__main__":
    sys.exit(main())
