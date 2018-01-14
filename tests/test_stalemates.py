# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest
import pychess


class StalemateTests(unittest.TestCase):
    def test_stalemate_king_pawn_vs_king(self):
        board = pychess.board.SetupBoard('4k3/4P3/5K2/8/8/8/8/8 w KQkq -')

        board.algebraic_move(pychess.PieceColor.WHITE, 'Ke6')

        king = board.get_king(pychess.PieceColor.BLACK)

        stalemated = king.is_stalemated()
        checkmated = king.is_checkmated()

        self.assertTrue(stalemated and not checkmated)

    def test_stalemate_king_rook_pawn_vs_king(self):
        board = pychess.board.SetupBoard('k7/8/PK6/8/8/8/8/8 w KQkq -')

        board.algebraic_move(pychess.PieceColor.WHITE, 'a7')

        king = board.get_king(pychess.PieceColor.BLACK)

        stalemated = king.is_stalemated()
        checkmated = king.is_checkmated()

        self.assertTrue(stalemated and not checkmated)

    def test_stalemate_the_wrong_bishop(self):
        board = pychess.board.SetupBoard('7k/8/6KP/8/4B3/8/8/8 w KQkq -')

        board.algebraic_move(pychess.PieceColor.WHITE, 'Bd5')

        king = board.get_king(pychess.PieceColor.BLACK)

        stalemated = king.is_stalemated()
        checkmated = king.is_checkmated()

        self.assertTrue(stalemated and not checkmated)

    def test_stalemate_king_rook_pawn_vs_queen(self):
        board = pychess.board.SetupBoard('7K/7P/8/8/8/1k1q4/8/8 w KQkq -')

        board.algebraic_move(pychess.PieceColor.BLACK, 'Qg6')

        king = board.get_king(pychess.PieceColor.WHITE)

        stalemated = king.is_stalemated()
        checkmated = king.is_checkmated()

        self.assertTrue(stalemated and not checkmated)

    def test_stalemate_king_rook_vs_rook_pawn(self):
        board = pychess.board.SetupBoard('8/6R1/8/5b2/5k1K/8/8/5r2 w KQkq -')

        board.algebraic_move(pychess.PieceColor.WHITE, 'Rg4')
        board.algebraic_move(pychess.PieceColor.BLACK, 'Bxg4')

        king = board.get_king(pychess.PieceColor.WHITE)

        stalemated = king.is_stalemated()
        checkmated = king.is_checkmated()

        self.assertTrue(stalemated and not checkmated)

    def test_stalemate_the_wrong_bishop_variation(self):
        board = pychess.board.SetupBoard('8/8/8/8/2b5/1pP5/1P1k4/K7 w KQkq -')

        board.algebraic_move(pychess.PieceColor.BLACK, 'Kc1')

        king = board.get_king(pychess.PieceColor.WHITE)

        stalemated = king.is_stalemated()
        checkmated = king.is_checkmated()

        self.assertTrue(stalemated and not checkmated)

    def test_stalemate_trapped_king(self):
        board = pychess.board.SetupBoard('8/8/p7/k1pK4/1pP5/1P6/P7/8 w KQkq -')

        board.algebraic_move(pychess.PieceColor.WHITE, 'Kc6')

        king = board.get_king(pychess.PieceColor.BLACK)

        stalemated = king.is_stalemated()
        checkmated = king.is_checkmated()

        self.assertTrue(stalemated and not checkmated)

    def test_stalemate_trapped_king_variation(self):
        board = pychess.board.SetupBoard('8/6p1/5p2/5P1K/4k2P/8/8/8 w - -')

        board.algebraic_move(pychess.PieceColor.BLACK, 'Kxf5')

        king = board.get_king(pychess.PieceColor.WHITE)

        stalemated = king.is_stalemated()
        checkmated = king.is_checkmated()

        self.assertTrue(stalemated and not checkmated)


if __name__ == '__main__':
    unittest.main()
