# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest
import pychess


class PinTests(unittest.TestCase):
    def test_diagonally_pinned_w_pawns(self):
        board = pychess.board.SetupBoard('b3k3/7b/4n3/3P1P2/2n1K1n1/3P1P2/8/1b5b w - -')

        pinned_piece = board.get_pawns(pychess.PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertFalse(moves)

    def test_capture_diagonal_pinner_wP(self):
        board = pychess.board.SetupBoard('4k3/7b/2b5/3P1P2/4K3/8/8/8 w - -')

        pinned_piece = board.get_pawns(pychess.PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['dxc6'])

    def test_diagonally_pinned_b_pawns(self):
        board = pychess.board.SetupBoard('B3K3/7B/8/3p1p2/2N1k1N1/3p1p2/4N3/1B5B w - -')

        pinned_piece = board.get_pawns(pychess.PieceColor.BLACK)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertFalse(moves)

    def test_capture_diagonal_pinner_bP(self):
        board = pychess.board.SetupBoard('4k3/3p1p2/6B1/8/B7/8/8/4K3 w - -')

        pinned_piece = board.get_pawns(pychess.PieceColor.BLACK)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['fxg6'])

    def test_diagonally_not_pinned_w_piece(self):
        board = pychess.board.SetupBoard('4k3/8/8/b7/7b/2P5/3P1P2/4K3 w - -')

        pinned_piece = board.get_pawns(pychess.PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['c4', 'd3', 'd4'])

    def test_diagonally_not_pinned_b_piece(self):
        board = pychess.board.SetupBoard('4k3/3p1p2/2p5/7B/B7/8/8/4K3 w - -')

        pinned_piece = board.get_pawns(pychess.PieceColor.BLACK)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['d6', 'd5', 'c5'])

    def test_diagonally_pinned_w_rooks(self):
        board = pychess.board.SetupBoard('b3k3/7b/8/2bR1R2/4Kn2/3R1R2/3b4/1b5b w - -')

        pinned_piece = board.get_rooks(pychess.PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertFalse(moves)

    def test_diagonally_pinned_b_rooks(self):
        board = pychess.board.SetupBoard('B3K3/7B/8/2Br1r2/4kN2/3r1r2/3B4/1B5B w - -')

        pinned_piece = board.get_rooks(pychess.PieceColor.BLACK)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertFalse(moves)

    def test_diagonally_pinned_w_knights(self):
        board = pychess.board.SetupBoard('b3k3/7b/8/2bN1Nb1/4K3/3N1N2/3b4/1b5b w - -')

        pinned_piece = board.get_knights(pychess.PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertFalse(moves)

    def test_diagonally_pinned_b_knights(self):
        board = pychess.board.SetupBoard('B3K3/7B/8/2Bn1nB1/4k3/3n1n2/3B4/1B5B w - -')

        pinned_piece = board.get_knights(pychess.PieceColor.BLACK)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertFalse(moves)

    def test_same_rising_diagonal(self):
        same_r1 = pychess.pieces.Piece.same_rising_diagonal((0, 0), (7, 7))
        same_r2 = pychess.pieces.Piece.same_rising_diagonal((7, 7), (0, 0))

        self.assertTrue(same_r1 == same_r2 and same_r1)

    def test_same_falling_diagonal(self):
        same_r1 = pychess.pieces.Piece.same_falling_diagonal((0, 7), (7, 0))
        same_r2 = pychess.pieces.Piece.same_falling_diagonal((7, 0), (0, 7))

        self.assertTrue(same_r1 == same_r2 and same_r1)

    def test_diagonally_pinned_w_queens(self):
        board = pychess.board.SetupBoard('b3k3/7b/8/3Q1Q2/4KPP1/3QPQ2/4P1N1/1b5b w - -')

        pinned_piece = board.get_queens(pychess.PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['Qf2', 'Qf1', 'Qg3', 'Qh3', 'Qc2', 'Qc6', 'Qb7', 'Qg6', 'Qxa8', 'Qxb1', 'Qxh7'])

    def test_diagonally_pinned_b_queens(self):
        board = pychess.board.SetupBoard('B3K3/7B/8/3q1q2/4kpp1/3qpq2/4p1n1/1B5B w - -')

        pinned_piece = board.get_queens(pychess.PieceColor.BLACK)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['Qf2', 'Qf1', 'Qg3', 'Qh3', 'Qc2', 'Qc6', 'Qb7', 'Qg6', 'Qxa8', 'Qxb1', 'Qxh7'])

    def test_file_pinned_pawns_one_not_pinned(self):
        board = pychess.board.SetupBoard('2r1k3/8/8/2P5/1nKn4/2P5/8/2q5 w - -')

        pinned_piece = board.get_pawns(pychess.PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['c6'])

    def test_file_pinned_pawns_one_not_pinned_on_second_rank(self):
        board = pychess.board.SetupBoard('4k1q1/8/8/8/8/5b2/6P1/6K1 w - -')

        pinned_piece = board.get_pawns(pychess.PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['g3', 'g4'])

    def test_file_pinned_pawns_en_passant(self):
        board = pychess.board.SetupBoard('4r1k1/ppp2ppp/8/3pP3/8/8/8/4K3 w - d6')

        pinned_piece = board.get_pawns(pychess.PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['e6'])

    def test_file_pinned_bishops_all_pinned(self):
        board = pychess.board.SetupBoard('3kq3/8/5p2/4B3/4K3/4B3/3r4/4r3 w - -')

        pinned_piece = board.get_bishops(pychess.PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertFalse(moves)

    def test_file_pinned_bishops_one_not_pinned(self):
        board = pychess.board.SetupBoard('3kq3/8/5p2/4B3/3nKn2/4B3/8/4n3 w - -')

        pinned_piece = board.get_bishops(pychess.PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['Bf2', 'Bg1', 'Bd2', 'Bc1', 'Bxd4', 'Bxf4'])

    def test_file_pinned_bishops_one_not_pinned_by_block(self):
        board = pychess.board.SetupBoard('3kq3/8/5p2/4B3/3nKn2/4B3/4N3/4r3 w - -')

        pinned_piece = board.get_bishops(pychess.PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['Bf2', 'Bg1', 'Bd2', 'Bc1', 'Bxd4', 'Bxf4'])

    def test_file_pinned_knights_all_pinned(self):
        board = pychess.board.SetupBoard('3kq3/8/6n1/4N3/4K3/4N3/6n1/4r3 w - -')

        pinned_piece = board.get_knights(pychess.PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertFalse(moves)

    def test_file_pinned_knights_one_not_pinned(self):
        board = pychess.board.SetupBoard('3kq3/8/6n1/3PNP2/2P1K1P1/4N3/2P3n1/4n3 w - -')

        pinned_piece = board.get_knights(pychess.PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['Nxg2', 'Nd1', 'Nf1'])

    def test_file_pinned_knights_one_not_pinned_by_block(self):
        board = pychess.board.SetupBoard('3kq3/8/6n1/3PNP2/2PPKPP1/4N3/2P1N1n1/4r3 w - -')

        pinned_piece = board.get_knights(pychess.PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['Nxg2', 'Nd1', 'Nf1', 'Nc3', 'Ng3', 'Nc1', 'Ng1'])

    def test_file_pinned_rooks_all_pinned(self):
        board = pychess.board.SetupBoard('3kq3/8/5r2/4R3/4K3/4R3/3r4/4r3 w - -')

        pinned_piece = board.get_rooks(pychess.PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['Re2', 'Rxe1', 'Re6', 'Re7', 'Rxe8'])

    def test_file_pinned_rooks_one_not_pinned(self):
        board = pychess.board.SetupBoard('3kq3/8/5r2/4R3/3pKp2/3PR3/3r4/4n3 w - - 0 1')

        pinned_piece = board.get_rooks(pychess.PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['Re2', 'Rxe1', 'Rf3', 'Rg3', 'Rh3', 'Re6', 'Re7', 'Rxe8'])

    def test_file_pinned_rooks_one_not_pinned_by_block(self):
        board = pychess.board.SetupBoard('3kq3/8/5r2/3nR3/4Kp2/3PR3/3rR3/4n3 w - -')

        pinned_piece = board.get_rooks(pychess.PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['Rf3', 'Rg3', 'Rh3', 'Re6', 'Re7', 'Rxe8', 'Rxd2', 'Rxe1', 'Rf2', 'Rg2', 'Rh2'])

    def test_file_pinned_queens_all_pinned(self):
        board = pychess.board.SetupBoard('3kq3/8/5r2/4Q3/4K3/4Q3/3r4/4r3 w - -')

        pinned_piece = board.get_queens(pychess.PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['Qe2', 'Qxe1', 'Qe6', 'Qe7', 'Qxe8'])

    def test_file_pinned_queens_one_not_pinned(self):
        board = pychess.board.SetupBoard('3kq3/8/5r2/4Q3/3pKp2/3PQ3/3r4/4n3 w - - 0 1')

        pinned_piece = board.get_queens(pychess.PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['Qe2', 'Qxe1', 'Qxd2', 'Qf2', 'Qg1', 'Qf3', 'Qg3', 'Qh3', 'Qxd4', 'Qxf4',
                                      'Qe6', 'Qe7', 'Qxe8'])

    def test_file_pinned_queens_one_not_pinned_by_block(self):
        board = pychess.board.SetupBoard('3kq3/8/5r2/4Q3/3pKp2/3PQ3/3rR3/4n3 w - -')

        pinned_piece = board.get_queens(pychess.PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['Qxd2', 'Qf2', 'Qg1', 'Qf3', 'Qg3', 'Qh3', 'Qxd4', 'Qxf4',
                                      'Qe6', 'Qe7', 'Qxe8'])

    def test_rank_pinned_pawns_all_pinned(self):
        board = pychess.board.SetupBoard('44k3/8/8/8/6r1/r2PKP1q/8/8 w - -')

        pinned_piece = board.get_pawns(pychess.PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertFalse(moves)

    def test_rank_pinned_pawns_one_not_pinned(self):
        board = pychess.board.SetupBoard('4k3/8/8/8/6r1/r2PKP1b/8/8 w - -')

        pinned_piece = board.get_pawns(pychess.PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['f4', 'fxg4'])

    def test_rank_pinned_pawns_one_not_pinned_by_block(self):
        board = pychess.board.SetupBoard('4k3/8/8/8/6r1/r2PKPNq/8/8 w - -')

        pinned_piece = board.get_pawns(pychess.PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['f4', 'fxg4'])

    def test_rank_pinned_bishops_all_pinned(self):
        board = pychess.board.SetupBoard('4k3/8/8/8/6r1/r2BKB1q/8/8 w - -')

        pinned_piece = board.get_bishops(pychess.PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertFalse(moves)

    def test_rank_pinned_bishops_one_not_pinned(self):
        board = pychess.board.SetupBoard('4k3/8/8/8/4n1r1/r2BKB1n/8/8 w - -')

        pinned_piece = board.get_bishops(pychess.PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['Be2', 'Bd1', 'Bxg4', 'Bxe4', 'Bg2', 'Bh1'])

    def test_rank_pinned_bishops_one_not_pinned_by_block(self):
        board = pychess.board.SetupBoard('4k3/8/8/8/4n1r1/r2BKBNr/8/8 w - -')

        pinned_piece = board.get_bishops(pychess.PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['Be2', 'Bd1', 'Bxg4', 'Bxe4', 'Bg2', 'Bh1'])

    def test_rank_pinned_knights_all_pinned(self):
        board = pychess.board.SetupBoard('7k/8/1P1P1n2/r5P1/r1NKN2q/6P1/1n1P1P2/8 w - -')

        pinned_piece = board.get_knights(pychess.PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertFalse(moves)

    def test_rank_pinned_knights_one_not_pinned(self):
        board = pychess.board.SetupBoard('7k/8/1P1P1n2/r5P1/n1NKN2q/6P1/1n1P1P2/8 w - -')

        pinned_piece = board.get_knights(pychess.PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['Nxb2', 'Ne3', 'Nxa5', 'Ne5', 'Na3'])

    def test_rank_pinned_knights_one_not_pinned_by_block(self):
        board = pychess.board.SetupBoard('7k/8/1P1P1n2/r5P1/nBNKN2q/6P1/1n1P1P2/8 w - -')

        pinned_piece = board.get_knights(pychess.PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['Nxb2', 'Ne3', 'Nxa5', 'Ne5', 'Na3'])

    def test_rank_pinned_rooks_all_pinned(self):
        board = pychess.board.SetupBoard('7k/8/8/2P1n3/r1RKR2q/2n5/4P3/8 w - -')

        pinned_piece = board.get_rooks(pychess.PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['Rb4', 'Rxa4', 'Rf4', 'Rg4', 'Rxh4'])

    def test_rank_pinned_rooks_one_not_pinned(self):
        board = pychess.board.SetupBoard('7k/8/8/2P1n3/n1RKR2q/2n5/4P3/8 w - -')

        pinned_piece = board.get_rooks(pychess.PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['Rb4', 'Rxa4', 'Rf4', 'Rg4', 'Rxh4', 'Rxc3'])

    def test_rank_pinned_rooks_one_not_pinned_by_block(self):
        board = pychess.board.SetupBoard('7k/8/8/2P1n3/r1RKRQ1q/2n5/4P3/8 w - -')

        pinned_piece = board.get_rooks(pychess.PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['Rb4', 'Rxa4', 'Rxe5', 'Re3'])

    def test_rank_pinned_queens_all_pinned(self):
        board = pychess.board.SetupBoard('7k/8/2R1R3/2P1nb2/r1QKQ2q/2nP4/4P3/8 w - -')

        pinned_piece = board.get_queens(pychess.PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['Qb4', 'Qxa4', 'Qf4', 'Qg4', 'Qxh4'])

    def test_rank_pinned_queens_one_not_pinned(self):
        board = pychess.board.SetupBoard('7k/8/2R1R3/2P1nb2/n1QKQ2q/2nP4/4P3/8 w - -')

        pinned_piece = board.get_queens(pychess.PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['Qb4', 'Qxa4', 'Qf4', 'Qg4', 'Qxh4', 'Qd5', 'Qb3', 'Qa2', 'Qb5', 'Qa6', 'Qxc3'])

    def test_rank_pinned_queens_one_not_pinned_by_block(self):
        board = pychess.board.SetupBoard('7k/8/2R1R3/2P1nb2/qRQKQ2q/2nP4/4P3/8 w - -')

        pinned_piece = board.get_queens(pychess.PieceColor.WHITE)

        moves = []
        for p in pinned_piece:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['Qf4', 'Qg4', 'Qxh4', 'Qd5', 'Qb3', 'Qa2', 'Qb5', 'Qa6', 'Qxc3'])


if __name__ == '__main__':
    unittest.main()
