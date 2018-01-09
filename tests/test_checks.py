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

    def test_knight_check(self):
        board = SetupBoard('8/8/8/3k4/8/8/4N3/4K3 w - -')

        board.algebraic_move(PieceColor.WHITE, 'Nc3')

        king = board.get_king(PieceColor.BLACK)

        self.assertTrue(king.in_check() and board.algebraic_history()[-1] == 'Nc3+')

    def test_knight_move_uncovered_rook_check(self):
        board = SetupBoard('8/8/8/3k4/8/8/3N4/3RK3 w - -')

        board.algebraic_move(PieceColor.WHITE, 'Nf3')

        king = board.get_king(PieceColor.BLACK)

        self.assertTrue(king.in_check() and board.algebraic_history()[-1] == 'Nf3+')

    def test_bishop_check(self):
        board = SetupBoard('8/8/8/3k4/8/8/4B3/4K3 w - -')

        board.algebraic_move(PieceColor.WHITE, 'Bf3')

        king = board.get_king(PieceColor.BLACK)

        self.assertTrue(king.in_check() and board.algebraic_history()[-1] == 'Bf3+')

    def test_bishop_move_uncovered_queen_check(self):
        board = SetupBoard('8/8/8/3k4/8/8/3B4/3QK3 w - -')

        board.algebraic_move(PieceColor.WHITE, 'Be3')

        king = board.get_king(PieceColor.BLACK)

        self.assertTrue(king.in_check() and board.algebraic_history()[-1] == 'Be3+')

    def test_rook_check(self):
        board = SetupBoard('8/8/8/3k4/8/8/8/4KR2 w - -')

        board.algebraic_move(PieceColor.WHITE, 'Rf5')

        king = board.get_king(PieceColor.BLACK)

        self.assertTrue(king.in_check() and board.algebraic_history()[-1] == 'Rf5+')

    def test_rook_move_uncovered_bishop_check(self):
        board = SetupBoard('8/8/8/3k4/8/8/6R1/4K2B w - -')

        board.algebraic_move(PieceColor.WHITE, 'Rg8')

        king = board.get_king(PieceColor.BLACK)

        self.assertTrue(king.in_check() and board.algebraic_history()[-1] == 'Rg8+')

    def test_queen_check(self):
        board = SetupBoard('8/8/8/3k4/8/8/8/4KQ2 w - -')

        board.algebraic_move(PieceColor.WHITE, 'Qf3')

        king = board.get_king(PieceColor.BLACK)

        self.assertTrue(king.in_check() and board.algebraic_history()[-1] == 'Qf3+')

    def test_king_move_uncovered_rook_check(self):
        board = SetupBoard('8/8/8/3k4/8/8/3K4/3R4 w - -')

        board.algebraic_move(PieceColor.WHITE, 'Ke2')

        king = board.get_king(PieceColor.BLACK)

        self.assertTrue(king.in_check() and board.algebraic_history()[-1] == 'Ke2+')

    def test_knight_promotion_check(self):
        board = SetupBoard('8/5k1P/8/8/8/8/8/4K3 w - -')

        board.algebraic_move(PieceColor.WHITE, 'h8=N')

        king = board.get_king(PieceColor.BLACK)

        self.assertTrue(king.in_check() and board.algebraic_history()[-1] == 'h8=N+'
                        and len(board.get_knights(PieceColor.WHITE)) > 0)

    def test_knight_promotion_capture_check(self):
        board = SetupBoard('6r1/4k2P/8/8/8/8/8/4K3 w - -')

        board.algebraic_move(PieceColor.WHITE, 'hxg8=N')

        king = board.get_king(PieceColor.BLACK)

        self.assertTrue(king.in_check() and board.algebraic_history()[-1] == 'hxg8=N+'
                        and len(board.get_knights(PieceColor.WHITE)) > 0)

    def test_bishop_promotion_check(self):
        board = SetupBoard('8/7P/5k2/8/8/8/8/4K3 w - -')

        board.algebraic_move(PieceColor.WHITE, 'h8=B')

        king = board.get_king(PieceColor.BLACK)

        self.assertTrue(king.in_check() and board.algebraic_history()[-1] == 'h8=B+'
                        and len(board.get_bishops(PieceColor.WHITE)) > 0)

    def test_bishop_promotion_capture_check(self):
        board = SetupBoard('6q1/7P/4k3/8/8/8/8/4K3 w - -')

        board.algebraic_move(PieceColor.WHITE, 'hxg8=B')

        king = board.get_king(PieceColor.BLACK)

        self.assertTrue(king.in_check() and board.algebraic_history()[-1] == 'hxg8=B+'
                        and len(board.get_bishops(PieceColor.WHITE)) > 0)

    def test_rook_promotion_check(self):
        board = SetupBoard('4k3/7P/8/8/8/8/8/4K3 w - -')

        board.algebraic_move(PieceColor.WHITE, 'h8=R')

        king = board.get_king(PieceColor.BLACK)

        self.assertTrue(king.in_check() and board.algebraic_history()[-1] == 'h8=R+'
                        and len(board.get_rooks(PieceColor.WHITE)) > 0)

    def test_rook_promotion_capture_check(self):
        board = SetupBoard('4k1b1/7P/8/8/8/8/8/4K3 w - -')

        board.algebraic_move(PieceColor.WHITE, 'hxg8=R')

        king = board.get_king(PieceColor.BLACK)

        self.assertTrue(king.in_check() and board.algebraic_history()[-1] == 'hxg8=R+'
                        and len(board.get_rooks(PieceColor.WHITE)) > 0)

    def test_queen_promotion_check(self):
        board = SetupBoard('4k3/7P/8/8/8/8/8/4K3 w - -')

        board.algebraic_move(PieceColor.WHITE, 'h8=Q')

        king = board.get_king(PieceColor.BLACK)

        self.assertTrue(king.in_check() and board.algebraic_history()[-1] == 'h8=Q+'
                        and len(board.get_queens(PieceColor.WHITE)) > 0)

    def test_queen_promotion_capture_check(self):
        board = SetupBoard('4k1b1/7P/8/8/8/8/8/4K3 w - -')

        board.algebraic_move(PieceColor.WHITE, 'hxg8=Q')

        king = board.get_king(PieceColor.BLACK)

        self.assertTrue(king.in_check() and board.algebraic_history()[-1] == 'hxg8=Q+'
                        and len(board.get_queens(PieceColor.WHITE)) > 0)

    def test_block_falling_diagonal_bishop_check(self):
        board = SetupBoard('rnbqk1nr/ppp2ppp/4p3/3p4/1b1P4/1P3N2/P1P1PPPP/RNBQKB1R w KQkq - 1 4')

        pieces = board.get_all_pieces(PieceColor.WHITE)

        legal_moves = []

        for p in pieces:
            for m in p.moves():
                legal_moves.append(m.to_algebraic())

        self.assertCountEqual(legal_moves, ['c3', 'Nc3', 'Bd2', 'Qd2', 'Nbd2', 'Nfd2'])

    def test_block_rising_diagonal_queen_check(self):
        board = SetupBoard('2kr1bnr/pbpp1ppp/1pn5/8/7q/2N1B3/PPPQP1PP/3RKBNR w KQkq -')

        pieces = board.get_all_pieces(PieceColor.WHITE)

        legal_moves = []

        for p in pieces:
            for m in p.moves():
                legal_moves.append(m.to_algebraic())

        self.assertCountEqual(legal_moves, ['g3', 'Bf2'])

    def test_block_file_rook_check(self):
        board = SetupBoard('2k1rbnr/pbpp1ppp/1pn5/8/7q/1N6/PPPQ1BPP/3RKBNR w KQkq -')

        pieces = board.get_all_pieces(PieceColor.WHITE)

        legal_moves = []

        for p in pieces:
            for m in p.moves():
                legal_moves.append(m.to_algebraic())

        self.assertCountEqual(legal_moves, ['Qe2', 'Be2', 'Qe3', 'Ne2'])

    def test_block_file_queen_check(self):
        board = SetupBoard('2k1q1nr/pbpp1ppp/1pn5/8/7b/1N6/PPPQ1BPP/3RKBNR w KQkq -')

        pieces = board.get_all_pieces(PieceColor.WHITE)

        legal_moves = []

        for p in pieces:
            for m in p.moves():
                legal_moves.append(m.to_algebraic())

        self.assertCountEqual(legal_moves, ['Qe2', 'Be2', 'Qe3', 'Ne2'])

    def test_block_rank_queen_check(self):
        board = SetupBoard('4k3/7Q/B7/8/8/5N2/5PPP/q5K1 w - -')

        pieces = board.get_all_pieces(PieceColor.WHITE)

        legal_moves = []

        for p in pieces:
            for m in p.moves():
                legal_moves.append(m.to_algebraic())

        self.assertCountEqual(legal_moves, ['Qb1', 'Bf1', 'Ne1'])

    def test_block_rank_rook_check(self):
        board = SetupBoard('4k3/8/8/8/2nR4/1P2NQ2/P1P5/2K3r1 w - -')

        pieces = board.get_all_pieces(PieceColor.WHITE)

        legal_moves = []

        for p in pieces:
            for m in p.moves():
                legal_moves.append(m.to_algebraic())

        self.assertCountEqual(legal_moves, ['Rd1', 'Nd1', 'Nf1', 'Qd1', 'Qf1'])

    def test_force_capture_protected_queen(self):
        board = SetupBoard('3rk3/8/8/7B/2n5/1P6/P1P5/2Kq3R w - -')

        pieces = board.get_all_pieces(PieceColor.WHITE)

        legal_moves = []

        for p in pieces:
            for m in p.moves():
                legal_moves.append(m.to_algebraic())

        self.assertCountEqual(legal_moves, ['Rxd1', 'Bxd1'])

    def test_force_capture_queen(self):
        board = SetupBoard('4k3/8/8/7B/2n5/1P6/P1P5/2Kq3R w - -')

        pieces = board.get_all_pieces(PieceColor.WHITE)

        legal_moves = []

        for p in pieces:
            for m in p.moves():
                legal_moves.append(m.to_algebraic())

        self.assertCountEqual(legal_moves, ['Rxd1', 'Bxd1', 'Kxd1'])


if __name__ == '__main__':
    unittest.main()
