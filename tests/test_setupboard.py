# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest

import pychess.util.move

from pychess.pieces import King, Queen, Rook, Bishop, Knight, Pawn, PieceColor

from pychess.board import SetupBoard
from pychess.util.board import to_string_array


class SetupBoardTests(unittest.TestCase):
    def test_setup_empty_fen(self):
        board = SetupBoard()
        str_board = to_string_array(board)
        self.assertEqual(str_board, ['........',
                                     '........',
                                     '........',
                                     '........',
                                     '........',
                                     '........',
                                     '........',
                                     '........'
                                     ])

    def test_setup_standard_position(self):
        board = SetupBoard('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
        str_board = to_string_array(board)
        self.assertEqual(str_board, ['rnbqkbnr',
                                     'pppppppp',
                                     '........',
                                     '........',
                                     '........',
                                     '........',
                                     'PPPPPPPP',
                                     'RNBQKBNR'
                                     ])

    def test_setup_position_1_e4(self):
        board = SetupBoard('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1')
        str_board = to_string_array(board)
        self.assertEqual(str_board, ['rnbqkbnr',
                                     'pppppppp',
                                     '........',
                                     '........',
                                     '....P...',
                                     '........',
                                     'PPPP.PPP',
                                     'RNBQKBNR'
                                     ])

    def test_setup_position_1_e4_c5(self):
        board = SetupBoard('rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR w KQkq c6 0 2')
        str_board = to_string_array(board)
        self.assertEqual(str_board, ['rnbqkbnr',
                                     'pp.ppppp',
                                     '........',
                                     '..p.....',
                                     '....P...',
                                     '........',
                                     'PPPP.PPP',
                                     'RNBQKBNR'
                                     ])

    def test_setup_position_1_e4_c5_2_Nf3(self):
        board = SetupBoard('rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2')
        str_board = to_string_array(board)
        self.assertEqual(str_board, ['rnbqkbnr',
                                     'pp.ppppp',
                                     '........',
                                     '..p.....',
                                     '....P...',
                                     '.....N..',
                                     'PPPP.PPP',
                                     'RNBQKB.R'
                                     ])

    def test_setup_position_without_pieces(self):
        board = SetupBoard('4k3/pppppppp/8/8/8/8/PPPPPPPP/4K3 w - - 0 1')
        str_board = to_string_array(board)
        self.assertEqual(str_board, ['....k...',
                                     'pppppppp',
                                     '........',
                                     '........',
                                     '........',
                                     '........',
                                     'PPPPPPPP',
                                     '....K...'
                                     ])

    def test_setup_position_missing_king(self):
        with self.assertRaises(ValueError):
            board = SetupBoard('4k3/pppppppp/8/8/8/8/PPPPPPPP/8 w - - 0 1')

    def test_put_piece(self):
        board = SetupBoard('4k3/pppppppp/8/8/8/8/PPPPPPPP/4K3 w KQkq - 0 1')

        color = PieceColor.WHITE
        first_rank = board.get_first_rank(color)

        board.put_piece(Rook(board, (0, first_rank), color))
        board.put_piece(Knight(board, (1, first_rank), color))
        board.put_piece(Bishop(board, (2, first_rank), color))
        board.put_piece(Queen(board, (3, first_rank), color))
        board.put_piece(Bishop(board, (5, first_rank), color))
        board.put_piece(Knight(board, (6, first_rank), color))
        board.put_piece(Rook(board, (7, first_rank), color))

        color = PieceColor.BLACK
        first_rank = board.get_first_rank(color)

        board.put_piece(Rook(board, (0, first_rank), color))
        board.put_piece(Knight(board, (1, first_rank), color))
        board.put_piece(Bishop(board, (2, first_rank), color))
        board.put_piece(Queen(board, (3, first_rank), color))
        board.put_piece(Bishop(board, (5, first_rank), color))
        board.put_piece(Knight(board, (6, first_rank), color))
        board.put_piece(Rook(board, (7, first_rank), color))

        str_board = to_string_array(board)
        self.assertEqual(str_board, ['rnbqkbnr',
                                     'pppppppp',
                                     '........',
                                     '........',
                                     '........',
                                     '........',
                                     'PPPPPPPP',
                                     'RNBQKBNR'
                                     ])

        self.assertEqual(1, 1)

    def test_put_piece_too_many_kings(self):
        board = SetupBoard()

        board.put_piece(King(board, (0, 0), PieceColor.WHITE))
        board.put_piece(King(board, (7, 7), PieceColor.BLACK))

        with self.assertRaises(ValueError):
            # putting one too many kings on the board should raise an Error
            board.put_piece(King(board, (7, 0), PieceColor.WHITE))

    def test_put_piece_kings_too_close(self):
        board = SetupBoard()

        board.put_piece(King(board, (0, 0), PieceColor.WHITE))

        with self.assertRaises(ValueError):
            # putting one a king to close to the other one should raise an Error
            board.put_piece(King(board, (0, 1), PieceColor.BLACK))

    def test_put_piece_missing_king(self):
        with self.assertRaises(ValueError):
            # forgetting one king should raise an Error
            board = SetupBoard('4k3/pppppppp/8/8/8/8/PPPPPPPP/8 w KQkq - 0 1')
            print(to_string_array(board))

    def test_put_piece_pawn_on_last_rank(self):
        board = SetupBoard()

        with self.assertRaises(ValueError):
            # putting one a pawn on its respective last rank should raise an Error
            board.put_piece(Pawn(board, (0, board.get_last_rank(PieceColor.WHITE)), PieceColor.WHITE))

    def test_put_piece_occupied(self):
        board = SetupBoard('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')

        with self.assertRaises(ValueError):
            # putting one a pawn on its respective last rank should raise an Error
            board.put_piece(Pawn(board, (0, 0), PieceColor.WHITE))

    def test_pawn_en_passant_setup_wP(self):
        board = SetupBoard('rnbqkbnr/pppp1ppp/8/3PpP2/8/8/PPP2PPP/RNBQKBNR w KQkq e6')

        pawns = board.get_pawns(PieceColor.WHITE)

        moves = []
        for p in pawns:
            for m in p.moves():
                moves.append(m.to_algebraic())

        en_passant_moves = ['dxe6', 'fxe6']
        en_passants_found = []

        for em in en_passant_moves:
            if em in en_passant_moves:
                en_passants_found.append(em)

        self.assertCountEqual(en_passant_moves, en_passants_found)

    def test_pawn_en_passant_setup_bP(self):
        board = SetupBoard('rnbqkbnr/ppp1p1pp/8/8/3pPp2/8/PPPP1PPP/RNBQKBNR b KQkq e3')

        pawns = board.get_pawns(PieceColor.BLACK)

        moves = []
        for p in pawns:
            for m in p.moves():
                moves.append(m.to_algebraic())

        en_passant_moves = ['dxe3', 'fxe3']
        en_passants_found = []

        for em in en_passant_moves:
            if em in en_passant_moves:
                en_passants_found.append(em)

        self.assertCountEqual(en_passant_moves, en_passants_found)

    def test_corrupt_fen_1(self):
        with self.assertRaises(ValueError):
            board = SetupBoard('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPP')

    def test_corrupt_fen_2(self):
        with self.assertRaises(ValueError):
            board = SetupBoard('rnbqkbnr/ppp1p1pp/8/8/3pPp2/8/PPPP1PPP/RNBQKBNR ? KQkq e3')

    def test_corrupt_fen_3(self):
        with self.assertRaises(ValueError):
            board = SetupBoard('rnbqkbnr/ppp1p1pp/8/8/3pPp2/8/PPPP1PPP/RNBQKBNR w KQkq A3')

    def test_corrupt_fen_4(self):
        with self.assertRaises(ValueError):
            board = SetupBoard('rnbqkbnr/ppp1p1pp/8/8/3pPp2/8/PPPP1PPP/RNBQKBNR w KQkq ??')

    def test_corrupt_fen_5(self):
        with self.assertRaises(ValueError):
            board = SetupBoard('rnbqkbnr/ppp1p1pp/8/8/3p1p2/8/PPPPPPPP/RNBQKBNR b KQkq e3')

    def test_corrupt_fen_6(self):
        with self.assertRaises(ValueError):
            board = SetupBoard('rnbqkbnr/ppp1p1pp/8/8/3pNp2/8/PPPP1PPP/RNBQKBNR b KQkq e3')

    def test_corrupt_fen_7(self):
        with self.assertRaises(ValueError):
            board = SetupBoard('rnbqkbnr/ppp1p1pp/8/8/3ppp2/8/PPPP1PPP/RNBQKBNR b KQkq e3')


if __name__ == '__main__':
    unittest.main()
