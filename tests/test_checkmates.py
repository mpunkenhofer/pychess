# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest
import pychess


class CheckmatesTests(unittest.TestCase):
    def test_checkmate_two_major_pieces(self):
        board = pychess.board.SetupBoard('5k2/1R6/8/8/8/8/R7/4K3 w KQkq -')

        board.algebraic_move(pychess.pychess.PieceColor.WHITE, 'Ra8#')

        checkmated_king = board.get_king(pychess.PieceColor.BLACK)

        self.assertTrue(checkmated_king.is_checkmated())

    def test_checkmate_two_pawns(self):
        board = pychess.board.SetupBoard('4k3/4P3/3PK3/8/8/8/8/8 w KQkq -')

        board.algebraic_move(pychess.pychess.PieceColor.WHITE, 'd7#')

        checkmated_king = board.get_king(pychess.PieceColor.BLACK)

        self.assertTrue(checkmated_king.is_checkmated())

    def test_checkmate_back_rank(self):
        board = pychess.board.SetupBoard('6k1/5ppp/6r1/8/8/7P/5PP1/1R4K1 w KQkq -')

        board.algebraic_move(pychess.pychess.PieceColor.WHITE, 'Rb8#')

        checkmated_king = board.get_king(pychess.PieceColor.BLACK)

        self.assertTrue(checkmated_king.is_checkmated())

    def test_checkmate_diagonal_protected_queen(self):
        board = pychess.board.SetupBoard('r4rk1/ppp2ppp/8/8/8/1P5P/PQ3PP1/B4RK1 w KQkq -')

        board.algebraic_move(pychess.PieceColor.WHITE, 'Qxg7#')

        checkmated_king = board.get_king(pychess.PieceColor.BLACK)

        self.assertTrue(checkmated_king.is_checkmated())

    def test_checkmate_smothered(self):
        board = pychess.board.SetupBoard('r5rk/ppp3pp/8/4N3/8/1P5P/P4PP1/5RK1 w KQkq -')

        board.algebraic_move(pychess.PieceColor.WHITE, 'Nf7#')

        checkmated_king = board.get_king(pychess.PieceColor.BLACK)

        self.assertTrue(checkmated_king.is_checkmated())

    def test_checkmate_B_and_K_fianchetto_mate(self):
        board = pychess.board.SetupBoard('r4rk1/ppp2p1p/5Bp1/8/6N1/1P5P/P4PP1/5RK1 w KQkq -')

        board.algebraic_move(pychess.PieceColor.WHITE, 'Nh6#')

        checkmated_king = board.get_king(pychess.PieceColor.BLACK)

        self.assertTrue(checkmated_king.is_checkmated())

    def test_checkmate_anastasias_mate(self):
        board = pychess.board.SetupBoard('r4r2/ppp1Nppk/8/3R4/8/1P5P/P4PP1/5RK1 w KQkq -')

        board.algebraic_move(pychess.PieceColor.WHITE, 'Rh5#')

        checkmated_king = board.get_king(pychess.PieceColor.BLACK)

        self.assertTrue(checkmated_king.is_checkmated())

    def test_checkmate_two_bishops_mate(self):
        board = pychess.board.SetupBoard('r6k/p1p4p/1p6/8/8/B6P/B4PP1/5RK1 w KQkq -')

        board.algebraic_move(pychess.PieceColor.WHITE, 'Bb2#')

        checkmated_king = board.get_king(pychess.PieceColor.BLACK)

        self.assertTrue(checkmated_king.is_checkmated())

    def test_checkmate_queen_and_bishop_mate(self):
        board = pychess.board.SetupBoard('r4rk1/p1p2ppp/1p5B/8/8/6QP/5PP1/5RK1 w KQkq -')

        board.algebraic_move(pychess.PieceColor.WHITE, 'Qxg7#')

        checkmated_king = board.get_king(pychess.PieceColor.BLACK)

        self.assertTrue(checkmated_king.is_checkmated())

    def test_checkmate_queen_and_bishop_fianchetto_mate(self):
        board = pychess.board.SetupBoard('r4rk1/p4p1p/1p3QpB/8/8/6P1/5P2/6KR w KQkq -')

        board.algebraic_move(pychess.PieceColor.WHITE, 'Qg7#')

        checkmated_king = board.get_king(pychess.PieceColor.BLACK)

        self.assertTrue(checkmated_king.is_checkmated())

    def test_checkmate_queen_and_rook_mate(self):
        board = pychess.board.SetupBoard('r4rk1/p4p2/1p6/2q5/7Q/6P1/5P2/6KR w KQkq -')

        board.algebraic_move(pychess.PieceColor.WHITE, 'Qh8#')

        checkmated_king = board.get_king(pychess.PieceColor.BLACK)

        self.assertTrue(checkmated_king.is_checkmated())

    def test_checkmate_king_and_queen(self):
        board = pychess.board.SetupBoard('7k/Q7/5K2/1p6/p7/8/8/8 w - -')

        board.algebraic_move(pychess.PieceColor.WHITE, 'Qg7#')

        checkmated_king = board.get_king(pychess.PieceColor.BLACK)

        self.assertTrue(checkmated_king.is_checkmated())

    def test_checkmate_rook_and_bishop(self):
        board = pychess.board.SetupBoard('1r5k/1p5p/p7/8/8/B7/8/5KR1 w - -')

        board.algebraic_move(pychess.PieceColor.WHITE, 'Bb2#')

        checkmated_king = board.get_king(pychess.PieceColor.BLACK)

        self.assertTrue(checkmated_king.is_checkmated())


if __name__ == '__main__':
    unittest.main()
