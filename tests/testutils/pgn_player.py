# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import re


class PGNPlayer:
    def __init__(self, file=None):
        self._moves = []
        self._result = self._remainder = self._next_game = None
        self._cursor = 0

        if file:
            self.read_pgn_file(file)

    def read_pgn(self, content):
        read_one = False

        for i, line in enumerate(content):
            line = line.strip()
            if line and not line.startswith('['):
                line = re.sub('(\d+\.\s?)|({[^}]*})', '', line)
                raw_moves = line.split(' ')

                for m in raw_moves:
                    if read_one:
                        break

                    if m:
                        if m == '1-0':
                            self._result = 1
                            read_one = True
                        elif m == '0-1':
                            self._result = -1
                            read_one = True
                        elif m == '1/2-1/2':
                            self._result = 0
                            read_one = True
                        else:
                            self._moves.append(m)

                if read_one:
                    self.reset()
                    if content[i + 1:]:
                        next_game = PGNPlayer()
                        next_game.read_pgn(content[i+1:])
                        if next_game.get_moves():
                            self._next_game = next_game
                    return

    def read_pgn_file(self, file):
        with open(file) as f:
            content = f.readlines()

        self.read_pgn(content)

    def next_game(self):
        return self._next_game

    def get_moves(self):
        return self._moves

    def next_move(self):
        if self._cursor < len(self._moves):
            i = self._cursor
            self._cursor += 1
            return self._moves[i]
        else:
            return None

    def reset(self):
        self._cursor = 0

    def draw(self):
        if self._result is None:
            raise ValueError('PGNPlayer: Unknown game result')
        else:
            return self._result == 0

    def white_win(self):
        if self._result is None:
            raise ValueError('PGNPlayer: Unknown game result')
        else:
            return self._result == 1

    def black_win(self):
        if self._result is None:
            raise ValueError('PGNPlayer: Unknown game result')
        else:
            return self._result == -1
