# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest

from pychess.board import SetupBoard
from pychess.pieces import PieceColor


class MoveTests(unittest.TestCase):
    def test_pawn_moves(self):
        fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
        board = SetupBoard(fen)
        self.assertEqual(board.fen(), fen)

    def test_queen_moves_with_wQ_on_d4(self):
        board = SetupBoard('4k3/8/8/8/3Q4/8/8/4K3 w KQkq -')
        queen = board.get_queens(PieceColor.WHITE)[0]

        moves = [m.to_algebraic() for m in queen.moves()]

        self.assertCountEqual(moves, ['Qc4', 'Qb4', 'Qa4', 'Qe4', 'Qf4', 'Qg4', 'Qh4',  # file
                                      'Qd3', 'Qd2', 'Qd1', 'Qd5', 'Qd6', 'Qd7', 'Qd8',  # rank
                                      'Qc5', 'Qb6', 'Qa7',  # falling diagonal up
                                      'Qe3', 'Qf2', 'Qg1',  # falling diagonal down
                                      'Qc3', 'Qb2', 'Qa1',  # rising diagonal down
                                      'Qe5', 'Qf6', 'Qg7', 'Qh8'  # rising diagonal up
                                      ])

    def test_queen_moves_with_bQ_on_d4(self):
        board = SetupBoard('4k3/8/8/8/3q4/8/8/4K3 w KQkq -')
        queen = board.get_queens(PieceColor.BLACK)[0]

        moves = [m.to_algebraic() for m in queen.moves()]

        self.assertCountEqual(moves, ['Qc4', 'Qb4', 'Qa4', 'Qe4', 'Qf4', 'Qg4', 'Qh4',  # file
                                      'Qd3', 'Qd2', 'Qd1', 'Qd5', 'Qd6', 'Qd7', 'Qd8',  # rank
                                      'Qc5', 'Qb6', 'Qa7',  # falling diagonal up
                                      'Qe3', 'Qf2', 'Qg1',  # falling diagonal down
                                      'Qc3', 'Qb2', 'Qa1',  # rising diagonal down
                                      'Qe5', 'Qf6', 'Qg7', 'Qh8'  # rising diagonal up
                                      ])

    def test_queen_moves_with_wQ_on_d4_including_captures(self):
        board = SetupBoard('3nk2n/n7/8/8/n2Q3n/8/8/n2nK1n1 w KQkq -')
        queen = board.get_queens(PieceColor.WHITE)[0]

        moves = [m.to_algebraic() for m in queen.moves()]

        self.assertCountEqual(moves, ['Qc4', 'Qb4', 'Qxa4', 'Qe4', 'Qf4', 'Qg4', 'Qxh4',  # file
                                      'Qd3', 'Qd2', 'Qxd1', 'Qd5', 'Qd6', 'Qd7', 'Qxd8',  # rank
                                      'Qc5', 'Qb6', 'Qxa7',  # falling diagonal up
                                      'Qe3', 'Qf2', 'Qxg1',  # falling diagonal down
                                      'Qc3', 'Qb2', 'Qxa1',  # rising diagonal down
                                      'Qe5', 'Qf6', 'Qg7', 'Qxh8'  # rising diagonal up
                                      ])

    def test_queen_moves_with_bQ_on_d4_including_captures(self):
        board = SetupBoard('3Nk2N/N7/8/8/N2q3N/8/8/N2NK1N1 w KQkq -')
        queen = board.get_queens(PieceColor.BLACK)[0]

        moves = [m.to_algebraic() for m in queen.moves()]

        self.assertCountEqual(moves, ['Qc4', 'Qb4', 'Qxa4', 'Qe4', 'Qf4', 'Qg4', 'Qxh4',  # file
                                      'Qd3', 'Qd2', 'Qxd1', 'Qd5', 'Qd6', 'Qd7', 'Qxd8',  # rank
                                      'Qc5', 'Qb6', 'Qxa7',  # falling diagonal up
                                      'Qe3', 'Qf2', 'Qxg1',  # falling diagonal down
                                      'Qc3', 'Qb2', 'Qxa1',  # rising diagonal down
                                      'Qe5', 'Qf6', 'Qg7', 'Qxh8'  # rising diagonal up
                                      ])

    def test_queen_moves_with_wQ_on_d4_blocking_captures(self):
        board = SetupBoard('3nk2n/n2N2B1/1N6/8/nN1Q2Nn/8/1N1N1N2/n2nK1n1 w KQkq -')
        queen = board.get_queens(PieceColor.WHITE)[0]

        moves = [m.to_algebraic() for m in queen.moves()]

        self.assertCountEqual(moves, ['Qc4', 'Qe4', 'Qf4',  # file
                                      'Qd3', 'Qd5', 'Qd6',  # rank
                                      'Qc5',  # falling diagonal up
                                      'Qe3',  # falling diagonal down
                                      'Qc3',  # rising diagonal down
                                      'Qe5', 'Qf6'  # rising diagonal up
                                      ])

    def test_queen_moves_with_bQ_on_d4_blocking_captures(self):
        board = SetupBoard('3Nk2N/N2n2r1/1n6/8/Nn1q2rN/8/1n1n1n2/N2NK1N1 w KQkq -')
        queen = board.get_queens(PieceColor.BLACK)[0]

        moves = [m.to_algebraic() for m in queen.moves()]

        self.assertCountEqual(moves, ['Qc4', 'Qe4', 'Qf4',  # file
                                      'Qd3', 'Qd5', 'Qd6',  # rank
                                      'Qc5',  # falling diagonal up
                                      'Qe3',  # falling diagonal down
                                      'Qc3',  # rising diagonal down
                                      'Qe5', 'Qf6'  # rising diagonal up
                                      ])

    def test_rook_moves_with_wR_on_d4(self):
        board = SetupBoard('4k3/8/8/8/3R4/8/8/4K3 w KQkq -')
        rooks = board.get_rooks(PieceColor.WHITE)[0]

        moves = [m.to_algebraic() for m in rooks.moves()]

        self.assertCountEqual(moves, ['Rc4', 'Rb4', 'Ra4', 'Re4', 'Rf4', 'Rg4', 'Rh4',  # file
                                      'Rd3', 'Rd2', 'Rd1', 'Rd5', 'Rd6', 'Rd7', 'Rd8',  # rank
                                      ])

    def test_rook_moves_with_bR_on_d4(self):
        board = SetupBoard('4k3/8/8/8/3r4/8/8/4K3 w KQkq -')
        rooks = board.get_rooks(PieceColor.BLACK)[0]

        moves = [m.to_algebraic() for m in rooks.moves()]

        self.assertCountEqual(moves, ['Rc4', 'Rb4', 'Ra4', 'Re4', 'Rf4', 'Rg4', 'Rh4',  # file
                                      'Rd3', 'Rd2', 'Rd1', 'Rd5', 'Rd6', 'Rd7', 'Rd8',  # rank
                                      ])

    def test_rook_moves_with_wR_on_d4_including_captures(self):
        board = SetupBoard('3nk3/8/8/8/n2R3n/8/8/3nK3 w KQkq -')
        rooks = board.get_rooks(PieceColor.WHITE)[0]

        moves = [m.to_algebraic() for m in rooks.moves()]

        self.assertCountEqual(moves, ['Rc4', 'Rb4', 'Rxa4', 'Re4', 'Rf4', 'Rg4', 'Rxh4',  # file
                                      'Rd3', 'Rd2', 'Rxd1', 'Rd5', 'Rd6', 'Rd7', 'Rxd8',  # rank
                                      ])

    def test_rook_moves_with_bR_on_d4_including_captures(self):
        board = SetupBoard('3Nk3/8/8/8/N2r3N/8/8/3NK3 w KQkq -')
        rooks = board.get_rooks(PieceColor.BLACK)[0]

        moves = [m.to_algebraic() for m in rooks.moves()]

        self.assertCountEqual(moves, ['Rc4', 'Rb4', 'Rxa4', 'Re4', 'Rf4', 'Rg4', 'Rxh4',  # file
                                      'Rd3', 'Rd2', 'Rxd1', 'Rd5', 'Rd6', 'Rd7', 'Rxd8',  # rank
                                      ])

    def test_rook_moves_with_wR_on_d4_blocking_captures(self):
        board = SetupBoard('3nk3/3N4/8/8/nN1R2Nn/8/3N4/3nK3 w KQkq -')
        rooks = board.get_rooks(PieceColor.WHITE)[0]

        moves = [m.to_algebraic() for m in rooks.moves()]

        self.assertCountEqual(moves, ['Rc4', 'Re4', 'Rf4',  # file
                                      'Rd3', 'Rd5', 'Rd6',  # rank
                                      ])

    def test_rook_moves_with_bR_on_d4_blocking_captures(self):
        board = SetupBoard('3Nk3/3n4/8/8/Nn1r2nN/8/3n4/3NK3 w KQkq -')
        rooks = board.get_rooks(PieceColor.BLACK)[0]

        moves = [m.to_algebraic() for m in rooks.moves()]

        self.assertCountEqual(moves, ['Rc4', 'Re4', 'Rf4',  # file
                                      'Rd3', 'Rd5', 'Rd6',  # rank
                                      ])

    def test_bishop_moves_with_wB_on_e4(self):
        board = SetupBoard('4k3/8/8/8/4B3/8/8/4K3 w KQkq -')
        bishop = board.get_bishops(PieceColor.WHITE)[0]

        moves = [m.to_algebraic() for m in bishop.moves()]

        self.assertCountEqual(moves, ['Bd5', 'Bc6', 'Bb7', 'Ba8',  # falling diagonal up
                                      'Bf3', 'Bg2', 'Bh1',  # falling diagonal down
                                      'Bd3', 'Bc2', 'Bb1',  # rising diagonal down
                                      'Bf5', 'Bg6', 'Bh7',  # rising diagonal up
                                      ])

    def test_bishop_moves_with_wB_on_d4(self):
        board = SetupBoard('4k3/8/8/8/3B4/8/8/4K3 w KQkq -')
        bishop = board.get_bishops(PieceColor.WHITE)[0]

        moves = [m.to_algebraic() for m in bishop.moves()]

        self.assertCountEqual(moves, ['Bc5', 'Bb6', 'Ba7',  # falling diagonal up
                                      'Be3', 'Bf2', 'Bg1',  # falling diagonal down
                                      'Bc3', 'Bb2', 'Ba1',  # rising diagonal down
                                      'Be5', 'Bf6', 'Bg7', 'Bh8'  # rising diagonal up
                                      ])

    def test_bishop_moves_with_bB_on_d4(self):
        board = SetupBoard('4k3/8/8/8/3b4/8/8/4K3 w KQkq -')
        bishop = board.get_bishops(PieceColor.BLACK)[0]

        moves = [m.to_algebraic() for m in bishop.moves()]

        self.assertCountEqual(moves, ['Bc5', 'Bb6', 'Ba7',  # falling diagonal up
                                      'Be3', 'Bf2', 'Bg1',  # falling diagonal down
                                      'Bc3', 'Bb2', 'Ba1',  # rising diagonal down
                                      'Be5', 'Bf6', 'Bg7', 'Bh8'  # rising diagonal up
                                      ])

    def test_bishop_moves_with_wB_on_d4_including_captures(self):
        board = SetupBoard('4k2n/n7/8/8/3B4/8/8/n3K1n1 w KQkq -')
        bishop = board.get_bishops(PieceColor.WHITE)[0]

        moves = [m.to_algebraic() for m in bishop.moves()]

        self.assertCountEqual(moves, ['Bc5', 'Bb6', 'Bxa7',  # falling diagonal up
                                      'Be3', 'Bf2', 'Bxg1',  # falling diagonal down
                                      'Bc3', 'Bb2', 'Bxa1',  # rising diagonal down
                                      'Be5', 'Bf6', 'Bg7', 'Bxh8'  # rising diagonal up
                                      ])

    def test_bishop_moves_with_bB_on_d4_including_captures(self):
        board = SetupBoard('4k2N/N7/8/8/3b4/8/8/N3K1N1 w KQkq -')
        bishop = board.get_bishops(PieceColor.BLACK)[0]

        moves = [m.to_algebraic() for m in bishop.moves()]

        self.assertCountEqual(moves, ['Bc5', 'Bb6', 'Bxa7',  # falling diagonal up
                                      'Be3', 'Bf2', 'Bxg1',  # falling diagonal down
                                      'Bc3', 'Bb2', 'Bxa1',  # rising diagonal down
                                      'Be5', 'Bf6', 'Bg7', 'Bxh8'  # rising diagonal up
                                      ])

    def test_bishop_moves_with_wB_on_d4_blocking_captures(self):
        board = SetupBoard('4k2n/n5R1/1N6/8/3B4/8/1N3N2/n3K1n1 w KQkq -')
        bishop = board.get_bishops(PieceColor.WHITE)[0]

        moves = [m.to_algebraic() for m in bishop.moves()]

        self.assertCountEqual(moves, ['Bc5',  # falling diagonal up
                                      'Be3',  # falling diagonal down
                                      'Bc3',  # rising diagonal down
                                      'Be5', 'Bf6'  # rising diagonal up
                                      ])

    def test_bishop_moves_with_bB_on_d4_blocking_captures(self):
        board = SetupBoard('4k2N/N5n1/1n6/8/3b4/8/1n3n2/N3K1N1 w KQkq -')
        bishop = board.get_bishops(PieceColor.BLACK)[0]

        moves = [m.to_algebraic() for m in bishop.moves()]

        self.assertCountEqual(moves, ['Bc5',  # falling diagonal up
                                      'Be3',  # falling diagonal down
                                      'Bc3',  # rising diagonal down
                                      'Be5', 'Bf6'  # rising diagonal up
                                      ])

    def test_knight_moves_with_wN_on_e4(self):
        board = SetupBoard('4k3/8/8/8/4N3/8/8/4K3 w KQkq -')
        knight = board.get_knights(PieceColor.WHITE)[0]

        moves = [m.to_algebraic() for m in knight.moves()]

        self.assertCountEqual(moves, ['Nd2', 'Nf2', 'Ng3', 'Ng5', 'Nf6', 'Nd6', 'Nc5', 'Nc3'])

    def test_knight_moves_with_bN_on_e4(self):
        board = SetupBoard('4k3/8/8/8/4n3/8/8/4K3 w KQkq -')
        knight = board.get_knights(PieceColor.BLACK)[0]

        moves = [m.to_algebraic() for m in knight.moves()]

        self.assertCountEqual(moves, ['Nd2', 'Nf2', 'Ng3', 'Ng5', 'Nf6', 'Nd6', 'Nc5', 'Nc3'])

    def test_knight_moves_with_wN_on_e4_including_captures(self):
        board = SetupBoard('4k3/8/3n1n2/2n3n1/4N3/2n3n1/3n1n2/4K3 w KQkq -')
        knight = board.get_knights(PieceColor.WHITE)[0]

        moves = [m.to_algebraic() for m in knight.moves()]

        self.assertCountEqual(moves, ['Nxd2', 'Nxf2', 'Nxg3', 'Nxg5', 'Nxf6', 'Nxd6', 'Nxc5', 'Nxc3'])

    def test_knight_moves_with_bN_on_e4_including_captures(self):
        board = SetupBoard('4k3/8/3B1B2/2N3N1/4n3/2N3N1/3N1N2/4K3 w KQkq -')
        knight = board.get_knights(PieceColor.BLACK)[0]

        moves = [m.to_algebraic() for m in knight.moves()]

        self.assertCountEqual(moves, ['Nxd2', 'Nxf2', 'Nxg3', 'Nxg5', 'Nxf6', 'Nxd6', 'Nxc5', 'Nxc3'])


if __name__ == '__main__':
    unittest.main()
