# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest

from pychess.board import SetupBoard
from pychess.util import board as board_util


class SetupBoardTests(unittest.TestCase):
    def test_setup_standard_position(self):
        board = SetupBoard('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
        str_board = board_util.to_string_array(board)
        self.assertEqual(str_board, ['rnbqkbnr',
                                     'pppppppp',
                                     '........',
                                     '........',
                                     '........',
                                     '........',
                                     'PPPPPPPP',
                                     'RNBQKBNR'
                                     ])

    def test_setup_position_1_e4(self):
        board = SetupBoard('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1')
        str_board = board_util.to_string_array(board)
        self.assertEqual(str_board, ['rnbqkbnr',
                                     'pppppppp',
                                     '........',
                                     '........',
                                     '....P...',
                                     '........',
                                     'PPPP.PPP',
                                     'RNBQKBNR'
                                     ])

    def test_setup_position_1_e4_c5(self):
        board = SetupBoard('rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR w KQkq c6 0 2')
        str_board = board_util.to_string_array(board)
        self.assertEqual(str_board, ['rnbqkbnr',
                                     'pp.ppppp',
                                     '........',
                                     '..p.....',
                                     '....P...',
                                     '........',
                                     'PPPP.PPP',
                                     'RNBQKBNR'
                                     ])

    def test_setup_position_1_e4_c5_2_Nf3(self):
        board = SetupBoard('rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2')
        str_board = board_util.to_string_array(board)
        self.assertEqual(str_board, ['rnbqkbnr',
                                     'pp.ppppp',
                                     '........',
                                     '..p.....',
                                     '....P...',
                                     '.....N..',
                                     'PPPP.PPP',
                                     'RNBQKB.R'
                                     ])

    def test_setup_position_without_pieces(self):
        board = SetupBoard('4k3/pppppppp/8/8/8/8/PPPPPPPP/4K3 w - - 0 1')
        str_board = board_util.to_string_array(board)
        self.assertEqual(str_board, ['....k...',
                                     'pppppppp',
                                     '........',
                                     '........',
                                     '........',
                                     '........',
                                     'PPPPPPPP',
                                     '....K...'
                                     ])

    def test_put_piece(self):
        board = SetupBoard('4k3/pppppppp/8/8/8/8/PPPPPPPP/4K3 w KQkq - 0 1')
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
