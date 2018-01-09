# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest

from pychess.board import SetupBoard
from pychess.pieces import PieceColor


class CheckTests(unittest.TestCase):
    def test_pawn_check(self):
        board = SetupBoard('8/8/8/3k4/8/8/4P3/4K3 w - -')

        board.algebraic_move(PieceColor.WHITE, 'e4')

        king = board.get_king(PieceColor.BLACK)

        self.assertTrue(king.in_check() and board.algebraic_history()[-1] == 'e4+')

    def test_pawn_move_uncovered_bishop_check(self):
        board = SetupBoard('8/8/8/8/2k5/8/4P3/4KB2 w - -')

        board.algebraic_move(PieceColor.WHITE, 'e4')

        king = board.get_king(PieceColor.BLACK)

        self.assertTrue(king.in_check() and board.algebraic_history()[-1] == 'e4+')


if __name__ == '__main__':
    unittest.main()
