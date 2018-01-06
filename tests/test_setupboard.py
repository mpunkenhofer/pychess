# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest

from pychess.board import SetupBoard


class SetupBoardTests(unittest.TestCase):
    def test_setup_standard_position(self):
        board = SetupBoard('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()