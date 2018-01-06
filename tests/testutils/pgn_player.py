# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import re


class PGNPlayer:
    def __init__(self, file):
        self.moves = self.result = self.remainder = None
        self.cursor = 0
        self.read_pgn(file)

    def read_pgn(self, file):
        with open(file) as f:
            content = f.readlines()

        read_one = False

        for i, line in enumerate(content):
            if not line.startswith('['):
                line = re.sub('\d+\.\s?', '', line)
                raw_moves = line.split(' ')

                for m in raw_moves:
                    if read_one:
                        break

                    if not m.startswith('{'):
                        if m == '1-0':
                            self.result = 1
                            read_one = True
                        elif m == '0-1':
                            self.result = -1
                            read_one = True
                        elif m == '1/2-1/2':
                            self.result = 0
                            read_one = True
                        else:
                            self.moves.append(m)

                if read_one:
                    self.reset()
                    self.remainder = content[i:]
                    return

    def remainder(self):
        return self.remainder

    def get_moves(self):
        return self.moves

    def next_move(self):
        if self.cursor < len(self.moves):
            i = self.cursor
            self.cursor += 1
            return self.moves[i]
        else:
            return None

    def reset(self):
        self.cursor = 0

    def draw(self):
        if self.result is None:
            raise ValueError('PGNPlayer: Unknown game result')
        else:
            return self.result == 0

    def white_win(self):
        if self.result is None:
            raise ValueError('PGNPlayer: Unknown game result')
        else:
            return self.result == 1

    def black_win(self):
        if self.result is None:
            raise ValueError('PGNPlayer: Unknown game result')
        else:
            return self.result == -1
