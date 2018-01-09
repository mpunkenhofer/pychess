# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest

from pychess.board import SetupBoard
from pychess.pieces import PieceColor
from pychess.pieces import Piece


class PinTests(unittest.TestCase):
    def test_diagonally_pinned_w_pawns(self):
        board = SetupBoard('b3k3/7b/4n3/3P1P2/2n1K1n1/3P1P2/8/1b5b w - -')

        pinned_piece = board.get_pawns(PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertFalse(moves)

    def test_capture_diagonal_pinner_wP(self):
        board = SetupBoard('4k3/7b/2b5/3P1P2/4K3/8/8/8 w - -')

        pinned_piece = board.get_pawns(PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['dxc6'])

    def test_diagonally_pinned_b_pawns(self):
        board = SetupBoard('B3K3/7B/8/3p1p2/2N1k1N1/3p1p2/4N3/1B5B w - -')

        pinned_piece = board.get_pawns(PieceColor.BLACK)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertFalse(moves)

    def test_capture_diagonal_pinner_bP(self):
        board = SetupBoard('4k3/3p1p2/6B1/8/B7/8/8/4K3 w - -')

        pinned_piece = board.get_pawns(PieceColor.BLACK)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['fxg6'])

    def test_diagonally_not_pinned_w_piece(self):
        board = SetupBoard('4k3/8/8/b7/7b/2P5/3P1P2/4K3 w - -')

        pinned_piece = board.get_pawns(PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['c4', 'd3', 'd4'])

    def test_diagonally_not_pinned_b_piece(self):
        board = SetupBoard('4k3/3p1p2/2p5/7B/B7/8/8/4K3 w - -')

        pinned_piece = board.get_pawns(PieceColor.BLACK)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['d6', 'd5', 'c5'])

    def test_diagonally_pinned_w_rooks(self):
        board = SetupBoard('b3k3/7b/8/2bR1R2/4Kn2/3R1R2/3b4/1b5b w - -')

        pinned_piece = board.get_rooks(PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertFalse(moves)

    def test_diagonally_pinned_b_rooks(self):
        board = SetupBoard('B3K3/7B/8/2Br1r2/4kN2/3r1r2/3B4/1B5B w - -')

        pinned_piece = board.get_rooks(PieceColor.BLACK)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertFalse(moves)

    def test_diagonally_pinned_w_knights(self):
        board = SetupBoard('b3k3/7b/8/2bN1Nb1/4K3/3N1N2/3b4/1b5b w - -')

        pinned_piece = board.get_knights(PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertFalse(moves)

    def test_diagonally_pinned_b_knights(self):
        board = SetupBoard('B3K3/7B/8/2Bn1nB1/4k3/3n1n2/3B4/1B5B w - -')

        pinned_piece = board.get_knights(PieceColor.BLACK)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertFalse(moves)

    def test_same_rising_diagonal(self):
        same_r1 = Piece.same_rising_diagonal((0, 0), (7, 7))
        same_r2 = Piece.same_rising_diagonal((7, 7), (0, 0))

        self.assertTrue(same_r1 == same_r2 and same_r1)

    def test_same_falling_diagonal(self):
        same_r1 = Piece.same_falling_diagonal((0, 7), (7, 0))
        same_r2 = Piece.same_falling_diagonal((7, 0), (0, 7))

        self.assertTrue(same_r1 == same_r2 and same_r1)

    def test_diagonally_pinned_w_queens(self):
        board = SetupBoard('b3k3/7b/8/3Q1Q2/4KPP1/3QPQ2/4P1N1/1b5b w - -')

        pinned_piece = board.get_queens(PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['Qf2', 'Qf1', 'Qg3', 'Qh3', 'Qc2', 'Qc6', 'Qb7', 'Qg6', 'Qxa8', 'Qxb1', 'Qxh7'])

    def test_diagonally_pinned_b_queens(self):
        board = SetupBoard('B3K3/7B/8/3q1q2/4kpp1/3qpq2/4p1n1/1B5B w - -')

        pinned_piece = board.get_queens(PieceColor.BLACK)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['Qf2', 'Qf1', 'Qg3', 'Qh3', 'Qc2', 'Qc6', 'Qb7', 'Qg6', 'Qxa8', 'Qxb1', 'Qxh7'])

    def test_file_pinned_pawns_one_not_pinned(self):
        board = SetupBoard('2r1k3/8/8/2P5/1nKn4/2P5/8/2q5 w - -')

        pinned_piece = board.get_pawns(PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['c6'])

    def test_file_pinned_pawns_one_not_pinned_on_second_rank(self):
        board = SetupBoard('4k1q1/8/8/8/8/5b2/6P1/6K1 w - -')

        pinned_piece = board.get_pawns(PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['g3', 'g4'])

    def test_file_pinned_pawns_en_passant(self):
        board = SetupBoard('4r1k1/ppp2ppp/8/3pP3/8/8/8/4K3 w - d6')

        pinned_piece = board.get_pawns(PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['e6'])

    # TODO: file pinned bishops
    # TODO: file pinned knights
    # TODO: file pinned rooks
    # TODO: file pinned queens

    def test_rank_pinned_pawns_all_pinned(self):
        board = SetupBoard('44k3/8/8/8/6r1/r2PKP1q/8/8 w - -')

        pinned_piece = board.get_pawns(PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertFalse(moves)

    def test_rank_pinned_pawns_one_not_pinned(self):
        board = SetupBoard('4k3/8/8/8/6r1/r2PKP1b/8/8 w - -')

        pinned_piece = board.get_pawns(PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['f4', 'fxg4'])

    def test_rank_pinned_pawns_one_not_pinned_by_block(self):
        board = SetupBoard('4k3/8/8/8/6r1/r2PKPNq/8/8 w - -')

        pinned_piece = board.get_pawns(PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['f4', 'fxg4'])

    def test_rank_pinned_bishops_all_pinned(self):
        board = SetupBoard('4k3/8/8/8/6r1/r2BKB1q/8/8 w - -')

        pinned_piece = board.get_bishops(PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertFalse(moves)

    def test_rank_pinned_bishops_one_not_pinned(self):
        board = SetupBoard('4k3/8/8/8/4n1r1/r2BKB1n/8/8 w - -')

        pinned_piece = board.get_bishops(PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['Be2', 'Bd1', 'Bxg4', 'Bxe4', 'Bg2', 'Bh1'])

    def test_rank_pinned_bishops_one_not_pinned_by_block(self):
        board = SetupBoard('4k3/8/8/8/4n1r1/r2BKBNr/8/8 w - -')

        pinned_piece = board.get_bishops(PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['Be2', 'Bd1', 'Bxg4', 'Bxe4', 'Bg2', 'Bh1'])

    # TODO: rank pinned Knights
    # TODO: rank pinned rooks
    # TODO: rank pinned Queens


if __name__ == '__main__':
    unittest.main()
