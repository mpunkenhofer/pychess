# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest

from pychess.board import StandardBoard


class FENTests(unittest.TestCase):
    def test_fen_chess_starting_postion(self):
        board = StandardBoard()
        self.assertEqual(board.fen(), 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')


if __name__ == '__main__':
    unittest.main()
