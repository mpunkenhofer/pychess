# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

"""
note to self: use of mock is preferable:

from unittest import TestCase
from unittest.mock import patch, mock_open

from textwrap import dedent

class OpenTest(TestCase):
    DATA = dedent('''
        a,b,c
        x,y,z
        ''').strip()

    @patch("builtins.open", mock_open(read_data=DATA))
    def test_open(self):

        # Due to how the patching is done, any module accessing `open' for the
        # duration of this test get access to a mock instead (not just the test
        # module).
        with open("filename", "r") as f:
            result = f.read()

        open.assert_called_once_with("filename", "r")
        self.assertEqual(self.DATA, result)
        self.assertEqual("a,b,c\nx,y,z", result)
"""

import unittest
import os

from tests.testutils.pgn_player import PGNPlayer

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


class PGNPlayerTests(unittest.TestCase):
    def test_pgn_player_no_game(self):
        game = PGNPlayer()
        self.assertFalse(game.get_moves() and game.next_game())

    def test_pgn_player_one_game(self):
        game = PGNPlayer(os.path.join(THIS_DIR, 'pgns/games/Hikaru_vs_MagnusCarlsen_2018-01-03-1.pgn'))
        self.assertEqual(game.get_moves(), ['b3', 'a5', 'Bb2', 'a4', 'e3', 'e6', 'Nf3', 'Nf6', 'Nc3', 'a3', 'Bc1',
                                            'd5', 'd4', 'Bb4', 'Bd2', 'O-O', 'Bd3', 'Re8', 'Ne2', 'Bxd2+', 'Qxd2',
                                            'Nbd7', 'c4', 'e5', 'dxe5', 'Nxe5', 'Nxe5', 'Rxe5', 'O-O', 'dxc4', 'Bxh7+'])

    def test_pgn_player_one_game_with_timestamps(self):
        game = PGNPlayer(os.path.join(THIS_DIR, 'pgns/games/Hikaru_vs_MagnusCarlsen_2018-01-03-1-timestamps.pgn'))
        self.assertEqual(game.get_moves(), ['b3', 'a5', 'Bb2', 'a4', 'e3', 'e6', 'Nf3', 'Nf6', 'Nc3', 'a3', 'Bc1',
                                            'd5', 'd4', 'Bb4', 'Bd2', 'O-O', 'Bd3', 'Re8', 'Ne2', 'Bxd2+', 'Qxd2',
                                            'Nbd7', 'c4', 'e5', 'dxe5', 'Nxe5', 'Nxe5', 'Rxe5', 'O-O', 'dxc4', 'Bxh7+'])

    def test_pgn_player_next_move(self):
        game = PGNPlayer(os.path.join(THIS_DIR, 'pgns/games/Hikaru_vs_MagnusCarlsen_2018-01-03-1-timestamps.pgn'))

        moves = []
        next_move = game.next_move()

        while next_move:
            moves.append(next_move)
            next_move = game.next_move()

        self.assertEqual(moves, ['b3', 'a5', 'Bb2', 'a4', 'e3', 'e6', 'Nf3', 'Nf6', 'Nc3', 'a3', 'Bc1',
                                 'd5', 'd4', 'Bb4', 'Bd2', 'O-O', 'Bd3', 'Re8', 'Ne2', 'Bxd2+', 'Qxd2',
                                 'Nbd7', 'c4', 'e5', 'dxe5', 'Nxe5', 'Nxe5', 'Rxe5', 'O-O', 'dxc4', 'Bxh7+'])

    def test_pgn_player_reset(self):
        game = PGNPlayer(os.path.join(THIS_DIR, 'pgns/games/Hikaru_vs_MagnusCarlsen_2018-01-03-1-timestamps.pgn'))

        moves = []
        next_move = game.next_move()

        while next_move:
            moves.append(next_move)
            next_move = game.next_move()

        game.reset()

        next_move = game.next_move()

        while next_move:
            moves.append(next_move)
            next_move = game.next_move()

        self.assertEqual(moves, ['b3', 'a5', 'Bb2', 'a4', 'e3', 'e6', 'Nf3', 'Nf6', 'Nc3', 'a3', 'Bc1',
                                 'd5', 'd4', 'Bb4', 'Bd2', 'O-O', 'Bd3', 'Re8', 'Ne2', 'Bxd2+', 'Qxd2',
                                 'Nbd7', 'c4', 'e5', 'dxe5', 'Nxe5', 'Nxe5', 'Rxe5', 'O-O', 'dxc4', 'Bxh7+'] * 2)

    def test_pgn_player_white_win(self):
        game = PGNPlayer(os.path.join(THIS_DIR, 'pgns/games/Hikaru_vs_MagnusCarlsen_2018-01-03-1.pgn'))
        game_timestamps = PGNPlayer(os.path.join(THIS_DIR,
                                                 'pgns/games/Hikaru_vs_MagnusCarlsen_2018-01-03-1-timestamps.pgn'))
        self.assertTrue(game.white_win() and game_timestamps.white_win())

    def test_pgn_player_black_win(self):
        game = PGNPlayer(os.path.join(THIS_DIR, 'pgns/games/MagnusCarlsen_vs_Hikaru_2018-01-03-1.pgn'))
        self.assertTrue(game.black_win())

    def test_pgn_player_draw(self):
        game = PGNPlayer(os.path.join(THIS_DIR, 'pgns/games/Hikaru_vs_MagnusCarlsen_2018-01-03-2.pgn'))
        self.assertTrue(game.draw())

    def test_pgn_player_two_games(self):
        games = []

        current_game = PGNPlayer(os.path.join(THIS_DIR, 'pgns/games/lichess_necator_2018-01-06-two_games.pgn'))
        games.append(current_game.get_moves())

        while current_game.next_game():
            games.append(current_game.next_game().get_moves())
            current_game = current_game.next_game()

        self.assertEqual(games,
                         [['e4', 'e6', 'Nf3', 'd5', 'exd5', 'exd5', 'd4', 'Nf6', 'Nc3', 'Bb4', 'Bd2', 'O-O', 'Bd3',
                           'c6',
                           'O-O', 'Bg4', 'Re1', 'Nbd7', 'Be2', 'h6', 'h3', 'Bh5', 'g4', 'Bg6', 'Nh4', 'Bh7', 'Nf5',
                           'Bxf5', 'gxf5', 'Bxc3', 'Bxc3', 'Ne4', 'f3', 'Nxc3', 'bxc3', 'Qf6', 'Qd2', 'Qxf5', 'Kh2',
                           'Nf6', 'f4', 'Nh5', 'Rf1', 'Rae8', 'Bxh5', 'Qxh5', 'Rae1', 'Qf5', 'Re5', 'Qd7', 'Rfe1',
                           'Rxe5', 'fxe5', 'Re8', 'Rf1', 'Qe6', 'Qf4', 'Re7', 'Rg1', 'Kh7', 'Qg3', 'f6', 'exf6', 'Qxf6',
                           'Qd3+', 'Kg8', 'Qg3', 'Re2+', 'Rg2', 'Rxg2+', 'Qxg2', 'Qf4+', 'Qg3', 'Qxg3+', 'Kxg3', 'Kf7',
                           'Kg4', 'Kf6', 'Kf4', 'g6', 'h4', 'a5', 'a4', 'g5+', 'hxg5+', 'hxg5+', 'Kg4', 'Kg6', 'Kg3',
                           'Kf5', 'Kg2', 'Kf4', 'Kf1', 'g4', 'Ke1', 'Kf3'],
                          ['e4', 'e6', 'Nf3', 'd5', 'exd5', 'exd5', 'd4', 'Nf6', 'Bd3', 'Bd6', 'O-O', 'O-O', 'Re1',
                           'c6', 'h3', 'Be6', 'c3', 'Nbd7', 'Bg5', 'h6', 'Bh4', 'Be7', 'Nbd2', 'Re8', 'Qb3', 'Qc7',
                           'Bg3', 'Qc8', 'Ne5', 'b5', 'Nxd7', 'Nxd7', 'Nf3', 'Nb6', 'Ne5', 'Nc4', 'Qc2', 'Nxe5', 'Bxe5',
                           'Bf8', 'Rac1', 'a5', 'Qe2', 'Qd7', 'Qf3', 'a4', 'Qg3', 'Ra7', 'Bf4', 'Bf5', 'Bxf5', 'Rxe1+',
                           'Rxe1', 'Qxf5', 'Bxh6', 'Qc2', 'Re8', 'Qg6', 'Bf4', 'Qxg3', 'Bxg3', 'Re7', 'Rc8', 'Re6',
                           'Kh2', 'g6', 'Be5', 'a3', 'bxa3', 'g5', 'f4', 'Kh7', 'fxg5', 'Kg6', 'Rxf8', 'Kxg5', 'Rg8+',
                           'Kf5', 'Rg5+', 'Ke4', 'h4', 'Kd3', 'g4', 'Kc4']])

    def test_pgn_player_three_games(self):
        games = []

        current_game = PGNPlayer(os.path.join(THIS_DIR, 'pgns/games/lichess_necator_2018-01-06-three_games.pgn'))
        games.append(current_game.get_moves())

        while current_game.next_game():
            games.append(current_game.next_game().get_moves())
            current_game = current_game.next_game()

        self.assertEqual(games,
                         [['e4', 'e6', 'Nf3', 'd5', 'exd5', 'exd5', 'd4', 'Nf6', 'Nc3', 'Bb4', 'Bd2', 'O-O', 'Bd3',
                           'c6',
                           'O-O', 'Bg4', 'Re1', 'Nbd7', 'Be2', 'h6', 'h3', 'Bh5', 'g4', 'Bg6', 'Nh4', 'Bh7', 'Nf5',
                           'Bxf5', 'gxf5', 'Bxc3', 'Bxc3', 'Ne4', 'f3', 'Nxc3', 'bxc3', 'Qf6', 'Qd2', 'Qxf5', 'Kh2',
                           'Nf6', 'f4', 'Nh5', 'Rf1', 'Rae8', 'Bxh5', 'Qxh5', 'Rae1', 'Qf5', 'Re5', 'Qd7', 'Rfe1',
                           'Rxe5', 'fxe5', 'Re8', 'Rf1', 'Qe6', 'Qf4', 'Re7', 'Rg1', 'Kh7', 'Qg3', 'f6', 'exf6', 'Qxf6',
                           'Qd3+', 'Kg8', 'Qg3', 'Re2+', 'Rg2', 'Rxg2+', 'Qxg2', 'Qf4+', 'Qg3', 'Qxg3+', 'Kxg3', 'Kf7',
                           'Kg4', 'Kf6', 'Kf4', 'g6', 'h4', 'a5', 'a4', 'g5+', 'hxg5+', 'hxg5+', 'Kg4', 'Kg6', 'Kg3',
                           'Kf5', 'Kg2', 'Kf4', 'Kf1', 'g4', 'Ke1', 'Kf3'],
                          ['e4', 'e6', 'Nf3', 'd5', 'exd5', 'exd5', 'd4', 'Nf6', 'Bd3', 'Bd6', 'O-O', 'O-O', 'Re1',
                           'c6', 'h3', 'Be6', 'c3', 'Nbd7', 'Bg5', 'h6', 'Bh4', 'Be7', 'Nbd2', 'Re8', 'Qb3', 'Qc7',
                           'Bg3', 'Qc8', 'Ne5', 'b5', 'Nxd7', 'Nxd7', 'Nf3', 'Nb6', 'Ne5', 'Nc4', 'Qc2', 'Nxe5', 'Bxe5',
                           'Bf8', 'Rac1', 'a5', 'Qe2', 'Qd7', 'Qf3', 'a4', 'Qg3', 'Ra7', 'Bf4', 'Bf5', 'Bxf5', 'Rxe1+',
                           'Rxe1', 'Qxf5', 'Bxh6', 'Qc2', 'Re8', 'Qg6', 'Bf4', 'Qxg3', 'Bxg3', 'Re7', 'Rc8', 'Re6',
                           'Kh2', 'g6', 'Be5', 'a3', 'bxa3', 'g5', 'f4', 'Kh7', 'fxg5', 'Kg6', 'Rxf8', 'Kxg5', 'Rg8+',
                           'Kf5', 'Rg5+', 'Ke4', 'h4', 'Kd3', 'g4', 'Kc4'],
                          ['d4', 'Nf6', 'c4', 'e6', 'Nc3', 'd5', 'Nf3', 'Be7', 'Bg5', 'O-O', 'e3', 'b6', 'cxd5', 'exd5',
                           'Bd3', 'Ba6', 'Qe2', 'Bxd3', 'Qxd3', 'c5', 'dxc5', 'bxc5', 'Bxf6', 'Bxf6', 'Qxd5', 'Qxd5',
                           'Nxd5', 'Bxb2', 'Rb1', 'Ba3', 'Nc7']])

        if __name__ == '__main__':
            unittest.main()
