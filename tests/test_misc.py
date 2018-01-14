# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest
import pychess


class MiscellaneousTests(unittest.TestCase):
    def test_misc_1(self):
        board = pychess.board.StandardBoard()

        rook = board.get_piece((0, 0))
        knight = board.get_piece((1, 0))
        bishop = board.get_piece((2, 0))
        queen = board.get_piece((3, 0))
        king = board.get_piece((4, 0))

        white_pcs = rook.is_rook() and knight.is_knight() and bishop.is_bishop() and queen.is_queen() and king.is_king()
        white_pcs = white_pcs and rook.is_white() and knight.is_white() and bishop.is_white() and queen.is_white() \
                    and king.is_white()

        rook = board.get_piece((0, 7))
        knight = board.get_piece((1, 7))
        bishop = board.get_piece((2, 7))
        queen = board.get_piece((3, 7))
        king = board.get_piece((4, 7))

        black_pcs = rook.is_rook() and knight.is_knight() and bishop.is_bishop() and queen.is_queen() and king.is_king()
        black_pcs = black_pcs and rook.is_black() and knight.is_black() and bishop.is_black() and queen.is_black() \
                    and king.is_black()

        self.assertTrue(white_pcs and black_pcs)

    def test_is_first_and_is_last_file(self):
        board = pychess.board.StandardBoard()

        king_rook = board.get_piece((0, 0))
        queen_rook = board.get_piece((7, 0))

        self.assertTrue(board.is_last_file(queen_rook.color, queen_rook.position)
                        and board.is_first_file(king_rook.color, king_rook.position))

    def test_get_coordinates_1(self):
        board = pychess.board.StandardBoard()

        king_rook = board.get_piece((0, 0))
        queen_rook = board.get_piece((7, 0))

        x1, y1, x2, y2 = pychess.pieces.Piece.get_coordinates(king_rook, queen_rook)

        self.assertTrue(king_rook.position == (x1, y1) and queen_rook.position == (x2, y2))

    def test_get_coordinates_2(self):
        board = pychess.board.StandardBoard()

        king_rook = board.get_piece((0, 0))

        x1, y1 = pychess.pieces.Piece.get_coordinates(king_rook)

        self.assertTrue(king_rook.position == (x1, y1))

    def test_no_pieces_between(self):
        board = pychess.board.StandardBoard()

        king_rook = board.get_piece((0, 0))
        black_king = board.get_king(pychess.PieceColor.BLACK)

        self.assertEqual(king_rook.pieces_between(black_king), [])


if __name__ == '__main__':
    unittest.main()
