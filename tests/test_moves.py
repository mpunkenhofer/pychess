# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest
import pychess


class MoveTests(unittest.TestCase):
    def test_queen_moves_with_wQ_on_d4(self):
        board = pychess.board.SetupBoard('4k3/8/8/8/3Q4/8/8/4K3 w KQkq -')
        queen = board.get_queens(pychess.PieceColor.WHITE)[0]

        moves = [m.to_algebraic() for m in queen.moves()]

        self.assertCountEqual(moves, ['Qc4', 'Qb4', 'Qa4', 'Qe4', 'Qf4', 'Qg4', 'Qh4',  # file
                                      'Qd3', 'Qd2', 'Qd1', 'Qd5', 'Qd6', 'Qd7', 'Qd8',  # rank
                                      'Qc5', 'Qb6', 'Qa7',  # falling diagonal up
                                      'Qe3', 'Qf2', 'Qg1',  # falling diagonal down
                                      'Qc3', 'Qb2', 'Qa1',  # rising diagonal down
                                      'Qe5', 'Qf6', 'Qg7', 'Qh8'  # rising diagonal up
                                      ])

    def test_queen_moves_with_bQ_on_d4(self):
        board = pychess.board.SetupBoard('4k3/8/8/8/3q4/8/8/4K3 w KQkq -')
        queen = board.get_queens(pychess.PieceColor.BLACK)[0]

        moves = [m.to_algebraic() for m in queen.moves()]

        self.assertCountEqual(moves, ['Qc4', 'Qb4', 'Qa4', 'Qe4', 'Qf4', 'Qg4', 'Qh4',  # file
                                      'Qd3', 'Qd2', 'Qd1', 'Qd5', 'Qd6', 'Qd7', 'Qd8',  # rank
                                      'Qc5', 'Qb6', 'Qa7',  # falling diagonal up
                                      'Qe3', 'Qf2', 'Qg1',  # falling diagonal down
                                      'Qc3', 'Qb2', 'Qa1',  # rising diagonal down
                                      'Qe5', 'Qf6', 'Qg7', 'Qh8'  # rising diagonal up
                                      ])

    def test_queen_moves_with_wQ_on_d4_including_captures(self):
        board = pychess.board.SetupBoard('3nk2n/n7/8/8/n2Q3n/8/8/n2nK1n1 w KQkq -')
        queen = board.get_queens(pychess.PieceColor.WHITE)[0]

        moves = [m.to_algebraic() for m in queen.moves()]

        self.assertCountEqual(moves, ['Qc4', 'Qb4', 'Qxa4', 'Qe4', 'Qf4', 'Qg4', 'Qxh4',  # file
                                      'Qd3', 'Qd2', 'Qxd1', 'Qd5', 'Qd6', 'Qd7', 'Qxd8',  # rank
                                      'Qc5', 'Qb6', 'Qxa7',  # falling diagonal up
                                      'Qe3', 'Qf2', 'Qxg1',  # falling diagonal down
                                      'Qc3', 'Qb2', 'Qxa1',  # rising diagonal down
                                      'Qe5', 'Qf6', 'Qg7', 'Qxh8'  # rising diagonal up
                                      ])

    def test_queen_moves_with_bQ_on_d4_including_captures(self):
        board = pychess.board.SetupBoard('3Nk2N/N7/8/8/N2q3N/8/8/N2NK1N1 w KQkq -')
        queen = board.get_queens(pychess.PieceColor.BLACK)[0]

        moves = [m.to_algebraic() for m in queen.moves()]

        self.assertCountEqual(moves, ['Qc4', 'Qb4', 'Qxa4', 'Qe4', 'Qf4', 'Qg4', 'Qxh4',  # file
                                      'Qd3', 'Qd2', 'Qxd1', 'Qd5', 'Qd6', 'Qd7', 'Qxd8',  # rank
                                      'Qc5', 'Qb6', 'Qxa7',  # falling diagonal up
                                      'Qe3', 'Qf2', 'Qxg1',  # falling diagonal down
                                      'Qc3', 'Qb2', 'Qxa1',  # rising diagonal down
                                      'Qe5', 'Qf6', 'Qg7', 'Qxh8'  # rising diagonal up
                                      ])

    def test_queen_moves_with_wQ_on_d4_blocking_captures(self):
        board = pychess.board.SetupBoard('3nk2n/n2N2B1/1N6/8/nN1Q2Nn/8/1N1N1N2/n2nK1n1 w KQkq -')
        queen = board.get_queens(pychess.PieceColor.WHITE)[0]

        moves = [m.to_algebraic() for m in queen.moves()]

        self.assertCountEqual(moves, ['Qc4', 'Qe4', 'Qf4',  # file
                                      'Qd3', 'Qd5', 'Qd6',  # rank
                                      'Qc5',  # falling diagonal up
                                      'Qe3',  # falling diagonal down
                                      'Qc3',  # rising diagonal down
                                      'Qe5', 'Qf6'  # rising diagonal up
                                      ])

    def test_queen_moves_with_bQ_on_d4_blocking_captures(self):
        board = pychess.board.SetupBoard('3Nk2N/N2n2r1/1n6/8/Nn1q2rN/8/1n1n1n2/N2NK1N1 w KQkq -')
        queen = board.get_queens(pychess.PieceColor.BLACK)[0]

        moves = [m.to_algebraic() for m in queen.moves()]

        self.assertCountEqual(moves, ['Qc4', 'Qe4', 'Qf4',  # file
                                      'Qd3', 'Qd5', 'Qd6',  # rank
                                      'Qc5',  # falling diagonal up
                                      'Qe3',  # falling diagonal down
                                      'Qc3',  # rising diagonal down
                                      'Qe5', 'Qf6'  # rising diagonal up
                                      ])

    def test_rook_moves_with_wR_on_d4(self):
        board = pychess.board.SetupBoard('4k3/8/8/8/3R4/8/8/4K3 w KQkq -')
        rooks = board.get_rooks(pychess.PieceColor.WHITE)[0]

        moves = [m.to_algebraic() for m in rooks.moves()]

        self.assertCountEqual(moves, ['Rc4', 'Rb4', 'Ra4', 'Re4', 'Rf4', 'Rg4', 'Rh4',  # file
                                      'Rd3', 'Rd2', 'Rd1', 'Rd5', 'Rd6', 'Rd7', 'Rd8',  # rank
                                      ])

    def test_rook_moves_with_bR_on_d4(self):
        board = pychess.board.SetupBoard('4k3/8/8/8/3r4/8/8/4K3 w KQkq -')
        rooks = board.get_rooks(pychess.PieceColor.BLACK)[0]

        moves = [m.to_algebraic() for m in rooks.moves()]

        self.assertCountEqual(moves, ['Rc4', 'Rb4', 'Ra4', 'Re4', 'Rf4', 'Rg4', 'Rh4',  # file
                                      'Rd3', 'Rd2', 'Rd1', 'Rd5', 'Rd6', 'Rd7', 'Rd8',  # rank
                                      ])

    def test_rook_moves_with_wR_on_d4_including_captures(self):
        board = pychess.board.SetupBoard('3nk3/8/8/8/n2R3n/8/8/3nK3 w KQkq -')
        rooks = board.get_rooks(pychess.PieceColor.WHITE)[0]

        moves = [m.to_algebraic() for m in rooks.moves()]

        self.assertCountEqual(moves, ['Rc4', 'Rb4', 'Rxa4', 'Re4', 'Rf4', 'Rg4', 'Rxh4',  # file
                                      'Rd3', 'Rd2', 'Rxd1', 'Rd5', 'Rd6', 'Rd7', 'Rxd8',  # rank
                                      ])

    def test_rook_moves_with_bR_on_d4_including_captures(self):
        board = pychess.board.SetupBoard('3Nk3/8/8/8/N2r3N/8/8/3NK3 w KQkq -')
        rooks = board.get_rooks(pychess.PieceColor.BLACK)[0]

        moves = [m.to_algebraic() for m in rooks.moves()]

        self.assertCountEqual(moves, ['Rc4', 'Rb4', 'Rxa4', 'Re4', 'Rf4', 'Rg4', 'Rxh4',  # file
                                      'Rd3', 'Rd2', 'Rxd1', 'Rd5', 'Rd6', 'Rd7', 'Rxd8',  # rank
                                      ])

    def test_rook_moves_with_wR_on_d4_blocking_captures(self):
        board = pychess.board.SetupBoard('3nk3/3N4/8/8/nN1R2Nn/8/3N4/3nK3 w KQkq -')
        rooks = board.get_rooks(pychess.PieceColor.WHITE)[0]

        moves = [m.to_algebraic() for m in rooks.moves()]

        self.assertCountEqual(moves, ['Rc4', 'Re4', 'Rf4',  # file
                                      'Rd3', 'Rd5', 'Rd6',  # rank
                                      ])

    def test_rook_moves_with_bR_on_d4_blocking_captures(self):
        board = pychess.board.SetupBoard('3Nk3/3n4/8/8/Nn1r2nN/8/3n4/3NK3 w KQkq -')
        rooks = board.get_rooks(pychess.PieceColor.BLACK)[0]

        moves = [m.to_algebraic() for m in rooks.moves()]

        self.assertCountEqual(moves, ['Rc4', 'Re4', 'Rf4',  # file
                                      'Rd3', 'Rd5', 'Rd6',  # rank
                                      ])

    def test_bishop_moves_with_wB_on_e4(self):
        board = pychess.board.SetupBoard('4k3/8/8/8/4B3/8/8/4K3 w KQkq -')
        bishop = board.get_bishops(pychess.PieceColor.WHITE)[0]

        moves = [m.to_algebraic() for m in bishop.moves()]

        self.assertCountEqual(moves, ['Bd5', 'Bc6', 'Bb7', 'Ba8',  # falling diagonal up
                                      'Bf3', 'Bg2', 'Bh1',  # falling diagonal down
                                      'Bd3', 'Bc2', 'Bb1',  # rising diagonal down
                                      'Bf5', 'Bg6', 'Bh7',  # rising diagonal up
                                      ])

    def test_bishop_moves_with_wB_on_d4(self):
        board = pychess.board.SetupBoard('4k3/8/8/8/3B4/8/8/4K3 w KQkq -')
        bishop = board.get_bishops(pychess.PieceColor.WHITE)[0]

        moves = [m.to_algebraic() for m in bishop.moves()]

        self.assertCountEqual(moves, ['Bc5', 'Bb6', 'Ba7',  # falling diagonal up
                                      'Be3', 'Bf2', 'Bg1',  # falling diagonal down
                                      'Bc3', 'Bb2', 'Ba1',  # rising diagonal down
                                      'Be5', 'Bf6', 'Bg7', 'Bh8'  # rising diagonal up
                                      ])

    def test_bishop_moves_with_bB_on_d4(self):
        board = pychess.board.SetupBoard('4k3/8/8/8/3b4/8/8/4K3 w KQkq -')
        bishop = board.get_bishops(pychess.PieceColor.BLACK)[0]

        moves = [m.to_algebraic() for m in bishop.moves()]

        self.assertCountEqual(moves, ['Bc5', 'Bb6', 'Ba7',  # falling diagonal up
                                      'Be3', 'Bf2', 'Bg1',  # falling diagonal down
                                      'Bc3', 'Bb2', 'Ba1',  # rising diagonal down
                                      'Be5', 'Bf6', 'Bg7', 'Bh8'  # rising diagonal up
                                      ])

    def test_bishop_moves_with_wB_on_d4_including_captures(self):
        board = pychess.board.SetupBoard('4k2n/n7/8/8/3B4/8/8/n3K1n1 w KQkq -')
        bishop = board.get_bishops(pychess.PieceColor.WHITE)[0]

        moves = [m.to_algebraic() for m in bishop.moves()]

        self.assertCountEqual(moves, ['Bc5', 'Bb6', 'Bxa7',  # falling diagonal up
                                      'Be3', 'Bf2', 'Bxg1',  # falling diagonal down
                                      'Bc3', 'Bb2', 'Bxa1',  # rising diagonal down
                                      'Be5', 'Bf6', 'Bg7', 'Bxh8'  # rising diagonal up
                                      ])

    def test_bishop_moves_with_bB_on_d4_including_captures(self):
        board = pychess.board.SetupBoard('4k2N/N7/8/8/3b4/8/8/N3K1N1 w KQkq -')
        bishop = board.get_bishops(pychess.PieceColor.BLACK)[0]

        moves = [m.to_algebraic() for m in bishop.moves()]

        self.assertCountEqual(moves, ['Bc5', 'Bb6', 'Bxa7',  # falling diagonal up
                                      'Be3', 'Bf2', 'Bxg1',  # falling diagonal down
                                      'Bc3', 'Bb2', 'Bxa1',  # rising diagonal down
                                      'Be5', 'Bf6', 'Bg7', 'Bxh8'  # rising diagonal up
                                      ])

    def test_bishop_moves_with_wB_on_d4_blocking_captures(self):
        board = pychess.board.SetupBoard('4k2n/n5R1/1N6/8/3B4/8/1N3N2/n3K1n1 w KQkq -')
        bishop = board.get_bishops(pychess.PieceColor.WHITE)[0]

        moves = [m.to_algebraic() for m in bishop.moves()]

        self.assertCountEqual(moves, ['Bc5',  # falling diagonal up
                                      'Be3',  # falling diagonal down
                                      'Bc3',  # rising diagonal down
                                      'Be5', 'Bf6'  # rising diagonal up
                                      ])

    def test_bishop_moves_with_bB_on_d4_blocking_captures(self):
        board = pychess.board.SetupBoard('4k2N/N5n1/1n6/8/3b4/8/1n3n2/N3K1N1 w KQkq -')
        bishop = board.get_bishops(pychess.PieceColor.BLACK)[0]

        moves = [m.to_algebraic() for m in bishop.moves()]

        self.assertCountEqual(moves, ['Bc5',  # falling diagonal up
                                      'Be3',  # falling diagonal down
                                      'Bc3',  # rising diagonal down
                                      'Be5', 'Bf6'  # rising diagonal up
                                      ])

    def test_knight_moves_with_wN_on_e4(self):
        board = pychess.board.SetupBoard('4k3/8/8/8/4N3/8/8/4K3 w KQkq -')
        knight = board.get_knights(pychess.PieceColor.WHITE)[0]

        moves = [m.to_algebraic() for m in knight.moves()]

        self.assertCountEqual(moves, ['Nd2', 'Nf2', 'Ng3', 'Ng5', 'Nf6', 'Nd6', 'Nc5', 'Nc3'])

    def test_knight_moves_with_bN_on_e4(self):
        board = pychess.board.SetupBoard('4k3/8/8/8/4n3/8/8/4K3 w KQkq -')
        knight = board.get_knights(pychess.PieceColor.BLACK)[0]

        moves = [m.to_algebraic() for m in knight.moves()]

        self.assertCountEqual(moves, ['Nd2', 'Nf2', 'Ng3', 'Ng5', 'Nf6', 'Nd6', 'Nc5', 'Nc3'])

    def test_knight_moves_with_wN_on_e4_including_captures(self):
        board = pychess.board.SetupBoard('4k3/8/3n1n2/2n3n1/4N3/2n3n1/3n1n2/4K3 w KQkq -')
        knight = board.get_knights(pychess.PieceColor.WHITE)[0]

        moves = [m.to_algebraic() for m in knight.moves()]

        self.assertCountEqual(moves, ['Nxd2', 'Nxf2', 'Nxg3', 'Nxg5', 'Nxf6', 'Nxd6', 'Nxc5', 'Nxc3'])

    def test_knight_moves_with_bN_on_e4_including_captures(self):
        board = pychess.board.SetupBoard('4k3/8/3B1B2/2N3N1/4n3/2N3N1/3N1N2/4K3 w KQkq -')
        knight = board.get_knights(pychess.PieceColor.BLACK)[0]

        moves = [m.to_algebraic() for m in knight.moves()]

        self.assertCountEqual(moves, ['Nxd2', 'Nxf2', 'Nxg3', 'Nxg5', 'Nxf6', 'Nxd6', 'Nxc5', 'Nxc3'])

    def test_king_moves_with_wK_on_e4(self):
        board = pychess.board.SetupBoard('4k3/8/8/8/4K3/8/8/8 w KQkq -')
        king = board.get_king(pychess.PieceColor.WHITE)

        moves = [m.to_algebraic() for m in king.moves()]

        self.assertCountEqual(moves, ['Ke5', 'Ke3', 'Kd3', 'Kd4', 'Kd5', 'Kf3', 'Kf4', 'Kf5'])

    def test_king_moves_with_bK_on_e4(self):
        board = pychess.board.SetupBoard('4K3/8/8/8/4k3/8/8/8 w KQkq -')
        king = board.get_king(pychess.PieceColor.BLACK)

        moves = [m.to_algebraic() for m in king.moves()]

        self.assertCountEqual(moves, ['Ke5', 'Ke3', 'Kd3', 'Kd4', 'Kd5', 'Kf3', 'Kf4', 'Kf5'])

    def test_king_moves_with_wK_on_a1(self):
        board = pychess.board.SetupBoard('4k3/8/8/8/8/8/8/K7 w KQkq -')
        king = board.get_king(pychess.PieceColor.WHITE)

        moves = [m.to_algebraic() for m in king.moves()]

        self.assertCountEqual(moves, ['Kb1', 'Kb2', 'Ka2'])

    def test_king_moves_with_bK_on_h8(self):
        board = pychess.board.SetupBoard('7k/8/8/8/8/8/8/4K3 w KQkq -')
        king = board.get_king(pychess.PieceColor.BLACK)

        moves = [m.to_algebraic() for m in king.moves()]

        self.assertCountEqual(moves, ['Kh7', 'Kg8', 'Kg7'])

    def test_pawn_moves_with_wPs(self):
        board = pychess.board.SetupBoard('7k/5P2/4P3/3P4/2P5/1P6/P7/4K3 w KQkq -')
        pawns = board.get_pawns(pychess.PieceColor.WHITE)

        moves = []

        for p in pawns:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['a3', 'a4', 'b4', 'c5', 'd6', 'e7', 'f8=Q', 'f8=R', 'f8=B', 'f8=N'])

    def test_pawn_moves_with_wPs_and_blocker(self):
        board = pychess.board.SetupBoard('4k3/8/8/8/5N1N/1N1NPPPP/PPPP4/1K6 w KQkq -')
        pawns = board.get_pawns(pychess.PieceColor.WHITE)

        moves = []

        for p in pawns:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['a3', 'a4', 'c3', 'c4', 'e4', 'g4'])

    def test_pawn_moves_with_bPs(self):
        board = pychess.board.SetupBoard('4k3/p7/1p6/2p5/3p4/4p3/5p2/1K6 w KQkq -')
        pawns = board.get_pawns(pychess.PieceColor.BLACK)

        moves = []

        for p in pawns:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['a6', 'a5', 'b5', 'c4', 'd3', 'e2', 'f1=Q', 'f1=R', 'f1=B', 'f1=N'])

    def test_pawn_moves_with_bPs_and_blocker(self):
        board = pychess.board.SetupBoard('4k3/4pppp/ppppn1n1/n1n5/8/8/8/1K6 w KQkq -')
        pawns = board.get_pawns(pychess.PieceColor.BLACK)

        moves = []

        for p in pawns:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['h6', 'h5', 'f6', 'f5', 'd5', 'b5'])

    def test_pawn_captures_with_wPs(self):
        board = pychess.board.SetupBoard('4k3/nnnnnnnn/1P1P1P1P/nnnnnnnn/P1P1P1P1/8/8/1K6 w KQkq -')
        pawns = board.get_pawns(pychess.PieceColor.WHITE)

        moves = []

        for p in pawns:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['axb5', 'cxb5', 'cxd5', 'exd5', 'exf5', 'gxf5', 'gxh5',  # rank 4 pawns
                                      'bxa7', 'bxc7', 'dxc7', 'dxe7', 'fxe7', 'fxg7', 'hxg7'  # rank 6 pawns
                                      ])

    def test_pawn_captures_with_bPs(self):
        board = pychess.board.SetupBoard('4k3/8/8/p1p1p1p1/NNNNNNNN/1p1p1p1p/NNNNNNNN/1K6 w KQkq -')
        pawns = board.get_pawns(pychess.PieceColor.BLACK)

        moves = []

        for p in pawns:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['axb4', 'cxb4', 'cxd4', 'exd4', 'exf4', 'gxf4', 'gxh4',  # rank 5 pawns
                                      'bxa2', 'bxc2', 'dxc2', 'dxe2', 'fxe2', 'fxg2', 'hxg2'  # rank 3 pawns
                                      ])

    def test_pawn_promotion_captures_with_wPs(self):
        board = pychess.board.SetupBoard('nnnn3k/PPPP4/8/8/8/8/8/1K6 w KQkq -')
        pawns = board.get_pawns(pychess.PieceColor.WHITE)

        moves = []

        for p in pawns:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['axb8=Q', 'axb8=R', 'axb8=B', 'axb8=N',  # a pawn
                                      'bxa8=Q', 'bxa8=R', 'bxa8=B', 'bxa8=N', 'bxc8=Q', 'bxc8=R', 'bxc8=B', 'bxc8=N',
                                      'cxb8=Q', 'cxb8=R', 'cxb8=B', 'cxb8=N', 'cxd8=Q', 'cxd8=R', 'cxd8=B', 'cxd8=N',
                                      'dxc8=Q', 'dxc8=R', 'dxc8=B', 'dxc8=N'   # d pawn
                                      ])

    def test_pawn_promotion_captures_with_bPs(self):
        board = pychess.board.SetupBoard('7k/8/8/8/8/8/pppp4/NNNN3K w KQkq -')
        pawns = board.get_pawns(pychess.PieceColor.BLACK)

        moves = []

        for p in pawns:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['axb1=Q', 'axb1=R', 'axb1=B', 'axb1=N',  # a pawn
                                      'bxa1=Q', 'bxa1=R', 'bxa1=B', 'bxa1=N', 'bxc1=Q', 'bxc1=R', 'bxc1=B', 'bxc1=N',
                                      'cxb1=Q', 'cxb1=R', 'cxb1=B', 'cxb1=N', 'cxd1=Q', 'cxd1=R', 'cxd1=B', 'cxd1=N',
                                      'dxc1=Q', 'dxc1=R', 'dxc1=B', 'dxc1=N'   # d pawn
                                      ])

    def test_pawn_en_passant_wPs(self):
        board = pychess.board.SetupBoard('rnbqkbnr/pppppppp/8/3P1P2/8/8/PPP2PPP/RNBQKBNR b KQkq -')

        board.algebraic_move(pychess.PieceColor.BLACK, 'e5')

        pawns = board.get_pawns(pychess.PieceColor.WHITE)

        moves = []
        for p in pawns:
            for m in p.moves():
                moves.append(m.to_algebraic())

        en_passant_moves = ['dxe6', 'fxe6']
        en_passants_found = []

        for em in en_passant_moves:
            if em in moves:
                en_passants_found.append(em)

        self.assertCountEqual(en_passant_moves, en_passants_found)

    def test_pawn_en_passant_bPs(self):
        board = pychess.board.SetupBoard('rnbqkbnr/ppp1p1pp/8/8/3p1p2/8/PPPPPPPP/RNBQKBNR w KQkq -')

        board.algebraic_move(pychess.PieceColor.WHITE, 'e4')

        pawns = board.get_pawns(pychess.PieceColor.BLACK)

        moves = []
        for p in pawns:
            for m in p.moves():
                moves.append(m.to_algebraic())

        en_passant_moves = ['dxe3', 'fxe3']
        en_passants_found = []

        for em in en_passant_moves:
            if em in moves:
                en_passants_found.append(em)

        self.assertCountEqual(en_passant_moves, en_passants_found)

    def test_castling_short_w(self):
        board = pychess.board.SetupBoard('rnbqk2r/pppppppp/8/8/8/8/PPPPPPPP/RNBQK2R w KQkq -')

        king = board.get_king(pychess.PieceColor.WHITE)
        moves = [m.to_algebraic() for m in king.moves()]

        self.assertCountEqual(moves, ['Kf1', 'O-O'])

    def test_castling_short_b(self):
        board = pychess.board.SetupBoard('rnbqk2r/pppppppp/8/8/8/8/PPPPPPPP/RNBQK2R w KQkq -')

        king = board.get_king(pychess.PieceColor.BLACK)
        moves = [m.to_algebraic() for m in king.moves()]

        self.assertCountEqual(moves, ['Kf8', 'O-O'])

    def test_castling_long_w(self):
        board = pychess.board.SetupBoard('r3kbnr/pppppppp/8/8/8/8/PPPPPPPP/R3KBNR w KQkq -')

        king = board.get_king(pychess.PieceColor.WHITE)
        moves = [m.to_algebraic() for m in king.moves()]

        self.assertCountEqual(moves, ['Kd1', 'O-O-O'])

    def test_castling_long_b(self):
        board = pychess.board.SetupBoard('r3kbnr/pppppppp/8/8/8/8/PPPPPPPP/R3KBNR w KQkq -')

        king = board.get_king(pychess.PieceColor.BLACK)
        moves = [m.to_algebraic() for m in king.moves()]

        self.assertCountEqual(moves, ['Kd8', 'O-O-O'])

    def test_castling_short_and_long_w(self):
        board = pychess.board.SetupBoard('r3k2r/pppppppp/8/8/8/8/PPPPPPPP/R3K2R w KQkq -')

        king = board.get_king(pychess.PieceColor.WHITE)
        moves = [m.to_algebraic() for m in king.moves()]

        self.assertCountEqual(moves, ['Kd1', 'O-O-O', 'Kf1', 'O-O'])

    def test_castling_short_and_long_b(self):
        board = pychess.board.SetupBoard('r3k2r/pppppppp/8/8/8/8/PPPPPPPP/R3K2R w KQkq -')

        king = board.get_king(pychess.PieceColor.BLACK)
        moves = [m.to_algebraic() for m in king.moves()]

        self.assertCountEqual(moves, ['Kd8', 'O-O-O', 'Kf8', 'O-O'])

    def test_not_castling_short_1_w(self):
        board = pychess.board.SetupBoard('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKB1R w KQkq -')

        king = board.get_king(pychess.PieceColor.WHITE)
        moves = [m.to_algebraic() for m in king.moves()]

        self.assertFalse(moves)

    def test_not_castling_short_1_b(self):
        board = pychess.board.SetupBoard('rnbqkb1r/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq -')

        king = board.get_king(pychess.PieceColor.BLACK)
        moves = [m.to_algebraic() for m in king.moves()]

        self.assertFalse(moves)

    def test_not_castling_short_2_w(self):
        board = pychess.board.SetupBoard('rnbqk1nr/pppppppp/8/8/8/8/PPPPPPPP/RNBQK1NR w KQkq -')

        king = board.get_king(pychess.PieceColor.WHITE)
        moves = [m.to_algebraic() for m in king.moves()]

        self.assertCountEqual(moves, ['Kf1'])

    def test_not_castling_short_2_b(self):
        board = pychess.board.SetupBoard('rnbqk1nr/pppppppp/8/8/8/8/PPPPPPPP/RNBQK1NR w KQkq -')

        king = board.get_king(pychess.PieceColor.BLACK)
        moves = [m.to_algebraic() for m in king.moves()]

        self.assertCountEqual(moves, ['Kf8'])

    def test_not_castling_long_1_w(self):
        board = pychess.board.SetupBoard('r1bqkbnr/pppppppp/8/8/8/8/PPPPPPPP/R1BQKBNR w KQkq -')

        king = board.get_king(pychess.PieceColor.WHITE)
        moves = [m.to_algebraic() for m in king.moves()]

        self.assertFalse(moves)

    def test_not_castling_long_1_b(self):
        board = pychess.board.SetupBoard('r1bqkbnr/pppppppp/8/8/8/8/PPPPPPPP/R1BQKBNR w KQkq -')

        king = board.get_king(pychess.PieceColor.BLACK)
        moves = [m.to_algebraic() for m in king.moves()]

        self.assertFalse(moves)

    def test_not_castling_long_2_w(self):
        board = pychess.board.SetupBoard('r2qkbnr/pppppppp/8/8/8/8/PPPPPPPP/R2QKBNR w KQkq -')

        king = board.get_king(pychess.PieceColor.WHITE)
        moves = [m.to_algebraic() for m in king.moves()]

        self.assertFalse(moves)

    def test_not_castling_long_2_b(self):
        board = pychess.board.SetupBoard('r2qkbnr/pppppppp/8/8/8/8/PPPPPPPP/R2QKBNR w KQkq -')

        king = board.get_king(pychess.PieceColor.BLACK)
        moves = [m.to_algebraic() for m in king.moves()]

        self.assertFalse(moves)

    def test_not_castling_long_3_w(self):
        board = pychess.board.SetupBoard('rnb1kbnr/pppppppp/8/8/8/8/PPPPPPPP/RNB1KBNR w KQkq -')

        king = board.get_king(pychess.PieceColor.WHITE)
        moves = [m.to_algebraic() for m in king.moves()]

        self.assertCountEqual(moves, ['Kd1'])

    def test_not_castling_long_3_b(self):
        board = pychess.board.SetupBoard('rnb1kbnr/pppppppp/8/8/8/8/PPPPPPPP/RNB1KBNR w KQkq -')

        king = board.get_king(pychess.PieceColor.BLACK)
        moves = [m.to_algebraic() for m in king.moves()]

        self.assertCountEqual(moves, ['Kd8'])

    def test_not_castling_short_missing_rook_w(self):
        board = pychess.board.SetupBoard('rnbqk3/pppppppp/8/8/8/8/PPPPPPPP/RNBQK3 w KQkq -')

        king = board.get_king(pychess.PieceColor.WHITE)
        moves = [m.to_algebraic() for m in king.moves()]

        self.assertCountEqual(moves, ['Kf1'])

    def test_not_castling_short_missing_rook_b(self):
        board = pychess.board.SetupBoard('rnbqk3/pppppppp/8/8/8/8/PPPPPPPP/RNBQK3 w KQkq -')

        king = board.get_king(pychess.PieceColor.BLACK)
        moves = [m.to_algebraic() for m in king.moves()]

        self.assertCountEqual(moves, ['Kf8'])

    def test_not_castling_long_missing_rook_w(self):
        board = pychess.board.SetupBoard('4kbnr/pppppppp/8/8/8/8/PPPPPPPP/4KBNR w KQkq -')

        king = board.get_king(pychess.PieceColor.WHITE)
        moves = [m.to_algebraic() for m in king.moves()]

        self.assertCountEqual(moves, ['Kd1'])

    def test_not_castling_long_missing_rook_b(self):
        board = pychess.board.SetupBoard('4kbnr/pppppppp/8/8/8/8/PPPPPPPP/4KBNR w KQkq -')

        king = board.get_king(pychess.PieceColor.BLACK)
        moves = [m.to_algebraic() for m in king.moves()]

        self.assertCountEqual(moves, ['Kd8'])

    def test_not_castling_long_king_in_check_w(self):
        board = pychess.board.SetupBoard('r3k1nr/pppp1ppp/8/8/7b/8/PPPPP1PP/R3KBNR w Kk -')

        king = board.get_king(pychess.PieceColor.WHITE)
        moves = [m.to_algebraic() for m in king.moves()]

        self.assertTrue(moves == ['Kd1'] and king.in_check())

    def test_not_castling_long_king_in_check_b(self):
        board = pychess.board.SetupBoard('r3kbnr/ppppp1pp/8/7B/8/8/PPPP1PPP/R3KBNR w Kk -')

        king = board.get_king(pychess.PieceColor.BLACK)
        moves = [m.to_algebraic() for m in king.moves()]

        self.assertTrue(moves == ['Kd8'] and king.in_check())

    def test_not_castling_short_king_in_check_w(self):
        board = pychess.board.SetupBoard('rnbqk2r/ppp1pppp/8/b7/8/8/PPP1PPPP/RNBQK2R w KQkq -')

        king = board.get_king(pychess.PieceColor.WHITE)
        moves = [m.to_algebraic() for m in king.moves()]

        self.assertTrue(moves == ['Kf1'] and king.in_check())

    def test_not_castling_short_king_in_check_b(self):
        board = pychess.board.SetupBoard('rnbqk2r/ppp1pppp/8/8/B7/8/PPP1PPPP/RNBQK2R w KQkq -')

        king = board.get_king(pychess.PieceColor.BLACK)
        moves = [m.to_algebraic() for m in king.moves()]

        self.assertTrue(moves == ['Kf8'] and king.in_check())

    def test_not_castling_short_king_move_in_check_w(self):
        board = pychess.board.SetupBoard('rnbqk2r/ppp3pp/5p2/2b1p3/2B1P3/5P2/PPP3PP/RNBQK2R w KQkq -')

        king = board.get_king(pychess.PieceColor.WHITE)
        moves = [m.to_algebraic() for m in king.moves()]

        self.assertCountEqual(moves, ['Kf1', 'Ke2'])

    def test_not_castling_short_king_move_in_check_b(self):
        board = pychess.board.SetupBoard('rnbqk2r/ppp3pp/5p2/2b1p3/2B1P3/5P2/PPP3PP/RNBQK2R w KQkq -')

        king = board.get_king(pychess.PieceColor.BLACK)
        moves = [m.to_algebraic() for m in king.moves()]

        self.assertCountEqual(moves, ['Ke7', 'Kf8'])

    def test_not_castling_short_king_move_through_check_w(self):
        board = pychess.board.SetupBoard('rnbqkr2/ppppp1pp/8/8/8/8/PPPPP1PP/RNBQK2R w KQkq -')

        king = board.get_king(pychess.PieceColor.WHITE)

        self.assertFalse(king.moves())

    def test_not_castling_short_king_move_through_check_b(self):
        board = pychess.board.SetupBoard('rnbqk2r/ppppp1pp/8/8/8/8/PPPPP1PP/RNBQKR2 w KQkq -')

        king = board.get_king(pychess.PieceColor.BLACK)

        self.assertFalse(king.moves())

    def test_not_castling_long_king_through_check_w(self):
        board = pychess.board.SetupBoard('r3k1nr/pp2qppp/3p4/B3p3/b3P3/3P4/PP2QPPP/R3K1NR w KQkq -')

        king = board.get_king(pychess.PieceColor.WHITE)
        moves = [m.to_algebraic() for m in king.moves()]

        self.assertCountEqual(moves, ['Kd2', 'Kf1'])

    def test_not_castling_long_king_through_check_b(self):
        board = pychess.board.SetupBoard('r3k1nr/pp2qppp/3p4/B3p3/b3P3/3P4/PP2QPPP/R3K1NR w KQkq -')

        king = board.get_king(pychess.PieceColor.BLACK)
        moves = [m.to_algebraic() for m in king.moves()]

        self.assertCountEqual(moves, ['Kd7', 'Kf8'])

    def test_two_w_queen_on_same_diagonal(self):
        board = pychess.board.SetupBoard('Q7/6k1/8/8/8/8/5K2/7Q w - -')
        queens = board.get_queens(pychess.PieceColor.WHITE)

        moves = []
        for p in queens:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['Qa7', 'Qa6', 'Qa5', 'Qa4', 'Qa3', 'Qa2', 'Qaa1',  # file
                                      'Qh2', 'Qh3', 'Qh4', 'Qh5', 'Qh6', 'Qh7', 'Qhh8',
                                      'Qb8', 'Qc8', 'Qd8', 'Qe8', 'Qf8', 'Qg8', 'Qah8',  # rank
                                      'Qg1', 'Qf1', 'Qe1', 'Qd1', 'Qc1', 'Qb1', 'Qha1',
                                      'Qhg2', 'Qhf3', 'Qhe4', 'Qhd5', 'Qhc6', 'Qhb7',  # falling diagonal up
                                      'Qag2', 'Qaf3', 'Qae4', 'Qad5', 'Qac6', 'Qab7'   # falling diagonal down
                                      ])

    def test_two_b_queen_on_same_diagonal(self):
        board = pychess.board.SetupBoard('q7/6k1/8/8/8/8/5K2/7q w - -')
        queens = board.get_queens(pychess.PieceColor.BLACK)

        moves = []
        for p in queens:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['Qa7', 'Qa6', 'Qa5', 'Qa4', 'Qa3', 'Qa2', 'Qaa1',  # file
                                      'Qh2', 'Qh3', 'Qh4', 'Qh5', 'Qh6', 'Qh7', 'Qhh8',
                                      'Qb8', 'Qc8', 'Qd8', 'Qe8', 'Qf8', 'Qg8', 'Qah8',  # rank
                                      'Qg1', 'Qf1', 'Qe1', 'Qd1', 'Qc1', 'Qb1', 'Qha1',
                                      'Qhg2', 'Qhf3', 'Qhe4', 'Qhd5', 'Qhc6', 'Qhb7',  # falling diagonal up
                                      'Qag2', 'Qaf3', 'Qae4', 'Qad5', 'Qac6', 'Qab7'   # falling diagonal down
                                      ])

    def test_two_w_bishops_on_same_diagonal(self):
        board = pychess.board.SetupBoard('B7/6k1/8/8/8/8/5K2/7B w - -')
        bishops = board.get_bishops(pychess.PieceColor.WHITE)

        moves = []
        for p in bishops:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['Bhg2', 'Bhf3', 'Bhe4', 'Bhd5', 'Bhc6', 'Bhb7',  # falling diagonal up
                                      'Bag2', 'Baf3', 'Bae4', 'Bad5', 'Bac6', 'Bab7'   # falling diagonal down
                                      ])

    def test_two_b_bishops_on_same_diagonal(self):
        board = pychess.board.SetupBoard('b7/6k1/8/8/8/8/5K2/7b w - -')
        bishops = board.get_bishops(pychess.PieceColor.BLACK)

        moves = []
        for p in bishops:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['Bhg2', 'Bhf3', 'Bhe4', 'Bhd5', 'Bhc6', 'Bhb7',  # falling diagonal up
                                      'Bag2', 'Baf3', 'Bae4', 'Bad5', 'Bac6', 'Bab7'   # falling diagonal down
                                      ])

    def test_two_w_rooks_on_same_rank(self):
        board = pychess.board.SetupBoard('8/5k2/8/8/8/8/5K2/R6R w KQkq -')
        rooks = board.get_rooks(pychess.PieceColor.WHITE)

        moves = []
        for p in rooks:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['Rab1', 'Rac1', 'Rad1', 'Rae1', 'Raf1', 'Rag1',  # rank
                                      'Rhb1', 'Rhc1', 'Rhd1', 'Rhe1', 'Rhf1', 'Rhg1',  # files
                                      'Ra2', 'Ra3', 'Ra4', 'Ra5', 'Ra6', 'Ra7', 'Ra8',
                                      'Rh2', 'Rh3', 'Rh4', 'Rh5', 'Rh6', 'Rh7', 'Rh8'
                                      ])

    def test_two_b_rooks_on_same_rank(self):
        board = pychess.board.SetupBoard('8/5k2/8/8/8/8/5K2/r6r w KQkq -')
        rooks = board.get_rooks(pychess.PieceColor.BLACK)

        moves = []
        for p in rooks:
            for m in p.moves():
                moves.append(m.to_algebraic())

        self.assertCountEqual(moves, ['Rab1', 'Rac1', 'Rad1', 'Rae1', 'Raf1', 'Rag1',  # rank
                                      'Rhb1', 'Rhc1', 'Rhd1', 'Rhe1', 'Rhf1', 'Rhg1',  # files
                                      'Ra2', 'Ra3', 'Ra4', 'Ra5', 'Ra6', 'Ra7', 'Ra8',
                                      'Rh2', 'Rh3', 'Rh4', 'Rh5', 'Rh6', 'Rh7', 'Rh8'
                                      ])

    def test_w_knights_with_same_squares(self):
        board = pychess.board.SetupBoard('3k4/8/8/2N1N3/1N3N2/8/1N3N2/K7 w - -')
        knights = board.get_knights(pychess.PieceColor.WHITE)

        moves = []
        for p in knights:
            for m in p.moves():
                moves.append(m.to_algebraic())

        duplicates = False
        seen = set()

        for m in moves:
            if m not in seen:
                seen.add(m)
            else:
                duplicates = True
                break

        self.assertFalse(duplicates)

    def test_b_knights_with_same_squares(self):
        board = pychess.board.SetupBoard('3k4/8/8/2n1n3/1n3n2/8/1n3n2/K7 w - -')
        knights = board.get_knights(pychess.PieceColor.BLACK)

        moves = []
        for p in knights:
            for m in p.moves():
                moves.append(m.to_algebraic())

        duplicates = False
        seen = set()

        for m in moves:
            if m not in seen:
                seen.add(m)
            else:
                duplicates = True
                break

        self.assertFalse(duplicates)

    def test_king_moves_with_protected_backrank_1(self):
        board = pychess.board.SetupBoard('7k/8/8/8/8/8/5P1P/2q3K1 w - -')
        king = board.get_king(pychess.PieceColor.WHITE)

        moves = [m.to_algebraic() for m in king.moves()]

        self.assertCountEqual(moves, ['Kg2'])

    def test_king_moves_with_protected_backrank_2(self):
        board = pychess.board.SetupBoard('7k/8/8/8/8/8/5P2/2q3K1 w - -')
        king = board.get_king(pychess.PieceColor.WHITE)

        moves = [m.to_algebraic() for m in king.moves()]

        self.assertCountEqual(moves, ['Kg2', 'Kh2'])

    def test_king_moves_with_protected_squares_by_dark_square_bishops(self):
        board = pychess.board.SetupBoard('1b3b1k/8/8/b7/3K4/8/8/2b5 w - -')
        king = board.get_king(pychess.PieceColor.WHITE)

        moves = [m.to_algebraic() for m in king.moves()]

        self.assertCountEqual(moves, ['Kd3', 'Ke4', 'Kd5', 'Kc4'])

    def test_king_moves_with_protected_squares_by_light_square_bishops(self):
        board = pychess.board.SetupBoard('7k/8/4b3/1b3b2/3K4/8/8/8 w - -')
        king = board.get_king(pychess.PieceColor.WHITE)

        moves = [m.to_algebraic() for m in king.moves()]

        self.assertCountEqual(moves, ['Kc5', 'Kc3', 'Ke5', 'Ke3'])

    def test_king_moves_with_rank_only_possible(self):
        board = pychess.board.SetupBoard('7k/8/8/q7/3K4/7r/8/8 w - -')
        king = board.get_king(pychess.PieceColor.WHITE)

        moves = [m.to_algebraic() for m in king.moves()]

        self.assertCountEqual(moves, ['Kc4', 'Ke4'])

    def test_king_moves_with_file_only_possible(self):
        board = pychess.board.SetupBoard('2q4k/8/8/8/3K4/8/8/4r3 w - -')
        king = board.get_king(pychess.PieceColor.WHITE)

        moves = [m.to_algebraic() for m in king.moves()]

        self.assertCountEqual(moves, ['Kd3', 'Kd5'])

    def test_king_moves_with_protected_squares_and_blocking_pieces(self):
        board = pychess.board.SetupBoard('5b1k/8/1n3p2/8/3K4/2RNB3/8/8 w - -')
        king = board.get_king(pychess.PieceColor.WHITE)

        moves = [m.to_algebraic() for m in king.moves()]

        self.assertCountEqual(moves, ['Ke4'])

    def test_invalid_algebraic_move(self):
        board = pychess.board.StandardBoard()

        with self.assertRaises(RuntimeError):
            board.algebraic_move(pychess.PieceColor.BLACK, 'e4')

    def test_none__move(self):
        board = pychess.board.StandardBoard()

        with self.assertRaises(RuntimeError):
            board._move(None)

    def test_none_move(self):
        board = pychess.board.StandardBoard()

        with self.assertRaises(RuntimeError):
            board.move(None)


if __name__ == '__main__':
    unittest.main()
