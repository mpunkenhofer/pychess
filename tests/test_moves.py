# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest

from pychess.board import SetupBoard


class MoveTests(unittest.TestCase):
    def test_pawn_moves(self):
        board = SetupBoard('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
        self.assertEqual(board.fen(), 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')


if __name__ == '__main__':
    unittest.main()
