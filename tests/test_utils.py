# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest
import pychess.util.board
import pychess.util.move
import pychess.util.position
import pychess.util.rules

from pychess.board import SetupBoard
from pychess.board import StandardBoard
from pychess.pieces import PieceColor


class UtilTests(unittest.TestCase):
    def test_board_to_string_array(self):
        board = StandardBoard()
        str_board = pychess.util.board.to_string_array(board)
        self.assertEqual(str_board, ['rnbqkbnr',
                                     'pppppppp',
                                     '........',
                                     '........',
                                     '........',
                                     '........',
                                     'PPPPPPPP',
                                     'RNBQKBNR'
                                     ])

    def test_move_from_algebraic(self):
        board = StandardBoard()

        move = pychess.util.move.from_algebraic(board, PieceColor.WHITE, 'e4')
        board.move(move)

        self.assertEqual(board.fen(), 'rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1')

    def test_to_algebraic_None_board(self):
        p = pychess.util.position.to_algebraic((0, 0))
        self.assertEqual(p, 'a1')

    def test_to_algebraic_board(self):
        board = StandardBoard()
        p = pychess.util.position.to_algebraic((7, 7), board)
        self.assertEqual(p, 'h8')

    def test_to_algebraic_None_pos(self):
        with self.assertRaises(ValueError):
            p = pychess.util.position.to_algebraic(None)

    def test_from_algebraic_None_board(self):
        p = pychess.util.position.from_algebraic('a1')
        self.assertEqual(p, (0, 0))

    def test_from_algebraic_board(self):
        board = StandardBoard()
        p = pychess.util.position.from_algebraic('h8', board)
        self.assertEqual(p, (7, 7))

    def test_from_algebraic_None_pos(self):
        with self.assertRaises(ValueError):
            p = pychess.util.position.from_algebraic(None)

    def test_from_algebraic_invalid_pos(self):
        with self.assertRaises(ValueError):
            p = pychess.util.position.from_algebraic('Z3')

    def test_insufficient_material_starting_pos(self):
        board = StandardBoard()
        self.assertFalse(pychess.util.rules.insufficient_material(board))

    def test_insufficient_material_b_b_vs_k(self):
        board = SetupBoard('4k3/4b3/8/8/8/8/8/4K3 w KQkq -')
        self.assertTrue(pychess.util.rules.insufficient_material(board))

    def test_insufficient_material_b_n_vs_k(self):
        board = SetupBoard('4k3/4b3/8/8/8/8/8/4K3 w KQkq -')
        self.assertTrue(pychess.util.rules.insufficient_material(board))

    def test_insufficient_material_w_b_vs_k(self):
        board = SetupBoard('4k3/8/8/8/8/8/4B3/4K3 w KQkq -')
        self.assertTrue(pychess.util.rules.insufficient_material(board))

    def test_insufficient_material_w_n_vs_k(self):
        board = SetupBoard('4k3/8/8/8/8/8/4N3/4K3 w KQkq -')
        self.assertTrue(pychess.util.rules.insufficient_material(board))

    def test_insufficient_material_w_n_b_vs_k(self):
        board = SetupBoard('4k3/8/8/8/8/5N2/4B3/4K3 w KQkq -')
        self.assertFalse(pychess.util.rules.insufficient_material(board))

    def test_insufficient_material_b_n_b_vs_k(self):
        board = SetupBoard('4k3/3nb3/8/8/8/8/8/4K3 w KQkq -')
        self.assertFalse(pychess.util.rules.insufficient_material(board))

    def test_insufficient_material_b_n_vs_w_b(self):
        board = SetupBoard('4k3/3b4/8/8/8/8/4N3/4K3 w KQkq -')
        self.assertFalse(pychess.util.rules.insufficient_material(board))


if __name__ == '__main__':
    unittest.main()
