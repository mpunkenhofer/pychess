# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import pychess
import pygame

from examples.guichess.resources import SpriteSheetPositions, SpriteSize


class GuiPiece(pygame.sprite.Sprite):
    def __init__(self, piece, rectangle):
        pygame.sprite.Sprite.__init__(self)

        self.piece = piece

        rect = pygame.Rect(rectangle)

        self.sprite_sheet = pygame.image.load('examples/guichess/resources/chess_pieces.png')

        image = pygame.Surface(rect.size, pygame.SRCALPHA, 32)
        image.blit(self.sprite_sheet, (0, 0), rect)

        self.image = image

        self.rect = self.get_position_on_surface()

        self.selected = False

    def update(self, *args):
        self.rect = self.get_position_on_surface()

    def get_position_on_surface(self):
        file_max = (self.piece.board.get_top_right()[0] - self.piece.board.get_bottom_left()[0]) * SpriteSize
        rank_max = (self.piece.board.get_top_right()[1] - self.piece.board.get_bottom_left()[0]) * SpriteSize

        return file_max - (self.piece.position[0] * SpriteSize), rank_max - (self.piece.position[1] * SpriteSize)


class GuiKing(pychess.pieces.King, GuiPiece):
    def __init__(self, board, pos, c):
        pychess.pieces.King.__init__(self, board, pos, c)
        GuiPiece.__init__(self, self, SpriteSheetPositions[self.type][self.color] + (SpriteSize, SpriteSize))


class GuiQueen(pychess.pieces.Queen, GuiPiece):
    def __init__(self, board, pos, c):
        pychess.pieces.Queen.__init__(self, board, pos, c)
        GuiPiece.__init__(self, self, SpriteSheetPositions[self.type][self.color] + (SpriteSize, SpriteSize))


class GuiRook(pychess.pieces.Rook, GuiPiece):
    def __init__(self, board, pos, c):
        pychess.pieces.Rook.__init__(self, board, pos, c)
        GuiPiece.__init__(self, self, SpriteSheetPositions[self.type][self.color] + (SpriteSize, SpriteSize))


class GuiBishop(pychess.pieces.Bishop, GuiPiece):
    def __init__(self, board, pos, c):
        pychess.pieces.Bishop.__init__(self, board, pos, c)
        GuiPiece.__init__(self, self, SpriteSheetPositions[self.type][self.color] + (SpriteSize, SpriteSize))


class GuiKnight(pychess.pieces.Knight, GuiPiece):
    def __init__(self, board, pos, c):
        pychess.pieces.Knight.__init__(self, board, pos, c)
        GuiPiece.__init__(self, self, SpriteSheetPositions[self.type][self.color] + (SpriteSize, SpriteSize))


class GuiPawn(pychess.pieces.Pawn, GuiPiece):
    def __init__(self, board, pos, c):
        pychess.pieces.Pawn.__init__(self, board, pos, c)
        GuiPiece.__init__(self, self, SpriteSheetPositions[self.type][self.color] + (SpriteSize, SpriteSize))
