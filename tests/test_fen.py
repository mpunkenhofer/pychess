# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest

from pychess.board import StandardBoard
from pychess.pieces import PieceColor


class FENTests(unittest.TestCase):
    def test_fen_chess_starting_postion(self):
        board = StandardBoard()
        self.assertEqual(board.fen(), 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')

    def test_fen_after_1_e4(self):
        board = StandardBoard()

        board.algebraic_move(PieceColor.WHITE, 'e4')

        self.assertEqual(board.fen(), 'rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1')

    def test_fen_after_1_e4_c5(self):
        board = StandardBoard()

        board.algebraic_move(PieceColor.WHITE, 'e4')
        board.algebraic_move(PieceColor.BLACK, 'c5')

        self.assertEqual(board.fen(), 'rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR w KQkq c6 0 2')

    def test_fen_after_1_e4_c5_2_Nf3(self):
        board = StandardBoard()

        board.algebraic_move(PieceColor.WHITE, 'e4')
        board.algebraic_move(PieceColor.BLACK, 'c5')
        board.algebraic_move(PieceColor.WHITE, 'Nf3')

        self.assertEqual(board.fen(), 'rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2')


if __name__ == '__main__':
    unittest.main()
