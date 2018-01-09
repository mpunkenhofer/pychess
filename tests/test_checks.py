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

    def test_block_bishop_check_with_bishop(self):
        board = SetupBoard('rnbqk1nr/ppp2ppp/4p3/3p4/1b1P4/1P3N2/P1P1PPPP/RNBQKB1R w KQkq - 1 4')

        pieces = board.get_all_pieces(PieceColor.WHITE)

        legal_moves = []

        for p in pieces:
            for m in p.moves():
                legal_moves.append(m.to_algebraic())

        self.assertCountEqual(legal_moves, ['c3', 'Nc3', 'Bd2', 'Qd2', 'Nbd2', 'Nfd2'])

    def test_force_capture_bishop(self):
        board = SetupBoard('rnbqk1nr/ppp2ppp/4p3/3p4/3P4/1P3N2/P1PbPPPP/RN1QKB1R w KQkq - 0 5')

        pieces = board.get_all_pieces(PieceColor.WHITE)

        legal_moves = []

        for p in pieces:
            for m in p.moves():
                legal_moves.append(m.to_algebraic())

        self.assertCountEqual(legal_moves, ['Qxd2', 'Nfxd2', 'Nbxd2', 'Kxd2'])


if __name__ == '__main__':
    unittest.main()
