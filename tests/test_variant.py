# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import unittest
import pychess

from unittest.mock import patch, mock_open
from textwrap import dedent

from tests.testutils.pgn_player import PGNPlayer


class VariantTests(unittest.TestCase):
    game = dedent("""
        1. d4 d5 2. Nf3 e6 3. b3 Bb4+ 4. Bd2 Bxd2+
        5. Nbxd2 Nf6 6. e3 O-O 7. c4 dxc4 8. Nxc4 b6
        9. Qc2 Bb7 10. O-O-O c5 11. dxc5 Qe7 12. cxb6 a6
        13. Be2 Nbd7 14. Kb1 Be4 15. Qxe4 Nxe4 16. a4 Rfc8
        17. b7 Rab8 18. bxc8=Q+ Rxc8 19. Nd4 Rxc4 20. Bxc4 e5
        21. Nf3 Nxf2 22. Rxd7 Qxd7 23. Nxe5 Qd2 24. Nxf7 Nd3
        25. Nh6+ Kh8 26. Nf7+ Kg8 27. Ne5+ Kf8 28. Nxd3 Qxe3
        29. Re1 Qb6 30. Ka2 h5 31. Re6 Qd4 32. Rxa6 Qf2+
        33. Ka3 Qc5+ 34. Nxc5 h4 35. Rd6 h3 36. gxh3 Ke8
        37. a5 Kf8 38. a6 Ke8 39. a7 Kf8 40. Rd7 Ke8
        41. a8=R#
    """)

    @patch("builtins.open", mock_open(read_data=game))
    def test_standard_variant(self):
        variant = pychess.variant.Standard()
        pgn = PGNPlayer('filename')

        pgn_move = pgn.next_move()
        player = pychess.PieceColor.WHITE

        while pgn_move and not variant.is_checkmated(player) and not variant.is_draw():
            variant.board.algebraic_move(player, pgn_move)
            player = pychess.PieceColor.WHITE if player == pychess.PieceColor.BLACK else pychess.PieceColor.BLACK
            pgn_move = pgn.next_move()

        self.assertEqual(variant.board.algebraic_history(), pgn.get_moves())


if __name__ == '__main__':
    unittest.main()
