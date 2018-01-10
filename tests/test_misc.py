# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest

from pychess.board import StandardBoard


class MiscellaneousTests(unittest.TestCase):
    def test_misc_1(self):
        board = StandardBoard()

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


if __name__ == '__main__':
    unittest.main()
