# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import pygame
import pychess

from pychess import PieceColor
from examples.guichess.pieces import GuiKing, GuiQueen, GuiRook, GuiBishop, GuiKnight, GuiPawn
from examples.guichess.resources import SpriteSize


class GuiBoard(pychess.board.StandardBoard):
    def __init__(self, surface, colors=((240, 217, 217), (142, 100, 100))):
        pychess.board.StandardBoard.__init__(self)

        self.surface = surface
        self.colors = colors

        self.pieces.clear()

        self.pieces = {(4, 0): GuiKing(self, (4, 0), PieceColor.WHITE),
                       (4, 7): GuiKing(self, (4, 7), PieceColor.BLACK),
                       (3, 0): GuiQueen(self, (3, 0), PieceColor.WHITE),
                       (3, 7): GuiQueen(self, (3, 7), PieceColor.BLACK),
                       (0, 0): GuiRook(self, (0, 0), PieceColor.WHITE),
                       (7, 0): GuiRook(self, (7, 0), PieceColor.WHITE),
                       (0, 7): GuiRook(self, (0, 7), PieceColor.BLACK),
                       (7, 7): GuiRook(self, (7, 7), PieceColor.BLACK),
                       (2, 0): GuiBishop(self, (2, 0), PieceColor.WHITE),
                       (5, 0): GuiBishop(self, (5, 0), PieceColor.WHITE),
                       (2, 7): GuiBishop(self, (2, 7), PieceColor.BLACK),
                       (5, 7): GuiBishop(self, (5, 7), PieceColor.BLACK),
                       (1, 0): GuiKnight(self, (1, 0), PieceColor.WHITE),
                       (6, 0): GuiKnight(self, (6, 0), PieceColor.WHITE),
                       (1, 7): GuiKnight(self, (1, 7), PieceColor.BLACK),
                       (6, 7): GuiKnight(self, (6, 7), PieceColor.BLACK)}

        for i in range(0, 8):
            self.pieces[(i, 1)] = GuiPawn(self, (i, 1), PieceColor.WHITE)
            self.pieces[(i, 6)] = GuiPawn(self, (i, 6), PieceColor.BLACK)

    def render(self):
        square_size = SpriteSize

        file_diff = self.get_top_right()[0] - self.get_bottom_left()[0]
        rank_diff = self.get_top_right()[1] - self.get_bottom_left()[0]

        for y in reversed(range(0, rank_diff + 1)):
            for x in range(0, file_diff + 1):
                current_square = (square_size * x, square_size * y, square_size, square_size)
                if x % 2 == 0 and y % 2 == 0 or x % 2 == 1 and y % 2 == 1:
                    pygame.draw.rect(self.surface, self.colors[0], current_square)
                else:
                    pygame.draw.rect(self.surface, self.colors[1], current_square)

        for _, s in self.pieces.items():
            self.surface.blit(s.image, s.rect)

        return self.surface

